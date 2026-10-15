# Corpus Ingestion & Passages Pipeline

Type: engineering
Status: open
Cap: 1 day (ingestion scripts & schema validation)

## Question

Build `src/prepare/ingest.py` to ingest, segment, and validate source passages from:
1. Nepali Wikipedia (`wikipedia`)
2. Nepali Government & Public Reports (`government_report`)
3. Contemporary News (`news`)

Requirements:
- Enforce length limits (150–350 tokens per passage).
- Validate each record against `EvaluationItem` in `src/prepare/schema.py`.
- Save clean passages to `data/derived/corpus_passages.jsonl`.
