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

<!-- Closed tickets will be indexed here as they resolve -->

## Not yet specified

- **Fork B/C contingency specifications**: If novelty search surfaces direct decomposition prior art, re-framing the paper around claim-type stratification and Nepali exclusion from XNLI/IndicXNLI (Fork B) or resource/analysis benchmark (Fork C).
- **Synthetic perturbation generation prompt designs**: Detailed prompt engineering for the 7 typed edits (graduates once Schema v1 and Rubric v1 are frozen).
- **GLIDE estimator selection specifics**: Choosing clustered/stratified estimators based on pilot variance and claim nesting (graduates during Sprint 1 wiring).

## Out of scope

- **Pipeline code execution and batch translation**: Belongs strictly to Sprint 1 (Days 4–14).
- **Bulk human annotation and post-editing**: Belongs strictly to Sprint 2 (Days 15–28).
- **Writing paper Results / Discussion**: Belongs strictly to Sprint 3 (Days 29–35).
