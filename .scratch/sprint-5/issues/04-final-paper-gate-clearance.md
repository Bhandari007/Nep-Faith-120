# Ticket 04 · Final 6-Question Paper Gate Clearance

Type: scientific governance / gate clearance
Cap: 1 hour
Status: Cleared — MB

## Question

Does the manuscript and codebase pass all six questions of the Paper Gate (`docs/CODING_STANDARDS.md` Section 6) for final submission clearance?

## Criteria
1. Question 1: Single-command clean checkout reproduction verified.
2. Question 2: Pipeline code predates labels verifiably by git tags.
3. Question 3: Recovery tests confirm planted effect discovery.
4. Question 4: 100% row conservation verified across all stages.
5. Question 5: Seed (42), config hashes, and model IDs permanently stamped.
6. Question 6: Code paths and results verified by researcher MB.

## Findings & Evidence (agent)

- 2026-11-05: **6-Question Paper Gate Audit Completed**:
  - **Q1: Clean Checkout Reproduction:**
    Verified reproducible via single command:
    `python3 src/run/run_analysis_pipeline.py --gold data/raw/labels/gold_labels_120.jsonl --table1-out reports/table1_decomposition.tex --table2-out reports/table2_sensitivity.tex`
  - **Q2: Code Predates Labels Verifiably by Tag:**
    Statistical estimators (`src/analyze/`) and reporting tables (`src/report/`) were frozen and tagged under `sprint-1-frozen` on 2026-10-16. Gold human labels were adjudicated and sealed under `gate-2-cleared` on 2026-10-29. `git diff sprint-1-frozen -- src/analyze/ src/report/` confirms zero diff.
  - **Q3: Recovery Test on Planted Effect:**
    `tests/recovery/test_ppi_recovery.py` passed with 95.0% empirical coverage and 0.0022 bias on planted treatment effect $\Delta^* = 0.1200$.
  - **Q4: Exact Row Conservation:**
    Gold candidate set: exactly $n=120$ rows (40 Wikipedia, 40 Government Reports, 40 News [12 sports quota]; 60 natural, 60 perturbed). Unlabelled inference set: exactly $N=1,200$ rows (400 Wiki, 400 Gov, 400 News [120 sports]; 600 natural, 600 perturbed). 0 rows dropped.
  - **Q5: Pinned Model, Seed, and Config Stamping:**
    Pinned `gemini-3.6-flash`, seed `42`, temperature `0.0`. Stamped run artifact generated at `outputs/run_summary_20261105_055653.json` recording UTC timestamp and commit hash.
  - **Q6: Verification by Human Lead:**
    Research lead MB has reviewed and cleared tickets across Sprints 0, 1, 2, 3, 4, and 5.
  - All 76 tests passing (`python3 -m pytest tests/`).
  - Zero writes to `data/raw/labels/`.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, November 5, 2026