"""NepFaith-120: Human Annotation Spreadsheet Exporter (XLSX / CSV).

Generates human-friendly dual-annotation spreadsheets and Condition C3 post-editing
workbooks under data/interim/preannotations/ to allow seamless collaboration via
Microsoft Excel, Google Sheets, or LibreOffice Calc.

Invariants:
- Zero writes to data/raw/labels/ (physical label isolation).
- Evaluators are strictly blinded to perturbation types and synthetic spans.
- Claims explicitly demarcated with CRITICAL or NON-CRITICAL indicators.
- Dropdown data validation configured for the 3 rubric verdicts:
  Supported, Contradicted, Not-in-context.
- Stopwatch timing and notes fields included for every item.
"""

import csv
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter


VERDICT_OPTIONS = ["Supported", "Contradicted", "Not-in-context"]

INSTRUCTIONS_TEXT = """NepFaith-120 Human Annotation Workbench
===============================================
Annotator: {annotator_name}
Reference Rubric: docs/RUBRIC_V1.md

INSTRUCTIONS FOR ANNOTATORS:
----------------------------
1. Core Task:
   Read the Nepali Context Passage (Condition C1) and the English Generated Answer.

2. Atomic Claim Evaluation:
   For every atomic claim in the "Annotations" tab, choose one of the three verdicts from the dropdown:
   - Supported: The claim is directly stated or logically entailed by the Nepali passage.
   - Contradicted: The claim directly contradicts facts explicitly asserted in the Nepali passage.
   - Not-in-context: The claim makes assertions completely absent, ungrounded, or unverifiable from the passage.

3. Claim Criticality:
   - CRITICAL: Essential factual proposition. If contradicted or ungrounded, the answer fails factual trust.
   - NON-CRITICAL: Secondary background context or supplementary detail.

4. Stopwatch Timing:
   Start your stopwatch before reading the passage and query.
   When you finish evaluating all claims for that item, record the elapsed time in mm:ss (e.g. 01:15).

5. Notes:
   Use the "Claim Rationale" or "Item Notes" columns to note any ambiguities, nuance, or edge cases.

HOW TO USE IN EXCEL / GOOGLE SHEETS:
-----------------------------------
- Switch to the "Annotations" tab.
- Click on cell in the "Verdict" column to select from the dropdown menu.
- Text cells have line-wrap enabled for easy reading.
"""

C3_INSTRUCTIONS_TEXT = """NepFaith-120 Condition C3 Post-Editing Workbench
================================================
Reference: docs/RUBRIC_V1.md · Minimal-Pair Translation Correction

PRINCIPLES FOR CONDITION C3 POST-EDITING:
-----------------------------------------
Goal: Isolate the Machine Translation Error Gap:
      Δ_MT = Accuracy(C3) - Accuracy(C2)

Rules:
1. Minimal Edit Distance:
   Start from the Raw IndicTrans2 translation (pre-filled in column 'Post-Edited Translation Slot (Condition C3)').
   Edit ONLY what is factually, syntactically, or semantically mistranslated.
   Do NOT rewrite fluent sentences merely to improve personal writing style.

2. Entity & Number Precision:
   Fix mistranslated proper nouns, names, dates, numbers, and units.

3. Evidentials & Epistemic Stance:
   Preserve uncertainty and hearsay markers (e.g., "भनिन्छ", "दाबी गरिएको छ").

4. Polarities & Negation:
   Ensure negation markers ("छैन", "होइन") are accurately reflected without inversion.

5. Clean / No Edit Needed:
   If the raw machine translation is already accurate and faithful, leave the slot unchanged.

6. Timing:
   Record elapsed stopwatch time (mm:ss) per passage.
"""


