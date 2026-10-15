# 7-Type Perturbation Engine

Type: engineering
Status: Clearance proposed — awaiting researcher
Cap: 2 days (perturbation operators, validation & unit tests)

## Question

Build `src/prepare/perturb.py` implementing deterministic and LLM-assisted perturbation generators across all 7 negative categories:
1. `entity_swap`: Replace key named entities with in-domain distractors.
2. `number_date_alteration`: Perturb numbers, dates, BS/AD calendar years, or percentages.
3. `negation_flip`: Invert polarity of a critical clause.
4. `misattribution`: Re-attribute findings, statements, or directives to the wrong source/body.
5. `register_shift`: Perturb honorific hierarchy causing grammatical/semantic distortion.
6. `unsupported_addition`: Inject plausible external assertions absent from the reference passage.
7. `invented_causality`: Falsely link two independent facts with causal connectives ("because", "leading to").

Requirements:
- Adhere to `docs/RUBRIC_V1.md` Section 5.
- Target appropriate ground truth labels (`Contradicted` for active conflicts, `Not-in-context` for external confabulations).
- Maintain deterministic seeds and span tracking (`perturbation_span`).
- Support both rule-based deterministic perturbations and LLM-assisted perturbations via `GeminiRotator`.

## Findings & Evidence (agent)

1. **Engine Built (`src/prepare/perturb.py`):**
   - Implemented specialized perturbation operators for all 7 negative categories with in-domain Nepali entity distractors, Nepali financial/census numbers/dates, polarity inverters, institution misattributions, honorific register distorters, plausible external additions, and spurious causal connectives.
   - Built deterministic dispatcher `apply_perturbation(answer_en, perturbation_type, seed)` returning both the perturbed answer text and explicit `perturbation_span` for provenance tracking.
2. **Schema & Rubric Compliance:**
   - Perturbation enum mapped strictly to `PerturbationType.NUMBER_DATE_ALTERATION` and the remaining 6 categories.
   - Target labels match `Contradicted` vs `Not-in-context` distinction codified in `docs/RUBRIC_V1.md`.
3. **Unit Tests:**
   - Implemented `tests/test_perturb.py` validating that each of the 7 operators alters text, records spans, and obeys strict seed determinism.
   - Test execution: 2/2 passed (`pytest tests/test_perturb.py -v`).

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
