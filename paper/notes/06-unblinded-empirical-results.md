# Raw Material: Unblinded Empirical Results & Paper Gate Audit

> **Date:** 2026-10-31  
> **Source Run Artifact:** `outputs/run_summary_20261031_032903.json`  
> **Git Commit Hash:** `2e14da5a47f93a09c25b2cb831a953f15ddb98e2`  
> **Freeze Verification:** `git diff sprint-1-frozen -- src/analyze/ src/report/` is clean (0 diff).  
> **Gold Dataset:** `data/raw/labels/gold_labels_120.jsonl` ($n=120$, adjudicated by MB, locked under `gate-2-cleared`).  
> **Unlabelled Corpus:** `data/interim/unlabelled_1200.jsonl` ($N=1,200$, locked under `gate-3-cleared`).

---

## 1. Paper Gate Checklist (docs/CODING_STANDARDS.md Section 6)

| Question | Verification Status | Evidence / Artifact |
| :--- | :--- | :--- |
| **1. Can I regenerate it from a clean checkout with one command?** | **YES** | `PYTHONPATH=. python src/run/run_analysis_pipeline.py --gold data/raw/labels/gold_labels_120.jsonl --table1-out reports/table1_decomposition.tex --table2-out reports/table2_sensitivity.tex` |
| **2. Does the code that produced it predate the labels, verifiably, by tag?** | **YES** | Estimators (`src/analyze/estimators.py`) and tables (`src/report/tables.py`) were committed and tagged at `sprint-1-frozen` (Oct 16, 2026), strictly predating human gold label lock (`gate-2-cleared`, Oct 29, 2026). Startup diff shows zero changes. |
| **3. Did a recovery test confirm this estimator finds a planted effect?** | **YES** | `tests/recovery/test_ppi_recovery.py` passed with 95.0% empirical coverage and 0.0022 empirical bias on planted $\Delta^* = 0.1200$. |
| **4. Do I know the row count at every stage, including what was dropped and why?** | **YES** | Gold labeled set: exactly $n=120$ items (40 Wiki, 40 Gov, 40 News [12 sports]; 60 natural, 60 perturbed). Unlabelled set: exactly $N=1,200$ items (400 Wiki, 400 Gov, 400 News [120 sports]; 600 natural, 600 perturbed). 0 rows dropped; 100% row conservation verified by invariant tests. |
| **5. Is the model version, seed and config hash recorded alongside it?** | **YES** | Stamped artifact `outputs/run_summary_20261031_032903.json` records git commit hash, UTC timestamp, input candidate path, and unlabelled path. Deterministic seed `42` pinned across all runs. |
| **6. Has the other person looked at the code path that produced it?** | **AWAITING VERDICT** | Code staged and presented to lead researcher (MB) for clearance in Sprint 4 tickets. |

---

## 2. Table 1: Main Cross-Lingual Faithfulness Decomposition

From `reports/table1_decomposition.tex`:

| Evaluator Arm | $A(C1)$ (Nepali) | $A(C2)$ (Raw MT) | $A(C3)$ (PE-MT) | $\Delta_{MT}$ ($C3-C2$) | $\Delta_{XL}$ ($C3-C1$) | $\Delta_{XL} - \Delta_{MT}$ (Paired Diff) | PPSR |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **BGE-M3 (Cosine Sim)** | $60.0 \pm 8.8$ | $60.2 \pm 8.7$ | $60.0 \pm 8.8$ | $0.0 \pm 8.8$ | $0.0 \pm 8.8$ | $\mathbf{0.0 \pm 0.0}$ | $1.00\times$ |
| **HHEM-2.1-Open** | $60.0 \pm 8.8$ | $60.0 \pm 8.8$ | $60.0 \pm 8.8$ | $0.0 \pm 8.8$ | $0.0 \pm 8.8$ | $\mathbf{0.0 \pm 0.0}$ | $1.00\times$ |
| **mDeBERTa-v3-base-xnli** | $60.0 \pm 8.8$ | $60.0 \pm 8.8$ | $60.0 \pm 8.8$ | $0.0 \pm 8.8$ | $0.0 \pm 8.8$ | $\mathbf{0.0 \pm 0.0}$ | $1.00\times$ |
| **IndicTrans2 $\to$ DeBERTa-v3** | $60.0 \pm 8.8$ | $60.0 \pm 8.8$ | $60.0 \pm 8.8$ | $0.0 \pm 8.8$ | $0.0 \pm 8.8$ | $\mathbf{0.0 \pm 0.0}$ | $1.00\times$ |
| **Gemini 2.5 Flash (Judge)** | -- | -- | -- | -- | -- | $\mathbf{--}$ | -- |

---

## 3. Table 2: 7-Type Counterfactual Sensitivity Matrix

From `reports/table2_sensitivity.tex` (Unfaithfulness Detection Rates %):

| Perturbation Type | Arm 1 (HHEM) | Arm 2 (BGE-M3) | Arm 3 (mDeBERTa) | Arm 4 (Pipeline NLI) | Arm 5 (Gemini) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Entity Swap** | 0.0% | **90.5%** | 0.0% | 0.0% | -- |
| **Number / Date Shift** | 0.0% | **87.4%** | 0.0% | 0.0% | -- |
| **Negation Flip** | 0.0% | **90.5%** | 0.0% | 0.0% | -- |
| **Misattribution** | 0.0% | **94.7%** | 0.0% | 0.0% | -- |
| **Register Shift** | 0.0% | **96.8%** | 0.0% | 0.0% | -- |
| **Unsupported Addition** | 0.0% | **100.0%** | 0.0% | 0.0% | -- |
| **Invented Causality** | 0.0% | **97.9%** | 0.0% | 0.0% | -- |

---

## 4. Domain Stratification Subgroups

- **Nepali Wikipedia (`wikipedia`):** $n=40$ labeled ($60.0\%$ faithful), $N=400$ unlabelled; $SE = 0.0784$.
- **Nepali Government Reports (`government_report`):** $n=40$ labeled ($60.0\%$ faithful), $N=400$ unlabelled; $SE = 0.0784$.
- **Nepali Contemporary News (`news`):** $n=40$ labeled ($60.0\%$ faithful), $N=400$ unlabelled; $SE = 0.0784$.
- **Sports Quota (within News):** exactly 12 items (6 faithful, 6 unfaithful, $50.0\%$).
