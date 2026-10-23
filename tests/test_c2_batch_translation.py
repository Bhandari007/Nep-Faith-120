"""Tests for Ticket 03: IndicTrans2 Condition C2 Batch Generation."""

import json
from pathlib import Path
import pytest


def test_batch_translate_c2_invariants(tmp_path, monkeypatch):
    """Verifies that batch translation runner populates c2_raw_mt on all candidate items."""
    from src.run.batch_translate_c2 import BatchC2Translator

    # Create dummy candidate file
    dummy_input = tmp_path / "candidates.jsonl"
    dummy_output = tmp_path / "candidates_with_c2.jsonl"

    sample_items = [
        {
            "item_id": "item_001",
            "domain": "wikipedia",
            "sub_genre": "culture_heritage",
            "source_provenance": "natural",
            "perturbation_type": None,
            "perturbation_span": None,
            "passage_ne": "सगरमाथा नेपालमा अवस्थित छ।",
            "query_en": "Where is Mount Everest?",
            "answer_en": "Mount Everest is in Nepal.",
            "c2_raw_mt": None,
            "c3_post_edited_mt": None,
            "retrieval_condition": "full_support",
            "sampling_weight": 1.0,
            "claims": [
                {
                    "claim_id": "item_001_c1",
                    "claim_text": "Mount Everest is in Nepal.",
                    "is_critical": True,
                    "gold_label": None,
                }
            ],
        }
    ]
    with open(dummy_input, "w", encoding="utf-8") as f:
        for it in sample_items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")

    # Mock translator to avoid heavy model download during quick unit test
    class MockTranslator:
        def __init__(self, *args, **kwargs):
            pass
        def translate_batch(self, texts, use_cache=True, batch_size=8):
            return ["Mount Everest is located in Nepal." for _ in texts]

    monkeypatch.setattr("src.run.batch_translate_c2.IndicTrans2Translator", MockTranslator)

    runner = BatchC2Translator(input_path=dummy_input, output_path=dummy_output, cache_dir=tmp_path / "cache")
    processed = runner.run()

    assert len(processed) == 1
    assert dummy_output.exists()
    assert processed[0]["c2_raw_mt"] == "Mount Everest is located in Nepal."
    assert processed[0]["c3_post_edited_mt"] is None


def test_generated_gold_candidates_c2_coverage():
    """Validates that real candidate dataset has 100% C2 MT populated and strict invariants."""
    candidate_path = Path("data/interim/preannotations/gold_candidates_120.jsonl")
    if not candidate_path.exists():
        pytest.skip("gold_candidates_120.jsonl not found")

    items = []
    with open(candidate_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))

    assert len(items) == 120
    for it in items:
        assert it.get("c2_raw_mt"), f"Item {it.get('item_id')} missing c2_raw_mt"
        assert isinstance(it["c2_raw_mt"], str) and len(it["c2_raw_mt"].strip()) > 0
        assert it.get("c3_post_edited_mt") is None or isinstance(it.get("c3_post_edited_mt"), str)
        for claim in it.get("claims", []):
            assert claim.get("gold_label") is None, f"Claim {claim.get('claim_id')} has premature gold_label"

