# Condition C3 Human Post-Editing Workbench Setup

Type: engineering / tooling
Status: Cleared
Cap: 1 day (post-editing interface and minimal-pair guidelines)

## Question

Build and export the Condition $C3$ post-editing workbench to `data/interim/preannotations/post_edit_c3_workbench.md`:
1. Side-by-side presentation:
   - Source Nepali Passage ($p_{ne}$)
   - Raw IndicTrans2 Machine Translation ($p_{c2} = \text{MT}(p_{ne})$)
   - Editable Human Post-Edited Translation field ($p_{c3} = \text{PE}(\text{MT}(p_{ne}))$)
2. Guidelines incorporated:
   - Strict adherence to minimal-pair post-editing (correct translation errors such as aspect collapse, dropped evidentials, negation flips, entity misnomers, but preserve the underlying phrasing/syntax of MT to eliminate stylistic confounds).
   - Stopwatch duration entry per item.
3. Formatted to ensure minimal cognitive burden and rapid post-editing (~2 min/passage, projected ~4 hours total).

## Findings & Evidence (agent)

- **Workbench Generation & Architecture:**
  - Implemented `src/prepare/export_c3_workbench.py`.
  - Generated `data/interim/preannotations/post_edit_c3_workbench.md` (1,975 lines, 137 KB).
  - Deduplicated by passage: Grouped the 120 candidate items into exactly 60 unique authentic reference passages ($p_{ne}$), cutting human post-editing burden by 50% while guaranteeing cross-item consistency.
  - Side-by-side layout:
    1. Source Nepali text ($p_{ne}$)
    2. Raw IndicTrans2 MT ($p_{c2}$)
    3. Editable $p_{c3}$ text box initialized with $p_{c2}$ (minimal edit distance design).
    4. Stopwatch elapsed timing field (`Stopwatch Elapsed Time: [ mm:ss ]`).
    5. Fine-grained translation error checklist (entity mistranslation, number/date distortion, omission, polarity flip, aspect collapse, evidential distortion, or clean/no edit needed).
  - Invariant tests: `tests/test_c3_workbench_export.py` passing (33/33 tests pass project-wide). Zero writes to `data/raw/labels/`.
- **Completed Human Post-Editing Intake & Audit (2026-10-23):**
  - Audited researcher completed workbench: `data/interim/preannotations/post_edit_c3_workbench.md`.
  - 100% passage coverage: All 60 unique reference passages (covering all 120 candidate items) reviewed.
  - Minimal-pair edits applied: 54 passages post-edited ($p_{c3} \neq p_{c2}$), correcting entity mistranslations and date/numeral shifts while strictly preserving MT phrasing.
  - Accurate translations retained: 6 passages verified as fluent/faithful without modification (`[X] Clean / No edit needed`).
  - Error distribution recorded:
    - Number / Date / Metric distortion: 49 passages
    - Omission / Dropped clauses: 11 passages
    - Entity / Proper Noun mistranslation: 8 passages
    - Clean / No edit needed: 6 passages
    - Tense / Aspect collapse: 1 passage
  - Stopwatch entry: Passage 1 recorded (`0m:50s`); remainder use aggregate timing.
  - Compliance: Zero writes to `data/raw/labels/`. Absolute Prohibition 1 & 2 fully maintained.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
Status: Cleared - [MB, October 23, 2026]