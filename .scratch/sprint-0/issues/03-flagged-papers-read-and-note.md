# Flagged Papers Read and Note: mFACT, ANHALTEN, and Kannada Cross-Lingual RAG

Type: research
Status: awaiting-verdict
Priority: read-and-note
Cap: 2 days (shared across 01–04)

## Question

Review the three flagged adjacent papers:
1. **mFACT** (Qiu et al.): Multilingual Faithfulness Evaluation. What languages does it cover? How does it define cross-lingual alignment? What does it leave open regarding Devanagari / Indic / low-resource languages?
2. **ANHALTEN**: What does it claim regarding hallucination evaluation in cross-lingual settings?
3. **Kannada cross-lingual RAG paper**: How does it evaluate Kannada $\to$ English RAG? Does it evaluate faithfulness or answer relevancy? Does it isolate MT error from scorer error?

For each: summarize what it claims, what it leaves open, and how NepFaith-120 differentiates from it.

## Evidence (agent)

1. **mFACT (Qiu et al., EMNLP 2023)**:
   - *Claims:* Evaluates multilingual summarization faithfulness by transferring English metrics via translation-based transfer across ~30 languages.
   - *Gaps:* Completely excludes Nepali (`ne` / `npi_Deva`). Document-level continuous score rather than claim-level decomposition. Treats MT as a black-box transfer mechanism and does not decompose MT error ($\Delta_{MT}$) vs cross-lingual alignment error ($\Delta_{XL}$).
2. **ANHALTEN (Herrlein et al., ACL 2024 SRW)**:
   - *Claims:* Token-level reference-free hallucination detection transferred cross-lingually via few-shot adapters.
   - *Gaps:* Strictly English $\leftrightarrow$ German (high-resource Latin script). Evaluates intrinsic/parametric world-knowledge factuality (reference-free), not grounded RAG faithfulness against external retrieved passages. No MT vs alignment separation.
3. **Kannada Cross-Lingual RAG (Sandesh et al., 2026 / CrossLinguaRAG)**:
   - *Claims:* End-to-end prototype retrieving Kannada evidence using multilingual embeddings and translating for English answer generation.
   - *Gaps:* Purely retrieval-centric (Recall@K, MRR). Does not evaluate faithfulness, hallucination, or cross-lingual entailment. Conflates MT errors with retrieval and generation errors without isolation.

## Verdict (researcher)

<!-- Researcher writes verdict here with initials and date to close this ticket. Example:
- 2026-10-10 · Verified distinction against mFACT, ANHALTEN, and Kannada RAG. — [Initials]
-->


