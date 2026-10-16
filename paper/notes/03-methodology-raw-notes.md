# Paper Section: 3. Methodology & Dataset Construction

> **Status:** Seed Draft (Living Section)  
> **Target Venue:** ACL / EMNLP / NAACL

---

## 1. Experimental Conditions & Decomposition Framework
For every evaluation item $i$, we consider a retrieved Nepali context passage $c_{\text{ne}}$, a generated English answer $a_{\text{en}}$, and its segmented atomic claims $\{k_{ij}\}_{j=1}^{M_i}$. Each item is evaluated across three conditions:
- **$C1$ (Direct Cross-Lingual Evaluation):** The evaluator $E$ scores English claims against the original Nepali passage:
  $$\hat{Y}_{ij}^{(C1)} = E(c_{\text{ne}}, k_{ij})$$
- **$C2$ (Raw Machine Translation):** The passage is translated into English via IndicTrans2 ($MT(c_{\text{ne}})$) and evaluated monolingually:
  $$\hat{Y}_{ij}^{(C2)} = E(MT(c_{\text{ne}}), k_{ij})$$
- **$C3$ (Human Post-Edited MT Ceiling):** The MT output is post-edited by a human translator ($PE(MT(c_{\text{ne}}))$) to correct MT distortions and evaluated monolingually:
  $$\hat{Y}_{ij}^{(C3)} = E(PE(MT(c_{\text{ne}})), k_{ij})$$

### The Decomposition Metrics
Let $A(C)$ denote evaluator agreement (or F1/accuracy) relative to human consensus ground truth $Y_{ij}$ under condition $C$:
$$\Delta_{MT} = A(C3) - A(C2) \quad \text{(Cost of Machine Translation)}$$
$$\Delta_{XL} = A(C3) - A(C1) \quad \text{(Cost of Cross-Lingual Evaluation)}$$
$$\text{Hypothesis } H1: \Delta_{XL} > \Delta_{MT}$$

## 2. Claim-Level Annotation Unit & Rubric
- **Atomic Claim Unit:** Answers are decomposed into atomic, self-contained factual claims (mirroring RAGAS claim extraction).
- **Three-Way Grounded Labels:**
  1. `Supported`: Entailed directly by the reference passage.
  2. `Contradicted`: Factually conflicts with or contradicts the reference passage.
  3. `Not-in-context`: Information is not present in the reference passage, neither confirmed nor contradicted.
  *(Note: $\text{Contradicted} \ne \text{Not-in-context}$.)*
- **Derived Item Faithfulness:** An answer is faithful if and only if all constituent claims are supported.
- **Critical-Claim Override:** If any claim flagged as *critical* is contradicted or not-in-context, the entire item is deemed unfaithful.

## 3. The 7 Typed Perturbations (Guaranteeing Hard Negatives)
To avoid label imbalance where generated answers are overwhelmingly faithful, 50% of the corpus is generated through a deterministic perturbation engine applying one of 7 typed edits:
1. **Entity Swap:** Replacing named entities with in-domain distractors.
2. **Number / Date Alteration:** Modifying numerical quantities or calendar dates.
3. **Negation Flip:** Inserting or removing syntactic negation.
4. **Attribution Removal / Misattribution:** Shifting quoted statements or findings to wrong agents.
5. **Honorific / Register Shift:** Modifying Nepali honorific markers affecting politeness/social rank.
6. **Unsupported Addition:** Adding plausible external claims not grounded in context.
7. **Invented Causal Relation:** Creating false cause-and-effect links between true propositions.

## 4. Evaluator Arms (Frozen at Gate 0)
1. `HHEM-2.1-Open`: Vectara open-weights hallucination evaluation model.
2. `BGE-M3` / `LaBSE`: Multilingual dense embedding cosine similarity.
3. `mDeBERTa-v3-base-xnli`: Matched multilingual NLI encoder across C1, C2, and C3.
4. `IndicTrans2 → English NLI`: Machine translation pipeline into DeBERTa-v3-large-mnli.
5. `LLM-as-a-Judge`: Pinned open-weights/commercial LLMs at temperature 0.0 across C1, C2, and C3.

## 5. Source Corpus Stratification & Multi-Format Ingestion

### Domain Stratification
1. **Nepali Wikipedia (`wikipedia`, ~33%):** Geography, conservation areas, UNESCO World Heritage monuments, and historical biographies under CC BY-SA 4.0.
2. **Nepali Government & Public Reports (`government_report`, ~33%):**
   - High-density numerical data with near-zero pretraining contamination.
   - Sources: Nepal Rastra Bank (NRB) Macroeconomic Bulletins, National Statistics Office (NSO / CBS) Census 2078, Ministry of Finance Economic Surveys, Ministry of Health & Population annual health reports.
3. **Contemporary News & Dedicated Sports Stratum (`news`, ~33%):**
   - General News: *OnlineKhabar*, *Setopati*, *Kantipur Daily*, *Gorkhapatra*.
   - **Sports Sub-Stratum (30% of News):** *HamroKhelkud*, Cricket Association of Nepal (CAN), All Nepal Football Association (ANFA). Features match scores, overs, run rates, tournament years, and player named entities for fine-grained perturbation testing.

### Multi-Format Ingestion Strategy
To prevent PDF formatting artifacts from contaminating faithfulness evaluation:
- **Digital Searchable PDFs:** Extracted via `pypdf` with Unicode Normalization Form C (`unicodedata.normalize('NFC')`) to resolve conjunct splitting (halant ्) and vowel diacritics.
- **Legacy 8-bit Font PDFs:** Automated detection and character-mapping transliteration for legacy Preeti/Kantipur encoding.
- **Scanned Image PDFs:** Automated routing to Gemini Vision OCR (`gemini-3.6-flash`) with prompt-constrained verbatim transcription preserving tables, numbers, and dates.
- **Passage Bounding:** Chunks bounded to 150–350 tokens (1–3 paragraphs); fragments < 80 tokens discarded.

