# IndicTrans2 C2 Batch Translation Runner (Unlabelled 1,200)

Type: model inference / machine translation
Status: Pending Ticket 02
Cap: 0.5 day

## Question

Generate Condition $C2$ raw machine translations for all unique authentic Nepali passages in the unlabelled corpus:
1. Translate ~600 unique passages using local GPU inference with `ai4bharat/indictrans2-indic-en-dist-200M` (`npi_Deva` -> `eng_Latn`).
2. Deduplicate translations by passage hash with SHA-256 disk caching under `cache/translations/`.
3. Populate `c2_raw_mt` field for all 1,200 items in `data/interim/unlabelled_1200.jsonl`.
4. Invariant: 100% C2 coverage across all items; zero null or empty translations.

## Findings & Evidence (agent)

- Executed `BatchC2Translator` across `data/interim/unlabelled_1200.jsonl`.
- Leveraged deduplicated SHA-256 disk cache under `cache/translations/`.
- 100% C2 coverage: All 1,200 items populated with valid `c2_raw_mt` (0 missing).
- Zero writes to `data/raw/labels/`. Status: Clearance proposed — awaiting researcher.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, October 23, 2026