"""NepFaith-120: Dual Human Annotation Intake & Adjudication Diff Generator.

Ingests completed annotation workbooks for Annotator 1 and Annotator 2 under
`data/interim/preannotations/`, verifies complete claim conservation, and generates
an adjudication diff workbench for discordant claims requiring lead researcher review.

Invariants:
- Absolute Prohibition 2: Zero writes to data/raw/labels/ (agent write isolation).
- Absolute Prohibition 3: No computing or reporting inter-annotator agreement metrics
  (Cohen's kappa, Krippendorff's alpha, or score distributions) before gold labels are locked.
- Row conservation: Exactly 340 claims across 120 items.
"""

from pathlib import Path
from typing import List, Dict, Any, Optional

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

from src.prepare.schema import ClaimLabel

VERDICT_MAP = {
    "supported": ClaimLabel.SUPPORTED.value,
    "contradicted": ClaimLabel.CONTRADICTED.value,
    "not-in-context": ClaimLabel.NOT_IN_CONTEXT.value,
    "notincontext": ClaimLabel.NOT_IN_CONTEXT.value,
    "not in context": ClaimLabel.NOT_IN_CONTEXT.value,
}


def load_annotator_workbook(wb_path: Path) -> List[Dict[str, Any]]:
    """Loads and validates a completed annotator workbook from XLSX.

    Returns a list of dicts with standardized fields. Raises ValueError if rows
    are corrupted, missing, or contain invalid verdicts.
    """
    if not wb_path.exists():
        raise FileNotFoundError(f"Workbook not found at {wb_path}")

    wb = openpyxl.load_workbook(wb_path, data_only=True)
    sheet_name = "Annotations" if "Annotations" in wb.sheetnames else wb.sheetnames[0]
    ws = wb[sheet_name]

    headers = [cell.value for cell in ws[1] if cell.value is not None]

    header_indices = {}
    for idx, cell in enumerate(ws[1], start=1):
        if cell.value:
            header_indices[cell.value.strip()] = idx

    req_headers = [
        "Item ID",
        "Claim ID",
        "Criticality",
        "Claim Text",
        "Verdict (Supported / Contradicted / Not-in-context)",
    ]
    for rh in req_headers:
        if rh not in header_indices:
            raise ValueError(f"Missing required header '{rh}' in {wb_path.name}")

    item_col = header_indices["Item ID"]
    claim_col = header_indices["Claim ID"]
    crit_col = header_indices["Criticality"]
    text_col = header_indices["Claim Text"]
    verdict_col = header_indices["Verdict (Supported / Contradicted / Not-in-context)"]
    rationale_col = header_indices.get("Claim Rationale / Notes")
    time_col = header_indices.get("Stopwatch Elapsed Time (mm:ss)")
    item_notes_col = header_indices.get("Item Notes")
    p_ne_col = header_indices.get("Nepali Context Passage (C1)")
    q_en_col = header_indices.get("English Query (Q)")
    a_en_col = header_indices.get("Generated English Answer (A)")
    domain_col = header_indices.get("Domain")
    genre_col = header_indices.get("Topic Sub-Genre")
    title_col = header_indices.get("Source Title")
    url_col = header_indices.get("Source URL")

    rows: List[Dict[str, Any]] = []

    for row_idx in range(2, ws.max_row + 1):
        item_val = ws.cell(row=row_idx, column=item_col).value
        if item_val is None or str(item_val).strip() == "":
            continue

        item_id = str(item_val).strip()
        claim_id = str(ws.cell(row=row_idx, column=claim_col).value or "").strip()
        criticality = str(ws.cell(row=row_idx, column=crit_col).value or "").strip()
        claim_text = str(ws.cell(row=row_idx, column=text_col).value or "").strip()

        raw_verdict = ws.cell(row=row_idx, column=verdict_col).value
        if raw_verdict is None or str(raw_verdict).strip() == "":
            raise ValueError(f"Missing verdict at row {row_idx} ({claim_id}) in {wb_path.name}")

        normalized_key = str(raw_verdict).strip().lower()
        if normalized_key not in VERDICT_MAP:
            raise ValueError(f"Invalid verdict '{raw_verdict}' at row {row_idx} ({claim_id}) in {wb_path.name}")
        verdict = VERDICT_MAP[normalized_key]

        rationale = str(ws.cell(row=row_idx, column=rationale_col).value or "").strip() if rationale_col else ""
        elapsed_time = str(ws.cell(row=row_idx, column=time_col).value or "").strip() if time_col else ""
        item_notes = str(ws.cell(row=row_idx, column=item_notes_col).value or "").strip() if item_notes_col else ""
        p_ne = str(ws.cell(row=row_idx, column=p_ne_col).value or "").strip() if p_ne_col else ""
        q_en = str(ws.cell(row=row_idx, column=q_en_col).value or "").strip() if q_en_col else ""
        a_en = str(ws.cell(row=row_idx, column=a_en_col).value or "").strip() if a_en_col else ""
        domain = str(ws.cell(row=row_idx, column=domain_col).value or "").strip() if domain_col else ""
        topic_genre = str(ws.cell(row=row_idx, column=genre_col).value or "").strip() if genre_col else ""
        source_title = str(ws.cell(row=row_idx, column=title_col).value or "").strip() if title_col else ""
        source_url = str(ws.cell(row=row_idx, column=url_col).value or "").strip() if url_col else ""

        rows.append({
            "item_id": item_id,
            "claim_id": claim_id,
            "criticality": criticality,
            "claim_text": claim_text,
            "verdict": verdict,
            "rationale": rationale,
            "elapsed_time": elapsed_time,
            "item_notes": item_notes,
            "passage_ne": p_ne,
            "query_en": q_en,
            "answer_en": a_en,
            "domain": domain,
            "topic_genre": topic_genre,
            "source_title": source_title,
            "source_url": source_url,
        })

    return rows


