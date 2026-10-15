# Pin Models and Environment

Type: task
Status: awaiting-verdict
Cap: 0.5 day (pinned checkpoints & lockfile)

## Question

Specify and freeze exact model checkpoints, inference parameters, and environment dependencies:
1. **Generator Model**: Must be open-weights (e.g. Llama 3 / Mistral family) and strictly from a different model family than any evaluated judge model.
2. **Judge Models**: Pinned model checkpoints, evaluated with temperature 0.0.
3. **Translation Model**: Pinned IndicTrans2 checkpoint (distilled variant fitting VRAM budget, e.g. `ai4bharat/indictrans2-indic-en-dist-200M`).
4. **NLI Evaluator**: `mDeBERTa-v3-base-xnli-multilingual-nli-2mil7` or similar pinned checkpoint.
5. **Vectara HHEM**: Pinned version of `vectara/hallucination_evaluation_model` (HHEM-2.1-Open).
6. **Environment**: Python environment locked with pinned dependency versions (transformers, torch, vllm/ollama, ragas, glide-inference).

## Evidence (agent)

1. **Hardware Constraints Profiling**:
   - Host environment: NVIDIA GeForce RTX 3050 Laptop GPU (4,096 MiB VRAM).
   - Local discriminative models (`indictrans2-dist-200M` ~800MB, `mDeBERTa-v3-base` ~560MB, `HHEM-2.1` ~500MB, `bge-m3` ~1.1GB) fit comfortably within the 4GB VRAM footprint in `float16`.
   - Generator (8B) and LLM Judge are configured for quantized local inference or API endpoints with strict prompt-hash deterministic caching.

2. **Model Family Independence Guarantee**:
   - **Generator**: `meta-llama/Meta-Llama-3-8B-Instruct` (Llama family).
   - **LLM Judge**: `gemini-1.5-flash-002` (Gemini family, Google DeepMind) / `Qwen/Qwen2.5-7B-Instruct` (Qwen family).
   - **Independence rule verified:** The evaluator model family does not overlap with the generator model family, eliminating circular self-preference bias.

3. **Pinned Checkpoints & Parameters (Recorded in `config/models.json`)**:
   - **Translation**: `ai4bharat/indictrans2-indic-en-dist-200M` (`src: npi_Deva`, `tgt: eng_Latn`).
   - **Arm 1 (HHEM)**: `vectara/hallucination_evaluation_model` (HHEM-2.1-Open).
   - **Arm 2 (Dense Similarity)**: `BAAI/bge-m3` (cosine similarity).
   - **Arm 3 (Cross-Lingual NLI)**: `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`.
   - **Arm 4 (Pipeline MT -> NLI)**: `indictrans2-dist-200M` $\to$ `cross-encoder/nli-deberta-v3-large`.
   - **Arm 5 (LLM Judge)**: `gemini-2.5-flash` at `temperature: 0.0`, `seed: 42`, utilizing round-robin key rotation across user-supplied API keys with exponential backoff on 429.
   - **Deterministic Seed**: Global pipeline seed pinned to `42`.

4. **Environment Lockfile**:
   - Pinned dependencies committed in `requirements.txt` covering PyTorch, HuggingFace Transformers, SentencePiece, Ragas, and GLIDE statistical inference libraries.

## Verdict (researcher)

<!-- Researcher writes verdict with initials and date to close this ticket. Example:
- 2026-10-15 · Approved model selections and pinned configuration in config/models.json. — [Initials]
-->

