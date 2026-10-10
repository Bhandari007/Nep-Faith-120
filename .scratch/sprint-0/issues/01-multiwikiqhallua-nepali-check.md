# MultiWikiQHalluA 215-Language Release Nepali Coverage Check

Type: research
Status: resolved
Priority: go/no-go

## Question

Does MultiWikiQHalluA's synthetic hallucination dataset release across 215 languages include Nepali (`ne` / `npi_Deva`)?

If yes:
1. What is the format, license, passage source, and perturbation distribution for Nepali items in MultiWikiQHalluA?
2. Does it overlap with our proposed resource contribution, or can we utilize it as an item source to save data construction time while differentiating on claim-level typed errors and cross-lingual RAG evaluation?
3. What is the recommendation for Gate 0?

## Answer

1. **Nepali Coverage & Dataset Profile**:
   - While the base MultiWikiQA covered 306 languages (including Nepali), MultiWikiQHalluA truncated rollout to 215 languages due to compute limits. The authors did not evaluate Nepali or train classifiers on it (only 30 European languages received trained models).
   - *Format:* Monolingual $(context, question, answer)$ triples from Wikipedia (CC BY 4.0).
   - *Perturbations:* Generated via LettuceDetect's `HallucinationGenerator` with an instruction-tuned LLM and a continuous Beta-distributed error intensity ($\mu \approx 0.2$). No discrete typed edits.
2. **Overlap with NepFaith-120**:
   - **Zero Benchmark Overlap:** MultiWikiQHalluA is a monolingual token-classification reading comprehension benchmark. It does not evaluate cross-lingual entailment, machine translation degradation ($\Delta_{MT}$ vs $\Delta_{XL}$ across $C1/C2/C3$), or RAG claim-level faithfulness.
   - **Poor Item Source Utility:** Monolingual Nepali answers (short 1–4 word extractive spans) rather than multi-sentence English RAG answers; lacks propositional claim segmentation and NepFaith-120's 7 typed perturbation categories.
3. **Gate 0 Recommendation**:
   - **Differentiate deliberately**: Do not ingest MultiWikiQHalluA as an item source. Construct our planned ~1,500 passages across the three planned domains (Wikipedia, Government reports, News) with our 7 typed edits and cross-lingual query/answer pairs.

