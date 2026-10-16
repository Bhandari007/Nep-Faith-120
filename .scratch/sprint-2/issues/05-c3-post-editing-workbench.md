# Condition C3 Human Post-Editing Workbench Setup

Type: engineering / tooling
Status: Clearance proposed — awaiting researcher
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

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
