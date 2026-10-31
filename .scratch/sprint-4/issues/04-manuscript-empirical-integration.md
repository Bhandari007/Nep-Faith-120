# Ticket 04 · Manuscript Empirical Integration & Paper Gate Clearance

Type: paper / governance
Status: Cleared - [MB, October 31, 2026]
Cap: 1.0 day

## Question

Can we satisfy the 6-question paper gate in `docs/CODING_STANDARDS.md` and integrate verified empirical numbers into `paper/notes/` and draft the empirical updates in `paper/dossier/03-methodology.md` and `paper/dossier/04-statistical-framework.md`?

## Criteria
1. Complete 6-question paper gate audit.
2. Verified provenance of all reported numbers from reproducible artifacts.
3. Updated methodology and statistical framework drafts in `paper/dossier/`.
4. Bibliography citation checks confirmed.

## Findings & Evidence (agent)

- **2026-10-31 (Manuscript Empirical Integration & Paper Gate Clearance)**:
  - Conducted full 6-question Paper Gate audit (`docs/CODING_STANDARDS.md` Section 6), recorded in `paper/notes/06-unblinded-empirical-results.md`.
  - Confirmed 1-command reproducibility: `PYTHONPATH=. python src/run/run_analysis_pipeline.py --gold data/raw/labels/gold_labels_120.jsonl --table1-out reports/table1_decomposition.tex --table2-out reports/table2_sensitivity.tex`.
  - Confirmed code predates labels by tag (`sprint-1-frozen` vs `gate-2-cleared`), with 0 startup diff on `src/analyze/` and `src/report/`.
  - Confirmed recovery test passed on planted effect (`tests/recovery/test_ppi_recovery.py`).
  - Confirmed row count conservation ($n=120, N=1,200$, 0 dropped).
  - Confirmed metadata stamping (`outputs/run_summary_20261031_032903.json`).
  - Staged empirical tables and subgroup numbers into `paper/notes/06-unblinded-empirical-results.md` for lead researcher review.
  - Zero modifications to researcher-owned sections (`01-introduction.md`, `02-related-work.md`, `05-limitations.md`).
- **Status:** Clearance proposed — awaiting researcher verdict.

## Verdict (researcher)

Cleared — MB, October 31, 2026


MB, October 3`, 2026