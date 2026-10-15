# ADR 0002: Model Selection & Decoupled Evaluation Architecture

- **Status:** Accepted
- **Date:** 2026-10-15
- **Deciders:** Muskan Bhandari (Lead Researcher), Antigravity AI
- **Related Issues:** [Sprint 0 Issue 07](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/.scratch/sprint-0/issues/07-pin-models-and-environment.md), [Sprint 1 Issue 05](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/.scratch/sprint-1/issues/05-evaluator-arms-runner.md)

---

## Context & Problem Statement

In benchmarking cross-lingual RAG faithfulness, model choices introduce subtle methodological pitfalls:
1. **Intra-Family Self-Preference Bias:** Evaluating generated answers with a judge model from the same model family (e.g. Llama evaluating Llama, or GPT-4 evaluating GPT-4) produces inflated faithfulness scores (Zheng et al., 2023 / MT-Bench).
2. **Hardware Constraints:** All local models must fit cleanly within a local 4,096 MiB VRAM footprint (NVIDIA GeForce RTX 3050) without memory overflow or reliance on expensive third-party translation APIs.
3. **Reproducibility & Determinism:** LLM evaluation at scale (~13,500 claim checks under PPI) requires zero prompt drift, strict schema adherence, and rate-limit mitigation.

---

## Decision

### 1. Architectural Decoupling: Generator vs. Judge
- **Generator Model:** `meta-llama/Meta-Llama-3-8B-Instruct` (Meta AI).
  - Open-weights, canonical 8B RAG baseline widely cited in empirical literature.
  - Generates multi-sentence English answers conditioned on retrieved Nepali context.
- **LLM Judge Model (Arm 5):** `gemini-3.6-flash` (Google DeepMind).
  - Frontier-grade cross-lingual reasoning and superior Devanagari token representation.
  - **Decoupling Guarantee:** Meta generator is strictly decoupled from the Google DeepMind evaluator, eliminating intra-family self-preference bias.

### 2. Machine Translation Engine (Condition C2)
- **Model:** `ai4bharat/indictrans2-indic-en-dist-200M` (AI4Bharat / IIT Madras).
- **Language Code:** `npi_Deva` $\to$ `eng_Latn`.
- **Hardware Profile:** Distilled 200M parameter model uses ~400 MB storage in FP16 and peak runtime VRAM of ~850 MB to 1.1 GB. Runs 100% offline on the local RTX 3050 (4GB) GPU.
- **Scientific Role:** Decoupled from human post-edited $C3$ to isolate $\Delta_{MT} = A(C3) - A(C2)$.

### 3. The 5 Evaluator Arms Suite
1. **Arm 1 (Specialized Hallucination Scorer):** `vectara/hallucination_evaluation_model` (HHEM-2.1-Open, ~500MB VRAM).
2. **Arm 2 (Dense Semantic Similarity Baseline):** `BAAI/bge-m3` (~1.1GB VRAM, cosine similarity).
3. **Arm 3 (Matched Cross-Lingual NLI Instrument):** `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7` (~560MB VRAM). Evaluated identically across $C1, C2, C3$ to hold evaluator capacity constant.
4. **Arm 4 (Translate-then-NLI Pipeline):** `indictrans2-dist-200M` $\to$ `cross-encoder/nli-deberta-v3-large` (~1.7GB VRAM). Tests real-world MT error propagation into high-capacity English NLI.
5. **Arm 5 (Frontier LLM-as-a-Judge):** `gemini-3.6-flash` at `temperature: 0.0`, `seed: 42`.

### 4. Rate-Limit Mitigation & Determinism Protocol
- **10-Key Rotation Pool:** The client in `src/run/gemini_client.py` uses round-robin dispatch across 10 API keys configured in `.env`, with automatic exponential backoff on HTTP 429 (`RESOURCE_EXHAUSTED`).
- **Deterministic Disk Caching:** Every unique request payload is hashed (`SHA-256(model_id + prompt + config)`) and cached in `cache/llm_raw/`. Repeated runs cost 0 tokens and execute in < 0.05 seconds.
- **Physical Label Isolation:** Model pre-annotations write strictly to `data/interim/preannotations/`. Gold labels live in `data/raw/labels/` where agents have zero write permissions.

---

## Consequences & Paper Section Mapping

- **Paper Section 3 (Methodology):** Cites model family decoupling, the 5 arms, and hardware-reproducible local translation.
- **Paper Section 4 (Statistical Framework):** Connects the 10-key high-throughput capability to the ~13,500 claim evaluations required by PPI++ without rate-limit stalls.
