# NepFaith-120: Decoupling Translation Error from Cross-Lingual Evaluation in Low-Resource RAG Faithfulness

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Tests Passing](https://img.shields.io/badge/tests-76%20passed-brightgreen.svg)]()
[![Paper Format](https://img.shields.io/badge/paper-IEEE%20Conference-orange.svg)](paper/manuscript.html)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> **Why cross-lingual faithfulness scoring fails on Nepali $\to$ English RAG, and how much of the failure is translation's fault.**  
> A causal error decomposition benchmark decoupling machine translation error ($\Delta_{\text{MT}}$) from cross-lingual evaluation bottlenecks ($\Delta_{\text{XL}}$) using a minimal-pair human post-edited translation ceiling ($C3$) and Prediction-Powered Inference (PPI++).

---

## Authors

- **Muskan Bhandari** (`bmuskan007@gmail.com`)
- **Sujan Sharma** (`ersujansharma@gmail.com`)

---

## Table of Contents
1. [Core Scientific Concept](#1-core-scientific-concept)
2. [Environment Setup & Installation](#2-environment-setup--installation)
3. [Running the Experiments](#3-running-the-experiments)
   - [Evaluating with Frontier LLM Judges (Gemini / GPT / Local OSS)](#evaluating-with-frontier-llm-judges)
   - [Evaluating with Classical Baselines (HHEM, BGE-M3, mDeBERTa)](#evaluating-with-classical-baselines)
4. [Statistical Analysis & Table Generation (PPI++)](#4-statistical-analysis--table-generation)
5. [Running Verification & Integrity Tests](#5-running-verification--integrity-tests)
6. [Reading & Compiling the Paper](#6-reading--compiling-the-paper)
7. [Repository Structure & Data Artifacts](#7-repository-structure--data-artifacts)

---

## 1. Core Scientific Concept

When evaluating whether an English generated answer is faithful to a retrieved Nepali passage, systems face a dilemma:
- **Condition $C1$ (Direct Cross-Lingual):** The evaluator scores the English claim directly against the verbatim Nepali context.
- **Condition $C2$ (Translate-then-Evaluate):** The Nepali context is machine-translated into English via neural MT (IndicTrans2), and scored monolingually.
- **Condition $C3$ (Human Post-Edited Ceiling):** Bilingual human editors minimally correct MT errors while preserving phrasing.

### The Causal Error Decomposition
$$\Delta_{\text{MT}} = A(C3) - A(C2) \quad \text{(Penalty attributable strictly to MT errors)}$$
$$\Delta_{\text{XL}} = A(C3) - A(C1) \quad \text{(Penalty attributable strictly to cross-lingual reasoning)}$$
$$\text{Paired Difference} = \Delta_{\text{XL}} - \Delta_{\text{MT}} = A(C2) - A(C1)$$

**Key Empirical Finding:** On frontier LLM judges (`gemini-3.6-flash`), $A(C1) = 56.7\%$ ($91.67\%$ agreement with human ground truth), but drops to $A(C2) = 4.2\%$ under raw MT (a **52.5 percentage point collapse**). Human post-editing restores faithfulness to $A(C3) = 31.7\%$, proving that **machine translation noise is the dominant driver of evaluation failure** ($\Delta_{\text{MT}} = +27.5\%$, $\Delta_{\text{XL}} = -25.0\%$).

---

## 2. Environment Setup & Installation

### Prerequisites
- Python 3.10, 3.11, or 3.12
- Git

### Quick Setup
```bash
# 1. Clone the repository
git clone https://github.com/muskanbhandari/NepFaith-120.git
cd NepFaith-120

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Configure API Keys (Choose your provider)
```bash
# If running Gemini (Default frontier judge):
export GEMINI_API_KEY="your-gemini-api-key"

# If running OpenAI GPT models:
export OPENAI_API_KEY="your-openai-api-key"
```

---

## 3. Running the Experiments

All model scoring runs through [`src/run/evaluate_corpus.py`](src/run/evaluate_corpus.py). Results are cached deterministically under `cache/scorers/` so identical prompt calls are never billed twice.

### Evaluating with Frontier LLM Judges

#### A. Google Gemini (Default Arm 5)
```bash
python src/run/evaluate_corpus.py \
  --input data/interim/preannotations/gold_candidates_120.jsonl \
  --output data/interim/predictions/predictions_candidates_120.jsonl \
  --arms arm5_gemini \
  --provider gemini \
  --model-id gemini-3.6-flash \
  --conditions C1 C2 C3
```

#### B. OpenAI GPT Models (`gpt-4o`, `gpt-4o-mini`, `o1`)
```bash
export OPENAI_API_KEY="sk-..."

python src/run/evaluate_corpus.py \
  --input data/interim/preannotations/gold_candidates_120.jsonl \
  --output data/interim/predictions/predictions_gpt4o_120.jsonl \
  --arms arm5_gemini \
  --provider openai \
  --model-id gpt-4o \
  --conditions C1 C2 C3
```

#### C. Local Open-Source Models via vLLM / Ollama
The pipeline natively supports any local or self-hosted model running an OpenAI-compatible endpoint.

*Example with [vLLM](https://github.com/vllm-project/vllm):*
```bash
# Start your local vLLM instance
vllm serve meta-llama/Llama-3.1-70B-Instruct --port 8000

# Run evaluation against localhost
python src/run/evaluate_corpus.py \
  --input data/interim/preannotations/gold_candidates_120.jsonl \
  --output data/interim/predictions/predictions_llama70b_120.jsonl \
  --arms arm5_gemini \
  --provider openai_compatible \
  --base-url http://localhost:8000/v1 \
  --model-id meta-llama/Llama-3.1-70B-Instruct \
  --conditions C1 C2 C3
```

*Example with [Ollama](https://ollama.com/):*
```bash
# Run against local Ollama instance (default port 11434)
python src/run/evaluate_corpus.py \
  --input data/interim/preannotations/gold_candidates_120.jsonl \
  --output data/interim/predictions/predictions_qwen_120.jsonl \
  --arms arm5_gemini \
  --provider openai_compatible \
  --base-url http://localhost:11434/v1 \
  --model-id qwen2.5:72b \
  --conditions C1 C2 C3
```

*Example with Cloud Providers ([OpenRouter](https://openrouter.ai/), [Groq](https://groq.com/)):*
```bash
export OPENAI_API_KEY="your-openrouter-key"

python src/run/evaluate_corpus.py \
  --input data/interim/preannotations/gold_candidates_120.jsonl \
  --output data/interim/predictions/predictions_openrouter_120.jsonl \
  --arms arm5_gemini \
  --provider openai_compatible \
  --base-url https://openrouter.ai/api/v1 \
  --model-id qwen/qwen-2.5-72b-instruct \
  --conditions C1 C2 C3
```

---

### Evaluating with Classical Baselines

To run the four classical open-source baseline arms (HHEM, BGE-M3, mDeBERTa, Pipeline NLI):
```bash
python src/run/evaluate_corpus.py \
  --input data/interim/preannotations/gold_candidates_120.jsonl \
  --output data/interim/predictions/predictions_candidates_120.jsonl \
  --arms arm1_hhem arm2_bgem3 arm3_mdeberta arm4_pipeline_nli \
  --conditions C1 C2 C3
```

---

## 4. Statistical Analysis & Table Generation

Once model predictions are generated, run the statistical analysis pipeline to compute cluster-robust Prediction-Powered Inference (PPI++) and regenerate publication LaTeX tables:

```bash
PYTHONPATH=. python src/run/run_analysis_pipeline.py \
  --gold data/raw/labels/gold_labels_120.jsonl \
  --candidates data/interim/predictions/predictions_candidates_120.jsonl \
  --unlabelled data/interim/predictions/predictions_unlabelled_1200.jsonl \
  --table1-out reports/table1_decomposition.tex \
  --table2-out reports/table2_sensitivity.tex \
  --summary-out outputs/run_summary_latest.json
```

This updates:
- `reports/table1_decomposition.tex`: Main decomposition table with standard errors & PPSR.
- `reports/table2_sensitivity.tex`: 7-type perturbation detection matrix.
- `outputs/run_summary_latest.json`: Timestamped, versioned metadata snapshot.

---

## 5. Running Verification & Integrity Tests

The repository maintains a rigorous test suite of 76 tests covering statistical recovery, data invariants, citation audits, and manuscript formatting:

```bash
# Run the complete test suite
python -m pytest tests/

# Run specific test suites:
python -m pytest tests/recovery/test_ppi_recovery.py  # Monte Carlo planted effect recovery
python -m pytest tests/test_manuscript.py            # LaTeX environment & table verification
python -m pytest tests/test_citations.py             # Human citation verification audit
python -m pytest tests/invariants/                   # Zero-leakage row conservation tests
```

---

## 6. Reading & Compiling the Paper

The complete manuscript is drafted in publication-ready **IEEE two-column conference format**.

### Option A: Immediate In-Browser Reader (Zero Install Needed)
Open [`paper/manuscript.html`](paper/manuscript.html) directly in Google Chrome, Firefox, or Safari:
```bash
# Linux
xdg-open paper/manuscript.html

# macOS
open paper/manuscript.html
```
*Renders an interactive IEEE two-column view with MathJax formulas, complete tables, and bibliography.*

### Option B: Compile in Overleaf
1. Upload the pre-built bundle: [`paper/nepfaith120_ieee_manuscript.zip`](paper/nepfaith120_ieee_manuscript.zip).
2. Click **Recompile** in Overleaf to produce the camera-ready PDF.

### Option C: Compile Locally with `pdflatex`
```bash
cd paper
pdflatex manuscript_standalone.tex
bibtex manuscript_standalone
pdflatex manuscript_standalone.tex
pdflatex manuscript_standalone.tex
```

---

## 7. Repository Structure & Data Artifacts

```
NepFaith-120/
├── data/
│   ├── raw/corpus/                    # Immutable crawled Nepali source passages
│   ├── raw/labels/                    # Adjudicated gold labels (n=120)
│   ├── interim/preannotations/        # Candidate items before scoring (n=120)
│   └── interim/predictions/           # Stamped model evaluations (n=120, N=1,200)
│
├── src/
│   ├── prepare/                       # Passage crawler, proposition extractor, 7-type perturbator
│   ├── run/                           # Scorers (Arms 1–5), Gemini rotator, evaluate_corpus CLI
│   ├── analyze/                       # Cluster-robust PPI++ estimators (FROZEN)
│   └── report/                        # LaTeX table generators (FROZEN)
│
├── reports/
│   ├── table1_decomposition.tex       # Table 1: C1, C2, C3 decomposition & PPSR
│   └── table2_sensitivity.tex         # Table 2: 7-type perturbation detection rates
│
├── paper/
│   ├── manuscript.html                # Interactive IEEE reader with MathJax
│   ├── manuscript_standalone.tex      # Self-contained IEEE conference LaTeX
│   ├── manuscript.tex                 # Modular master LaTeX draft
│   ├── nepfaith120_ieee_manuscript.zip# Overleaf / arXiv submission package
│   ├── references.bib                 # 100% human-verified BibTeX entries
│   └── notes/                         # Unblinded empirical findings & error logs
│
├── cache/scorers/                     # Deterministic LLM response cache
├── tests/                             # 76 passing unit, invariant & recovery tests
└── requirements.txt                   # Locked environment dependencies
```

---

## Citation

```bibtex
@inproceedings{bhandari2026nepfaith120,
  author    = {Bhandari, Muskan and Sharma, Sujan},
  title     = {NepFaith-120: Decoupling Translation Error from Cross-Lingual Evaluation in Low-Resource RAG Faithfulness},
  booktitle = {Proceedings of the IEEE Conference on Artificial Intelligence (CAI)},
  year      = {2026}
}
```
