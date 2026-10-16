# Human Dual-Annotation Workbench & Tooling Setup

Type: engineering / tooling
Status: Clearance proposed — awaiting researcher
Cap: 1 day (workbench generation script, dual sheets, and pilot stopwatch harness)

## Question

Build and export human dual-annotation workbenches to `data/interim/preannotations/` to allow seamless, frictionless annotation for Annotator 1 and Annotator 2:
1. Export structured annotation workbenches:
   - `data/interim/preannotations/workbench_annotator_1.md`
   - `data/interim/preannotations/workbench_annotator_2.md`
2. Each item display must include:
   - Item ID, Domain, Provenance metadata (blinded from evaluator during scoring).
   - Passage in Nepali ($C1$).
   - English Query and Generated English Answer.
   - List of atomic claims with `[is_critical]` indicators.
   - 3 selectable options per claim: `[ ] Supported`, `[ ] Contradicted`, `[ ] Not-in-context`.
   - Elapsed stopwatch entry field (`mm:ss`).
   - Notes / justification field.
3. Formatted to ensure zero JSON wrangling for human annotators.
4. Compliant with `docs/RUBRIC_V1.md` and `docs/PILOT_ANNOTATION_SHEET.md`.

## Findings & Evidence (agent)

- **Workbench Generation & Verification:**
  - Implemented `export_annotation_workbenches` in `src/prepare/export_workbenches.py`.
  - Generated dual markdown files:
    - `data/interim/preannotations/workbench_annotator_1.md` (5,821 lines, 264 KB)
    - `data/interim/preannotations/workbench_annotator_2.md` (5,821 lines, 264 KB)
  - Complete coverage: All 120 items and all 340 claims rendered with clear checkboxes:
    - `[ ] Supported`
    - `[ ] Contradicted`
    - `[ ] Not-in-context`
  - Criticality tagging: All critical claims explicitly demarcated with `**[CRITICAL CLAIM]**` and non-critical claims with `*[NON-CRITICAL CLAIM]*`.
  - Blinded protocol: Perturbation categories and synthetic perturbation spans are strictly omitted from item text to prevent annotator bias.
  - Ergonomics: Standardized stopwatch timing fields (`Stopwatch Elapsed Time: [ mm:ss ]`) and item/claim notes fields included.
  - **Spreadsheet Workbenches (XLSX / CSV for Excel and Google Sheets):**
    - Implemented `export_annotation_sheets` and `export_c3_sheet` in `src/prepare/export_sheets.py`.
    - Generated styled Excel workbooks with dropdown data validation (`Supported`, `Contradicted`, `Not-in-context`), instructions tabs, frozen header panes, and auto-wrapped text:
      - `data/interim/preannotations/workbench_annotator_1.xlsx` (76 KB)
      - `data/interim/preannotations/workbench_annotator_2.xlsx` (76 KB)
      - `data/interim/preannotations/post_edit_c3_workbench.xlsx` (37 KB)
    - Generated standardized CSV equivalents for 1-click import into Google Sheets:
      - `data/interim/preannotations/workbench_annotator_1.csv` (510 KB, 340 claim rows)
      - `data/interim/preannotations/workbench_annotator_2.csv` (510 KB, 340 claim rows)
      - `data/interim/preannotations/post_edit_c3_workbench.csv` (110 KB, 60 unique passages)
  - Invariant tests: `tests/test_workbench_export.py` and `tests/test_sheet_export.py` passing (38/38 repo tests green). Zero writes to `data/raw/labels/`.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
