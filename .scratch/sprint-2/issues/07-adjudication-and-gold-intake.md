# Adjudication Protocol & Gold Label Data Intake

Type: human adjudication & data intake
Status: Active
Cap: 2 days (human adjudication & verification)

## Question

Adjudicate any label disagreements between Annotator 1 and Annotator 2 and commit the official gold benchmark to `data/raw/labels/`:
1. Generate adjudication diff table highlighting items with claim verdict discrepancies.
2. Lead researcher reviews discordant claims and makes definitive tie-breaker calls adhering to `docs/RUBRIC_V1.md`.
3. Researcher commits the finalized gold labels into `data/raw/labels/gold_labels_120.jsonl`.
4. Invariant checks:
   - Physical label isolation: AI agent confirms it never wrote to `data/raw/labels/`.
   - Critical claim override applied: item-level binary faithfulness $A_i$ computed according to pre-registered rule.
   - Non-zero claim conservation across all 120 items.

## Findings & Evidence (agent)

- **2026-10-29 (Adjudication Parsing & Candidate Gold Compilation)**:
  - Ingested completed researcher adjudications from [`data/interim/preannotations/adjudication_workbench.md`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/data/interim/preannotations/adjudication_workbench.md): exactly 19/19 discordant claims adjudicated.
  - Built compilation engine in `src/prepare/compile_gold_dataset.py` with accompanying TDD test suite `tests/test_gold_assembly.py` (56/56 tests passing project-wide).
  - Fused consensus verdicts (321 claims) and adjudicated verdicts (19 claims) into complete ground truth for all 340 claims (0 missing values, 0 invalid enums).
  - Evaluated item-level binary faithfulness $A_i$ using pre-registered critical claim override rule across all 120 items.
  - Staged verified benchmark files in `data/interim/preannotations/`:
    - [`data/interim/preannotations/candidate_gold_labels_120.jsonl`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/data/interim/preannotations/candidate_gold_labels_120.jsonl) (120 EvaluationItem records)
    - [`data/interim/preannotations/candidate_gold_claims_120.jsonl`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/data/interim/preannotations/candidate_gold_claims_120.jsonl) (340 AtomicClaim records)
  - Strict Invariant Verification:
    - Absolute Prohibition 1 (The Freeze): `git diff sprint-1-frozen -- src/analyze/ src/report/` is clean (0 changes).
    - Absolute Prohibition 2 (Gold Isolation): `data/raw/labels/` remains untouched (agent wrote 0 files to gold directory).
    - Absolute Prohibition 3 (No Peeking): Evaluator metrics ($\kappa$, $\alpha$, performance intervals) have NOT been calculated.
    - Absolute Prohibition 4 (No Resampling): 120 items conserved exactly across pre-registered strata.
  - Status: Staged and ready for researcher copy into `data/raw/labels/gold_labels_120.jsonl`. Clearance proposed — awaiting researcher verdict.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, October 29, 2026