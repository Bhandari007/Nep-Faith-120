# Human Dual-Annotation Workbench & Tooling Setup

Type: engineering / tooling
Status: Active
Cap: 1 day (workbench generation script, dual sheets, and pilot stopwatch harness)

## Question

Build and export human dual-annotation workbenches to `data/interim/preannotations/` to allow seamless, frictionless annotation for Annotator 1 and Annotator 2:
1. Export structured annotation workbenches:
   - `data/interim/preannotations/workbench_annotator_1.md`
   - `data/interim/preannotations/workbench_annotator_2.md`
2. Each item display must include:
   - Item ID, Domain, Provenance metadata (blinded from evaluator during scoring).
   - Passage in Nepali ($C1$).
   - English Query and Generated English Answer.
   - List of atomic claims with `[is_critical]` indicators.
   - 3 selectable options per claim: `[ ] Supported`, `[ ] Contradicted`, `[ ] Not-in-context`.
   - Elapsed stopwatch entry field (`mm:ss`).
   - Notes / justification field.
3. Formatted to ensure zero JSON wrangling for human annotators.
4. Compliant with `docs/RUBRIC_V1.md` and `docs/PILOT_ANNOTATION_SHEET.md`.

## Findings & Evidence (agent)

<!-- Agent records file generation, structure, and ergonomics verification here -->

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
