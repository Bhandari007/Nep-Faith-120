# Unlabelled 1,200 Item Assembly & 7-Type Perturbations

Type: data engineering / synthetic perturbation
Status: Pending Ticket 01
Cap: 1 day

## Question

Assemble $N=1,200$ stratified evaluation items from the 600 authentic reference passages:
1. Stratification: Exactly 400 Wikipedia, 400 Government Report, and 400 News items.
2. Provenance balance: Exactly 600 Natural RAG items (50%) and 600 Perturbed items (50%).
3. Perturbation coverage: 600 negative items partitioned evenly across the 7 pre-registered types:
   - `entity_swap`
   - `number_date_alteration`
   - `negation_flip`
   - `misattribution`
   - `register_shift`
   - `unsupported_addition`
   - `invented_causality`
4. Formatted as valid `EvaluationItem` records into `data/interim/unlabelled_1200.jsonl`.
5. Prohibition adherence: Zero writes to `data/raw/labels/`.

## Findings & Evidence (agent)

- Implemented `src/prepare/assemble_unlabelled.py` with exact pre-registered quota constraints:
  - 1,200 items generated into `data/interim/unlabelled_1200.jsonl`.
  - Exactly 400 Wikipedia, 400 Gov Reports, 400 News items.
  - Exactly 120 sports items in News (30% mandatory quota).
  - Exactly 600 Natural (50%) and 600 Perturbed items (50%).
  - Balanced representation across all 7 perturbation types (`entity_swap`: 86, `number_date_alteration`: 86, `negation_flip`: 86, `misattribution`: 86, `register_shift`: 86, `unsupported_addition`: 85, `invented_causality`: 85).
- TDD unit tests written and verified in `tests/test_unlabelled_assembly.py` (100% passing).
- Zero writes to `data/raw/labels/`. Status: Clearance proposed — awaiting researcher.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, October 23, 2026