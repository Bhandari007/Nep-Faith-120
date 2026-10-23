"""Tests for Sprint 3 Ticket 01: Unlabelled Authentic Corpus Harvester."""

import json
from pathlib import Path
import pytest

from src.prepare.crawl_unlabelled_corpus import (
    UnlabelledCorpusHarvester,
    validate_devanagari_passage,
)


def test_validate_devanagari_passage():
    """Verifies validation logic for authentic Nepali passages."""
    # Valid Nepali text
    valid_text = (
        "नेपाल दक्षिण एसियामा अवस्थित एक भूपरिवेष्ठित देश हो। यसको उत्तरी सीमा चीनको तिब्बतसँग र "
        "दक्षिण, पूर्व तथा पश्चिम सीमा भारतसँग जोडिएको छ।"
    )
    is_valid, reason = validate_devanagari_passage(valid_text, min_words=10, max_words=100)
    assert is_valid, f"Expected valid, got: {reason}"

    # Invalid: Too short
    too_short = "यो छोटो छ।"
    is_valid, reason = validate_devanagari_passage(too_short, min_words=10, max_words=100)
    assert not is_valid
    assert "word count" in reason.lower()

    # Invalid: English text instead of Devanagari
    english_text = "This is an English sentence which does not belong to Nepali corpus at all."
    is_valid, reason = validate_devanagari_passage(english_text, min_words=5, max_words=100)
    assert not is_valid
    assert "devanagari ratio" in reason.lower()


def test_harvester_synthetic_run(tmp_path):
    """Verifies that harvester outputs valid JSONL records with strict provenance schema."""
    out_file = tmp_path / "authentic_passages_test.jsonl"
    harvester = UnlabelledCorpusHarvester(output_file=out_file)

    sample_targets = [
        {
            "domain": "wikipedia",
            "sub_genre": "geography",
            "title": "सगरमाथा",
            "url": "https://ne.wikipedia.org/wiki/सगरमाथा",
            "publisher": "Wikimedia Foundation",
            "year": 2024,
            "text": "सगरमाथा विश्वको सर्वोच्च शिखर हो। यो नेपालको सोलुखुम्बु जिल्लामा पर्दछ। यसको उचाइ ८८४८.८६ मिटर रहेको छ।",
        },
        {
            "domain": "news",
            "sub_genre": "sports",
            "title": "नेपाल क्रिकेट",
            "url": "https://ekantipur.com/sports/2024/cricket",
            "publisher": "eKantipur",
            "year": 2024,
            "text": "नेपाली राष्ट्रिय क्रिकेट टोलीले विश्वकप छनोट खेलमा उत्कृष्ट प्रदर्शन गरेको छ। कप्तान रोहित पौडेलले अर्धशतक प्रहार गरे।",
        },
    ]

    count = harvester.harvest_targets(sample_targets)
    assert count == 2
    assert out_file.exists()

    with open(out_file, "r", encoding="utf-8") as f:
        records = [json.loads(line) for line in f]

    assert len(records) == 2
    for r in records:
        assert "passage_id" in r
        assert r["domain"] in ("wikipedia", "news", "government_report")
        assert "source_url" in r and r["source_url"].startswith("http")
        assert len(r["passage_ne"].strip()) > 0
        assert r["word_count"] >= 10
