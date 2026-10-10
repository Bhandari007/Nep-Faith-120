# Hunt for Prior MT-vs-Alignment Decomposition of Faithfulness Evaluators

Type: research
Status: awaiting-verdict
Priority: go/no-go (contribution-killer check)
Cap: 2 days (shared across 01–04)

## Question

Has prior literature decomposed translation error vs cross-lingual evaluator alignment error for cross-lingual faithfulness / hallucination scoring (specifically comparing $A(C3) - A(C2)$ vs $A(C3) - A(C1)$)?

Investigate:
1. Faithfulness and hallucination literature in multilingual/cross-lingual RAG and QA (e.g. arXiv, ACL, EMNLP, NAACL, ICLR).
2. Machine translation evaluation literature where source-induced vs translation-induced error decomposition is standard practice.
3. Does any work measure this directly on low-resource / Indic languages?
4. What is the novelty evidence for the researcher?

## Evidence (agent)

1. **Prior Art Decomposition Check**: No prior work decomposes cross-lingual faithfulness scoring into machine translation error vs cross-lingual evaluator alignment error using a human post-edited MT ceiling ($C3$).
   - Standard RAG eval frameworks (RAGAS, TruLens, HHEM) evaluate either monolingually or via black-box prompt translation without isolating MT vs cross-lingual scoring error.
   - Classic XNLI / Translate-Test literature (Conneau et al. 2018; Artetxe et al. 2020; Agrawal et al. 2024) analyzes *symmetric* classification tasks and directly compares $A(\text{Translate-Test}) - A(\text{Zero-Shot})$ without a human post-edited MT oracle ($C3$), thus conflating MT noise with model reasoning failure.
   - MT evaluation literature (MQM, WMT) separates source vs translation errors to judge the MT engine itself, not downstream asymmetric claim verification.
2. **Indic / Low-Resource Scope**:
   - Indic hallucination benchmarks (e.g. BHRAM-IL 2025) measure generative hallucinations in QA, not faithfulness evaluator reliability.
   - Indic translation studies (Agrawal et al., EACL 2024) identify translation errors *in benchmark data*, not faithfulness scoring pipelines.
   - Zero existing benchmarks evaluate cross-lingual RAG faithfulness for Nepali $\to$ English.
3. **No Direct Scoop**: Search across arXiv and ACL Anthology found no paper conducting this decomposition.

## Verdict (researcher)

<!-- Researcher writes verdict here with initials and date to close this ticket. Example:
- 2026-10-10 · Fork A chosen. Verified no direct prior art; proceeding with decomposition as Contribution #1. — [Initials]
-->


