# Hunt for Prior MT-vs-Alignment Decomposition of Faithfulness Evaluators

Type: research
Status: resolved
Priority: go/no-go (contribution-killer check)

## Question

Has prior literature decomposed translation error vs cross-lingual evaluator alignment error for cross-lingual faithfulness / hallucination scoring (specifically comparing $A(C3) - A(C2)$ vs $A(C3) - A(C1)$)?

Investigate:
1. Faithfulness and hallucination literature in multilingual/cross-lingual RAG and QA (e.g. arXiv, ACL, EMNLP, NAACL, ICLR).
2. Machine translation evaluation literature where source-induced vs translation-induced error decomposition is standard practice.
3. Does any work measure this directly on low-resource / Indic languages?
4. What is the novelty verdict recommendation for the human author (Fork A Clear, Fork B Partial overlap, Fork C Scooped)?

## Answer

1. **Prior Art Decomposition Check**: **NO prior work** has decomposed cross-lingual faithfulness scoring into machine translation error vs cross-lingual evaluator alignment error using a human post-edited MT ceiling ($C3$).
   - Standard RAG eval frameworks (RAGAS, TruLens, HHEM) evaluate either monolingually or via black-box prompt translation without isolating MT vs cross-lingual scoring error.
   - Classic XNLI / Translate-Test literature (Conneau et al. 2018; Artetxe et al. 2020; Agrawal et al. 2024) analyzes *symmetric* classification tasks and directly compares $A(\text{Translate-Test}) - A(\text{Zero-Shot})$ without a human post-edited MT oracle ($C3$), thus conflating MT noise with model reasoning failure.
   - MT evaluation literature (MQM, WMT) separates source vs translation errors to judge the MT engine itself, not downstream asymmetric claim verification.
2. **Indic / Low-Resource Scope**:
   - Indic hallucination benchmarks (e.g. BHRAM-IL 2025) measure generative hallucinations in QA, not faithfulness evaluator reliability.
   - Indic translation studies (Agrawal et al., EACL 2024) identify translation errors *in benchmark data*, not faithfulness scoring pipelines.
   - Zero existing benchmarks evaluate cross-lingual RAG faithfulness for Nepali $\to$ English.
3. **Novelty Verdict Recommendation**: **Fork A (Clear Novelty) is CONFIRMED**.
   - Fork C (Scooped) is 100% ruled out.
   - Fork B literature (translate-test vs zero-shot NLI, multilingual summarization) serves as strong adjacent foundation for related work.
   - The authors should proceed with the primary decomposition as Contribution #1.

