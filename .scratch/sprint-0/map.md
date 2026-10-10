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
  - Agent gathers research evidence for 01–04; the novelty verdict (Fork choice) is strictly a human decision.
  - Priority: Tickets 01 (MultiWikiQHalluA) and 02 (MT-vs-alignment decomposition) are go/no-go gates.
  - Hard cap of 2 days total across 01–04.
  - Ticket 05 (Rubric v1 & Timed Pilot) runs on an independent parallel track on the critical path.
  - Pre-registration is written by hand; no ticket is created for it.

## Decisions so far
- [MultiWikiQHalluA 215-Language Release Nepali Coverage Check](issues/01-multiwikiqhallua-nepali-check.md): MultiWikiQHalluA has zero benchmark overlap (monolingual extractive QA token tagging, not cross-lingual RAG faithfulness) and poor item utility (short extractive answers, no typed edits). Recommendation for Gate 0: differentiate deliberately with our own 3-domain corpus.
- [Hunt for Prior MT-vs-Alignment Decomposition of Faithfulness Evaluators](issues/02-mt-vs-alignment-decomposition-prior-art.md): Novelty check confirmed Fork A (Clear Novelty) — no prior work decomposes MT error ($\Delta_{MT}$) vs cross-lingual evaluator alignment ($\Delta_{XL}$) using a human post-edited MT ceiling ($C3$). Fork C (Scooped) is 100% ruled out.
- [Flagged Papers Read and Note: mFACT, ANHALTEN, and Kannada Cross-Lingual RAG](issues/03-flagged-papers-read-and-note.md): mFACT (summarization, excludes Nepali, no MT/alignment split), ANHALTEN (German reference-free token tagging), and Kannada RAG (retrieval-only, no faithfulness eval) leave NepFaith-120's causal decomposition and Nepali Devanagari RAG benchmark completely unaddressed.
- [Evaluate PPI-Efficiency Literature Angle](issues/04-ppi-efficiency-literature-evaluation.md): Demote PPI efficiency to supporting methodology (claimed by Gao et al. 2026 & StratPPI); keep error decomposition primary, and use cluster-robust stratified paired PPI for nested claims.

## Not yet specified

- **Fork B/C contingency specifications**: If novelty search surfaces direct decomposition prior art, re-framing the paper around claim-type stratification and Nepali exclusion from XNLI/IndicXNLI (Fork B) or resource/analysis benchmark (Fork C).
- **Synthetic perturbation generation prompt designs**: Detailed prompt engineering for the 7 typed edits (graduates once Schema v1 and Rubric v1 are frozen).
- **GLIDE estimator selection specifics**: Choosing clustered/stratified estimators based on pilot variance and claim nesting (graduates during Sprint 1 wiring).

## Out of scope

- **Pipeline code execution and batch translation**: Belongs strictly to Sprint 1 (Days 4–14).
- **Bulk human annotation and post-editing**: Belongs strictly to Sprint 2 (Days 15–28).
- **Writing paper Results / Discussion**: Belongs strictly to Sprint 3 (Days 29–35).
