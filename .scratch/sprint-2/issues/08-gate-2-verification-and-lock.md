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

- **2026-10-29 (Gate 2 Deliverables & Invariants Verification)**:
  - Gold benchmark verified at [`data/raw/labels/gold_labels_120.jsonl`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/data/raw/labels/gold_labels_120.jsonl) (353,976 bytes, human-committed via strict physical isolation).
  - Executed Gate 2 invariant test suite (`tests/invariants/test_gate2_invariants.py`):
    - Exact 120-item conservation across 3 strata: 40 Wikipedia, 40 Government Reports, 40 News.
    - News sports quota: exactly 12 items (30.0%).
    - Provenance balance: exactly 60 Natural items (50.0%) and 60 Perturbed items (50.0%) across all 7 pre-registered perturbation types.
    - Claim conservation: exactly 340 claims across 120 items, 100% assigned valid gold labels (`Supported`, `Contradicted`, `Not-in-context`).
    - Derived item faithfulness $A_i$: 100% boolean coverage applying the pre-registered critical claim override rule.
    - Full counterfactual context coverage: $p_{ne}$, $c2_{\text{raw}}$, and $c3_{\text{post-edit}}$ populated for all 120 items.
  - Absolute Prohibition 1 (The Freeze): `git diff sprint-1-frozen -- src/analyze/ src/report/` confirmed 100% clean (0 lines changed).
  - Absolute Prohibition 2 (Gold Isolation): Agent confirmed zero write paths to `data/raw/labels/` (enforced via PermissionError safeguard).
  - Absolute Prohibition 3 (No Peeking): Strictly upheld (zero agreement metrics or score distributions computed).
  - Complete test suite: **58/58 tests passing** (`PYTHONPATH=. pytest`).
  - Gate 2 lock: Ready for Git tag `gate-2-cleared`.
  - Status: Clearance proposed — awaiting researcher verdict and tagging.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, October 29, 2026