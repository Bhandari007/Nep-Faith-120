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


def test_configurable_arm5_llm_judge_openai_compatible(tmp_path, monkeypatch):
    """Verifies that Arm 5 can be configured with an OpenAI-compatible / OSS endpoint."""
    from src.run.scorers import Arm5LLMJudge
    import unittest.mock as mock

    judge = Arm5LLMJudge(
        provider="openai_compatible",
        model_id="gpt-4o",
        api_key="mock-api-key",
        base_url="https://api.openai.com/v1",
        cache_dir=tmp_path,
    )
    assert judge.provider == "openai_compatible"
    assert judge.model_id == "gpt-4o"

    # Mock requests.post
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "choices": [
            {
                "message": {
                    "content": '{"verdict": "Supported", "confidence": 0.98, "rationale": "Directly supported by the text."}'
                }
            }
        ]
    }

    with mock.patch("requests.post", return_value=mock_response):
        passage = "Kathmandu is the capital of Nepal."
        claim = "Kathmandu is Nepal's capital."
        res = judge.score_claim(passage, claim, use_cache=False)
        assert res["score"] == 1.0
        assert res["predicted_label"] == ClaimLabel.SUPPORTED.value
        assert res["confidence"] == 0.98
        assert res["provider"] == "openai_compatible"
        assert res["model_id"] == "gpt-4o"


def test_arm5_cache_isolation_across_models(tmp_path):
    """Verifies that Arm 5 isolates cache entries across different models/providers."""
    from src.run.scorers import Arm5LLMJudge
    import unittest.mock as mock

    mock_resp1 = mock.Mock()
    mock_resp1.status_code = 200
    mock_resp1.json.return_value = {
        "choices": [{"message": {"content": '{"verdict": "Supported", "confidence": 0.9}'}}]
    }

    mock_resp2 = mock.Mock()
    mock_resp2.status_code = 200
    mock_resp2.json.return_value = {
        "choices": [{"message": {"content": '{"verdict": "Contradicted", "confidence": 0.8}'}}]
    }

    judge_a = Arm5LLMJudge(
        provider="openai_compatible",
        model_id="model-alpha",
        api_key="mock",
        cache_dir=tmp_path,
    )
    judge_b = Arm5LLMJudge(
        provider="openai_compatible",
        model_id="model-beta",
        api_key="mock",
        cache_dir=tmp_path,
    )

    passage = "Sample passage"
    claim = "Sample claim"

    with mock.patch("requests.post", return_value=mock_resp1):
        res_a = judge_a.score_claim(passage, claim, use_cache=True)

    with mock.patch("requests.post", return_value=mock_resp2):
        res_b = judge_b.score_claim(passage, claim, use_cache=True)

    # Different models must have independent cache files and results
    assert res_a["predicted_label"] == "Supported"
    assert res_b["predicted_label"] == "Contradicted"
    cache_files = list(tmp_path.glob("*.json"))
    assert len(cache_files) == 2


def test_arm5_gemini_judge_evaluation(tmp_path):
    """Verifies that Arm 5 Gemini evaluator correctly formats responses and maps verdicts."""
    from src.run.scorers import Arm5LLMJudge
    import unittest.mock as mock

    judge = Arm5LLMJudge(
        provider="gemini",
        model_id="gemini-3.6-flash",
        cache_dir=tmp_path,
        api_keys=["mock_key_1", "mock_key_2"],
    )
    assert judge.provider == "gemini"
    assert judge.model_id == "gemini-3.6-flash"

    # Mock evaluate_claim on rotator
    mock_eval = {
        "claim": "Test claim",
        "label": "Supported",
        "explanation": "Directly supported by the Nepali passage.",
        "confidence": 0.95,
        "cached": False,
        "key_used": "mock...",
    }

    with mock.patch.object(judge.rotator, "evaluate_claim", return_value=mock_eval):
        res = judge.score_claim("Nepali passage", "Test claim", use_cache=False)
        assert res["score"] == 1.0
        assert res["predicted_label"] == "Supported"
        assert res["confidence"] == 0.95


def test_gemini_rotator_request_tracking(tmp_path):
    """Verifies that GeminiRotator accurately tracks request count, cache hits, and key usage."""
    from src.run.gemini_client import GeminiRotator
    import unittest.mock as mock

    rotator = GeminiRotator(
        api_keys=["key_alpha", "key_beta"],
        cache_dir=str(tmp_path / "llm_cache"),
        pace_delay=0.0,
    )
    assert rotator.total_requests_made == 0
    assert rotator.total_cache_hits == 0

    mock_resp = mock.Mock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "candidates": [{"content": {"parts": [{"text": '{"result": "ok"}'}]}}]
    }

    with mock.patch("requests.post", return_value=mock_resp):
        res1 = rotator.generate_content("test prompt 1", use_cache=True)
        assert res1["cached"] is False
        assert rotator.total_requests_made == 1
        assert rotator.total_cache_hits == 0

        # Second call to same prompt should hit cache
        res2 = rotator.generate_content("test prompt 1", use_cache=True)
        assert res2["cached"] is True
        assert rotator.total_requests_made == 1
        assert rotator.total_cache_hits == 1

        stats = rotator.get_stats()
        assert stats["total_requests_made"] == 1
        assert stats["total_cache_hits"] == 1
        assert len(stats["requests_by_key"]) == 1



