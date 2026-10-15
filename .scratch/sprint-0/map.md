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
- 2026-10-15 · [T06 · Licensing Audit](issues/06-source-domain-licensing-audit.md): Audited Nepali Wikipedia (CC BY-SA 4.0), Gov Reports (Nepal Copyright Act Sec 4/16 public domain/research exception), and News snippets. Recommend hybrid direct release with passage metadata and URL attribution.
- 2026-10-15 · [T07 · Pin Models & Env](issues/07-pin-models-and-environment.md): Pinned generator (`Meta-Llama-3-8B-Instruct`), MT (`indictrans2-dist-200M`), evaluator arms (`HHEM-2.1-Open`, `bge-m3`, `mDeBERTa-v3-base-xnli`, `indictrans2->deberta-large`, `gemini-2.5-flash` with 10-key rotation at T=0.0) in `config/models.json` and locked `requirements.txt`. VRAM verified for 4GB RTX 3050.
- 2026-10-15 · [T05 · Rubric v1 & Pilot](issues/05-rubric-v1-and-timed-annotation-pilot.md): Codified Rubric v1 (`docs/RUBRIC_V1.md`) with 3-way labels, 7 perturbation types, and critical override. Assembled 8 pilot items with 23 pre-segmented claims in `tests/fixtures/pilot_8_items.json` and timing sheet `docs/PILOT_ANNOTATION_SHEET.md`.
- 2026-10-15 · [T08 · Freeze Schema v1](issues/08-freeze-schema-v1.md): Completed consumer justification audit for all fields. Implemented Pydantic models in `src/prepare/schema.py` and exported machine-readable `config/schema_v1.json`. Validated cleanly across all 8 pilot items.

## Verdicts (researcher)

<!-- A verdict line requires researcher initials and date. A ticket cannot close with an empty verdict. -->
2026-10-15 · Fork A (Clear Novelty) selected. Findings 01–04 confirmed; no prior work isolates MT vs cross-lingual evaluator failure via human post-editing. —
  MB

## Not yet specified

- **Fork B/C contingency specifications**: If novelty search surfaces direct decomposition prior art, re-framing the paper around claim-type stratification and Nepali exclusion from XNLI/IndicXNLI (Fork B) or resource/analysis benchmark (Fork C).
- **Synthetic perturbation generation prompt designs**: Detailed prompt engineering for the 7 typed edits (graduates once Schema v1 and Rubric v1 are frozen).
- **GLIDE estimator selection specifics**: Choosing clustered/stratified estimators based on pilot variance and claim nesting (graduates during Sprint 1 wiring).

## Out of scope

- **Pipeline code execution and batch translation**: Belongs strictly to Sprint 1 (Days 4–14).
- **Bulk human annotation and post-editing**: Belongs strictly to Sprint 2 (Days 15–28).
- **Writing paper Results / Discussion**: Belongs strictly to Sprint 3 (Days 29–35).
