# Reading Docket · 2026-10-10 · Sprint 0 Foundations

> **Researcher:** Human Lead  
> **Status:** Pending Researcher Answers  
> **Protocol Rule:** When resuming or starting a session, the AI agent must read this file first. If any answer is missing or incomplete, the agent MUST immediately stop, proceed no further with pipeline coding, and actively guide the researcher on the missing concepts.

---

## Instructions
1. Read the papers and targeted sections below.
2. Type your answers directly into the `### Your Answer:` sections under each question.
3. Save the file.
4. When you notify the agent or start the next turn, the agent will verify your answers before any downstream work proceeds.

---

## Module 1: Prediction-Powered Inference (PPI) — Statistical Engine

### Primary Sources
- **Angelopoulos et al. (Science 2023)**: *"Prediction-Powered Inference"* ([arXiv:2301.09652](https://arxiv.org/abs/2301.09652)) — Focus on Section 1 & 2 (the core intuition and mathematical formulation).
- **Gao, Sicilia, & Shi (arXiv:2608.26638 / EMNLP 2026)**: *"Which Metrics Save the Most Human Annotation?"* — Focus on the introduction, the definition of PPSR, and Section 3 on paired evaluations.

### Questions

#### Q1.1: The Core Mechanism of PPI
*Why is an unlabelled dataset with proxy predictions able to shrink error bars on a small human-labelled set without introducing model bias? How does the debiasing/imputation term work mathematically and conceptually?*

### Your Answer:
<!-- Enter your answer below this line -->


---

#### Q1.2: Fallback Under Poor Proxy Performance
*What happens to the confidence interval if the proxy evaluator has near-zero or negative correlation with human ground truth? How does PPI++ (adaptive tuning parameter $\lambda^*$) protect against variance inflation?*

### Your Answer:
<!-- Enter your answer below this line -->


---

#### Q1.3: Paired vs. Unpaired Evaluation
*Why does our experimental design evaluate the exact same item across all three conditions ($C1$ cross-lingual, $C2$ raw MT, and $C3$ post-edited MT)? How does this paired structure exploit covariance cancellation when estimating $\Delta_{XL} - \Delta_{MT}$?*

### Your Answer:
<!-- Enter your answer below this line -->


---

## Module 2: Claim-Level Faithfulness in RAG — Primary Evaluation Unit

### Primary Sources
- **Es et al. (EACL 2024)**: *"RAGAS: Automated Evaluation of Retrieval Augmented Generation"* ([arXiv:2309.15217](https://arxiv.org/abs/2309.15217)) — Focus on the **Faithfulness** section and claim extraction prompts.

### Questions

#### Q2.1: Atomic Claim Decomposition
*How does RAGAS break down a generated answer into individual atomic claims? What constitutes a valid atomic claim, and why do we evaluate at the claim level rather than assigning a single scalar score to the entire answer?*

### Your Answer:
<!-- Enter your answer below this line -->


---

#### Q2.2: Entailment vs. Lexical Matching
*Why is faithfulness evaluation framed as an entailment / NLI problem rather than lexical or n-gram matching (like BLEU or ROUGE)? What specific failure occurs if you attempt cross-lingual lexical matching between Nepali and English?*

### Your Answer:
<!-- Enter your answer below this line -->


---

#### Q2.3: Label Distinction: Contradicted vs. Not-in-Context
*In our rubric (`GLOSSARY.md`), why must `Contradicted` be strictly distinguished from `Not-in-context`? Give a concrete example showing how an LLM confabulation differs from an active factual contradiction.*

### Your Answer:
<!-- Enter your answer below this line -->


---

## Module 3: Machine Translation & Indic Language Behavior

### Primary Sources
- **Gala et al. (AI4Bharat, 2023)**: *"IndicTrans2: Towards High-Quality and Accessible Machine Translation Models for all 22 Scheduled Indian Languages"* ([arXiv:2305.16438](https://arxiv.org/abs/2305.16438)) — Review Nepali (`npi_Deva`) translation performance and distilled variants.
- **Agrawal, Fazili, & Jyothi (EACL 2024)**: *"Translation Errors Significantly Impact Low-Resource Languages in Cross-Lingual Learning"* ([arXiv:2402.02080](https://arxiv.org/abs/2402.02080)).

### Questions

#### Q3.1: Translation Noise in Indic NLP
*What types of translation errors are most prevalent when translating low-resource Indic languages like Nepali to English (e.g. named entities, numbers, honorifics, complex predicates), and how do they corrupt downstream semantic evaluation?*

### Your Answer:
<!-- Enter your answer below this line -->


---

#### Q3.2: Rationale for Condition C3
*Why is Condition $C3$ strictly defined as human post-edited machine translation ($PE(MT)$) rather than a translation generated from scratch by a human translator? Why is this distinction crucial for isolating $\Delta_{MT} = A(C3) - A(C2)$?*

### Your Answer:
<!-- Enter your answer below this line -->

