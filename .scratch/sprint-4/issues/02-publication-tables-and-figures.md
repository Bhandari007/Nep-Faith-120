# Ticket 02 · Publication LaTeX Tables & Figures

Type: reporting / publication
Status: Cleared - [MB, October 31, 2026]
Cap: 0.5 day

## Question

Can we generate publication-grade LaTeX tables (Table 1: Main Decomposition, Table 2: 7-Type Sensitivity Matrix) stamped with reproducibility metadata (git commit hash, config hash, timestamp) into `reports/` and `outputs/`?

## Criteria
1. TDD test verifying table generation and LaTeX compilation syntax.
2. Table 1 contains estimates, 95% CIs, and PPSR across all arms for C1, C2, C3, $\Delta_{MT}$, $\Delta_{XL}$, and paired difference.
3. Table 2 contains 7-type perturbation sensitivity matrix.
4. Output files written to `reports/` and stamped in `outputs/`.
5. Zero modifications to frozen layers.

## Findings & Evidence (agent)

- **2026-10-31 (Publication LaTeX Tables & Artifact Generation)**:
  - Table 1 (`reports/table1_decomposition.tex`) generated with booktabs syntax, containing $A(C1), A(C2), A(C3)$, $\Delta_{MT}, \Delta_{XL}$, paired difference $\Delta_{XL} - \Delta_{MT}$, and PPSR for all evaluator arms.
  - Table 2 (`reports/table2_sensitivity.tex`) generated with 7-type perturbation detection rates across arms (Arm 2 BGE-M3: Entity Swap 90.5%, Number/Date Shift 87.4%, Negation Flip 90.5%, Misattribution 94.7%, Register Shift 96.8%, Unsupported Addition 100.0%, Invented Causality 97.9%).
  - Reproducibility stamping implemented and verified in `outputs/run_summary_20261031_032903.json`.
  - Tests passing in `tests/test_unblinded_pipeline.py` and `tests/test_report.py`.
  - Freeze check clean (0 diff on `src/analyze/` and `src/report/`).
  - Zero writes to `data/raw/labels/`.
- **Status:** Clearance proposed — awaiting researcher verdict.

## Verdict (researcher)

Cleared — MB, October 31, 2026


MB, October 31, 2026