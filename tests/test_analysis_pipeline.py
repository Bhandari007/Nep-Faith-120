"""Tests for End-to-End Analysis & Table Generation Pipeline."""

import json
from pathlib import Path
import pytest

from src.run.run_analysis_pipeline import run_pipeline_dry_run


def test_analysis_pipeline_dry_run(tmp_path):
    """Verifies that the full analysis pipeline connects proxy predictions to LaTeX tables."""
    # Create sample unlabelled predictions
    unlab_file = tmp_path / "predictions_unlabelled.jsonl"
    cand_file = tmp_path / "predictions_candidates.jsonl"

    sample_unlab = [
        {
            "item_id": f"unlab_{i:04d}",
            "domain": "wikipedia",
            "predictions": {
                "arm2_bgem3": {
                    "C1": {"derived_faithfulness": 1 if i % 2 == 0 else 0},
                    "C2": {"derived_faithfulness": 1 if i % 3 == 0 else 0},
                    "C3": {"derived_faithfulness": 1},
                }
            }
        }
        for i in range(20)
    ]
    with open(unlab_file, "w", encoding="utf-8") as f:
        for rec in sample_unlab:
            f.write(json.dumps(rec) + "\n")

    sample_cand = [
        {
            "item_id": f"item_{i:03d}",
            "domain": "wikipedia",
            "predictions": {
                "arm2_bgem3": {
                    "C1": {"derived_faithfulness": 1 if i % 2 == 0 else 0},
                    "C2": {"derived_faithfulness": 1 if i % 3 == 0 else 0},
                    "C3": {"derived_faithfulness": 1},
                }
            }
        }
        for i in range(10)
    ]
    with open(cand_file, "w", encoding="utf-8") as f:
        for rec in sample_cand:
            f.write(json.dumps(rec) + "\n")

    out_table1 = tmp_path / "table1_dryrun.tex"
    out_table2 = tmp_path / "table2_dryrun.tex"

    summary = run_pipeline_dry_run(
        cand_predictions_path=cand_file,
        unlab_predictions_path=unlab_file,
        table1_output_path=out_table1,
        table2_output_path=out_table2,
    )

    assert out_table1.exists()
    assert out_table2.exists()
    assert "arm2_bgem3" in summary
    assert "diff_str" in summary["arm2_bgem3"]

    table1_content = out_table1.read_text(encoding="utf-8")
    assert "\\begin{table*}" in table1_content
    assert "BGE-M3 (Cosine Sim)" in table1_content
