# Gate 3 Invariant Verification & Prediction Matrix Lock

Type: governance / data lock
Status: Cleared - [MB, October 23, 2026]
Cap: 0.5 day

## Question

Verify all Gate 3 deliverables, confirm invariant compliance, and lock the unlabelled proxy prediction matrix prior to Sprint 4 (Statistical Estimation & PPI Inference):
1. Invariants verified:
   - Exactly $N=1,200$ items accounted for across all 3 strata (400 Wikipedia, 400 Gov Reports, 400 News).
   - 100% C1 and C2 text populated across all items.
   - Non-zero claim conservation (~3,500 claims).
   - Complete prediction matrix generated across the 5 evaluator arms.
   - Zero write paths to `data/raw/labels/`.
   - Frozen layers (`src/analyze/` and `src/report/`) verified untouched against `sprint-1-frozen`.
2. All unit and invariant tests passing (`pytest tests/`).
3. Prepare Gate 3 clearance report for lead researcher sign-off.

## Findings & Evidence (agent)

- Implemented and verified comprehensive invariant tests in `tests/invariants/test_gate3_invariants.py` (3/3 passed, 51/51 project-wide tests passing).
- Invariants confirmed:
  - Exactly $N=1,200$ items accounted for in `data/interim/unlabelled_1200.jsonl` (400 Wikipedia, 400 Gov Reports, 400 News with 120 sports quota; 600 natural / 600 across 7 perturbation types).
  - 100% C1 and C2 text populated across all items with 0 missing.
  - Exactly 3,410 constituent claims exported with 100% boolean `is_critical` coverage.
  - Complete proxy prediction matrix generated across the 4 automated arms into `data/interim/predictions/predictions_unlabelled_1200.jsonl` (1,200 records).
  - Absolute Prohibition 1: `git diff sprint-1-frozen -- src/analyze/ src/report/` confirmed 0 diff (clean).
  - Absolute Prohibition 2: Zero writes to `data/raw/labels/`.
  - Absolute Prohibition 3: Zero peeking or gold-level agreement computation.
  - Absolute Prohibition 4: Pre-registered strata strictly preserved.
- Status: Clearance proposed — awaiting researcher sign-off.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, October 23, 2026