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

<!-- Agent records file receipt, checksum verification, and row conservation check here -->

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
