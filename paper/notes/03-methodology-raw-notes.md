# Paper Section: 3. Methodology & Dataset Construction

> **Status:** Seed Draft (Living Section)  
> **Target Venue:** ACL / EMNLP / NAACL

---

## 1. Experimental Conditions & Decomposition Framework
For every evaluation item $i$, we consider a retrieved Nepali context passage $c_{\text{ne}}$, a generated English answer $a_{\text{en}}$, and its segmented atomic claims $\{k_{ij}\}_{j=1}^{M_i}$. Each item is evaluated across three conditions:
- **$C1$ (Direct Cross-Lingual Evaluation):** The evaluator $E$ scores English claims against the original Nepali passage:
  $$\hat{Y}_{ij}^{(C1)} = E(c_{\text{ne}}, k_{ij})$$
- **$C2$ (Raw Machine Translation):** The passage is translated into English via IndicTrans2 ($MT(c_{\text{ne}})$) and evaluated monolingually:
  $$\hat{Y}_{ij}^{(C2)} = E(MT(c_{\text{ne}}), k_{ij})$$
- **$C3$ (Human Post-Edited MT Ceiling):** The MT output is post-edited by a human translator ($PE(MT(c_{\text{ne}}))$) to correct MT distortions and evaluated monolingually:
  $$\hat{Y}_{ij}^{(C3)} = E(PE(MT(c_{\text{ne}})), k_{ij})$$

### The Decomposition Metrics
Let $A(C)$ denote evaluator agreement (or F1/accuracy) relative to human consensus ground truth $Y_{ij}$ under condition $C$:
$$\Delta_{MT} = A(C3) - A(C2) \quad \text{(Cost of Machine Translation)}$$
$$\Delta_{XL} = A(C3) - A(C1) \quad \text{(Cost of Cross-Lingual Evaluation)}$$
$$\text{Hypothesis } H1: \Delta_{XL} > \Delta_{MT}$$

## 2. Claim-Level Annotation Unit & Rubric
- **Atomic Claim Unit:** Answers are decomposed into atomic, self-contained factual claims (mirroring RAGAS claim extraction).
- **Three-Way Grounded Labels:**
  1. `Supported`: Entailed directly by the reference passage.
  2. `Contradicted`: Factually conflicts with or contradicts the reference passage.
  3. `Not-in-context`: Information is not present in the reference passage, neither confirmed nor contradicted.
  *(Note: $\text{Contradicted} \ne \text{Not-in-context}$.)*
- **Derived Item Faithfulness:** An answer is faithful if and only if all constituent claims are supported.
- **Critical-Claim Override:** If any claim flagged as *critical* is contradicted or not-in-context, the entire item is deemed unfaithful.

## 3. The 7 Typed Perturbations (Guaranteeing Hard Negatives)
To avoid label imbalance where generated answers are overwhelmingly faithful, 50% of the corpus is generated through a deterministic perturbation engine applying one of 7 typed edits:
1. **Entity Swap:** Replacing named entities with in-domain distractors.
2. **Number / Date Alteration:** Modifying numerical quantities or calendar dates.
3. **Negation Flip:** Inserting or removing syntactic negation.
4. **Attribution Removal / Misattribution:** Shifting quoted statements or findings to wrong agents.
5. **Honorific / Register Shift:** Modifying Nepali honorific markers affecting politeness/social rank.
6. **Unsupported Addition:** Adding plausible external claims not grounded in context.
7. **Invented Causal Relation:** Creating false cause-and-effect links between true propositions.

## 4. Evaluator Arms (Frozen at Gate 0)
1. `HHEM-2.1-Open`: Vectara open-weights hallucination evaluation model.
2. `BGE-M3` / `LaBSE`: Multilingual dense embedding cosine similarity.
3. `mDeBERTa-v3-base-xnli`: Matched multilingual NLI encoder across C1, C2, and C3.
4. `IndicTrans2 → English NLI`: Machine translation pipeline into DeBERTa-v3-large-mnli.
5. `LLM-as-a-Judge`: Pinned open-weights/commercial LLMs at temperature 0.0 across C1, C2, and C3.
