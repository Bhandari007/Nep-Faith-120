# Pin Models and Environment

Type: task
Status: open

## Question

Specify and freeze exact model checkpoints, inference parameters, and environment dependencies:
1. **Generator Model**: Must be open-weights (e.g. Llama 3 / Mistral family) and strictly from a different model family than any evaluated judge model.
2. **Judge Models**: Pinned model checkpoints, evaluated with temperature 0.0.
3. **Translation Model**: Pinned IndicTrans2 checkpoint (distilled variant fitting VRAM budget, e.g. `ai4bharat/indictrans2-indic-en-dist-200M`).
4. **NLI Evaluator**: `mDeBERTa-v3-base-xnli-multilingual-nli-2mil7` or similar pinned checkpoint.
5. **Vectara HHEM**: Pinned version of `vectara/hallucination_evaluation_model` (HHEM-2.1-Open).
6. **Environment**: Python environment locked with pinned dependency versions (transformers, torch, vllm/ollama, ragas, glide-inference).
