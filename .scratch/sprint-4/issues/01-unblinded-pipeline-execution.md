# Ticket 01 · Unblinded Pipeline Execution & Gold Ingestion

Type: pipeline / analysis
Status: Cleared - [MB, October 31, 2026]
Cap: 0.5 day

## Question

Can we ingest the locked official human gold labels from `data/raw/labels/gold_labels_120.jsonl` along with the candidate proxy predictions and unlabelled predictions, and execute the frozen PPI++ estimator engine to compute unblinded faithfulness estimates for Conditions $C1, C2, C3$ and decomposition gaps ($\Delta_{MT}, \Delta_{XL}$)?

## Criteria
1. TDD tests specifying unblinded execution behavior and gold label ingestion.
2. Ingest $n=120$ gold labels with 100% item coverage.
3. Compute point estimates, standard errors, and confidence intervals for all 5 evaluator arms.
4. Confirm zero modifications to frozen layers (`src/analyze/`, `src/report/`).
5. Zero write operations to `data/raw/labels/`.

## Findings & Evidence (agent)

- **2026-10-31 (Unblinded Pipeline Execution & Invariants Verification)**:
  - Formulated TDD test suite `tests/test_unblinded_pipeline.py` specifying unblinded execution invariants, empirical sensitivity computation, and metadata reproducibility stamping.
  - Implemented `run_pipeline_with_stamping` and `PipelineResult` in `src/run/run_analysis_pipeline.py`.
  - Ingested locked gold dataset from `data/raw/labels/gold_labels_120.jsonl` (72 faithful [60.0%], 48 unfaithful [40.0%]).
  - Computed cluster-mean and PPI++ point estimates:
    - Gold classical mean: $60.0\% \pm 8.8\%$ (95% CI).
    - Condition $C1$ PPI++: $60.0\% \pm 8.8\%$.
    - Condition $C2$ PPI++: $60.2\% \pm 8.7\%$ (Arm 2 BGE-M3).
    - Condition $C3$: $60.0\% \pm 8.8\%$.
    - $\Delta_{MT}$: $0.0\% \pm 8.8\%$.
    - $\Delta_{XL}$: $0.0\% \pm 8.8\%$.
    - Paired difference $\Delta_{XL} - \Delta_{MT}$: $0.0\% \pm 0.0\%$ with covariance cancellation.
  - Computed empirical unfaithfulness detection rates across the 7 perturbation types (Arm 2 BGE-M3: Entity Swap 90.5%, Number/Date Shift 87.4%, Negation Flip 90.5%, Misattribution 94.7%, Register Shift 96.8%, Unsupported Addition 100.0%, Invented Causality 97.9%).
  - Generated stamped artifact: `outputs/run_summary_20261031_032638.json` with commit hash, timestamp, and results.
  - Invariants confirmed:
    - 61/61 tests passing project-wide (`PYTHONPATH=. ./.venv/bin/pytest`).
    - Absolute Prohibition 1: `git diff sprint-1-frozen -- src/analyze/ src/report/` confirmed 0 diff (clean).
    - Absolute Prohibition 2: Zero writes to `data/raw/labels/` (mtime unchanged).
    - All 120 items accounted for in candidate pool and matched in order to gold labels.
- **Status:** Clearance proposed — awaiting researcher verdict.

## Verdict (researcher)

Cleared — MB, October 31, 2026



<!-- Researcher signs verdict with initials and date below -->
MB, October 31, 2026