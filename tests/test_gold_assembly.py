"""NepFaith-120: Tests for Gold Dataset Compilation & Invariant Verification.

Verifies:
1. Parsing of completed researcher adjudications from `adjudication_workbench.md`.
2. Compilation of consensus + adjudicated claim verdicts into gold labels.
3. Pre-registered critical claim override rule for derived item faithfulness ($Y_i$).
4. Absolute Prohibition 2: Zero writes to `data/raw/labels/` (all outputs strictly staged in `data/interim/`).
5. Complete row and item conservation (120/120 items, 340/340 claims).
"""

from pathlib import Path
import json
import pytest

from src.prepare.compile_gold_dataset import (
    parse_adjudications_from_markdown,
    compile_gold_dataset,
)
from src.prepare.schema import EvaluationItem, ClaimLabel


def test_parse_adjudications():
    """Verify parsing of the 19 researcher adjudications."""
    md_path = Path("data/interim/preannotations/adjudication_workbench.md")
    if not md_path.exists():
        pytest.skip("adjudication_workbench.md not found")

    adjudications = parse_adjudications_from_markdown(md_path)
    assert len(adjudications) == 19

    valid_labels = {ClaimLabel.SUPPORTED.value, ClaimLabel.CONTRADICTED.value, ClaimLabel.NOT_IN_CONTEXT.value}
    for claim_id, verdict in adjudications.items():
        assert verdict in valid_labels


def test_compile_gold_dataset(tmp_path):
    """Verify end-to-end gold dataset compilation and schema invariants."""
    wb1_path = Path("data/interim/preannotations/workbench_annotator_1_completed.xlsx")
    wb2_path = Path("data/interim/preannotations/workbench_annotator_2_completed.xlsx")
    adj_path = Path("data/interim/preannotations/adjudication_workbench.md")
    candidates_path = Path("data/interim/preannotations/gold_candidates_120.jsonl")

    if not all(p.exists() for p in [wb1_path, wb2_path, adj_path, candidates_path]):
        pytest.skip("Required input files for gold compilation missing")

    out_items_path = tmp_path / "candidate_gold_labels_120.jsonl"
    out_claims_path = tmp_path / "candidate_gold_claims_120.jsonl"

    items, claims = compile_gold_dataset(
        ann1_workbook=wb1_path,
        ann2_workbook=wb2_path,
        adjudication_md=adj_path,
        candidates_jsonl=candidates_path,
        output_items_path=out_items_path,
        output_claims_path=out_claims_path,
    )

    # 1. Invariant: 120 items, 340 claims
    assert len(items) == 120
    assert len(claims) == 340

    assert out_items_path.exists()
    assert out_claims_path.exists()

    # 2. Strict schema verification using Pydantic model
    total_claims = 0
    for it in items:
        eval_item = EvaluationItem.model_validate(it)
        assert eval_item.derived_item_label is not None
        assert isinstance(eval_item.derived_item_label, bool)

        # Critical claim override invariant check:
        has_critical_failure = any(
            c.is_critical and c.gold_label in (ClaimLabel.CONTRADICTED, ClaimLabel.NOT_IN_CONTEXT)
            for c in eval_item.claims
        )
        if has_critical_failure:
            assert eval_item.derived_item_label is False

        all_supported = all(c.gold_label == ClaimLabel.SUPPORTED for c in eval_item.claims)
        if all_supported:
            assert eval_item.derived_item_label is True

        total_claims += len(eval_item.claims)

    assert total_claims == 340

    # 3. Absolute Prohibition 2: verify compile_gold_dataset blocks direct writes to data/raw/labels/
    with pytest.raises(PermissionError):
        compile_gold_dataset(
            ann1_workbook=wb1_path,
            ann2_workbook=wb2_path,
            adjudication_md=adj_path,
            candidates_jsonl=candidates_path,
            output_items_path=Path("data/raw/labels/blocked.jsonl"),
        )
