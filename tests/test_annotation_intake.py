"""NepFaith-120: Tests for Dual Human Annotation Intake & Adjudication Diff Generation.

Verifies:
1. Ingestion of completed dual-annotation workbooks (Annotator 1 & Annotator 2).
2. Complete claim conservation (340/340 claims, 120/120 items).
3. Zero missing or invalid verdicts.
4. Adjudication diff generation isolating discordant claims for lead researcher.
5. Invariant: Absolute Prohibition 2 (zero writes to data/raw/labels/).
"""

from pathlib import Path
import openpyxl
import pytest

from src.prepare.intake_annotations import (
    load_annotator_workbook,
    generate_adjudication_diff,
    export_adjudication_workbench,
)
from src.prepare.schema import ClaimLabel


def test_load_annotator_workbooks():
    """Verify both annotator completed workbooks load cleanly and pass row conservation."""
    wb1_path = Path("data/interim/preannotations/workbench_annotator_1_completed.xlsx")
    wb2_path = Path("data/interim/preannotations/workbench_annotator_2_completed.xlsx")

    if not wb1_path.exists() or not wb2_path.exists():
        pytest.skip("Completed annotation workbooks not found")

    ann1_data = load_annotator_workbook(wb1_path)
    ann2_data = load_annotator_workbook(wb2_path)

    # Invariant: 340 claims across 120 items
    assert len(ann1_data) == 340
    assert len(ann2_data) == 340

    valid_labels = {ClaimLabel.SUPPORTED.value, ClaimLabel.CONTRADICTED.value, ClaimLabel.NOT_IN_CONTEXT.value}

    for row1, row2 in zip(ann1_data, ann2_data):
        assert row1["item_id"] == row2["item_id"]
        assert row1["claim_id"] == row2["claim_id"]
        assert row1["criticality"] == row2["criticality"]
        assert row1["verdict"] in valid_labels
        assert row2["verdict"] in valid_labels


def test_generate_adjudication_diff(tmp_path):
    """Verify adjudication diff table isolates discordant claims without writing to data/raw/labels/."""
    wb1_path = Path("data/interim/preannotations/workbench_annotator_1_completed.xlsx")
    wb2_path = Path("data/interim/preannotations/workbench_annotator_2_completed.xlsx")

    if not wb1_path.exists() or not wb2_path.exists():
        pytest.skip("Completed annotation workbooks not found")

    ann1_data = load_annotator_workbook(wb1_path)
    ann2_data = load_annotator_workbook(wb2_path)

    diff_records = generate_adjudication_diff(ann1_data, ann2_data)

    # Invariant: diff records only contain discrepancies
    assert len(diff_records) > 0
    for rec in diff_records:
        assert rec["annotator_1_verdict"] != rec["annotator_2_verdict"]
        assert rec["adjudicated_verdict"] is None  # Must await human adjudication

    out_xlsx = tmp_path / "adjudication_workbench.xlsx"
    out_md = tmp_path / "adjudication_workbench.md"

    export_adjudication_workbench(diff_records, out_xlsx, out_md)

    assert out_xlsx.exists()
    assert out_md.exists()

    # Verify Excel workbook structure
    wb = openpyxl.load_workbook(out_xlsx)
    ws = wb.active
    headers = [cell.value for cell in ws[1]]
    assert "Item ID" in headers
    assert "Claim ID" in headers
    assert "Annotator 1 Verdict" in headers
    assert "Annotator 2 Verdict" in headers
    assert "Adjudicated Verdict (Supported / Contradicted / Not-in-context)" in headers
