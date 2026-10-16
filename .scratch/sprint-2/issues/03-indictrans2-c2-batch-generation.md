# IndicTrans2 C2 Batch Translation Runner

Type: engineering
Status: Active
Cap: 1 day (batch translation run, disk cache verification, and leakage audit)

## Question

Generate Condition $C2$ raw machine translations for all 120 Nepali passages using `src/run/translate.py` (IndicTrans2-200M):
1. Execute locally on GPU/CPU with `ai4bharat/indictrans2-indic-en-dist-200M` (`npi_Deva` -> `eng_Latn`).
2. Populate `c2_raw_mt` field for each item in the pre-annotation records.
3. Verify deterministic caching under `cache/translations/` keyed on SHA-256.
4. Verify pipeline invariants: zero cross-condition contamination, strict passage conservation.

## Findings & Evidence (agent)

<!-- Agent records runtime, cache hits, translation examples, and invariant checks here -->

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