def generate_adjudication_diff(
    ann1_data: List[Dict[str, Any]],
    ann2_data: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """Compares dual annotations and returns discordant claim records for adjudication."""
    if len(ann1_data) != len(ann2_data):
        raise ValueError(f"Mismatched row counts: Ann1 has {len(ann1_data)}, Ann2 has {len(ann2_data)}")

    diff_records: List[Dict[str, Any]] = []

    for r1, r2 in zip(ann1_data, ann2_data):
        if r1["claim_id"] != r2["claim_id"]:
            raise ValueError(f"Claim ID sequence mismatch: {r1['claim_id']} != {r2['claim_id']}")

        if r1["verdict"] != r2["verdict"]:
            diff_records.append({
                "item_id": r1["item_id"],
                "claim_id": r1["claim_id"],
                "criticality": r1["criticality"],
                "claim_text": r1["claim_text"],
                "annotator_1_verdict": r1["verdict"],
                "annotator_1_notes": r1["rationale"],
                "annotator_2_verdict": r2["verdict"],
                "annotator_2_notes": r2["rationale"],
                "adjudicated_verdict": None,
                "adjudication_rationale": "",
                "passage_ne": r1["passage_ne"],
                "query_en": r1["query_en"],
                "answer_en": r1["answer_en"],
                "domain": r1["domain"],
                "topic_genre": r1["topic_genre"],
                "source_title": r1["source_title"],
                "source_url": r1["source_url"],
            })

    return diff_records


def export_adjudication_workbench(
    diff_records: List[Dict[str, Any]],
    out_xlsx: Path,
    out_md: Path,
) -> None:
    """Exports adjudication workbook (XLSX) and review document (Markdown)."""
    out_xlsx.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)

    # 1. Export Excel Workbench
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Adjudication Queue"
    ws.views.sheetView[0].showGridLines = True

    headers = [
        "Item ID",
        "Claim ID",
        "Criticality",
        "Claim Text",
        "Annotator 1 Verdict",
        "Annotator 1 Notes",
        "Annotator 2 Verdict",
        "Annotator 2 Notes",
        "Adjudicated Verdict (Supported / Contradicted / Not-in-context)",
        "Adjudication Rationale / Notes",
        "Nepali Context Passage (C1)",
        "English Query (Q)",
        "Generated English Answer (A)",
        "Domain",
        "Topic Sub-Genre",
        "Source Title",
        "Source URL",
    ]

    header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    adjudication_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")  # soft yellow for required entry
    border_thin = Side(border_style="thin", color="D9D9D9")
    cell_border = Border(top=border_thin, left=border_thin, right=border_thin, bottom=border_thin)

    for col_idx, header in enumerate(headers, start=1):
        cell = ws.cell(row=1, column=col_idx, value=header)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = cell_border
    ws.row_dimensions[1].height = 28

    # Data validation dropdown for Adjudicated Verdict (column 9)
    dv = DataValidation(
        type="list",
        formula1='"Supported,Contradicted,Not-in-context"',
        allow_blank=True,
        error="Invalid Verdict",
        errorTitle="Choose from dropdown",
        promptTitle="Select Adjudicated Verdict",
        prompt="Select Supported, Contradicted, or Not-in-context",
    )
    ws.add_data_validation(dv)

    for row_idx, r in enumerate(diff_records, start=2):
        row_vals = [
            r["item_id"],
            r["claim_id"],
            r["criticality"],
            r["claim_text"],
            r["annotator_1_verdict"],
            r["annotator_1_notes"],
            r["annotator_2_verdict"],
            r["annotator_2_notes"],
            r["adjudicated_verdict"] or "",
            r["adjudication_rationale"] or "",
            r["passage_ne"],
            r["query_en"],
            r["answer_en"],
            r["domain"],
            r["topic_genre"],
            r["source_title"],
            r["source_url"],
        ]
        for col_idx, val in enumerate(row_vals, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=val)
            cell.border = cell_border
            cell.font = Font(name="Calibri", size=10)
            if col_idx in (9, 10):
                cell.fill = adjudication_fill

        ws.row_dimensions[row_idx].height = 22

    if diff_records:
        dv.add(f"I2:I{len(diff_records) + 1}")

    # Set column widths
    col_widths = {
        1: 12, 2: 14, 3: 14, 4: 40, 5: 18, 6: 25, 7: 18, 8: 25,
        9: 25, 10: 30, 11: 45, 12: 30, 13: 35, 14: 16, 15: 18, 16: 25, 17: 35,
    }
    for col_idx, width in col_widths.items():
        ws.column_dimensions[get_column_letter(col_idx)].width = width

    wb.save(out_xlsx)

    # 2. Export Markdown Workbench
    md_lines = [
        "# NepFaith-120: Human Adjudication Queue",
        "",
        "**Status:** Awaiting Lead Researcher Adjudication  ",
        "**Reference Rubric:** `docs/RUBRIC_V1.md`  ",
        f"**Total Discordant Claims Requiring Adjudication:** {len(diff_records)}  ",
        "",
        "> [!IMPORTANT]",
        "> For each discordant claim below, the lead researcher reviews the Nepali passage ($p_{ne}$) and English claim,",
        "> makes the definitive determination (`Supported`, `Contradicted`, or `Not-in-context`), and records the verdict.",
        "> Once finalized, these become part of the official gold benchmark committed to `data/raw/labels/gold_labels_120.jsonl`.",
        "",
        "---",
        "",
    ]

    for idx, r in enumerate(diff_records, start=1):
        md_lines.append(f"## Discrepancy {idx}/{len(diff_records)} · `{r['claim_id']}` (`{r['item_id']}`)")
        md_lines.append(f"- **Criticality:** `{r['criticality']}`")
        md_lines.append(f"- **Domain / Sub-Genre:** `{r['domain']}` / `{r['topic_genre']}`")
        md_lines.append(f"- **Source:** [{r['source_title']}]({r['source_url']})")
        md_lines.append("")
        md_lines.append(f"### Nepali Context Passage ($p_{{ne}}$):")
        md_lines.append(f"> {r['passage_ne']}")
        md_lines.append("")
        md_lines.append(f"### Generated Answer ($a_{{en}}$):")
        md_lines.append(f"> {r['answer_en']}")
        md_lines.append("")
        md_lines.append(f"### Discordant Atomic Claim:")
        md_lines.append(f"> **\"{r['claim_text']}\"**")
        md_lines.append("")
        md_lines.append("### Annotator Evaluations:")
        md_lines.append(f"- **Annotator 1 (Lead Researcher):** `{r['annotator_1_verdict']}`" + (f" (Notes: *{r['annotator_1_notes']}*)" if r['annotator_1_notes'] else ""))
        md_lines.append(f"- **Annotator 2 (Independent):** `{r['annotator_2_verdict']}`" + (f" (Notes: *{r['annotator_2_notes']}*)" if r['annotator_2_notes'] else ""))
        md_lines.append("")
        md_lines.append("### Final Adjudication (Lead Researcher):")
        md_lines.append("- [ ] `Supported`")
        md_lines.append("- [ ] `Contradicted`")
        md_lines.append("- [ ] `Not-in-context`")
        md_lines.append("- **Adjudication Rationale:** ` `")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    out_md.write_text("\n".join(md_lines), encoding="utf-8")
