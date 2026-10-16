# IndicTrans2 Local Translation Runner

Type: engineering
Status: Cleared - [MB, 2026-10-16]
Cap: 1 day (runner implementation, device detection, and caching)

## Question

Build `src/run/translate.py` to translate Nepali contexts ($p_{ne}$) into English ($p_{c2} = \text{MT}(p_{ne})$) for experimental Condition $C2$ using `ai4bharat/indictrans2-indic-en-dist-200M`:
1. Execute locally in FP16 on GPU (or CPU fallback) without external cloud costs.
2. Target language tag: `eng_Latn`, source language tag: `npi_Deva`.
3. Deterministic disk caching under `cache/translations/` keyed on `SHA-256(passage_ne + model_id)` to ensure zero recomputation.
4. Schema compliance: populate `c2_raw_mt` on evaluation items.
5. Invariant: Condition $C2$ contexts must never leak gold human post-edits or condition labels.

## Findings & Evidence (agent)

1. **Hardware & Environment Setup:**
   - PyTorch 2.14.1 with CUDA 13.0 and Hugging Face Transformers installed.
   - Verified GPU device: `NVIDIA GeForce RTX 3050 Ti Laptop GPU` (4GB VRAM).
2. **Runner Built (`src/run/translate.py`):**
   - Implemented `IndicTrans2Translator` supporting single and batch translation with language tags (`npi_Deva` -> `eng_Latn`).
   - Device auto-selection with FP16 precision on CUDA.
   - Deterministic disk cache under `cache/translations/` keyed on `SHA-256`.
3. **Unit Tests Passing:**
   - `tests/test_translate.py` (3/3 passed in 3.58s): Validated initialization, deterministic cache keys, and instant cached retrieval without model overhead.

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
MB, 16 October 2026