### Fine-Grained 10-Domain Topical Stratification
To reflect realistic civic and technical deployment in Nepal, the 120 evaluation items are stratified across 10 specific topical domains:
1. **Health & Public Medicine (`health`, 10 items):** MoHP reports, NDHS surveys, clinical guidelines.
2. **Agriculture & Forestry (`agriculture`, 10 items):** MoALD censuses, indigenous crops, traditional unit conversions (*ropani*, *bigha*).
3. **Education & Demographics (`education`, 10 items):** MoEST flash reports, SEE pass rates, university enrollments.
4. **Economics & Remittance (`economy_finance`, 10 items):** NRB macroeconomic statistics, remittance inflows, *lakh*/*crore* numeral stress-tests.
5. **Disaster & Environment (`disaster_geography`, 10 items):** NDRRMA seismic/landslide bulletins, flood risk data, GLOF monitoring.
6. **Governance & Legal (`governance_law`, 10 items):** Constitution 2072 articles, local government jurisdiction, statutory gazettes.
7. **Sports (`sports`, 12 items):** Pre-registered 30% news quota: CAN cricket and ANFA football statistics.
8. **Culture & Heritage (`culture_heritage`, 15 items):** UNESCO monuments, BS vs AD calendar conversions (वि.सं.), cultural rituals.
9. **Geography & Biodiversity (`biodiversity_parks`, 15 items):** National parks, endangered wildlife censuses, Himalayan topography.
10. **Infrastructure & Energy (`infrastructure_tourism`, 18 items):** Hydropower MW capacity, Fast Track progress, tourist arrivals.

---

## 6. Authentic Live Corpus Ingestion Protocol (Path 2)

To ensure zero synthetic URL artifacts, eliminate 404 dead links, and provide complete public reproducibility, the evaluation reference bank was constructed through a verified live ingestion protocol:

### Stage 1: Live Discovery Engine
- **Search Instruments:** Targeted live queries using the Tavily Search API with site-restricted filters (`site:onlinekhabar.com`, `site:hamrokhelkud.com`, `site:gorkhapatraonline.com`, `site:mof.gov.np`, `site:nrb.org.np`, `site:cehrd.gov.np`) alongside direct MediaWiki REST queries (`ne.wikipedia.org`).
- **Domain Coverage:** Exactly 60 unique authentic passages harvested:
  - 20 Wikipedia articles (Culture, Biodiversity, Geography) with Devanagari URL encoding.
  - 20 Government & Official Gazette reports (Health, Agriculture, Education, Economy/Finance).
  - 20 Contemporary News articles (6 Sports [30% quota], 5 Disaster/Environment, 5 Governance/Law, 4 Infrastructure/Tourism).

### Stage 2: Programmatic HTTP 200 Verification Gate
- Prior to inclusion in `data/derived/authentic_passages_60.jsonl`, every candidate URL was subjected to an automated HTTP GET request asserting `response.status_code == 200`.
- **Pass Rate:** 60/60 targets verified (`HTTP 200 OK`, 0 failures).
- All Wikipedia paths were strictly encoded using `urllib.parse.quote` to eliminate Unicode handling errors across clients.

### Stage 3: Normalization & Provenance Capture
- Text extracted from article body tags was stripped of HTML boilerplate and navigation menus, then normalized under Unicode NFC (`unicodedata.normalize('NFC')`) to protect Devanagari conjuncts and halant markers.
- Every entry preserves full provenance metadata: `passage_id`, `domain`, `sub_genre`, `source_title`, `source_url`, `publisher`, `publication_year`, and `word_count`.

---

## 7. Downstream Processing & Workbench Generation

1. **Stratified Candidate Assembly (`assemble_candidates.py`):**
   - Ingests the 60 authentic passages and allocates 120 candidate evaluation items matching the exact 40/40/40 macro-strata and 10-domain distribution.
   - Pairs each passage into 1 Natural item (60 items total) and 1 Perturbed counterfactual item (60 items total) cycling across the 7 typed edits ($\ge 8$ items per edit type).
2. **Atomic Claim Decomposition (`export_claims.py`):**
   - Extracts 340 decontextualized factual propositions (mean 2.83 claims/item).
   - Enforces the critical claim invariant: every item contains $\ge 1$ claim marked `is_critical=True`.
3. **Condition C2 Local Batch Machine Translation (`batch_translate_c2.py`):**
   - Generates raw MT ($p_{c2}$) for all 120 items using `ai4bharat/indictrans2-indic-en-dist-200M` executed locally on GPU (`batch_size=2`, `num_beams=2`).
   - Translates the 60 unique passages once and maps back, caching translations under `cache/translations/` keyed on SHA-256 hashes.
4. **Human Evaluation Workbenches (`export_workbenches.py`, `export_c3_workbench.py`):**
   - Dual-annotation workbenches (`workbench_annotator_1.md`, `workbench_annotator_2.md`) generated under `data/interim/preannotations/` with clickable source links, blinded perturbations, and stopwatch fields.
   - Condition C3 post-editing workbench (`post_edit_c3_workbench.md`) formatted side-by-side for the 60 unique passages to isolate $\Delta_{MT} = A(C3) - A(C2)$ via minimal edit distance.



