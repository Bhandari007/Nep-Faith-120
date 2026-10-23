# Section 3: Methodology & Experimental Framework

## 3.1 Counterfactual Decomposition Framework

To rigorously isolate machine translation degradation from cross-lingual evaluation bottlenecks in low-resource Retrieval-Augmented Generation (RAG), we introduce a three-condition paired counterfactual framework. 

Let each evaluation instance $i$ consist of an authentic retrieved Nepali context passage $p_{ne}^{(i)}$, a user query $q^{(i)}$, and an English generation $a_{en}^{(i)}$. Following claim-level factual verification standards, the generated response is decomposed into a set of $M_i$ atomic, self-contained factual propositions:
$$\mathcal{K}_i = \{k_{ij}\}_{j=1}^{M_i}$$
where each claim $k_{ij}$ is evaluated under three distinct context conditions:

1. **Condition $C1$ (Direct Cross-Lingual Evaluation):**  
   The automated evaluator scores English claims directly against the verbatim Nepali source context:
   $$\hat{Y}_{ij}^{(C1)} = E(p_{ne}^{(i)}, k_{ij})$$
2. **Condition $C2$ (Translate-then-Evaluate / Raw MT):**  
   The Nepali context is translated into English using an off-the-shelf state-of-the-art Indic neural translation model (`ai4bharat/indictrans2-indic-en-dist-200M`), and the claims are evaluated monolingually:
   $$\hat{Y}_{ij}^{(C2)} = E(\text{MT}(p_{ne}^{(i)}), k_{ij})$$
3. **Condition $C3$ (Minimal-Pair Human Post-Edited Ceiling):**  
   To eliminate translation errors without introducing stylistic confounds, bilingual human editors minimally post-edit the machine-translated context ($\text{PE}(\text{MT}(p_{ne}^{(i)}))$) to correct numeral, entity, aspectual, and negation errors while preserving MT sentence phrasing:
   $$\hat{Y}_{ij}^{(C3)} = E(\text{PE}(\text{MT}(p_{ne}^{(i)})), k_{ij})$$

### The Decomposition Metrics
Let $A(C)$ represent the accuracy (or macro-F1) of an automated evaluator arm against adjudicated human consensus ground truth $Y_{ij}$ under context condition $C$. We formally decompose the overall evaluation gap into two orthogonal failure modes:
$$\Delta_{\text{MT}} = A(C3) - A(C2) \quad \text{(Penalty Attributable Strictly to MT Errors)}$$
$$\Delta_{\text{XL}} = A(C3) - A(C1) \quad \text{(Penalty Attributable Strictly to Cross-Lingual Reasoning)}$$

Our primary research hypothesis posits that across modern evaluator architectures, the cross-lingual semantic judgment bottleneck strictly dominates the machine translation error penalty:
$$H_1: \Delta_{\text{XL}} > \Delta_{\text{MT}} \iff A(C2) - A(C1) > 0$$

Testing $H_1$ reduces to evaluating the paired difference $A(C2) - A(C1)$, where the human post-edited counterfactual $C3$ serves as the shared reference ceiling.

---

## 3.2 Corpus Stratification & Ingestion

To guard against domain-specific artifacts and ensure robust out-of-domain statistical validity, the evaluation corpus is stratified across three macro-domains:

1. **Nepali Wikipedia (`wikipedia`, 33.3%):**  
   Verifiable encyclopedic articles spanning cultural monuments, national parks, geographical features, and historical biographies licensed under CC BY-SA 4.0. Ingested via the official Wikimedia REST API with introductory lead extraction.
2. **Nepali Government & Public Records (`government_report`, 33.3%):**  
   High-density statistical and tabular texts with minimal representation in general pretraining corpora. Sourced from the National Statistics Office (Census 2078), Ministry of Finance Economic Surveys, Nepal Rastra Bank Macroeconomic Reports, and Ministry of Health Annual Reports (public domain under Nepal Copyright Act 2002, Sec 4/16).
3. **Contemporary Nepali News & Sports (`news`, 33.3%):**  
   Sourced from national publishers (*OnlineKhabar*, *eKantipur*, *Setopati*, *Gorkhapatra*).  
   *Pre-registered Quota:* Exactly 30% of the news stratum is allocated to sports journalism (*HamroKhelkud*, Cricket Association of Nepal, All Nepal Football Association). Sports reporting provides dense entity tracking, chronological match scores, overs, run rates, and tournament statistics, presenting a rigorous test for fine-grained factual drift.