def load_candidate_items(candidates_path: Path) -> List[Dict[str, Any]]:
    """Loads candidate items from jsonl file."""
    candidates_path = Path(candidates_path)
    if not candidates_path.exists():
        raise FileNotFoundError(f"Candidate file not found: {candidates_path}")

    items: List[Dict[str, Any]] = []
    with open(candidates_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items


def export_annotation_sheets(
    candidates_path: Path = Path("data/interim/preannotations/gold_candidates_120.jsonl"),
    output_xlsx_1: Path = Path("data/interim/preannotations/workbench_annotator_1.xlsx"),
    output_xlsx_2: Path = Path("data/interim/preannotations/workbench_annotator_2.xlsx"),
    output_csv_1: Path = Path("data/interim/preannotations/workbench_annotator_1.csv"),
    output_csv_2: Path = Path("data/interim/preannotations/workbench_annotator_2.csv"),
):
    """Exports dual annotation spreadsheets in XLSX and CSV formats."""
    # Hard prohibition check
    for p in [output_xlsx_1, output_xlsx_2, output_csv_1, output_csv_2]:
        assert "data/raw/labels" not in str(p), f"PROHIBITION: Cannot write to gold label directory: {p}"

    items = load_candidate_items(candidates_path)

    # Prepare tabular data
    headers = [
        "Item ID",
        "Claim ID",
        "Criticality",
        "Claim Text",
        "Verdict (Supported / Contradicted / Not-in-context)",
        "Claim Rationale / Notes",
        "Stopwatch Elapsed Time (mm:ss)",
        "Item Notes",
        "Nepali Context Passage (C1)",
        "English Query (Q)",
        "Generated English Answer (A)",
        "Domain",
        "Topic Sub-Genre",
        "Source Title",
        "Source URL",
    ]

    rows = []
    for item in items:
        item_id = item["item_id"]
        domain = item.get("domain", "")
        sub_genre = item.get("sub_genre", "")
        passage_ne = item.get("passage_ne", "").strip()
        query_en = item.get("query_en", "").strip()
        answer_en = item.get("answer_en", "").strip()
        source_title = item.get("source_title", "")
        source_url = item.get("source_url", "")
        claims = item.get("claims", [])

        for c_idx, claim in enumerate(claims, start=1):
            claim_id = claim.get("claim_id", f"{item_id}_c{c_idx}")
            claim_text = claim.get("claim_text", "").strip()
            is_critical = claim.get("is_critical", False)
            crit_label = "CRITICAL" if is_critical else "NON-CRITICAL"

            # In the spreadsheet, time and item notes can be populated on row or per item
            rows.append({
                "Item ID": item_id,
                "Claim ID": claim_id,
                "Criticality": crit_label,
                "Claim Text": claim_text,
                "Verdict (Supported / Contradicted / Not-in-context)": "",
                "Claim Rationale / Notes": "",
                "Stopwatch Elapsed Time (mm:ss)": "",
                "Item Notes": "",
                "Nepali Context Passage (C1)": passage_ne,
                "English Query (Q)": query_en,
                "Generated English Answer (A)": answer_en,
                "Domain": domain,
                "Topic Sub-Genre": sub_genre,
                "Source Title": source_title,
                "Source URL": source_url,
            })

    # Export CSVs
    for csv_path in [output_csv_1, output_csv_2]:
        csv_path = Path(csv_path)
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)

    # Export XLSXs with styling and data validation
    for xlsx_path, annotator_name in [(output_xlsx_1, "Annotator 1"), (output_xlsx_2, "Annotator 2")]:
        _build_annotation_workbook(xlsx_path, annotator_name, headers, rows)


