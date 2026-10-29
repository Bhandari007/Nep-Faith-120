# Dual Human Annotation & Stopwatch Timing Execution

Type: human annotation
Status: Active
Cap: 14 days (human annotation window; ~8.5–9.0 total human hours)

## Question

Execute the dual-annotator human evaluation on the 120 items (~350–400 claims) and human post-editing of Condition $C3$:
1. Annotators (Muskan Bhandari + Annotator 2) independently annotate all items using `workbench_annotator_1.md` and `workbench_annotator_2.md` following `docs/RUBRIC_V1.md`.
2. Record stopwatch duration (minutes:seconds) per item and claim.
3. Complete minimal-pair post-editing of all 120 passages in `post_edit_c3_workbench.md`.
4. Hard Rule: No peeking by the AI agent during annotation. The agent does NOT compute agreement metrics or distributions until adjudication is complete.

## Findings & Evidence (agent)

- **2026-10-18 (Intake & URL Verification)**:
  - Ingested completed annotation workbench from lead researcher (Annotator 1): [`data/interim/preannotations/workbench_annotator_1_completed.xlsx`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/data/interim/preannotations/workbench_annotator_1_completed.xlsx).
  - Validation check: 120/120 items present, 340/340 claims verified, 340/340 verdicts populated (zero missing verdicts). Stopwatch durations recorded.
  - Resolved 404 URL discrepancies across candidate set: Mapped authentic live URLs from `data/derived/authentic_passages_60.jsonl` into `SEED_META` in `src/prepare/assemble_candidates.py`.
  - Re-exported candidate pools, claims, and dual-annotation workbenches. Updated `workbench_annotator_1_completed.xlsx` metadata columns (columns 14-15) with live links while verifying 100% byte-for-byte fidelity of all 340 verdicts, times, and qualitative comments.
  - HTTP Connectivity Verification: 59 / 59 unique URLs in `gold_candidates_120.jsonl` verified returning `HTTP 200 OK`.
  - Prohibition Compliance: Zero writes to `data/raw/labels/`. Strict compliance with Absolute Prohibition 3 (No Peeking) — no agreement metrics ($\kappa, \alpha$) or score distributions computed. All 39 unit and integration tests passing.
  - Next state: Awaiting Annotator 2 completed workbench intake and lead researcher decision on Condition C3 post-edits.

- **2026-10-29 (Annotator 2 Intake & Adjudication Queue Export)**:
  - Ingested completed annotation workbench from Annotator 2: [`data/interim/preannotations/workbench_annotator_2_completed.xlsx`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/data/interim/preannotations/workbench_annotator_2_completed.xlsx).
  - Validation check: 120/120 items present, 340/340 claims verified in matching order with Annotator 1, 340/340 verdicts populated and strictly conform to rubric enum (`Supported`, `Contradicted`, `Not-in-context`). Zero missing verdicts.
  - Built ingestion & validation module `src/prepare/intake_annotations.py` and comprehensive test suite `tests/test_annotation_intake.py` (54/54 tests passing project-wide).
  - Generated adjudication diff workbenches for lead researcher review:
    - [`data/interim/preannotations/adjudication_workbench.xlsx`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/data/interim/preannotations/adjudication_workbench.xlsx) (with dropdown validation)
    - [`data/interim/preannotations/adjudication_workbench.md`](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/data/interim/preannotations/adjudication_workbench.md)
  - Isolated exactly 19 discordant claims requiring researcher tie-breaking (321 claims concordant).
  - Prohibition compliance: Zero writes to `data/raw/labels/`. Strict compliance with Absolute Prohibition 3 (No Peeking) — no $\kappa$, $\alpha$, or score distributions computed.
  - Status: Clearance proposed — awaiting researcher verdict.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, October 29, 2026