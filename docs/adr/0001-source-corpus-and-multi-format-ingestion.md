# ADR 0001: Source Corpus Selection & Multi-Format Ingestion Architecture

- **Status:** Accepted
- **Date:** 2026-10-15
- **Deciders:** Muskan Bhandari (Lead Researcher), Antigravity AI
- **Related Issues:** [Sprint 1 Issue 01](file:///home/leapfrog/Personal/ResearchProjects/NepFaith-120/.scratch/sprint-1/issues/01-corpus-ingestion.md)

---

## Context & Problem Statement

To evaluate cross-lingual faithfulness scoring in Nepali $\to$ English RAG, the source corpus must satisfy three critical requirements:
1. **Low Pretraining Contamination:** Passages must contain dense factual information (numbers, dates, tables, local names) that LLMs cannot answer from general parametric memory.
2. **Domain Diversity:** The benchmark must reflect varied linguistic registers—encyclopedic text, formal administrative/economic reports, and fast-paced journalistic/sports reporting.
3. **Multi-Format Technical Realities:** Nepali government publications are predominantly distributed as PDFs. These vary widely across modern searchable Unicode PDFs, legacy 8-bit non-Unicode font PDFs (Preeti/Kantipur), and scanned image-only PDFs. Scrambled conjuncts or OCR hallucinations in source passages would corrupt downstream faithfulness evaluation.

---

## Decision

### 1. Corpus Domain Stratification & Source Portals

The corpus is structured across three macro-strata, with an explicit sub-genre allocation for Sports:

| Domain | Sub-Genre & Quota | Selected Sources & Rationale | License / Legal Framework |
|---|---|---|---|
| **`wikipedia`** | General Encyclopedic (~33%) | `ne.wikipedia.org`: National parks, geography, UNESCO World Heritage monuments, prominent historical figures. | CC BY-SA 4.0 |
| **`government_report`** | Administrative & Economic (~33%) | **1. Nepal Rastra Bank (NRB):** *Current Macroeconomic & Financial Situation*, *Monetary Policy Statements*.<br>**2. National Statistics Office (NSO / CBS):** *National Population and Housing Census 2078*.<br>**3. Ministry of Finance (MoF):** *Economic Survey (आर्थिक सर्वेक्षण)*.<br>**4. Ministry of Health & Population (MoHP):** *Annual Health Reports*. | Nepal Copyright Act 2059 (Sec 4/16: Public domain civic reports / academic research exception). |
| **`news`** | Civic News (~23%) + **Sports (~10%)** | **Civic News:** `onlinekhabar.com`, `setopati.com`, `ekantipur.com`, `gorkhapatraonline.com`.<br>**Sports (30% of News Stratum):** `hamrokhelkud.net` (HamroKhelkud), Cricket Association of Nepal (CAN), All Nepal Football Association (ANFA). Features dense scores, match statistics, and player entities. | Fair Dealing / Research Excerpt Exception (< 350 words). |

### 2. Multi-Format PDF & Web Ingestion Architecture

The ingestion pipeline in `src/prepare/ingest.py` implements a 3-tier adaptive extraction strategy:

1. **Tier 1 (Digital Unicode PDFs):**  
   - Extracted via `pypdf`.
   - All extracted strings pass through Unicode Normalization Form C (`unicodedata.normalize('NFC', text)`), resolving conjunct consonant splitting (halants ्) and out-of-order vowel diacritics (*matras*).
2. **Tier 2 (Legacy 8-bit Preeti Fonts):**  
   - Automated detection of legacy ASCII distributions (`g]kfn` $\to$ `नेपाल`).
   - Transliterated via deterministic character mapping dictionary prior to tokenization.
3. **Tier 3 (Scanned Image-Only PDFs):**  
   - For pages with zero extractable text, pages are converted to images and transcribed using **Gemini Vision OCR** (`gemini-3.6-flash`) with strict prompt constraints: verbatim transcription, preservation of numerical tables and dates, no summarization.
   - Mitigates Tesseract's known error rate on complex Indic conjuncts and Devanagari numerals.

### 3. Chunking & Bounding Standards
- **Token Bounds:** Passages are chunked into **150 to 350 tokens** (1–3 paragraphs).
- **Discard Filter:** Chunks with fewer than 80 tokens, table-of-contents listings, or navigation links are dropped.
- **Attribution Metadata:** Every passage is assigned a unique `passage_id`, title, source URL, domain, license tag, and publication year in `data/derived/corpus_passages.jsonl`.

---

## Consequences

- **Positive:** Guarantees that numerical stress-tests in government and sports reports are leakage-free. Eliminates broken conjuncts and font gibberish.
- **Negative:** Scanned PDFs require multimodal API calls (safely absorbed by the 10-key rotating Gemini client).