All passages undergo Unicode NFC canonical normalization and Devanagari character verification, filtering out corrupted legacy 8-bit glyph encodings (Preeti/Kantipur font conversions).

---

## 3.3 Balanced Provenance: The 7-Type Perturbation Engine

Standard RAG benchmarks suffer from severe label imbalance, as generated responses are predominantly factual, causing automated evaluators to achieve artificially inflated accuracy through default heuristic agreement. To guarantee an exact 50% / 50% balance between faithful and unfaithful items, half of the corpus instances are generated via a deterministic, typed perturbation engine covering seven distinct counterfactual failure categories:

1. **`entity_swap`:** Replaces named entities (people, locations, organizations) with in-domain authentic distractors.
2. **`number_date_alteration`:** Perturbs numerical values, percentages, and Bikram Sambat (B.S.) / Gregorian (A.D.) calendar dates.
3. **`negation_flip`:** Reverses syntactic polarity by inserting or stripping Nepali negation affixes (`छैन` / `होइन`).
4. **`misattribution`:** Attributes authentic statements or statistics to an incorrect governing agency or spokesperson.
5. **`register_shift`:** Modifies Nepali honorific markers (high-honorific `हजुर` / `हुनुहुन्छ` vs. non-honorific `हो` / `गर्छ`), altering social authority and grammatical plurality.
6. **`unsupported_addition`:** Injects plausible external facts that are ungrounded by the retrieved context.
7. **`invented_causality`:** Connects two factually correct independent propositions with an unverified causal connective (`किनभने`, `फलस्वरूप`).

---

## 3.4 Claim Decomposition & Grounded Annotation Rubric

Evaluating full-paragraph answers as atomic units conflates multiple factual dimensions and obscures fine-grained hallucinations. We adopt proposition-level evaluation following the `docs/RUBRIC_V1.md` protocol:

1. **Decontextualization:** Answers are segmented into 2 to 5 self-contained atomic propositions, resolving coreferences to preserve independent verifiability.
2. **Three-Way Grounded Claim Labels:**
   - **`Supported`:** The claim is fully entailed by the reference passage.
   - **`Contradicted`:** The claim directly contradicts information in the reference passage.
   - **`Not-in-context`:** The claim asserts information absent from the passage, neither confirmed nor refuted ($\text{Contradicted} \ne \text{Not-in-context}$).
3. **Derived Item Faithfulness ($Y_i$):** An answer item $i$ is designated faithful ($Y_i = 1$) if and only if all constituent claims are `Supported`. If any claim flagged as `is_critical` is labeled `Contradicted` or `Not-in-context`, the item is assigned unfaithful ($Y_i = 0$).

---

## 3.5 Frozen Automated Evaluator Arms

The automated evaluation suite comprises five frozen instruments:

- **Arm 1 (Specialized Hallucination Model):** `vectara/hallucination_evaluation_model` (HHEM-2.1-Open), producing calibrated factual consistency probabilities.
- **Arm 2 (Dense Semantic Similarity Baseline):** `BAAI/bge-m3`, computing cosine embedding similarity between premise passage and claim hypothesis.
- **Arm 3 (Cross-Lingual NLI Instrument):** `MoritzLaurer/mDeBERTa-v3-base-xnli-multilingual-nli-2mil7`, evaluating cross-lingual premise-hypothesis entailment directly across $C1$, $C2$, and $C3$.
- **Arm 4 (Pipeline MT $\to$ English NLI):** `ai4bharat/indictrans2-indic-en-dist-200M` followed by monolingual `cross-encoder/nli-deberta-v3-large`.
- **Arm 5 (Frontier LLM-as-a-Judge):** `gemini-2.5-flash` evaluated at `temperature: 0.0`, `seed: 42`, utilizing round-robin key rotation across 10 API keys and deterministic prompt-hash disk caching. The generation LLM (`Meta-Llama-3-8B-Instruct`) is strictly decoupled from the evaluator judge to prevent self-enhancement bias.
