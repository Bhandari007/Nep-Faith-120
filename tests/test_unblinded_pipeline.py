"""Tests for Sprint 4: Unblinded Pipeline Execution & Gold Label Ingestion."""

import json
from pathlib import Path
import pytest

from src.run.run_analysis_pipeline import run_pipeline_dry_run


def test_unblinded_pipeline_execution(tmp_path):
    """Verifies that the unblinded pipeline ingests the locked gold labels and produces valid estimates."""
    gold_path = Path("data/raw/labels/gold_labels_120.jsonl")
    cand_path = Path("data/interim/predictions/predictions_candidates_120.jsonl")
    unlab_path = Path("data/interim/predictions/predictions_unlabelled_1200.jsonl")

    assert gold_path.exists(), "Official locked gold labels must exist"
    assert cand_path.exists(), "Candidate proxy predictions must exist"
    assert unlab_path.exists(), "Unlabelled proxy predictions must exist"

    # Temporary output paths for tables
    table1_out = tmp_path / "table1_unblinded.tex"
    table2_out = tmp_path / "table2_unblinded.tex"

    # Record mtime of gold_labels_120.jsonl to verify zero modification
    gold_mtime_before = gold_path.stat().st_mtime

    results = run_pipeline_dry_run(
        cand_predictions_path=cand_path,
        unlab_predictions_path=unlab_path,
        gold_labels_path=gold_path,
        table1_output_path=table1_out,
        table2_output_path=table2_out,
    )

    # Invariant: Zero writes to data/raw/labels/
    assert gold_path.stat().st_mtime == gold_mtime_before

    # Verify output tables exist
    assert table1_out.exists()
    assert table2_out.exists()

    # Verify evaluated arms
    assert len(results) >= 4, "Expected at least 4 automated evaluator arms"
    for arm_id, arm_stats in results.items():
        assert "c1_str" in arm_stats
        assert "c2_str" in arm_stats
        assert "c3_str" in arm_stats
        assert "delta_mt_str" in arm_stats
        assert "delta_xl_str" in arm_stats
        assert "diff_str" in arm_stats
        assert "ppsr" in arm_stats
        assert arm_stats["ppsr"] >= 0.0

    # Verify Table 1 content
    table1_text = table1_out.read_text(encoding="utf-8")
    assert "\\begin{table*}" in table1_text
    assert "\\toprule" in table1_text
    assert "\\bottomrule" in table1_text


def test_unblinded_pipeline_empirical_sensitivity_matrix(tmp_path):
    """Verifies that Table 2 computes actual empirical detection rates across 7 perturbation types."""
    gold_path = Path("data/raw/labels/gold_labels_120.jsonl")
    cand_path = Path("data/interim/predictions/predictions_candidates_120.jsonl")
    unlab_path = Path("data/interim/predictions/predictions_unlabelled_1200.jsonl")

    table1_out = tmp_path / "table1.tex"
    table2_out = tmp_path / "table2.tex"

    run_pipeline_dry_run(
        cand_predictions_path=cand_path,
        unlab_predictions_path=unlab_path,
        gold_labels_path=gold_path,
        table1_output_path=table1_out,
        table2_output_path=table2_out,
    )

    table2_text = table2_out.read_text(encoding="utf-8")
    assert "\\begin{table}" in table2_text
    assert "Entity Swap" in table2_text
    assert "Number / Date Shift" in table2_text
    assert "Negation Flip" in table2_text
    assert "Misattribution" in table2_text
    assert "Register Shift" in table2_text
    assert "Unsupported Addition" in table2_text
    assert "Invented Causality" in table2_text
    # Arm 2 on entity_swap should be ~90.5% (not placeholder 85.0%)
    assert "90.5" in table2_text



def test_unblinded_pipeline_reproducibility_stamping(tmp_path):
    """Verifies that run produces stamped metadata in outputs/ directory."""
    from src.run.run_analysis_pipeline import run_pipeline_with_stamping
    gold_path = Path("data/raw/labels/gold_labels_120.jsonl")
    cand_path = Path("data/interim/predictions/predictions_candidates_120.jsonl")
    unlab_path = Path("data/interim/predictions/predictions_unlabelled_1200.jsonl")

    outputs_dir = tmp_path / "outputs"
    table1_out = tmp_path / "table1.tex"
    table2_out = tmp_path / "table2.tex"

    stamp_file = run_pipeline_with_stamping(
        cand_predictions_path=cand_path,
        unlab_predictions_path=unlab_path,
        gold_labels_path=gold_path,
        table1_output_path=table1_out,
        table2_output_path=table2_out,
        outputs_dir=outputs_dir,
    )

    assert stamp_file.exists()
    stamp_data = json.loads(stamp_file.read_text(encoding="utf-8"))
    assert "git_commit_hash" in stamp_data
    assert "timestamp" in stamp_data
    assert "arm_results" in stamp_data
    assert "sensitivity_matrix" in stamp_data
    assert "domain_breakdown" in stamp_data


def test_stratified_domain_breakdown(tmp_path):
    """Verifies domain-stratified estimates across Wikipedia, Government Reports, and News."""
    from src.run.run_analysis_pipeline import compute_domain_breakdown
    gold_path = Path("data/raw/labels/gold_labels_120.jsonl")
    cand_path = Path("data/interim/predictions/predictions_candidates_120.jsonl")
    unlab_path = Path("data/interim/predictions/predictions_unlabelled_1200.jsonl")

    breakdown = compute_domain_breakdown(
        cand_predictions_path=cand_path,
        unlab_predictions_path=unlab_path,
        gold_labels_path=gold_path,
    )

    for domain in ["wikipedia", "government_report", "news"]:
        assert domain in breakdown
        info = breakdown[domain]
        assert info["n_labeled"] == 40
        assert info["n_unlabeled"] == 400
        assert "mean" in info
        assert "se" in info


