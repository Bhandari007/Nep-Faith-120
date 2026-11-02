"""NepFaith-120: Evaluation Corpus Runner (5 Evaluator Arms Orchestrator).

Executes automated scoring across conditions:
- Condition C1: Original Nepali context (p_ne)
- Condition C2: Raw IndicTrans2 MT context (p_c2)
- Condition C3: Human Post-Edited MT context (p_c3)

Calculates derived item-level binary faithfulness adherence:
All constituent claims supported = 1, any critical/constituent claim contradicted/not-in-context = 0.
Strictly respects Absolute Prohibition 2: Zero writes to `data/raw/labels/`.
"""

import json
import logging
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional

# Ensure project root is in sys.path when executed directly
project_root = Path(__file__).resolve().parents[2]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from src.prepare.schema import ClaimLabel
from src.run.scorers import BaseScorer, get_evaluator_suite

logger = logging.getLogger("EvaluateCorpus")


def compute_item_faithfulness_from_claims(claim_evaluations: List[Dict[str, Any]]) -> int:
    """Computes derived item-level binary faithfulness from constituent claim predictions.

    Pre-registered Rule:
    An answer item is faithful (1) iff all constituent claims are 'Supported'.
    If any claim flagged as critical (or any constituent claim) receives 'Contradicted'
    or 'Not-in-context', the item is designated Unfaithful (0).
    """
    if not claim_evaluations:
        return 0

    for c in claim_evaluations:
        label = str(c.get("predicted_label", "")).strip().lower()
        if label != ClaimLabel.SUPPORTED.value.lower():
            return 0
    return 1


def get_condition_passage(item: Dict[str, Any], condition: str) -> str:
    """Returns the appropriate passage text for the counterfactual condition."""
    cond = condition.upper()
    if cond == "C1":
        p = item.get("passage_ne")
    elif cond == "C2":
        p = item.get("c2_raw_mt")
    elif cond == "C3":
        p = item.get("c3_post_edited_mt") or item.get("c2_raw_mt")
    else:
        raise ValueError(f"Unknown condition: {condition}. Must be C1, C2, or C3.")

    if not p or not isinstance(p, str):
        raise ValueError(f"Item {item.get('item_id')} missing passage text for condition {condition}")
    return p.strip()


def evaluate_item_condition(
    item: Dict[str, Any],
    condition: str,
    scorer: BaseScorer,
    use_cache: bool = True,
) -> Dict[str, Any]:
    """Evaluates an item's constituent atomic claims under a specific condition with a scorer."""
    passage = get_condition_passage(item, condition)
    claims = item.get("claims", [])

    claim_evals: List[Dict[str, Any]] = []
    for cl in claims:
        claim_id = cl.get("claim_id")
        claim_text = cl.get("claim_text") or cl.get("text", "")
        is_critical = cl.get("is_critical", True)

        eval_res = scorer.score_claim(passage=passage, claim=claim_text, use_cache=use_cache)
        claim_evals.append({
            "claim_id": claim_id,
            "claim_text": claim_text,
            "is_critical": is_critical,
            "score": eval_res.get("score"),
            "predicted_label": eval_res.get("predicted_label"),
            "raw_output": eval_res,
        })

    derived_f = compute_item_faithfulness_from_claims(claim_evals)

    return {
        "item_id": item.get("item_id"),
        "condition": condition,
        "claim_evaluations": claim_evals,
        "derived_faithfulness": derived_f,
    }


