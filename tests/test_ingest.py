"""Tests for Corpus Ingestion and Normalization Pipeline."""

import pytest
from src.prepare.schema import Domain, CorpusPassage
from src.prepare.ingest import (
    normalize_devanagari,
    is_preeti_encoded,
    convert_preeti_to_unicode,
    count_tokens,
    chunk_into_passages,
    create_seed_corpus,
)


def test_normalize_devanagari():
    raw = "नेपाल\t  सरकार \r\n\n\n  काठमाडौँ  "
    norm = normalize_devanagari(raw)
    assert "\t" not in norm
    assert "\r" not in norm
    assert "  " not in norm
    assert norm == "नेपाल सरकार\n\nकाठमाडौँ"


def test_preeti_detection_and_transliteration():
    preeti_sample = "g]kfn ;/sf/ k|wfgdGqL"
    assert is_preeti_encoded(preeti_sample) is True

    unicode_sample = "नेपाल सरकार प्रधानमन्त्री"
    assert is_preeti_encoded(unicode_sample) is False

    translit = convert_preeti_to_unicode(preeti_sample)
    assert "नेपाल" in translit
    assert "सरकार" in translit
    assert "प्रधानमन्त्री" in translit


def test_chunk_into_passages():
    text = (
        "नेपाल एक सुन्दर देश हो। यसको राजधानी काठमाडौँ हो। "
        "यहाँ विभिन्न जातजाति र भाषाभाषीका मानिसहरू बसोबास गर्दछन्। "
        "सगरमाथा संसारको सर्वोच्च शिखर हो। यो नेपालको सोलुखुम्बु जिल्लामा पर्दछ।"
    )
    chunks = chunk_into_passages(text, min_tokens=5, max_tokens=20)
    assert len(chunks) >= 1
    for chunk in chunks:
        tok_len = count_tokens(chunk)
        assert tok_len <= 25  # allowance for boundary splitting


def test_create_seed_corpus_schema():
    seed = create_seed_corpus()
    assert len(seed) >= 7

    domains = set()
    sports_found = False

    for rec in seed:
        passage = CorpusPassage(**rec)
        domains.add(passage.domain)
        if passage.sub_genre == "sports":
            sports_found = True
            assert passage.domain == Domain.NEWS

    assert Domain.WIKIPEDIA in domains
    assert Domain.GOVERNMENT_REPORT in domains
    assert Domain.NEWS in domains
    assert sports_found is True
