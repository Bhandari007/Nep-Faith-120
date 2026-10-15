"""Tests for LaTeX Report Generator."""

import pytest
from src.report.tables import generate_table1_latex, generate_table2_latex, format_estimate_ci


def test_format_estimate_ci():
    res = format_estimate_ci(0.825, 0.02)
    assert res == "82.5 \\pm 3.9"


def test_generate_table1_latex(tmp_path):
    arm_data = {
        "arm1_hhem": {
            "c1_str": "65.2 \\pm 4.1",
            "c2_str": "74.8 \\pm 3.8",
            "c3_str": "82.0 \\pm 3.2",
            "delta_mt_str": "7.2 \\pm 2.1",
            "delta_xl_str": "16.8 \\pm 2.4",
            "diff_str": "9.6 \\pm 1.8",
            "ppsr": 1.72,
        }
    }
    tex_path = tmp_path / "table1.tex"
    content = generate_table1_latex(arm_data, output_path=tex_path)
    assert "\\begin{table*}" in content
    assert "\\textbf{HHEM-2.1-Open}" in content or "HHEM-2.1-Open" in content
    assert tex_path.exists()


def test_generate_table2_latex(tmp_path):
    matrix = {
        "entity_swap": {
            "arm1_hhem": 0.85,
            "arm2_bgem3": 0.42,
            "arm3_mdeberta": 0.78,
            "arm4_pipeline_nli": 0.82,
            "arm5_gemini": 0.94,
        }
    }
    tex_path = tmp_path / "table2.tex"
    content = generate_table2_latex(matrix, output_path=tex_path)
    assert "\\begin{table}" in content
    assert "Entity Swap" in content
    assert tex_path.exists()
