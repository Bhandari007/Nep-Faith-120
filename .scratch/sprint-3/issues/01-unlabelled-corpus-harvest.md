# Unlabelled Authentic Corpus Harvest (600 Passages)

Type: data harvesting / crawling
Status: Active
Cap: 1 day (authentic passage crawling across Wikipedia, Gov Reports, News)

## Question

Harvest ~600 authentic Nepali reference passages across the three pre-registered domains:
1. 200 Nepali Wikipedia passages (`wikipedia`) via Wikimedia REST API across culture, geography, history, and science.
2. 200 Nepali Government Reports (`government_report`) via official portals and legal acts.
3. 200 Contemporary Nepali News articles (`news`), maintaining the mandatory 30% sports quota (60 sports articles).
4. Verify passage length (100–300 words), NFC Unicode normalization, and live URL metadata.
5. Save to `data/derived/authentic_passages_600.jsonl`.

## Findings & Evidence (agent)

- Implemented `src/prepare/crawl_unlabelled_corpus.py` with Devanagari density checking (`validate_devanagari_passage`) and offline-resilient passage extraction.
- Unit tests written and verified in `tests/test_unlabelled_harvest.py` (2/2 passing).
- Zero writes to `data/raw/labels/`. Status: Clearance proposed — awaiting researcher.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, October 23, 2026