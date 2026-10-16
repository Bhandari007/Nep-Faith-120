# IndicTrans2 C2 Batch Translation Runner

Type: engineering
Status: Clearance proposed — awaiting researcher
Cap: 1 day (batch translation run, disk cache verification, and leakage audit)

## Question

Generate Condition $C2$ raw machine translations for all 120 Nepali passages using `src/run/translate.py` (IndicTrans2-200M):
1. Execute locally on GPU/CPU with `ai4bharat/indictrans2-indic-en-dist-200M` (`npi_Deva` -> `eng_Latn`).
2. Populate `c2_raw_mt` field for each item in the pre-annotation records.
3. Verify deterministic caching under `cache/translations/` keyed on SHA-256.
4. Verify pipeline invariants: zero cross-condition contamination, strict passage conservation.

## Findings & Evidence (agent)

- **Execution & Invariant Verification:**
  - Ran `BatchC2Translator` (`src/run/batch_translate_c2.py`) across `data/interim/preannotations/gold_candidates_120.jsonl`.
  - Exactly 120/120 candidate items have `c2_raw_mt` populated with non-empty English translations (100% coverage).
  - Deduplicated translation: 61 unique reference passages were translated and mapped to all 120 items.
  - Deterministic caching: 62 translation cache records created under `cache/translations/*.json` keyed on SHA-256 of `(text, npi_Deva, eng_Latn, model_id)`.
  - Condition $C3$ post-edited MT strictly unpopulated (`c3_post_edited_mt: None` for 120/120 items).
  - Physical label isolation verified: Zero writes to `data/raw/labels/`. All claims maintain `gold_label: None`.
  - Tests passing: `tests/test_c2_batch_translation.py` (both invariant and data coverage tests passing, 32/32 tests pass overall).

- **Sample Translation Quality Check:**
  - *item_001 (Wikipedia, Culture & Heritage):*
    - Source $p_{ne}$: "काठमाडौँ उपत्यकाका सातवटा स्मारक क्षेत्रहरू सन् १९७९ मा युनेस्को विश्व सम्पदा सूचीमा सूचीकृत भएका थिए..."
    - Raw MT $C2$: "Seven memorial areas in the Kathmandu Valley were listed on the UNESCO World Heritage List in 2001..." (Notice year MT error: 1979 translated as 2001, providing realistic MT failure counterfactuals to be corrected in $C3$).
  - *item_041 (Gov Report, Health):*
    - Source $p_{ne}$: "नेपाल स्वास्थ्य अनुसन्धान परिषद्का अनुसार नेपालमा नसर्ने रोगहरूको प्रकोप तीव्र रूपमा बढिरहेको छ..."
    - Raw MT $C2$: "According to the Nepal Health Research Council, the incidence of non-communicable diseases in Nepal is increasing rapidly..."
  - *item_081 (News, Sports):*
    - Source $p_{ne}$: "नेपाल राष्ट्रिय क्रिकेट टोलीले सन् २०२४ को आईसीसी पुरुष टी-२० विश्वकपमा दक्षिण अफ्रिका विरुद्ध ऐतिहासिक खेल खेलेको थियो..."
    - Raw MT $C2$: "The Nepal national cricket team played a historic match against South Africa in the 2024 ICC Men's T20 World Cup..."

## Verdict (researcher)

<!-- Researcher signs verdict with initials and date below -->
