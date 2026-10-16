# Gate 2 Verification & Data Lock

Type: governance
Status: Active
Cap: 0.5 day (data integrity checks, invariant verification, and tag preparation)

## Question

Verify all Gate 2 deliverables, confirm invariant compliance, and lock the gold evaluation dataset prior to Sprint 3 (Automated Scoring & Statistical Estimation):
1. Gold benchmark committed: `data/raw/labels/gold_labels_120.jsonl` exists and is non-empty.
2. Invariants verified:
   - Full 120 items accounted for across all 3 strata (40 Wikipedia, 40 Government Reports, 40 News).
   - Zero write paths from AI agent to `data/raw/labels/`.
   - Condition $C3$ post-edits complete and validated.
   - Analysis layer (`src/analyze/`) and reporting layer (`src/report/`) verified unchanged against `sprint-1-frozen`.
3. Invariant tests passing: `pytest tests/invariants/` and `pytest tests/` green.
4. Git tag `gate-2-cleared` prepared for researcher sign-off.

## Findings & Evidence (agent)

<!-- Agent records test suite verification and commit readiness here -->

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
