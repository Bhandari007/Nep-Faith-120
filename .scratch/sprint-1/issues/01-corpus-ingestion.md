# Corpus Ingestion & Passages Pipeline

Type: engineering
Status: Cleared - [MB, 2026-10-16]
Cap: 1 day (ingestion scripts & schema validation)

## Question

Build `src/prepare/ingest.py` to ingest, segment, and validate source passages from:
1. Nepali Wikipedia (`wikipedia`)
2. Nepali Government & Public Reports (`government_report`)
3. Contemporary News (`news`)

Requirements:
- Enforce length limits (150–350 tokens per passage).
- Validate each record against `CorpusPassage` in `src/prepare/schema.py`.
- Save clean passages to `data/derived/corpus_passages.jsonl`.
- Multi-format ingestion support: digital Unicode PDFs, legacy Preeti font transliteration, and Gemini Vision OCR fallback.
- Stratified inclusion of contemporary sports (30% quota of news stratum).

## Findings & Evidence (agent)

1. **Pipeline Implementation:** Built `src/prepare/ingest.py` with:
   - NFC Unicode normalization and zero-width joiner sanitation (`normalize_devanagari`).
   - Legacy 8-bit Preeti/Kantipur encoding detector and transliteration engine (`is_preeti_encoded`, `convert_preeti_to_unicode`).
   - Multi-format PDF extractor with Devanagari character density heuristic routing to `pypdf` or `GeminiRotator` OCR fallback.
   - Sentence/paragraph boundary chunker enforcing 150–350 token limits (`chunk_into_passages`).
   - Stratified seed corpus covering all 3 domains, including dedicated sports passages (`sports_hk_001`, `sports_can_001`).
2. **Schema Integration:** Added `CorpusPassage` Pydantic model to `src/prepare/schema.py`.
3. **Execution & Validation:** Executed `python -m src.prepare.ingest`:
   - Extracted and validated 7 seed passages into `data/derived/corpus_passages.jsonl`.
   - Stratification breakdown: 2 Wikipedia, 2 Government Reports, 3 News (including 2 Sports).
4. **Automated Unit Tests:** Implemented `tests/test_ingest.py` covering normalization, Preeti transliteration, chunking, and schema validation. All 4 tests pass (`pytest tests/test_ingest.py -v`).
5. **Decisions Recorded:** `docs/adr/0001-source-corpus-and-multi-format-ingestion.md` and `paper/notes/03-methodology-raw-notes.md`.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, 16 October 2026

