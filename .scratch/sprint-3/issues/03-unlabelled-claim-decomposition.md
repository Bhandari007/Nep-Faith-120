# Atomic Claim Decomposition & Criticality Tagging (Unlabelled 1,200)

Type: data engineering / claim extraction
Status: Pending Ticket 02
Cap: 0.5 day

## Question

Decompose the English answers of all 1,200 unlabelled evaluation items into atomic factual propositions:
1. Deconstruct answers into 2–5 atomic, self-contained claims per item (~3,500 claims total).
2. Assign explicit boolean `is_critical` flags adhering to `docs/RUBRIC_V1.md`.
3. Export to `data/interim/unlabelled_claims_1200.jsonl` and link within `unlabelled_1200.jsonl`.
4. Invariant: Non-zero claim conservation across all 1,200 items.

## Findings & Evidence (agent)

- Exported 3,410 atomic claims across all 1,200 unlabelled items to `data/interim/unlabelled_claims_1200.jsonl` using `ClaimsExporter`.
- Distribution: Mean 2.84 claims per item (bounded in [2, 5]).
- 100% `is_critical` coverage with boolean flags.
- Sub-genre distribution: culture_heritage (460), biodiversity_parks (460), infrastructure_tourism (624), health (240), agriculture (224), education (224), economy_finance (224), governance_law (208), sports (320), disaster_geography (426).
- Zero writes to `data/raw/labels/`. Status: Clearance proposed — awaiting researcher.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, October 23, 2026