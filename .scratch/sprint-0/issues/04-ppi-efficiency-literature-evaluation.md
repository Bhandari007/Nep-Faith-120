# Evaluate PPI-Efficiency Literature Angle

Type: research
Status: resolved
Priority: read-and-note

## Question

Read and evaluate the two recently flagged PPI papers:
1. "Which Metrics Save the Most Human Annotation?" (arXiv 2608.26638)
2. StratPPI's Seahorse section (multilingual summarization evaluation).

Determine:
1. What did these papers already establish regarding annotation efficiency and sample size reduction with PPI?
2. How should NepFaith-120 demote the PPI efficiency claim to a supporting methodology rather than primary novelty?
3. How does GLIDE support clustered and stratified estimators for nested claims in items?

## Answer

1. **Prior Art Findings**:
   - **Gao, Sicilia, & Shi (arXiv:2608.26638 / EMNLP 2026)** formalized the Prediction-Powered Saving Ratio (PPSR), showing neural metrics save 50%–80% of human annotation on WMT benchmarks via variance-reduction control variates in paired testing.
   - **Fisch et al. (StratPPI, NeurIPS 2024)** demonstrated on multilingual Seahorse (attribution evaluation) that stratifying by autorater confidence/slice achieves a 2x sample efficiency gain (300 human ratings yielding CIs equivalent to 600 classical human ratings).
2. **NepFaith-120 Positioning**:
   - **Demote PPI efficiency to supporting methodology**: Do not claim PPI cost savings as primary novelty (already established in prior art).
   - **Keep error decomposition primary**: The core scientific contribution is the causal decomposition between MT error ($\Delta_{MT}$) and cross-lingual scoring error ($\Delta_{XL}$) on Nepali → English RAG, alongside claim-type survival (H2).
   - Frame PPI (via GLIDE) strictly as the statistical inference engine ensuring valid finite-sample/asymptotic coverage when scaling from 120–150 gold items to 1,500 corpus items.
3. **Clustering & Stratification Strategy**:
   - Claims nested in an item violate i.i.d. assumptions ($\rho_{\text{ICC}} > 0$). Standard errors must cluster at `item_id`.
   - Combine StratPPI (stratified by domain, provenance, claim type) with Cluster-Robust PPI.
   - Exploit paired covariance cancellation across counterfactual conditions ($C1, C2, C3$) to achieve tight CIs on $\Delta_{XL} - \Delta_{MT}$ at $n=120\text{--}150$.

