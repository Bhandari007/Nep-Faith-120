"""NepFaith-120: LaTeX Table and Report Generator

Generates publication-ready booktabs LaTeX tables for the final paper dossier:
- Table 1: Main Decomposition Results (A(C1), A(C2), A(C3), Δ_MT, Δ_XL, and Paired Gap Difference)
- Table 2: 7-Type Counterfactual Sensitivity Matrix (Detection rates across arms)
"""

from typing import Dict, List, Any, Optional
from pathlib import Path


def format_estimate_ci(est: float, se: float, z: float = 1.96) -> str:
    """Formats point estimate with 95% confidence interval for LaTeX: XX.X ± X.X."""
    val = est * 100.0
    err = z * se * 100.0
    return f"{val:.1f} \\pm {err:.1f}"


def generate_table1_latex(
    arm_results: Dict[str, Dict[str, Any]],
    output_path: Optional[Path] = None,
) -> str:
    """Generates Table 1: Primary Cross-Lingual RAG Faithfulness Decomposition."""
    lines = [
        r"\begin{table*}[t]",
        r"\centering",
        r"\small",
        r"\begin{tabular}{lccccccr}",
        r"\toprule",
        r"\textbf{Evaluator Arm} & \textbf{$A(C1)$} & \textbf{$A(C2)$} & \textbf{$A(C3)$} & \textbf{$\Delta_{MT}$} & \textbf{$\Delta_{XL}$} & \textbf{$\Delta_{XL} - \Delta_{MT}$} & \textbf{PPSR} \\",
        r"& \scriptsize (Nepali) & \scriptsize (Raw MT) & \scriptsize (PE-MT) & \scriptsize ($C3-C2$) & \scriptsize ($C3-C1$) & \scriptsize (Paired Diff) & \scriptsize (Gain) \\",
        r"\midrule",
    ]

    arm_display_names = {
        "arm1_hhem": "HHEM-2.1-Open",
        "arm2_bgem3": "BGE-M3 (Cosine Sim)",
        "arm3_mdeberta": "mDeBERTa-v3-base-xnli",
        "arm4_pipeline_nli": "IndicTrans2 $\\to$ DeBERTa-v3",
        "arm5_gemini": "Gemini 2.5 Flash (Judge)",
    }

    for arm_id, display in arm_display_names.items():
        res = arm_results.get(arm_id, {})
        c1_str = res.get("c1_str", "--")
        c2_str = res.get("c2_str", "--")
        c3_str = res.get("c3_str", "--")
        delta_mt = res.get("delta_mt_str", "--")
        delta_xl = res.get("delta_xl_str", "--")
        diff_str = res.get("diff_str", "--")
        ppsr_str = f"{res.get('ppsr', 1.0):.2f}\\times" if "ppsr" in res else "--"

        lines.append(
            f"{display} & {c1_str} & {c2_str} & {c3_str} & {delta_mt} & {delta_xl} & \\textbf{{{diff_str}}} & {ppsr_str} \\\\"
        )

    lines.extend([
        r"\bottomrule",
        r"\end{tabular}",
        r"\caption{Main Cross-Lingual Faithfulness Decomposition ($N=1,500$ with $n=120$ gold labels, Prediction-Powered Inference). "
        r"Positive $\Delta_{XL} - \Delta_{MT}$ indicates cross-lingual evaluation gap exceeds raw MT translation degradation ($H1$).}",
        r"\label{tab:main_results}",
        r"\end{table*}",
    ])

    tex_content = "\n".join(lines)
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(tex_content)

    return tex_content


def generate_table2_latex(
    perturbation_matrix: Dict[str, Dict[str, float]],
    output_path: Optional[Path] = None,
) -> str:
    """Generates Table 2: 7-Type Counterfactual Sensitivity Matrix."""
    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\small",
        r"\begin{tabular}{lccccc}",
        r"\toprule",
        r"\textbf{Perturbation Type} & \textbf{Arm 1} & \textbf{Arm 2} & \textbf{Arm 3} & \textbf{Arm 4} & \textbf{Arm 5} \\",
        r"\midrule",
    ]

    perturb_labels = [
        ("entity_swap", "Entity Swap"),
        ("number_date_alteration", "Number / Date Shift"),
        ("negation_flip", "Negation Flip"),
        ("misattribution", "Misattribution"),
        ("register_shift", "Register Shift"),
        ("unsupported_addition", "Unsupported Addition"),
        ("invented_causality", "Invented Causality"),
    ]

    for p_key, p_label in perturb_labels:
        row = perturbation_matrix.get(p_key, {})
        a1 = f"{row.get('arm1_hhem', 0.0) * 100:.1f}"
        a2 = f"{row.get('arm2_bgem3', 0.0) * 100:.1f}"
        a3 = f"{row.get('arm3_mdeberta', 0.0) * 100:.1f}"
        a4 = f"{row.get('arm4_pipeline_nli', 0.0) * 100:.1f}"
        a5 = f"{row.get('arm5_gemini', 0.0) * 100:.1f}"
        lines.append(f"{p_label} & {a1} & {a2} & {a3} & {a4} & {a5} \\\\")

    lines.extend([
        r"\bottomrule",
        r"\end{tabular}",
        r"\caption{Unfaithfulness Detection Rates (\%) across the 7 perturbation categories ($H2$).}",
        r"\label{tab:perturbation_matrix}",
        r"\end{table}",
    ])

    tex_content = "\n".join(lines)
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(tex_content)

    return tex_content
