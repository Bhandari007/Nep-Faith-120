# Atomic Claim Decomposition & Criticality Tagging

Type: engineering
Status: Active
Cap: 1 day (claim extraction runner and rubric compliance checks)

## Question

Extract atomic factual propositions from all 120 candidate answers using `src/prepare/claims.py` adhering to `docs/RUBRIC_V1.md` Section 2:
1. Decompose multi-sentence English answers into standalone, checkable propositions (target: 2–5 claims per item, ~350–400 claims total).
2. Decontextualization: resolve indexicals and pronouns.
3. Atomicity: split conjunctions into independent checkable units.
4. Criticality Flagging: designate `is_critical=True` for claims answering the core query inquiry.
5. Invariant check: verify that every item has at least one claim marked `is_critical=True`.
6. Output stored in `data/interim/preannotations/claims_120.jsonl` and integrated into the candidate items.

## Findings & Evidence (agent)

<!-- Agent records extraction counts, claim statistics, and invariant checks here -->

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
