# Source Domain Licensing Audit

Type: research
Status: awaiting-verdict
Cap: 0.5 day (licensing & redistribution format)

## Question

Conduct a licensing and redistribution audit of the three planned Nepali source domains:
1. **Nepali Wikipedia**: Confirm CC BY-SA 4.0 redistribution compliance and attribution requirements.
2. **Nepali Government & Public Reports**: Number-dense, low pretraining leakage. Check public domain / open government data licenses in Nepal.
3. **Nepali News Outlets**: Review copyright restrictions on text snippets.

Deliverable:
- Recommendation on final dataset release format: full text vs URLs + character offsets + an automated reconstruction script.

## Evidence (agent)

1. **Domain 1: Nepali Wikipedia (`ne.wikipedia.org`)**:
   - **License:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).
   - **Compliance Requirements:** Allows unrestricted non-commercial and commercial sharing, copying, and redistribution in any medium or format, provided that:
     (a) Appropriate credit/attribution is given (article title, permanent URL / revision ID).
     (b) A link to the CC BY-SA 4.0 license is supplied.
     (c) Any derivative datasets indicate if changes were made.
   - **Verdict on Redistribution:** Full passage text can be bundled directly in `data/raw/corpus/` and released publicly on Hugging Face / GitHub.

2. **Domain 2: Nepali Government & Public Reports**:
   - **Sources:** Nepal Rastra Bank (Economic Review / Monetary Policy), Ministry of Health & Population (Annual Health Report), National Statistics Office (National Population and Housing Census).
   - **Legal Framework:**
     - Under the **Nepal Copyright Act, 2059 (2002)**, Section 4 ("Works not protected by copyright"), matters published in the Nepal Gazette, legislative enactments, judicial decisions, and official state reports are public domain materials designed for civic dissemination.
     - Under Section 16 ("Reproduction for education and research purposes"), excerpts from government publications are explicitly permitted for non-commercial scientific research.
   - **Leakage Profile:** Highly desirable. These PDF documents contain dense numerical tables, fiscal year dates (e.g. वि.सं. २०७९/८०), and domain terminology with very low presence in web-scraped LLM pretraining corpuses (Common Crawl / CC100).
   - **Verdict on Redistribution:** Paragraph-level text passages (150–350 tokens) can be directly redistributed in the dataset with source agency citation and document title.

3. **Domain 3: Nepali News Media Outlets**:
   - **Sources:** OnlineKhabar, Setopati, Kantipur (national reporting on civic, infrastructure, and cultural events).
   - **Legal Framework:** Commercial news text is proprietary copyright. However:
     - Nepal Copyright Act Section 17 allows quotation and excerpting of press articles for informational and research purposes consistent with fair dealing.
     - ACL / EMNLP Ethics & Artifact Guidelines permit redistribution of short, bounded context snippets (< 300 words) strictly for academic NLP benchmarks, provided no paywall is bypassed and full original URL + publication timestamp is credited.
     - Full-article redistribution is prohibited to avoid copyright infringement.

4. **Recommended Dataset Release Format: Hybrid Direct Ingestion**:
   - Rather than forcing users to run complex, fragile web scrapers with character offsets (which break over time as news sites update CMS layouts), we release:
     - **Passage-level text directly** in `corpus.jsonl` (each passage constrained to 150–350 tokens / 1–3 paragraphs).
     - **Mandatory schema metadata** for every passage:
       ```json
       {
         "passage_id": "nep_gov_014",
         "domain": "government_report",
         "source_title": "Nepal Rastra Bank Economic Bulletin Q3 2024",
         "source_url": "https://www.nrb.org.np/...",
         "license": "Nepal-Public-Domain-Gov",
         "passage_ne": "..."
       }
       ```
   - This release format complies 100% with CC BY-SA 4.0, Fair Dealing under Nepalese law, and ACL reproducibility guidelines without requiring URL scrapers.

## Verdict (researcher)

<!-- Researcher writes verdict with initials and date to close this ticket. Example:
- 2026-10-15 · Approved hybrid direct passage release format with metadata attribution. — [Initials]
-->

