# Stratified Sampling & 120 Candidate Corpus Assembly

Type: engineering
Status: Clearance proposed — awaiting researcher
Cap: 1 day (sampling script, schema validation, and balance checks)

## Question

Assemble the 120 candidate evaluation items adhering strictly to `docs/PREREGISTRATION.md` Section 4:
1. Macro-Stratification (40/40/40):
   - 40 Wikipedia passages (`wikipedia`)
   - 40 Government & Public Report passages (`government_report`)
   - 40 Contemporary News passages (`news`), containing a 30% quota (12 items) of sports reporting.
2. Approved 10-Domain Topical Taxonomy:
   - **Health & Public Medicine (`health`)**: ~10 items (MoHP reports, NDHS surveys, clinical guidelines).
   - **Agriculture & Rural Economy (`agriculture`)**: ~10 items (MoALD reports, agricultural census, community forestry).
   - **Education & Demographics (`education`)**: ~10 items (MoEST flash reports, SEE statistics, university records).
   - **Economics, Banking & Remittance (`economy_finance`)**: ~10 items (Nepal Rastra Bank reports, MoF economic survey, lakh/crore scale stress-tests).
   - **Disaster, Climate & Environment (`disaster_geography`)**: ~10 items (NDRRMA bulletins, earthquake/monsoon landslide data, GLOF alerts).
   - **Governance, Law & Constitution (`governance_law`)**: ~10 items (Constitution 2072, Supreme Court gazettes, local governance acts).
   - **Sports (`sports`)**: 12 items (Pre-registered 30% news quota: CAN cricket, ANFA football, HamroKhelkud).
   - **Culture, Heritage & History (`culture_heritage`)**: ~15 items (UNESCO monuments, indigenous festivals, Bikram Sambat dates).
   - **Geography, Parks & Biodiversity (`biodiversity_parks`)**: ~15 items (Sagarmatha, national park conservation, wildlife censuses).
   - **Infrastructure, Energy & Tourism (`infrastructure_tourism`)**: ~18 items (Fast Track, hydropower MW projects, tourist arrivals).
3. Provenance Balance:
   - 60 Natural RAG items (50%) generated from reference passages with full support, partial support, or distractors.
   - 60 Perturbed items (50%) generated via `src/prepare/perturb.py` evenly distributed across the 7 typed edits:
     1. `entity_swap` (~8–9 items)
     2. `number_date_alteration` (~8–9 items)
     3. `negation_flip` (~8–9 items)
     4. `misattribution` (~8–9 items)
     5. `register_shift` (~8–9 items)
     6. `unsupported_addition` (~8–9 items)
     7. `invented_causality` (~8–9 items)
4. Schema & Path Constraints:
   - Validate every candidate item against `EvaluationItem` in `src/prepare/schema.py`.
   - Output must be saved strictly to `data/interim/preannotations/gold_candidates_120.jsonl`.
   - Never write to `data/raw/labels/`.

## Findings & Evidence (agent)

1. **Assembly Engine Implemented (`src/prepare/assemble_candidates.py`)**:
   - Built `CandidateAssembler` with curated seed bank across all 10 approved topical domains.
   - Implemented exact allocation matrix:
     - 40 Wikipedia items: `culture_heritage` (15), `biodiversity_parks` (15), `infrastructure_tourism` (10).
     - 40 Government Report items: `health` (10), `agriculture` (10), `education` (10), `economy_finance` (10).
     - 40 News items: `sports` (12), `disaster_geography` (10), `governance_law` (10), `infrastructure_tourism` (8).
   - Provenance balance: Exactly 60 Natural and 60 Perturbed items (cycling through all 7 typed edits with $\ge 8$ items per type).
2. **Schema & Label Isolation Verified**:
   - Every candidate item validated against `EvaluationItem` with decomposed `AtomicClaim` objects.
   - Every item contains at least one claim flagged `is_critical=True`.
   - Hard Rule verified: All candidate claims have `gold_label=None` (zero machine pre-population of gold fields).
   - Output written strictly to `data/interim/preannotations/gold_candidates_120.jsonl` (120 lines, verified).
   - `data/raw/labels/` remains pristine with zero automated writes.
3. **Automated TDD Test Suite**:
   - Implemented `tests/test_candidate_assembly.py` (all 5 invariant checks passing in 0.08s).
   - Full repository test suite passes: **29/29 tests passed in 3.38s**.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, 16 October 2026
