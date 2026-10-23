"""Tests for Authentic Corpus Parallel Harvester (Path 2)."""

import json
from pathlib import Path
import pytest


def test_harvested_authentic_passages_invariants(tmp_path):
    """Verifies that the parallel authentic passage harvester outputs valid, traceable Devanagari passages."""
    from src.prepare.crawl_authentic_corpus import AuthenticCorpusHarvester

    out_file = tmp_path / "authentic_passages_test.jsonl"
    harvester = AuthenticCorpusHarvester(output_file=out_file, max_workers=4)

    # Test with a minimal target of Wikipedia articles
    test_targets = [
        {
            "domain": "wikipedia",
            "sub_genre": "culture_heritage",
            "source_type": "wikipedia",
            "title": "पशुपतिनाथ मन्दिर",
            "url": "https://ne.wikipedia.org/wiki/पशुपतिनाथ_मन्दिर",
            "text": "पशुपतिनाथको मन्दिर काठमाडौँ जिल्लामा रहेको ऐतिहासिक, धार्मिक एवं पर्यटकीय दृष्टिले महत्त्वपूर्ण स्थल हो। यो मन्दिर बागमती नदीको किनारमा रहेको छ।",
        },
        {
            "domain": "wikipedia",
            "sub_genre": "biodiversity_parks",
            "source_type": "wikipedia",
            "title": "सगरमाथा राष्ट्रिय निकुञ्ज",
            "url": "https://ne.wikipedia.org/wiki/सगरमाथा_राष्ट्रिय_निकुञ्ज",
            "text": "सगरमाथा राष्ट्रिय निकुञ्ज सन् १९७६ मा स्थापना भएको हो। यस निकुञ्जमा विश्वको सर्वोच्च शिखर सगरमाथा सहित ल्होत्से र नुप्त्से जस्ता प्रमुख हिमालहरू पर्दछन्।",
        },
    ]

    passages = harvester.harvest_targets(test_targets)
    assert len(passages) >= 2
    assert out_file.exists()

    for p in passages:
        assert p.passage_id
        assert p.domain in ["wikipedia", "government_report", "news"]
        assert p.sub_genre
        assert p.source_url.startswith("http")
        assert len(p.passage_ne.strip()) > 50
        # Verifies authentic Devanagari characters present
        assert any("\u0900" <= c <= "\u097f" for c in p.passage_ne)
        assert p.word_count >= 20


def test_authentic_passages_60_invariants():
    """Verifies that the compiled authentic 60 passages dataset strictly upholds all schema and domain quotas."""
    auth_file = Path("data/derived/authentic_passages_60.jsonl")
    assert auth_file.exists(), "authentic_passages_60.jsonl must exist"

    items = []
    with open(auth_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                items.append(json.loads(line))

    assert len(items) == 60, f"Expected exactly 60 authentic passages, got {len(items)}"

    domain_counts = {}
    sub_genre_counts = {}
    urls = set()

    for it in items:
        dom = it["domain"]
        sg = it["sub_genre"]
        u = it["source_url"]
        domain_counts[dom] = domain_counts.get(dom, 0) + 1
        sub_genre_counts[sg] = sub_genre_counts.get(sg, 0) + 1
        urls.add(u)

        assert it["source_title"] and len(it["source_title"]) >= 3
        assert u.startswith("http")
        assert len(it["passage_ne"].strip()) >= 40
        assert any("\u0900" <= c <= "\u097f" for c in it["passage_ne"])
        assert it["word_count"] >= 15

    # Exactly 20 per macro-stratum
    assert domain_counts.get("wikipedia") == 20
    assert domain_counts.get("government_report") == 20
    assert domain_counts.get("news") == 20

    # News must have exactly 6 sports passages (30% quota)
    assert sub_genre_counts.get("sports") == 6

    # All 60 URLs are distinct
    assert len(urls) == 60

