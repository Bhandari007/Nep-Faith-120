# Paper Section: 5. Empirical Findings, Qualitative Insights & Limitations

> **Status:** Seed Draft (Living Section)  
> **Target Venue:** ACL / EMNLP / NAACL

---

## 1. Qualitative Annotator Observations & Post-Edit Error Log
*(This section continuously records the qualitative findings, edge cases, and linguistic nuances discovered by the researcher during annotation and pilot phases.)*

- **Linguistic Quirks in Nepali $\to$ English MT:** (To be populated during S2.8 post-editing).
- **Claim Segmentation Boundary Cases:** (To be populated during S0.10 / Ticket 05 pilot).
- **Critical Claim Disagreements:** (To be populated during consensus adjudication).

## 2. Honest Limitations
Following the pre-registration and ethical disclosure requirements:
1. **Translator-as-Annotator Bias:** The human post-editing of condition $C3$ is performed by the authors/annotators, representing a favorable ceiling rather than independent crowd translation.
2. **Subset Sample Size on $C3$:** Human post-editing is limited to 30–40 stratified items due to time budget; this is cross-checked using the MT-preservation flag across all 120 sampled items.
3. **Pretraining Leakage:** Wikipedia items may have pretraining leakage into large language models; this threat is directly mitigated by including number-dense Government Reports and current News articles, and running the context-ablation probe.
4. **Evaluator Proxy Dependencies:** PPI guarantees valid coverage, but low proxy–human correlation reduces efficiency to classical inference.
