"""Tests for the 5 Evaluator Arms Suite."""

import pytest
from src.run.scorers import get_evaluator_suite, BaseScorer
from src.prepare.schema import ClaimLabel


def test_evaluator_suite_arms(tmp_path):
    suite = get_evaluator_suite(cache_dir=tmp_path)
    assert len(suite) == 5
    expected_arms = {"arm1_hhem", "arm2_bgem3", "arm3_mdeberta", "arm4_pipeline_nli", "arm5_gemini"}
    assert set(suite.keys()) == expected_arms


def test_scorer_deterministic_caching(tmp_path):
    suite = get_evaluator_suite(cache_dir=tmp_path)
    scorer = suite["arm2_bgem3"]

    passage = "Sagarmatha is Mount Everest located in Nepal."
    claim = "Mount Everest is located in Nepal."

    res1 = scorer.score_claim(passage, claim, use_cache=True)
    assert "score" in res1
    assert "predicted_label" in res1
    assert res1["arm_name"] == "arm2_bgem3"

    # Second call must hit cache
    res2 = scorer.score_claim(passage, claim, use_cache=True)
    assert res1 == res2
