# Wayfinder Map: Sprint 0 Foundations (Gate 0)

## Destination

Clear **Gate 0** of NepFaith-120: Foundations locked and verified so the pipeline build (Sprint 1) can proceed safely.
Exit criteria:
1. Novelty verdict recorded with chosen fork (Fork A Clear / Fork B Partial / Fork C Scooped) based on findings from 01–04 (human decision).
2. Pre-registration committed and timestamped (written by hand by humans).
3. Annotation time measured (minutes per item and per claim via 8-item pilot).
4. Schema v1 frozen with every field justified by an analysis that consumes it.

## Notes

- **Domain**: Cross-lingual faithfulness evaluation in Nepali → English RAG; error decomposition between Machine Translation ($\Delta_{MT}$) and cross-lingual alignment/scoring ($\Delta_{XL}$).
- **Key Skills**: `/grilling`, `/domain-modeling`, `/research`.
- **Standing Preferences & Constraints**:
  - **Reading Boundary**: The agent does NOT read/summarize papers autonomously. The agent prepares structured reading assignments, questions, and paper dockets for the human researcher. The researcher reads the literature to develop deep scientific domain expertise.
  - **Agent Role**: Organizing, coding, pipeline engineering, statistical modeling, data schemas, and environment tracking.
  - Pre-registration is written by hand; no ticket is created for it.

## Findings (agent)

- 2026-10-10 · [T01 · MultiWikiQHalluA Coverage](issues/01-multiwikiqhallua-nepali-check.md): MultiWikiQHalluA truncated to 215 languages; Nepali was never evaluated or trained on (30 European languages only). Monolingual extractive QA format with continuous Beta LLM perturbations. No direct overlap with cross-lingual RAG faithfulness or typed edits.
- 2026-10-10 · [T02 · MT-vs-Alignment Prior Art](issues/02-mt-vs-alignment-decomposition-prior-art.md): Searched arXiv, ACL Anthology, EMNLP, ICLR, and MT evaluation literature for decomposition of MT error vs cross-lingual evaluator alignment using human post-edited MT ($C3$). Found zero prior work. Closest hits: symmetric Translate-Test vs Zero-Shot XNLI without post-edited oracle (Conneau 2018, Agrawal 2024); multilingual summarization transfer without decomposition (Qiu 2023). Fork C (Scooped) has no evidence.
- 2026-10-10 · [T03 · Flagged Papers Analysis](issues/03-flagged-papers-read-and-note.md): mFACT (summarization, excludes Nepali, no MT/alignment split), ANHALTEN (German reference-free token tagging), and Kannada RAG (retrieval-only, no faithfulness eval). None address causal decomposition in Nepali Devanagari RAG.
- 2026-10-10 · [T04 · PPI Efficiency Literature](issues/04-ppi-efficiency-literature-evaluation.md): Gao et al. (EMNLP 2026 / arXiv:2608.26638) and StratPPI (NeurIPS 2024) already established that PPI saves 50%–80% human annotation. Claims nested in items violate i.i.d. ($\rho_{\text{ICC}} > 0$). Evidence indicates using cluster-robust stratified paired PPI and keeping error decomposition primary.

## Verdicts (researcher)

<!-- A verdict line requires researcher initials and date. A ticket cannot close with an empty verdict. -->

## Not yet specified

- **Fork B/C contingency specifications**: If novelty search surfaces direct decomposition prior art, re-framing the paper around claim-type stratification and Nepali exclusion from XNLI/IndicXNLI (Fork B) or resource/analysis benchmark (Fork C).
- **Synthetic perturbation generation prompt designs**: Detailed prompt engineering for the 7 typed edits (graduates once Schema v1 and Rubric v1 are frozen).
- **GLIDE estimator selection specifics**: Choosing clustered/stratified estimators based on pilot variance and claim nesting (graduates during Sprint 1 wiring).

## Out of scope

- **Pipeline code execution and batch translation**: Belongs strictly to Sprint 1 (Days 4–14).
- **Bulk human annotation and post-editing**: Belongs strictly to Sprint 2 (Days 15–28).
- **Writing paper Results / Discussion**: Belongs strictly to Sprint 3 (Days 29–35).