def evaluate_dataset(
    input_path: Path,
    output_path: Path,
    scorers: Dict[str, BaseScorer],
    conditions: Optional[List[str]] = None,
    use_cache: bool = True,
) -> int:
    """Runs specified scorers across conditions on an evaluation corpus JSONL.

    Results are written to output_path under data/interim/.
    Zero writes to data/raw/labels/.
    """
    if conditions is None:
        conditions = ["C1", "C2", "C3"]

    output_path = Path(output_path)
    if "data/raw/labels" in str(output_path):
        raise PermissionError("Absolute Prohibition 2 violated: Never write to data/raw/labels/.")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    items: List[Dict[str, Any]] = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                items.append(json.loads(line))

    existing_by_id: Dict[str, Dict[str, Any]] = {}
    if output_path.exists():
        try:
            with open(output_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        rec = json.loads(line)
                        if "item_id" in rec:
                            existing_by_id[rec["item_id"]] = rec
        except Exception as e:
            logger.warning(f"Could not load existing predictions from {output_path}: {e}")

    all_records_by_id: Dict[str, Dict[str, Any]] = dict(existing_by_id)
    evaluated_records: List[Dict[str, Any]] = []

    for idx, item in enumerate(items, 1):
        item_id = item.get("item_id")
        existing_rec = all_records_by_id.get(item_id, {})
        predictions_map = dict(existing_rec.get("predictions", {}))

        item_record: Dict[str, Any] = {
            "item_id": item_id,
            "domain": item.get("domain", existing_rec.get("domain")),
            "sub_genre": item.get("sub_genre", existing_rec.get("sub_genre")),
            "perturbation_type": item.get("perturbation_type", existing_rec.get("perturbation_type")),
            "source_provenance": item.get("source_provenance", existing_rec.get("source_provenance")),
            "predictions": predictions_map,
        }

        for arm_name, scorer in scorers.items():
            if arm_name not in item_record["predictions"]:
                item_record["predictions"][arm_name] = {}
            for cond in conditions:
                existing_cond = item_record["predictions"][arm_name].get(cond)
                if (
                    use_cache
                    and existing_cond
                    and "derived_faithfulness" in existing_cond
                    and existing_cond.get("claims")
                ):
                    continue
                res = evaluate_item_condition(item, cond, scorer, use_cache=use_cache)
                item_record["predictions"][arm_name][cond] = {
                    "derived_faithfulness": res["derived_faithfulness"],
                    "claims": res["claim_evaluations"],
                }

        all_records_by_id[item_id] = item_record
        evaluated_records.append(item_record)

        # Atomic checkpoint to disk after each item preserving all records
        tmp_out = output_path.with_suffix(".tmp")
        with open(tmp_out, "w", encoding="utf-8") as f:
            for it in items:
                it_id = it.get("item_id")
                rec = all_records_by_id.get(it_id)
                if rec:
                    f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        tmp_out.replace(output_path)

        if idx % 5 == 0 or idx == len(items):
            logger.info(f"Progress: Evaluated {idx}/{len(items)} items.")


    return len(evaluated_records)


if __name__ == "__main__":
    import argparse

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

    parser = argparse.ArgumentParser(description="NepFaith-120 Evaluation Suite Runner")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("data/interim/preannotations/gold_candidates_120.jsonl"),
        help="Input evaluation items JSONL",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/interim/predictions/predictions_candidates_120.jsonl"),
        help="Output predictions JSONL",
    )
    parser.add_argument(
        "--arms",
        nargs="+",
        default=["arm2_bgem3"],
        help="Evaluator arms to run (e.g. arm1_hhem arm2_bgem3 arm3_mdeberta arm4_pipeline_nli arm5_gemini)",
    )
    parser.add_argument(
        "--model-id",
        type=str,
        default="gemini-3.6-flash",
        help="Model ID for Arm 5 LLM Judge",
    )
    parser.add_argument(
        "--conditions",
        nargs="+",
        default=["C1", "C2", "C3"],
        help="Conditions to evaluate (C1, C2, C3)",
    )
    args = parser.parse_args()

    full_suite = get_evaluator_suite(llm_judge_config={"provider": "gemini", "model_id": args.model_id})
    selected_scorers = {k: full_suite[k] for k in args.arms if k in full_suite}
    count = evaluate_dataset(args.input, args.output, selected_scorers, conditions=args.conditions)
    print(f"Evaluated {count} items. Saved to {args.output}")