def _build_annotation_workbook(
    xlsx_path: Path,
    annotator_name: str,
    headers: List[str],
    rows: List[Dict[str, str]],
):
    """Builds a formatted Excel workbook with validation and guidelines."""
    wb = openpyxl.Workbook()

    # Sheet 1: Instructions & Rubric
    ws_inst = wb.active
    ws_inst.title = "Instructions & Rubric"
    ws_inst.views.sheetView[0].showGridLines = True

    font_title = Font(name="Calibri", size=14, bold=True, color="1F4E78")
    font_body = Font(name="Consolas", size=11, color="000000")

    ws_inst.column_dimensions["A"].width = 100
    for row_idx, line in enumerate(INSTRUCTIONS_TEXT.format(annotator_name=annotator_name).split("\n"), start=1):
        cell = ws_inst.cell(row=row_idx, column=1, value=line)
        cell.font = font_title if row_idx <= 2 else font_body

    # Sheet 2: Annotations
    ws = wb.create_sheet(title="Annotations")
    ws.views.sheetView[0].showGridLines = True

    # Styling definitions
    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    critical_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")  # soft yellow
    border_thin = Side(border_style="thin", color="D9D9D9")
    cell_border = Border(top=border_thin, left=border_thin, right=border_thin, bottom=border_thin)

    # Write headers
    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = cell_border
    ws.row_dimensions[1].height = 28

    # Data validation dropdown for Verdict (Column 5)
    dv = DataValidation(
        type="list",
        formula1=f'"{",".join(VERDICT_OPTIONS)}"',
        allow_blank=True,
        error="Invalid Verdict",
        errorTitle="Choose from dropdown",
        promptTitle="Select Verdict",
        prompt="Select Supported, Contradicted, or Not-in-context",
    )
    ws.add_data_validation(dv)

    # Write data rows
    for row_idx, r_data in enumerate(rows, start=2):
        is_crit = r_data["Criticality"] == "CRITICAL"
        for col_idx, header in enumerate(headers, start=1):
            val = r_data[header]
            cell = ws.cell(row=row_idx, column=col_idx, value=val)
            cell.border = cell_border
            cell.font = Font(name="Calibri", size=10)

            # Alignment & wrapping
            if col_idx in [1, 2, 3, 5, 7, 12, 13]:
                cell.alignment = Alignment(horizontal="center", vertical="top")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

            # Highlight critical claims
            if is_crit and col_idx == 3:
                cell.fill = critical_fill
                cell.font = Font(name="Calibri", size=10, bold=True, color="C00000")

            # Link hyperlink
            if col_idx == 15 and val.startswith("http"):
                cell.hyperlink = val
                cell.font = Font(name="Calibri", size=10, color="0563C1", underline="single")

        ws.row_dimensions[row_idx].height = 55

    # Apply data validation range to column E (Verdict)
    dv.add(f"E2:E{len(rows) + 1}")

    # Column widths
    col_widths = {
        1: 12,  # Item ID
        2: 15,  # Claim ID
        3: 16,  # Criticality
        4: 40,  # Claim Text
        5: 22,  # Verdict
        6: 25,  # Claim Notes
        7: 18,  # Stopwatch
        8: 20,  # Item Notes
        9: 45,  # Nepali Passage
        10: 30, # Query
        11: 35, # Answer
        12: 14, # Domain
        13: 18, # Sub-genre
        14: 20, # Source Title
        15: 30, # Source URL
    }
    for col_idx, width in col_widths.items():
        col_letter = get_column_letter(col_idx)
        ws.column_dimensions[col_letter].width = width

    # Freeze top row
    ws.freeze_panes = "A2"

    xlsx_path = Path(xlsx_path)
    xlsx_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(xlsx_path)
    wb.close()


