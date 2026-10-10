# Evaluate PPI-Efficiency Literature Angle

Type: research
Status: awaiting-verdict
Priority: read-and-note
Cap: 2 days (shared across 01–04)

## Question

Read and evaluate the two recently flagged PPI papers:
1. "Which Metrics Save the Most Human Annotation?" (arXiv 2608.26638)
2. StratPPI's Seahorse section (multilingual summarization evaluation).

Determine:
1. What did these papers already establish regarding annotation efficiency and sample size reduction with PPI?
2. How should NepFaith-120 demote the PPI efficiency claim to a supporting methodology rather than primary novelty?
3. How does GLIDE support clustered and stratified estimators for nested claims in items?

## Evidence (agent)

1. **Prior Art Findings**:
   - **Gao, Sicilia, & Shi (arXiv:2608.26638 / EMNLP 2026)** formalized the Prediction-Powered Saving Ratio (PPSR), showing neural metrics save 50%–80% of human annotation on WMT benchmarks via variance-reduction control variates in paired testing.
   - **Fisch et al. (StratPPI, NeurIPS 2024)** demonstrated on multilingual Seahorse (attribution evaluation) that stratifying by autorater confidence/slice achieves a 2x sample efficiency gain (300 human ratings yielding CIs equivalent to 600 classical human ratings).
2. **Methodological Framing**:
   - Demoting PPI efficiency to supporting methodology is strongly supported by prior art.
   - Core scientific contribution remains causal error decomposition ($\Delta_{MT}$ vs $\Delta_{XL}$) and claim-type survival (H2).
3. **Clustering & Stratification**:
   - Claims nested in an item violate i.i.d. assumptions ($\rho_{\text{ICC}} > 0$). Standard errors must cluster at `item_id`.
   - Exploit paired covariance cancellation across counterfactual conditions ($C1, C2, C3$).

## Verdict (researcher)

<!-- Researcher writes verdict here with initials and date to close this ticket. Example:
- 2026-10-10 · Confirmed: demote PPI efficiency to supporting engine; cluster at item_id. — [Initials]
-->


