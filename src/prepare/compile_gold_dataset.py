r"""NepFaith-120: Gold Dataset Compilation & Adjudication Fusion Module.

Combines dual-annotation consensus (321 claims) and lead researcher adjudications (19 claims)
from `data/interim/preannotations/adjudication_workbench.md`, computes item-level binary
faithfulness ($Y_i$) using the pre-registered critical claim override rule, and stages the
compiled gold benchmark for researcher verification.

Invariants:
- Absolute Prohibition 2: The agent NEVER writes to `data/raw/labels/`. Outputs strictly staged in `data/interim/`.
- Absolute Prohibition 3: Zero calculation or reporting of inter-annotator agreement metrics ($\kappa, \alpha$).
- Absolute Prohibition 4: Strict item and claim conservation (120 items, 340 claims).
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional

from src.prepare.schema import EvaluationItem, AtomicClaim, ClaimLabel
from src.prepare.intake_annotations import load_annotator_workbook, VERDICT_MAP


def parse_adjudications_from_markdown(md_path: Path) -> Dict[str, str]:
    """Parses completed researcher adjudications from adjudication_workbench.md."""
    if not md_path.exists():
        raise FileNotFoundError(f"Adjudication workbench not found at {md_path}")

    text = md_path.read_text(encoding="utf-8")
    blocks = text.split("## Discrepancy ")[1:]

    adjudications: Dict[str, str] = {}

    for idx, block in enumerate(blocks, start=1):
        header_line = block.splitlines()[0]
        claim_match = re.search(r"`([^`]+)`\s*\(`([^`]+)`\)", header_line)
        if not claim_match:
            raise ValueError(f"Could not parse Claim ID from discrepancy block {idx}: {header_line}")
        claim_id = claim_match.group(1).strip()

        checked: List[str] = []
        for line in block.splitlines():
            m = re.match(r"-\s*\[([xX])\]\s*`([^`]+)`", line.strip())
            if m:
                checked.append(m.group(2).strip())

        if len(checked) == 0:
            raise ValueError(f"Missing adjudicated verdict for claim '{claim_id}' in block {idx}")
        if len(checked) > 1:
            raise ValueError(f"Multiple conflicting verdicts checked for claim '{claim_id}' in block {idx}: {checked}")

        raw_verdict = checked[0]
        norm_key = raw_verdict.strip().lower()
        if norm_key not in VERDICT_MAP:
            raise ValueError(f"Invalid verdict '{raw_verdict}' for claim '{claim_id}' in block {idx}")

        adjudications[claim_id] = VERDICT_MAP[norm_key]

    return adjudications


def compile_gold_dataset(
    ann1_workbook: Path,
    ann2_workbook: Path,
    adjudication_md: Path,
    candidates_jsonl: Path,
    output_items_path: Path,
    output_claims_path: Optional[Path] = None,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Compiles the verified gold benchmark from consensus, adjudications, and candidate items.

    Enforces Absolute Prohibition 2: Never writes to data/raw/labels/.
    """
    # Enforce Absolute Prohibition 2
    raw_labels_dir = Path("data/raw/labels").resolve()
    if output_items_path.resolve().is_relative_to(raw_labels_dir):
        raise PermissionError("Agent write isolation: Output cannot be written directly to data/raw/labels/")
    if output_claims_path and output_claims_path.resolve().is_relative_to(raw_labels_dir):
        raise PermissionError("Agent write isolation: Output cannot be written directly to data/raw/labels/")

    # 1. Load dual annotations
    ann1_rows = load_annotator_workbook(ann1_workbook)
    ann2_rows = load_annotator_workbook(ann2_workbook)

    if len(ann1_rows) != len(ann2_rows):
        raise ValueError(f"Mismatched row counts: Ann1 has {len(ann1_rows)}, Ann2 has {len(ann2_rows)}")

    # 2. Parse adjudications
    adjudications = parse_adjudications_from_markdown(adjudication_md)

    # 3. Fuse claim-level ground truth
    gold_claims_map: Dict[str, str] = {}
    for r1, r2 in zip(ann1_rows, ann2_rows):
        cid = r1["claim_id"]
        v1 = r1["verdict"]
        v2 = r2["verdict"]

        if v1 == v2:
            gold_claims_map[cid] = v1
        else:
            if cid not in adjudications:
                raise ValueError(f"Discordant claim '{cid}' missing from adjudication file")
            gold_claims_map[cid] = adjudications[cid]

    # 4. Ingest into candidate items
    items: List[Dict[str, Any]] = []
    with open(candidates_jsonl, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                items.append(json.loads(line))

    if len(items) != 120:
        raise ValueError(f"Expected 120 candidate items, got {len(items)}")

    compiled_items: List[Dict[str, Any]] = []
    compiled_claims: List[Dict[str, Any]] = []

    for it_dict in items:
        # Reconstruct atomic claims with gold labels
        updated_claims: List[AtomicClaim] = []
        for c_dict in it_dict.get("claims", []):
            cid = c_dict["claim_id"]
            if cid not in gold_claims_map:
                raise ValueError(f"Missing gold label for claim '{cid}' in item '{it_dict['item_id']}'")

            gold_val = ClaimLabel(gold_claims_map[cid])
            c_obj = AtomicClaim(
                claim_id=cid,
                claim_text=c_dict["claim_text"],
                is_critical=c_dict.get("is_critical", True),
                gold_label=gold_val,
                c1_pred=c_dict.get("c1_pred"),
                c2_pred=c_dict.get("c2_pred"),
                c3_pred=c_dict.get("c3_pred"),
            )
            updated_claims.append(c_obj)
            compiled_claims.append({
                "claim_id": cid,
                "item_id": it_dict["item_id"],
                "domain": it_dict["domain"],
                "sub_genre": it_dict.get("sub_genre"),
                "claim_text": c_dict["claim_text"],
                "is_critical": c_dict.get("is_critical", True),
                "gold_label": gold_val.value,
            })

        # Validate with EvaluationItem and compute derived label
        it_dict["claims"] = [c.model_dump() for c in updated_claims]
        eval_item = EvaluationItem.model_validate(it_dict)
        derived_label = eval_item.compute_derived_label()
        eval_item.derived_item_label = derived_label

        compiled_items.append(eval_item.model_dump())

    # 5. Write staging outputs
    output_items_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_items_path, "w", encoding="utf-8") as f:
        for it in compiled_items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")

    if output_claims_path:
        output_claims_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_claims_path, "w", encoding="utf-8") as f:
            for c in compiled_claims:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")

    return compiled_items, compiled_claims


if __name__ == "__main__":
    wb1 = Path("data/interim/preannotations/workbench_annotator_1_completed.xlsx")
    wb2 = Path("data/interim/preannotations/workbench_annotator_2_completed.xlsx")
    adj = Path("data/interim/preannotations/adjudication_workbench.md")
    cand = Path("data/interim/preannotations/gold_candidates_120.jsonl")

    out_items = Path("data/interim/preannotations/candidate_gold_labels_120.jsonl")
    out_claims = Path("data/interim/preannotations/candidate_gold_claims_120.jsonl")

    items, claims = compile_gold_dataset(wb1, wb2, adj, cand, out_items, out_claims)
    print(f"Successfully compiled {len(items)} items and {len(claims)} claims into {out_items}")