def export_c3_sheet(
    candidates_path: Path = Path("data/interim/preannotations/gold_candidates_120.jsonl"),
    output_xlsx: Path = Path("data/interim/preannotations/post_edit_c3_workbench.xlsx"),
    output_csv: Path = Path("data/interim/preannotations/post_edit_c3_workbench.csv"),
):
    """Exports Condition C3 minimal-pair human post-editing sheets in XLSX and CSV."""
    assert "data/raw/labels" not in str(output_xlsx), "PROHIBITION: Cannot write to gold label directory"
    assert "data/raw/labels" not in str(output_csv), "PROHIBITION: Cannot write to gold label directory"

    items = load_candidate_items(candidates_path)

    # Group by unique passage
    passage_groups: Dict[str, Dict[str, Any]] = {}
    for item in items:
        p_ne = item.get("passage_ne", "").strip()
        item_id = item["item_id"]
        c2_mt = item.get("c2_raw_mt", "").strip()
        domain = item.get("domain", "")
        sub_genre = item.get("sub_genre", "")
        source_title = item.get("source_title", "")
        source_url = item.get("source_url", "")

        if p_ne not in passage_groups:
            passage_groups[p_ne] = {
                "passage_ne": p_ne,
                "c2_raw_mt": c2_mt,
                "linked_items": [item_id],
                "domain": domain,
                "sub_genre": sub_genre,
                "source_title": source_title,
                "source_url": source_url,
            }
        else:
            passage_groups[p_ne]["linked_items"].append(item_id)

    headers = [
        "Passage Index",
        "Linked Candidate Items",
        "Domain",
        "Topic Sub-Genre",
        "Source Title",
        "Source URL",
        "Source Passage (Nepali · C1)",
        "Raw IndicTrans2 MT (Condition C2)",
        "Post-Edited Translation Slot (Condition C3)",
        "Stopwatch Elapsed Time (mm:ss)",
        "Error Types Corrected",
        "Editor Notes / Justification",
    ]

    rows = []
    for idx, (p_ne, group) in enumerate(passage_groups.items(), start=1):
        items_str = ", ".join(group["linked_items"])
        rows.append({
            "Passage Index": f"Passage_{idx:02d}",
            "Linked Candidate Items": items_str,
            "Domain": group["domain"],
            "Topic Sub-Genre": group["sub_genre"],
            "Source Title": group["source_title"],
            "Source URL": group["source_url"],
            "Source Passage (Nepali · C1)": p_ne,
            "Raw IndicTrans2 MT (Condition C2)": group["c2_raw_mt"],
            "Post-Edited Translation Slot (Condition C3)": group["c2_raw_mt"],  # Initialized to C2 for minimal edit distance
            "Stopwatch Elapsed Time (mm:ss)": "",
            "Error Types Corrected": "",
            "Editor Notes / Justification": "",
        })

    # Export CSV
    output_csv = Path(output_csv)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    with open(output_csv, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    # Export XLSX
    output_xlsx = Path(output_xlsx)
    output_xlsx.parent.mkdir(parents=True, exist_ok=True)

    wb = openpyxl.Workbook()

    # Instructions Sheet
    ws_inst = wb.active
    ws_inst.title = "Post-Editing Principles"
    ws_inst.views.sheetView[0].showGridLines = True
    ws_inst.column_dimensions["A"].width = 100

    font_title = Font(name="Calibri", size=14, bold=True, color="1F4E78")
    font_body = Font(name="Consolas", size=11, color="000000")
    for row_idx, line in enumerate(C3_INSTRUCTIONS_TEXT.split("\n"), start=1):
        cell = ws_inst.cell(row=row_idx, column=1, value=line)
        cell.font = font_title if row_idx <= 2 else font_body

    # C3 Sheet
    ws = wb.create_sheet(title="C3 Post-Editing")
    ws.views.sheetView[0].showGridLines = True

    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    editable_fill = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")  # soft green
    border_thin = Side(border_style="thin", color="D9D9D9")
    cell_border = Border(top=border_thin, left=border_thin, right=border_thin, bottom=border_thin)

    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = cell_border
    ws.row_dimensions[1].height = 28

    for row_idx, r_data in enumerate(rows, start=2):
        for col_idx, header in enumerate(headers, start=1):
            val = r_data[header]
            cell = ws.cell(row=row_idx, column=col_idx, value=val)
            cell.border = cell_border
            cell.font = Font(name="Calibri", size=10)

            if col_idx in [1, 2, 3, 4, 10]:
                cell.alignment = Alignment(horizontal="center", vertical="top")
            else:
                cell.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)

            # Highlight C3 slot so human knows where to edit
            if col_idx == 9:
                cell.fill = editable_fill
                cell.font = Font(name="Calibri", size=10, bold=True, color="274E13")

            if col_idx == 6 and val.startswith("http"):
                cell.hyperlink = val
                cell.font = Font(name="Calibri", size=10, color="0563C1", underline="single")

        ws.row_dimensions[row_idx].height = 80

    col_widths = {
        1: 15,  # Passage Index
        2: 22,  # Linked Items
        3: 14,  # Domain
        4: 18,  # Sub-Genre
        5: 20,  # Source Title
        6: 28,  # Source URL
        7: 48,  # Nepali Passage
        8: 48,  # Raw C2 MT
        9: 48,  # C3 Slot
        10: 18, # Stopwatch
        11: 30, # Error Types
        12: 30, # Notes
    }
    for col_idx, width in col_widths.items():
        col_letter = get_column_letter(col_idx)
        ws.column_dimensions[col_letter].width = width

    ws.freeze_panes = "A2"
    wb.save(output_xlsx)
    wb.close()


def export_all_spreadsheets():
    """Generates all workbenches and sheets for Sprint 2."""
    print("Exporting dual-annotation spreadsheets (XLSX / CSV)...")
    export_annotation_sheets()
    print("Exporting Condition C3 post-editing spreadsheets (XLSX / CSV)...")
    export_c3_sheet()
    print("All spreadsheets successfully generated in data/interim/preannotations/.")


if __name__ == "__main__":
    export_all_spreadsheets()
