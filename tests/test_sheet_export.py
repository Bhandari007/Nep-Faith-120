"""Tests for Human Annotation Spreadsheet Exporter (XLSX / CSV).

Verifies that human-friendly spreadsheet workbenches are exported correctly
for Annotator 1 and Annotator 2 (and C3 post-editing) to allow frictionless
collaboration via Excel or Google Sheets.

Invariants:
- Zero writes to data/raw/labels/.
- Evaluators blinded to perturbation types.
- All 120 items and all 340 atomic claims represented.
- Essential columns and data validation for Verdict present.
"""

from pathlib import Path
import csv
import pytest
import openpyxl


def test_export_annotation_sheets(tmp_path):
    """Verifies dual annotation spreadsheet generation (XLSX and CSV)."""
    from src.prepare.export_sheets import export_annotation_sheets

    candidates_path = Path("data/interim/preannotations/gold_candidates_120.jsonl")
    if not candidates_path.exists():
        pytest.skip("gold_candidates_120.jsonl not found")

    out_xlsx_1 = tmp_path / "workbench_annotator_1.xlsx"
    out_xlsx_2 = tmp_path / "workbench_annotator_2.xlsx"
    out_csv_1 = tmp_path / "workbench_annotator_1.csv"
    out_csv_2 = tmp_path / "workbench_annotator_2.csv"

    export_annotation_sheets(
        candidates_path=candidates_path,
        output_xlsx_1=out_xlsx_1,
        output_xlsx_2=out_xlsx_2,
        output_csv_1=out_csv_1,
        output_csv_2=out_csv_2,
    )

    # 1. Verify files exist
    assert out_xlsx_1.exists()
    assert out_xlsx_2.exists()
    assert out_csv_1.exists()
    assert out_csv_2.exists()

    # 2. Verify CSV content
    with open(out_csv_2, "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        assert len(reader) == 340, f"Expected 340 claim rows, got {len(reader)}"

        first_row = reader[0]
        assert "Item ID" in first_row
        assert "Claim ID" in first_row
        assert "Criticality" in first_row
        assert "Claim Text" in first_row
        assert "Verdict (Supported / Contradicted / Not-in-context)" in first_row
        assert "Nepali Context Passage (C1)" in first_row
        assert "Stopwatch Elapsed Time (mm:ss)" in first_row

        # Verify blinding: no perturbation type column or leakage
        assert "perturbation_type" not in first_row
        for row in reader:
            assert row["Verdict (Supported / Contradicted / Not-in-context)"] == ""  # Unfilled

    # 3. Verify XLSX structure and validation
    wb = openpyxl.load_workbook(out_xlsx_2)
    assert "Annotations" in wb.sheetnames
    assert "Instructions & Rubric" in wb.sheetnames

    ws = wb["Annotations"]
    assert ws.max_row == 341  # 1 header row + 340 claim rows

    # Verify data validation exists for the Verdict column
    assert len(ws.data_validations.dataValidation) > 0

    wb.close()


def test_export_c3_sheet(tmp_path):
    """Verifies Condition C3 post-editing spreadsheet generation."""
    from src.prepare.export_sheets import export_c3_sheet

    candidates_path = Path("data/interim/preannotations/gold_candidates_120.jsonl")
    if not candidates_path.exists():
        pytest.skip("gold_candidates_120.jsonl not found")

    out_xlsx = tmp_path / "post_edit_c3_workbench.xlsx"
    out_csv = tmp_path / "post_edit_c3_workbench.csv"

    export_c3_sheet(
        candidates_path=candidates_path,
        output_xlsx=out_xlsx,
        output_csv=out_csv,
    )

    assert out_xlsx.exists()
    assert out_csv.exists()

    with open(out_csv, "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        assert len(reader) == 60, f"Expected 60 unique passages, got {len(reader)}"

        first_row = reader[0]
        assert "Passage Index" in first_row
        assert "Source Passage (Nepali · C1)" in first_row
        assert "Raw IndicTrans2 MT (Condition C2)" in first_row
        assert "Post-Edited Translation Slot (Condition C3)" in first_row
        assert "Stopwatch Elapsed Time (mm:ss)" in first_row
        # Pre-populated with C2 for minimal edit distance
        assert first_row["Post-Edited Translation Slot (Condition C3)"] == first_row["Raw IndicTrans2 MT (Condition C2)"]

    wb = openpyxl.load_workbook(out_xlsx)
    assert "C3 Post-Editing" in wb.sheetnames
    wb.close()
