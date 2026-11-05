# Paper Section: 5. Empirical Findings, Qualitative Insights & Limitations

> **Status:** Seed Draft (Living Section)  
> **Target Venue:** ACL / EMNLP / NAACL

---

## 1. Qualitative Annotator Observations & Post-Edit Error Log
- **Linguistic Quirks in Nepali $\to$ English MT:**
  - Named Entity Transliteration Drift: IndicTrans2 frequently transliterates local Nepali administrative wards, rivers, and historical figures with non-standard English phonetics, triggering false "Not-in-context" verdicts by downstream LLM judges.
  - Bikram Sambat (B.S.) Calendar vs. Gregorian (A.D.): Nepali official documents and news use Vikram Samvat dates (e.g., 2078 B.S.), which raw MT fails to convert to Gregorian years (2021/2022 A.D.), causing judges to flag valid temporal assertions as hallucinations.
  - Honorific Flattening: Nepali honorific pronominal systems (`हजुर`, `तपाईं`, `उहाँ`) and verb forms collapse into generic English "he/she/they", losing crucial social attribution nuance.

## 2. Honest Limitations
Following the pre-registration and ethical disclosure requirements:
1. **Translator-as-Annotator Bias:** The human post-editing of condition $C3$ is performed by bilingual expert annotators who understand the task objectives, representing a favorable ceiling rather than naive crowd post-editing.
2. **Evaluator Arm 5 Scope:** Due to free-tier API rate limits and daily project quotas, frontier LLM judge evaluation (`gemini-3.6-flash`) was executed exhaustively across the $n=120$ candidate gold benchmark across all conditions ($C1, C2, C3$), but not scaled across the entire $N=1,200$ unlabelled inference corpus.
3. **Pretraining Leakage:** Wikipedia items may have pretraining leakage into large language models; this threat is directly mitigated by including number-dense Government Reports and current News articles, and running the context-ablation probe.
4. **Evaluator Proxy Dependencies:** PPI guarantees valid coverage regardless of proxy quality, but low proxy–human correlation reduces efficiency to classical inference ($\text{PPSR} \to 1.0\times$).
