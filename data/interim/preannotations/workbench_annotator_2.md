# NepFaith-120 Human Annotation Workbench (Annotator 2)

**Version:** 1.0 (Locked Protocol)  
**Annotator:** Annotator 2  
**Reference Document:** `docs/RUBRIC_V1.md` and `docs/PILOT_ANNOTATION_SHEET.md`  
**Storage Protocol:** Save completed annotations to `data/interim/preannotations/workbench_annotator_2.md`. (Do not write directly to `data/raw/labels/`).

---

## Instructions for Human Annotators
1. **Core Task**: Read the **Nepali Context Passage** ($p_{ne}$) and the **English Generated Answer** ($a_{en}$).
2. **Atomic Claim Evaluation**: For every atomic claim listed under the answer, evaluate its factual consistency with the Nepali context passage:
   - `[X] Supported`: The claim is directly stated or logically entailed by the Nepali passage.
   - `[X] Contradicted`: The claim directly contradicts facts explicitly asserted in the Nepali passage.
   - `[X] Not-in-context`: The claim makes assertions completely absent, ungrounded, or unverifiable from the Nepali passage (hallucination/extrapolation).
3. **Criticality**: Claims marked `[CRITICAL]` represent essential, core factual propositions. Non-critical claims represent secondary background details.
4. **Stopwatch Timing**: Record the elapsed annotation time (`mm:ss`) using a standard stopwatch for each item.
5. **Marking**: Replace `[ ]` with `[X]` for your chosen verdict.

---

## Item: `item_001` (1/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> काठमाडौँ उपत्यकाका सातवटा स्मारक क्षेत्रहरू सन् १९७९ मा युनेस्को विश्व सम्पदा सूचीमा सूचीकृत भएका थिए। ती क्षेत्रहरूमा काठमाडौँ दरबार स्क्वायर, पाटन दरबार स्क्वायर, भक्तपुर दरबार स्क्वायर, स्वयम्भूनाथ, बौद्धनाथ, पशुपतिनाथ मन्दिर र चाँगुनारायण मन्दिर पर्दछन्। यी सम्पदाहरूले उपत्यकाको मल्लकालीन कला र नेवारी वास्तुकलालाई प्रतिनिधित्व गर्दछन्।

### User Query (English)
**Q:** When were the monument zones of Kathmandu Valley inscribed on the UNESCO World Heritage List and which sites are included?

### Generated Answer (English)
**A:** The seven monument zones of Kathmandu Valley were inscribed as a UNESCO World Heritage Site in 1979. They include Kathmandu, Patan, and Bhaktapur Durbar Squares, Swayambhunath, Boudhanath, Pashupatinath, and Changunarayan.

### Atomic Claims Evaluation

#### Claim 1: `item_001_c1` **[CRITICAL CLAIM]**
> "Kathmandu Valley's seven monument zones were inscribed in UNESCO World Heritage in 1979."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_001_c2` **[CRITICAL CLAIM]**
> "The sites include Kathmandu, Patan, and Bhaktapur Durbar Squares."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_001_c3` *[NON-CRITICAL CLAIM]*
> "The monuments represent Malla-period art and Newari architecture."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_002` (2/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> पशुपतिनाथ मन्दिर बागमती नदीको किनारमा अवस्थित हिन्दूहरूको पवित्र तीर्थस्थल हो। यो मन्दिर प्यागोडा शैलीमा निर्माण गरिएको छ र यसको छाना दुई तहको सुनको जलप लगाइएको तामाबाट बनेको छ। वि.सं. १९९० को महाभूकम्पमा पनि सुरक्षित रहेको यो मन्दिर क्षेत्रमा सन् १९७९ देखि गैर-हिन्दूहरूलाई मुख्य मन्दिर प्रवेशमा रोक लगाइएको छ।

### User Query (English)
**Q:** Where is the Pashupatinath Temple located and what architectural style does it feature?

### Generated Answer (English)
**A:** Pashupatinath Temple is situated on the banks of the Bagmati River in Kathmandu and features a two-tiered pagoda-style architectural design with gold-plated copper roofs.

### Atomic Claims Evaluation

#### Claim 1: `item_002_c1` **[CRITICAL CLAIM]**
> "Pashupatinath Temple is located on the banks of the Bagmati River."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_002_c2` **[CRITICAL CLAIM]**
> "The temple is constructed in a two-tiered pagoda style."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_002_c3` *[NON-CRITICAL CLAIM]*
> "Non-Hindus are prohibited from entering the inner sanctum of the main temple."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_003` (3/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> इन्द्रजात्रा काठमाडौँ उपत्यकाको नेवार समुदायले मनाउने सबैभन्दा ठूलो ऐतिहासिक जात्रा हो। यो जात्रा भाद्र शुक्ल द्वादशीका दिन हनुमानढोकामा लिंगो (इन्द्रध्वज) ठड्याएपछि सुरु हुन्छ र आठ दिनसम्म चल्दछ। जात्राको मुख्य दिन जीवित देवी कुमारी, गणेश र भैरवको रथ यात्रा गराइन्छ।

### User Query (English)
**Q:** How long does Indra Jatra last and what chariot procession takes place on its main day?

### Generated Answer (English)
**A:** Indra Jatra lasts for eight days after erecting the Indradhwoj pole at Hanuman Dhoka on Bhadra Shukla Dwadashi, featuring the chariot processions of Living Goddess Kumari, Ganesh, and Bhairav on the main day.

### Atomic Claims Evaluation

#### Claim 1: `item_003_c1` **[CRITICAL CLAIM]**
> "Indra Jatra lasts for eight days."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_003_c2` **[CRITICAL CLAIM]**
> "The festival features chariot processions of the Living Goddess Kumari, Ganesh, and Bhairav."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_003_c3` *[NON-CRITICAL CLAIM]*
> "The festival begins by erecting the Indradhwoj pole at Hanuman Dhoka."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_004` (4/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> नेपाल संवत् राष्ट्रिय विभूति शंखधर साख्वाले वि.सं. ९३६ (सन् ८७९) मा सुरु गरेका थिए। उनले काठमाडौँका गरिब जनताको ऋण मोचन गरी यो संवत् चलाएका हुन्। नेपाल सरकारले वि.सं. २०६५ मा नेपाल संवत्लाई राष्ट्रिय संवत्को रूपमा मान्यता दिएको थियो।

### User Query (English)
**Q:** Who initiated the Nepal Sambat calendar and why?

### Generated Answer (English)
**A:** National Luminary Shankhadhar Sakhwa initiated the Nepal Sambat calendar in 879 AD (936 BS) after clearing the debts of the impoverished citizens of Kathmandu.

### Atomic Claims Evaluation

#### Claim 1: `item_004_c1` **[CRITICAL CLAIM]**
> "Shankhadhar Sakhwa initiated the Nepal Sambat in 879 AD (936 BS)."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_004_c2` **[CRITICAL CLAIM]**
> "He founded the calendar by clearing the debts of poor citizens in Kathmandu."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_004_c3` *[NON-CRITICAL CLAIM]*
> "Nepal government officially recognized Nepal Sambat as a national calendar in 2065 BS."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_005` (5/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> चाँगुनारायण मन्दिर काठमाडौँ उपत्यकाको सबैभन्दा पुरानो हिन्दू मन्दिर मानिन्छ। यस मन्दिर परिसरमा वि.सं. ५२१ (सन् ४६४) को लिच्छवी राजा मानदेव प्रथमको शिलालेख फेला परेको छ, जुन नेपालको इतिहासको सबैभन्दा पुरानो प्रमाणिक अभिलेख हो। मन्दिर भक्तपुर जिल्लाको चाँगुनारायण नगरपालिकामा अवस्थित छ।

### User Query (English)
**Q:** What is the historical significance of the inscription at Changunarayan Temple?

### Generated Answer (English)
**A:** Changunarayan Temple houses the 464 AD (521 BS) stone inscription of Licchavi King Manadeva I, which is the oldest verified epigraphic record in Nepalese history.

### Atomic Claims Evaluation

#### Claim 1: `item_005_c1` **[CRITICAL CLAIM]**
> "Changunarayan Temple houses the 464 AD (521 BS) stone inscription of King Manadeva I."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_005_c2` **[CRITICAL CLAIM]**
> "The inscription of King Manadeva I is the oldest verified epigraphic record in Nepalese history."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_005_c3` *[NON-CRITICAL CLAIM]*
> "Changunarayan is located in Bhaktapur district."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_006` (6/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> स्वयम्भूनाथ स्तूप काठमाडौँ उपत्यकाको पश्चिम भागमा एउटा पहाडी टाकुरामा अवस्थित छ। यसलाई 'मंकी टेम्पल' का नामले पनि चिनिन्छ। स्तूपको शीर्ष भागमा चारै दिशामा हेरिरहेका बुद्धका आँखाहरू कुँदिएका छन्, जसले सर्वव्यापी ज्ञान र करुणाको प्रतीक जनाउँछ।

### User Query (English)
**Q:** What is depicted on the top of the Swayambhunath Stupa and what does it symbolize?

### Generated Answer (English)
**A:** The top of the Swayambhunath Stupa depicts the all-seeing eyes of Buddha painted in all four cardinal directions, symbolizing omnipresent wisdom and compassion.

### Atomic Claims Evaluation

#### Claim 1: `item_006_c1` **[CRITICAL CLAIM]**
> "Swayambhunath Stupa features Buddha's eyes painted facing all four cardinal directions."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_006_c2` **[CRITICAL CLAIM]**
> "Buddha's eyes symbolize omnipresent wisdom and compassion."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_006_c3` *[NON-CRITICAL CLAIM]*
> "Swayambhunath is commonly referred to as the Monkey Temple."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_007` (7/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> नेपालमा मनाइने छठ पर्व सूर्य देवता र छठी माताको उपासना गरिने प्रमुख चाड हो। चार दिनसम्म मनाइने यस पर्वमा अस्ताउँदो र उदाउँदो सूर्यलाई पवित्र नदी वा पोखरीको किनारमा अर्घ्य दिइन्छ। विशेषगरी तराई-मधेशमा मनाइने यो पर्व अहिले काठमाडौँ उपत्यका लगायत पहाडी क्षेत्रमा पनि लोकप्रिय भएको छ।

### User Query (English)
**Q:** Which deities are worshipped during Chhath festival and how is the offering made?

### Generated Answer (English)
**A:** During the four-day Chhath festival, devotees worship the Sun God (Surya) and Chhathi Maiya by offering arghya to the setting and rising sun along the banks of holy rivers and ponds.

### Atomic Claims Evaluation

#### Claim 1: `item_007_c1` **[CRITICAL CLAIM]**
> "Chhath is a four-day festival worshipping the Sun God and Chhathi Maiya."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_007_c2` **[CRITICAL CLAIM]**
> "Devotees offer arghya to both the setting and rising sun along water banks."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_008` (8/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> भक्तपुर दरबार स्क्वायरलाई '५५ झ्याले दरबार' र 'न्यातपोल मन्दिर' का लागि चिनिन्छ। राजा भूपतिन्द्र मल्लले निर्माण गर्न लगाएको न्यातपोल मन्दिर पाँच तल्ला भएको नेपालकै सबैभन्दा अग्लो प्यागोडा मन्दिर हो, जसको उचाइ करिब ३० मिटर रहेको छ।

### User Query (English)
**Q:** Who commissioned the construction of the Nyatapola Temple and what is its height?

### Generated Answer (English)
**A:** King Bhupatindra Malla commissioned the construction of the 5-story Nyatapola Temple in Bhaktapur, which stands approximately 30 meters tall as Nepal's tallest pagoda temple.

### Atomic Claims Evaluation

#### Claim 1: `item_008_c1` **[CRITICAL CLAIM]**
> "King Bhupatindra Malla commissioned the construction of the Nyatapola Temple."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_008_c2` **[CRITICAL CLAIM]**
> "Nyatapola Temple is a 5-story pagoda standing roughly 30 meters tall."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_008_c3` *[NON-CRITICAL CLAIM]*
> "Bhaktapur Durbar Square is famous for the 55-Window Palace."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_009` (9/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> काठमाडौँ उपत्यकाका सातवटा स्मारक क्षेत्रहरू सन् १९७९ मा युनेस्को विश्व सम्पदा सूचीमा सूचीकृत भएका थिए। ती क्षेत्रहरूमा काठमाडौँ दरबार स्क्वायर, पाटन दरबार स्क्वायर, भक्तपुर दरबार स्क्वायर, स्वयम्भूनाथ, बौद्धनाथ, पशुपतिनाथ मन्दिर र चाँगुनारायण मन्दिर पर्दछन्। यी सम्पदाहरूले उपत्यकाको मल्लकालीन कला र नेवारी वास्तुकलालाई प्रतिनिधित्व गर्दछन्।

### User Query (English)
**Q:** When were the monument zones of Kathmandu Valley inscribed on the UNESCO World Heritage List and which sites are included?

### Generated Answer (English)
**A:** The seven monument zones of Pokhara Valley were inscribed as a UNESCO World Heritage Site in 1979. They include Kathmandu, Patan, and Bhaktapur Durbar Squares, Swayambhunath, Boudhanath, Pashupatinath, and Changunarayan.

### Atomic Claims Evaluation

#### Claim 1: `item_009_c1` **[CRITICAL CLAIM]**
> "Pokhara Valley's seven monument zones were inscribed in UNESCO World Heritage in 1979."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_009_c2` **[CRITICAL CLAIM]**
> "The sites include Kathmandu, Patan, and Bhaktapur Durbar Squares."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_009_c3` *[NON-CRITICAL CLAIM]*
> "The monuments represent Malla-period art and Newari architecture."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_010` (10/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> पशुपतिनाथ मन्दिर बागमती नदीको किनारमा अवस्थित हिन्दूहरूको पवित्र तीर्थस्थल हो। यो मन्दिर प्यागोडा शैलीमा निर्माण गरिएको छ र यसको छाना दुई तहको सुनको जलप लगाइएको तामाबाट बनेको छ। वि.सं. १९९० को महाभूकम्पमा पनि सुरक्षित रहेको यो मन्दिर क्षेत्रमा सन् १९७९ देखि गैर-हिन्दूहरूलाई मुख्य मन्दिर प्रवेशमा रोक लगाइएको छ।

### User Query (English)
**Q:** Where is the Pashupatinath Temple located and what architectural style does it feature?

### Generated Answer (English)
**A:** Pashupatinath Temple is situated on the banks of the Bagmati River in Kathmandu and features a two-tiered pagoda-style architectural design with gold-plated copper roofs.

### Atomic Claims Evaluation

#### Claim 1: `item_010_c1` **[CRITICAL CLAIM]**
> "Pashupatinath Temple is located on the banks of the Bagmati River."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_010_c2` **[CRITICAL CLAIM]**
> "The temple is constructed in a two-tiered pagoda style."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_010_c3` *[NON-CRITICAL CLAIM]*
> "Non-Hindus are prohibited from entering the inner sanctum of the main temple."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_011` (11/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> इन्द्रजात्रा काठमाडौँ उपत्यकाको नेवार समुदायले मनाउने सबैभन्दा ठूलो ऐतिहासिक जात्रा हो। यो जात्रा भाद्र शुक्ल द्वादशीका दिन हनुमानढोकामा लिंगो (इन्द्रध्वज) ठड्याएपछि सुरु हुन्छ र आठ दिनसम्म चल्दछ। जात्राको मुख्य दिन जीवित देवी कुमारी, गणेश र भैरवको रथ यात्रा गराइन्छ।

### User Query (English)
**Q:** How long does Indra Jatra last and what chariot procession takes place on its main day?

### Generated Answer (English)
**A:** It is false that indra Jatra lasts for eight days after erecting the Indradhwoj pole at Hanuman Dhoka on Bhadra Shukla Dwadashi, featuring the chariot processions of Living Goddess Kumari, Ganesh, and Bhairav on the main day.

### Atomic Claims Evaluation

#### Claim 1: `item_011_c1` **[CRITICAL CLAIM]**
> "It is false that indra Jatra lasts for eight days."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_011_c2` **[CRITICAL CLAIM]**
> "The festival features chariot processions of the Living Goddess Kumari, Ganesh, and Bhairav."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_011_c3` *[NON-CRITICAL CLAIM]*
> "The festival begins by erecting the Indradhwoj pole at Hanuman Dhoka."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_012` (12/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> नेपाल संवत् राष्ट्रिय विभूति शंखधर साख्वाले वि.सं. ९३६ (सन् ८७९) मा सुरु गरेका थिए। उनले काठमाडौँका गरिब जनताको ऋण मोचन गरी यो संवत् चलाएका हुन्। नेपाल सरकारले वि.सं. २०६५ मा नेपाल संवत्लाई राष्ट्रिय संवत्को रूपमा मान्यता दिएको थियो।

### User Query (English)
**Q:** Who initiated the Nepal Sambat calendar and why?

### Generated Answer (English)
**A:** According to the Asian Development Bank, national Luminary Shankhadhar Sakhwa initiated the Nepal Sambat calendar in 879 AD (936 BS) after clearing the debts of the impoverished citizens of Kathmandu.

### Atomic Claims Evaluation

#### Claim 1: `item_012_c1` **[CRITICAL CLAIM]**
> "According to the Asian Development Bank, shankhadhar Sakhwa initiated the Nepal Sambat in 879 AD (936 BS)."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_012_c2` **[CRITICAL CLAIM]**
> "He founded the calendar by clearing the debts of poor citizens in Kathmandu."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_012_c3` *[NON-CRITICAL CLAIM]*
> "Nepal government officially recognized Nepal Sambat as a national calendar in 2065 BS."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_013` (13/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> चाँगुनारायण मन्दिर काठमाडौँ उपत्यकाको सबैभन्दा पुरानो हिन्दू मन्दिर मानिन्छ। यस मन्दिर परिसरमा वि.सं. ५२१ (सन् ४६४) को लिच्छवी राजा मानदेव प्रथमको शिलालेख फेला परेको छ, जुन नेपालको इतिहासको सबैभन्दा पुरानो प्रमाणिक अभिलेख हो। मन्दिर भक्तपुर जिल्लाको चाँगुनारायण नगरपालिकामा अवस्थित छ।

### User Query (English)
**Q:** What is the historical significance of the inscription at Changunarayan Temple?

### Generated Answer (English)
**A:** The respective authorities and multiple delegates Temple houses the 464 AD (521 BS) stone inscription of Licchavi King Manadeva I, which is the oldest verified epigraphic record in Nepalese history.

### Atomic Claims Evaluation

#### Claim 1: `item_013_c1` **[CRITICAL CLAIM]**
> "The respective authorities and multiple delegates Temple houses the 464 AD (521 BS) stone inscription of King Manadeva I."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_013_c2` **[CRITICAL CLAIM]**
> "The inscription of King Manadeva I is the oldest verified epigraphic record in Nepalese history."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_013_c3` *[NON-CRITICAL CLAIM]*
> "Changunarayan is located in Bhaktapur district."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_014` (14/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> स्वयम्भूनाथ स्तूप काठमाडौँ उपत्यकाको पश्चिम भागमा एउटा पहाडी टाकुरामा अवस्थित छ। यसलाई 'मंकी टेम्पल' का नामले पनि चिनिन्छ। स्तूपको शीर्ष भागमा चारै दिशामा हेरिरहेका बुद्धका आँखाहरू कुँदिएका छन्, जसले सर्वव्यापी ज्ञान र करुणाको प्रतीक जनाउँछ।

### User Query (English)
**Q:** What is depicted on the top of the Swayambhunath Stupa and what does it symbolize?

### Generated Answer (English)
**A:** The top of the Swayambhunath Stupa depicts the all-seeing eyes of Buddha painted in all four cardinal directions, symbolizing omnipresent wisdom and compassion. Furthermore, the initiative was financed through a low-interest loan from the Asian Development Bank.

### Atomic Claims Evaluation

#### Claim 1: `item_014_c1` **[CRITICAL CLAIM]**
> "Swayambhunath Stupa features Buddha's eyes painted facing all four cardinal directions. Furthermore, the initiative was financed through a low-interest loan from the Asian Development Bank."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_014_c2` **[CRITICAL CLAIM]**
> "Buddha's eyes symbolize omnipresent wisdom and compassion."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_014_c3` *[NON-CRITICAL CLAIM]*
> "Swayambhunath is commonly referred to as the Monkey Temple."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_015` (15/120)
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### Context Passage (Nepali · Condition C1)
> नेपालमा मनाइने छठ पर्व सूर्य देवता र छठी माताको उपासना गरिने प्रमुख चाड हो। चार दिनसम्म मनाइने यस पर्वमा अस्ताउँदो र उदाउँदो सूर्यलाई पवित्र नदी वा पोखरीको किनारमा अर्घ्य दिइन्छ। विशेषगरी तराई-मधेशमा मनाइने यो पर्व अहिले काठमाडौँ उपत्यका लगायत पहाडी क्षेत्रमा पनि लोकप्रिय भएको छ।

### User Query (English)
**Q:** Which deities are worshipped during Chhath festival and how is the offering made?

### Generated Answer (English)
**A:** During the four-day Chhath festival, devotees worship the Sun God (Surya) and Chhathi Maiya by offering arghya to the setting and rising sun along the banks of holy rivers and ponds, directly leading to an unprecedented national crisis.

### Atomic Claims Evaluation

#### Claim 1: `item_015_c1` **[CRITICAL CLAIM]**
> "Chhath is a four-day festival worshipping the Sun God and Chhathi Maiya, directly leading to an unprecedented national crisis."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_015_c2` **[CRITICAL CLAIM]**
> "Devotees offer arghya to both the setting and rising sun along water banks."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_016` (16/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> सगरमाथा राष्ट्रिय निकुञ्ज सन् १९७६ मा स्थापना भएको हो र सन् १९७९ मा युनेस्को विश्व प्राकृतिक सम्पदा सूचीमा सूचीकृत भएको थियो। १ हजार १४८ वर्ग किलोमिटरमा फैलिएको यस निकुञ्जमा विश्वको सर्वोच्च शिखर सगरमाथा (८,८४८.८६ मिटर) सहित ल्होत्से, नुप्त्से, चो ओयु र आमादब्लम जस्ता प्रमुख हिमालहरू पर्दछन्। यहाँ हिमचितुवा र कस्तुरी मृग पाइन्छन्।

### User Query (English)
**Q:** When was Sagarmatha National Park inscribed as a UNESCO World Heritage Site and what is its total area?

### Generated Answer (English)
**A:** Sagarmatha National Park was established in 1976 and inscribed as a UNESCO World Natural Heritage Site in 1979, spanning an area of 1,148 square kilometers.

### Atomic Claims Evaluation

#### Claim 1: `item_016_c1` **[CRITICAL CLAIM]**
> "Sagarmatha National Park was inscribed as a UNESCO Natural Heritage Site in 1979."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_016_c2` **[CRITICAL CLAIM]**
> "The park covers an area of 1,148 square kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_016_c3` *[NON-CRITICAL CLAIM]*
> "The park harbors endangered species such as the snow leopard and musk deer."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_017` (17/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> सन् २०२२ को राष्ट्रिय बाघ गणना अनुसार नेपालमा पाटे बाघको सङ्ख्या बढेर ३५५ पुगेको छ। सन् २०१० मा सेन्ट पिटर्सबर्ग सम्मेलनमा नेपालले गरेको बाघको सङ्ख्या दोब्बर बनाउने प्रतिबद्धता (१२१ बाट २४२) पूरा गरी नेपाल विश्वमै बाघको सङ्ख्या दोब्बर बनाउने पहिलो देश बनेको थियो। सबैभन्दा बढी बाघ चितवन राष्ट्रिय निकुञ्ज (१२८ वटा) मा रहेका छन्।

### User Query (English)
**Q:** What was the royal Bengal tiger population in Nepal according to the 2022 census and which park holds the largest count?

### Generated Answer (English)
**A:** Nepal's 2022 tiger census recorded 355 wild Bengal tigers, fulfilling its pledge to double its population from 2010. Chitwan National Park holds the largest population with 128 tigers.

### Atomic Claims Evaluation

#### Claim 1: `item_017_c1` **[CRITICAL CLAIM]**
> "Nepal recorded a population of 355 wild Bengal tigers in the 2022 census."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_017_c2` **[CRITICAL CLAIM]**
> "Nepal became the first country to double its wild tiger population from its 2010 baseline of 121."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_017_c3` *[NON-CRITICAL CLAIM]*
> "Chitwan National Park hosts the largest tiger population with 128 individuals."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_018` (18/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> बर्दिया राष्ट्रिय निकुञ्ज नेपालको तराई क्षेत्रमा अवस्थित सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज हो, जसको क्षेत्रफल ९६८ वर्ग किलोमिटर छ। यो निकुञ्ज कर्णाली नदीको पूर्वी किनारमा फैलिएको छ र यहाँ एकसिङ्गे गैँडा, पाटे बाघ र एसियाली हात्तीहरू पाइन्छन्। बर्दियामा १२५ वटा पाटे बाघ रहेका छन्।

### User Query (English)
**Q:** What is the area of Bardiya National Park and which river flows along its border?

### Generated Answer (English)
**A:** Bardiya National Park covers 968 square kilometers along the eastern bank of the Karnali River, making it the largest national park in Nepal's lowland Terai.

### Atomic Claims Evaluation

#### Claim 1: `item_018_c1` **[CRITICAL CLAIM]**
> "Bardiya National Park covers an area of 968 square kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_018_c2` **[CRITICAL CLAIM]**
> "The park lies along the eastern bank of the Karnali River."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_018_c3` *[NON-CRITICAL CLAIM]*
> "Bardiya is home to 125 wild Bengal tigers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_019` (19/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> रारा ताल नेपालको सबैभन्दा ठूलो र गहिरो ताल हो। यो कर्णाली प्रदेशको मुगु जिल्लामा समुद्र सतहबाट २ हजार ९९० मिटरको उचाइमा अवस्थित छ। यस तालको लम्बाइ करिब ५.१ किलोमिटर, चौडाइ २.७ किलोमिटर र अधिकतम गहिराइ १६७ मिटर रहेको छ। रारा ताल रारा राष्ट्रिय निकुञ्जभित्र पर्दछ।

### User Query (English)
**Q:** What is the maximum depth and elevation of Rara Lake in Nepal?

### Generated Answer (English)
**A:** Rara Lake is located in Mugu district at an elevation of 2,990 meters above sea level and has a maximum depth of 167 meters, making it Nepal's largest and deepest lake.

### Atomic Claims Evaluation

#### Claim 1: `item_019_c1` **[CRITICAL CLAIM]**
> "Rara Lake is situated at an elevation of 2,990 meters in Mugu district."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_019_c2` **[CRITICAL CLAIM]**
> "Rara Lake reaches a maximum depth of 167 meters."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_019_c3` *[NON-CRITICAL CLAIM]*
> "Rara Lake is Nepal's largest lake with a length of 5.1 kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_020` (20/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> अन्नपूर्ण संरक्षण क्षेत्र नेपालको सबैभन्दा ठूलो संरक्षण क्षेत्र हो, जसको क्षेत्रफल ७ हजार ६२९ वर्ग किलोमिटर छ। यो गण्डकी प्रदेशका कास्की, लमजुङ, म्याग्दी, मनाङ र मुस्ताङ जिल्लामा फैलिएको छ। यस क्षेत्रलाई राष्ट्रिय प्रकृति संरक्षण कोष (एनटीएनसी) ले स्थानीय समुदायको सहभागितामा व्यवस्थापन गर्दै आएको छ।

### User Query (English)
**Q:** What is the total area of the Annapurna Conservation Area and which entity manages it?

### Generated Answer (English)
**A:** The Annapurna Conservation Area spans 7,629 square kilometers across five districts and is managed by the National Trust for Nature Conservation (NTNC) with community participation.

### Atomic Claims Evaluation

#### Claim 1: `item_020_c1` **[CRITICAL CLAIM]**
> "Annapurna Conservation Area covers 7,629 square kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_020_c2` **[CRITICAL CLAIM]**
> "The area is managed by the National Trust for Nature Conservation (NTNC)."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_021` (21/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> लाङटाङ राष्ट्रिय निकुञ्ज नेपालको पहिलो हिमाली राष्ट्रिय निकुञ्ज हो, जुन सन् १९७६ मा स्थापना भएको थियो। १ हजार ७१० वर्ग किलोमिटरमा फैलिएको यस निकुञ्जले रसुवा, नुवाकोट र सिन्धुपाल्चोक जिल्लालाई ओगटेको छ। निकुञ्जभित्र पवित्र गोसाइँकुण्ड ताल अवस्थित छ, जहाँ जनैपूर्णिमाका दिन ठूलो मेला लाग्दछ।

### User Query (English)
**Q:** Which sacred lake is located inside Langtang National Park?

### Generated Answer (English)
**A:** The sacred Gosainkunda Lake is located within Langtang National Park, which was established in 1976 across Rasuwa, Nuwakot, and Sindhupalchok districts.

### Atomic Claims Evaluation

#### Claim 1: `item_021_c1` **[CRITICAL CLAIM]**
> "Gosainkunda Lake is located within Langtang National Park."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_021_c2` *[NON-CRITICAL CLAIM]*
> "Langtang was established as Nepal's first Himalayan national park in 1976."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_021_c3` *[NON-CRITICAL CLAIM]*
> "Langtang National Park covers 1,710 square kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_022` (22/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> नेपालमा हालसम्म ८८६ प्रजातिका चराहरू अभिलेखीकरण गरिएका छन्, जुन विश्वको कुल चरा प्रजातिको करिब ९ प्रतिशत हो। कोशी टप्पु वन्यजन्तु आरक्ष नेपालको प्रमुख चरा अवलोकन क्षेत्र हो, जहाँ ५२६ भन्दा बढी प्रजातिका चराहरू पाइन्छन्। काँडे भ्याकुर नेपालमा मात्र पाइने रैथाने चरा हो।

### User Query (English)
**Q:** Which bird species is endemic only to Nepal and how many bird species are recorded in Koshi Tappu?

### Generated Answer (English)
**A:** The Spiny Babbler (काँडे भ्याकुर) is the only endemic bird found exclusively in Nepal. Koshi Tappu Wildlife Reserve serves as a premier birding habitat hosting over 526 bird species.

### Atomic Claims Evaluation

#### Claim 1: `item_022_c1` **[CRITICAL CLAIM]**
> "The Spiny Babbler (Kande Bhyakur) is the only bird endemic exclusively to Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_022_c2` **[CRITICAL CLAIM]**
> "Koshi Tappu Wildlife Reserve hosts over 526 recorded bird species."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_022_c3` *[NON-CRITICAL CLAIM]*
> "A total of 886 bird species have been documented in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_023` (23/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> शुक्लाफाँटा राष्ट्रिय निकुञ्ज सुदूरपश्चिम प्रदेशको कञ्चनपुर जिल्लामा अवस्थित छ। यस निकुञ्जको क्षेत्रफल ३०५ वर्ग किलोमिटर छ। यहाँ विश्वकै सबैभन्दा ठूलो बाह्रसिङ्गा (स्वम्प डियर) को बथान पाइन्छ, जसको सङ्ख्या २ हजारभन्दा बढी रहेको छ।

### User Query (English)
**Q:** What is the primary wildlife attraction of Suklaphanta National Park in Kanchanpur?

### Generated Answer (English)
**A:** Suklaphanta National Park in Kanchanpur spans 305 square kilometers and hosts the world's largest herd of swamp deer (barasingha), numbering over 2,000 individuals.

### Atomic Claims Evaluation

#### Claim 1: `item_023_c1` *[NON-CRITICAL CLAIM]*
> "Suklaphanta National Park is located in Kanchanpur district."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_023_c2` **[CRITICAL CLAIM]**
> "The park hosts the world's largest herd of swamp deer, exceeding 2,000 individuals."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_023_c3` **[CRITICAL CLAIM]**
> "The park covers an area of 305 square kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_024` (24/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> सगरमाथा राष्ट्रिय निकुञ्ज सन् १९७६ मा स्थापना भएको हो र सन् १९७९ मा युनेस्को विश्व प्राकृतिक सम्पदा सूचीमा सूचीकृत भएको थियो। १ हजार १४८ वर्ग किलोमिटरमा फैलिएको यस निकुञ्जमा विश्वको सर्वोच्च शिखर सगरमाथा (८,८४८.८६ मिटर) सहित ल्होत्से, नुप्त्से, चो ओयु र आमादब्लम जस्ता प्रमुख हिमालहरू पर्दछन्। यहाँ हिमचितुवा र कस्तुरी मृग पाइन्छन्।

### User Query (English)
**Q:** When was Sagarmatha National Park inscribed as a UNESCO World Heritage Site and what is its total area?

### Generated Answer (English)
**A:** Sagarmatha National Park was established in 1976 and inscribed as a UNESCO World Natural Heritage Site in 1979, spanning an area of 1,136 square kilometers.

### Atomic Claims Evaluation

#### Claim 1: `item_024_c1` **[CRITICAL CLAIM]**
> "Sagarmatha National Park was inscribed as a UNESCO Natural Heritage Site in 1989."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_024_c2` **[CRITICAL CLAIM]**
> "The park covers an area of 1,148 square kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_024_c3` *[NON-CRITICAL CLAIM]*
> "The park harbors endangered species such as the snow leopard and musk deer."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_025` (25/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> सन् २०२२ को राष्ट्रिय बाघ गणना अनुसार नेपालमा पाटे बाघको सङ्ख्या बढेर ३५५ पुगेको छ। सन् २०१० मा सेन्ट पिटर्सबर्ग सम्मेलनमा नेपालले गरेको बाघको सङ्ख्या दोब्बर बनाउने प्रतिबद्धता (१२१ बाट २४२) पूरा गरी नेपाल विश्वमै बाघको सङ्ख्या दोब्बर बनाउने पहिलो देश बनेको थियो। सबैभन्दा बढी बाघ चितवन राष्ट्रिय निकुञ्ज (१२८ वटा) मा रहेका छन्।

### User Query (English)
**Q:** What was the royal Bengal tiger population in Nepal according to the 2022 census and which park holds the largest count?

### Generated Answer (English)
**A:** It is false that nepal's 2022 tiger census recorded 355 wild Bengal tigers, fulfilling its pledge to double its population from 2010. Chitwan National Park holds the largest population with 128 tigers.

### Atomic Claims Evaluation

#### Claim 1: `item_025_c1` **[CRITICAL CLAIM]**
> "It is false that nepal recorded a population of 355 wild Bengal tigers in the 2022 census."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_025_c2` **[CRITICAL CLAIM]**
> "Nepal became the first country to double its wild tiger population from its 2010 baseline of 121."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_025_c3` *[NON-CRITICAL CLAIM]*
> "Chitwan National Park hosts the largest tiger population with 128 individuals."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_026` (26/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> बर्दिया राष्ट्रिय निकुञ्ज नेपालको तराई क्षेत्रमा अवस्थित सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज हो, जसको क्षेत्रफल ९६८ वर्ग किलोमिटर छ। यो निकुञ्ज कर्णाली नदीको पूर्वी किनारमा फैलिएको छ र यहाँ एकसिङ्गे गैँडा, पाटे बाघ र एसियाली हात्तीहरू पाइन्छन्। बर्दियामा १२५ वटा पाटे बाघ रहेका छन्।

### User Query (English)
**Q:** What is the area of Bardiya National Park and which river flows along its border?

### Generated Answer (English)
**A:** According to the Asian Development Bank, bardiya National Park covers 968 square kilometers along the eastern bank of the Karnali River, making it the largest national park in Nepal's lowland Terai.

### Atomic Claims Evaluation

#### Claim 1: `item_026_c1` **[CRITICAL CLAIM]**
> "According to the Asian Development Bank, bardiya National Park covers an area of 968 square kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_026_c2` **[CRITICAL CLAIM]**
> "The park lies along the eastern bank of the Karnali River."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_026_c3` *[NON-CRITICAL CLAIM]*
> "Bardiya is home to 125 wild Bengal tigers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_027` (27/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> रारा ताल नेपालको सबैभन्दा ठूलो र गहिरो ताल हो। यो कर्णाली प्रदेशको मुगु जिल्लामा समुद्र सतहबाट २ हजार ९९० मिटरको उचाइमा अवस्थित छ। यस तालको लम्बाइ करिब ५.१ किलोमिटर, चौडाइ २.७ किलोमिटर र अधिकतम गहिराइ १६७ मिटर रहेको छ। रारा ताल रारा राष्ट्रिय निकुञ्जभित्र पर्दछ।

### User Query (English)
**Q:** What is the maximum depth and elevation of Rara Lake in Nepal?

### Generated Answer (English)
**A:** The respective authorities and multiple delegates Lake is located in Mugu district at an elevation of 2,990 meters above sea level and has a maximum depth of 167 meters, making it Nepal's largest and deepest lake.

### Atomic Claims Evaluation

#### Claim 1: `item_027_c1` **[CRITICAL CLAIM]**
> "The respective authorities and multiple delegates Lake is situated at an elevation of 2,990 meters in Mugu district."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_027_c2` **[CRITICAL CLAIM]**
> "Rara Lake reaches a maximum depth of 167 meters."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_027_c3` *[NON-CRITICAL CLAIM]*
> "Rara Lake is Nepal's largest lake with a length of 5.1 kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_028` (28/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> अन्नपूर्ण संरक्षण क्षेत्र नेपालको सबैभन्दा ठूलो संरक्षण क्षेत्र हो, जसको क्षेत्रफल ७ हजार ६२९ वर्ग किलोमिटर छ। यो गण्डकी प्रदेशका कास्की, लमजुङ, म्याग्दी, मनाङ र मुस्ताङ जिल्लामा फैलिएको छ। यस क्षेत्रलाई राष्ट्रिय प्रकृति संरक्षण कोष (एनटीएनसी) ले स्थानीय समुदायको सहभागितामा व्यवस्थापन गर्दै आएको छ।

### User Query (English)
**Q:** What is the total area of the Annapurna Conservation Area and which entity manages it?

### Generated Answer (English)
**A:** The Annapurna Conservation Area spans 7,629 square kilometers across five districts and is managed by the National Trust for Nature Conservation (NTNC) with community participation. Furthermore, the initiative was financed through a low-interest loan from the Asian Development Bank.

### Atomic Claims Evaluation

#### Claim 1: `item_028_c1` **[CRITICAL CLAIM]**
> "Annapurna Conservation Area covers 7,629 square kilometers. Furthermore, the initiative was financed through a low-interest loan from the Asian Development Bank."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_028_c2` **[CRITICAL CLAIM]**
> "The area is managed by the National Trust for Nature Conservation (NTNC)."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_029` (29/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> लाङटाङ राष्ट्रिय निकुञ्ज नेपालको पहिलो हिमाली राष्ट्रिय निकुञ्ज हो, जुन सन् १९७६ मा स्थापना भएको थियो। १ हजार ७१० वर्ग किलोमिटरमा फैलिएको यस निकुञ्जले रसुवा, नुवाकोट र सिन्धुपाल्चोक जिल्लालाई ओगटेको छ। निकुञ्जभित्र पवित्र गोसाइँकुण्ड ताल अवस्थित छ, जहाँ जनैपूर्णिमाका दिन ठूलो मेला लाग्दछ।

### User Query (English)
**Q:** Which sacred lake is located inside Langtang National Park?

### Generated Answer (English)
**A:** The sacred Gosainkunda Lake is located within Langtang National Park, which was established in 1976 across Rasuwa, Nuwakot, and Sindhupalchok districts, directly leading to an unprecedented national crisis.

### Atomic Claims Evaluation

#### Claim 1: `item_029_c1` **[CRITICAL CLAIM]**
> "Gosainkunda Lake is located within Langtang National Park, directly leading to an unprecedented national crisis."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_029_c2` *[NON-CRITICAL CLAIM]*
> "Langtang was established as Nepal's first Himalayan national park in 1976."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_029_c3` *[NON-CRITICAL CLAIM]*
> "Langtang National Park covers 1,710 square kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_030` (30/120)
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### Context Passage (Nepali · Condition C1)
> नेपालमा हालसम्म ८८६ प्रजातिका चराहरू अभिलेखीकरण गरिएका छन्, जुन विश्वको कुल चरा प्रजातिको करिब ९ प्रतिशत हो। कोशी टप्पु वन्यजन्तु आरक्ष नेपालको प्रमुख चरा अवलोकन क्षेत्र हो, जहाँ ५२६ भन्दा बढी प्रजातिका चराहरू पाइन्छन्। काँडे भ्याकुर नेपालमा मात्र पाइने रैथाने चरा हो।

### User Query (English)
**Q:** Which bird species is endemic only to Nepal and how many bird species are recorded in Koshi Tappu?

### Generated Answer (English)
**A:** The Spiny Babbler (काँडे भ्याकुर) is the only endemic bird found exclusively in Bhutan. Koshi Tappu Wildlife Reserve serves as a premier birding habitat hosting over 526 bird species.

### Atomic Claims Evaluation

#### Claim 1: `item_030_c1` **[CRITICAL CLAIM]**
> "The Spiny Babbler (Kande Bhyakur) is the only bird endemic exclusively to Bhutan."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_030_c2` **[CRITICAL CLAIM]**
> "Koshi Tappu Wildlife Reserve hosts over 526 recorded bird species."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_030_c3` *[NON-CRITICAL CLAIM]*
> "A total of 886 bird species have been documented in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_031` (31/120)
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> माथिल्लो तामाकोशी जलविद्युत आयोजना (४५६ मेगावाट) नेपालको आफ्नै स्रोत र साधनमा निर्माण भएको सबैभन्दा ठूलो जलविद्युत आयोजना हो। दोलखा जिल्लाको लामाबगरमा अवस्थित यस आयोजनाले वि.सं. २०७८ असारमा व्यावसायिक उत्पादन सुरु गरेको थियो। यस आयोजनाको भूमिगत विद्युतगृहमा ७६ मेगावाटका ६ वटा टर्बाइनहरू जडान गरिएका छन्।

### User Query (English)
**Q:** What is the installed capacity and location of the Upper Tamakoshi Hydropower Project?

### Generated Answer (English)
**A:** Upper Tamakoshi Hydropower Project has an installed capacity of 456 megawatts located at Lamabagar in Dolakha district, operating six 76 MW turbines in its underground powerhouse.

### Atomic Claims Evaluation

#### Claim 1: `item_031_c1` **[CRITICAL CLAIM]**
> "Upper Tamakoshi Hydropower Project has an installed capacity of 456 MW."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_031_c2` **[CRITICAL CLAIM]**
> "The project is located at Lamabagar in Dolakha district."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_031_c3` *[NON-CRITICAL CLAIM]*
> "Its underground powerhouse is equipped with six 76 MW turbines."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_032` (32/120)
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> नेपाल विद्युत प्राधिकरणका अनुसार नेपालको कुल जडित विद्युत क्षमता ३ हजार २०० मेगावाट नाघेको छ। वर्षायाममा नेपालले भारततर्फ दैनिक ६५० मेगावाटसम्म विद्युत निर्यात गर्दै आएको छ भने बंगलादेशतर्फ ४० मेगावाट विद्युत निर्यातको त्रिपक्षीय सम्झौता कार्यान्वयनमा आएको छ।

### User Query (English)
**Q:** What is the total installed electricity generation capacity in Nepal and how much is exported to Bangladesh?

### Generated Answer (English)
**A:** Nepal's total installed power capacity exceeds 3,200 MW, with daily exports up to 650 MW to India in monsoon and an agreement to export 40 MW to Bangladesh.

### Atomic Claims Evaluation

#### Claim 1: `item_032_c1` **[CRITICAL CLAIM]**
> "Nepal's total installed power capacity exceeds 3,200 MW."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_032_c2` **[CRITICAL CLAIM]**
> "Nepal has an agreement to export 40 MW of electricity to Bangladesh."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_032_c3` *[NON-CRITICAL CLAIM]*
> "Nepal exports up to 650 MW of electricity daily to India during the wet season."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_033` (33/120)
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> काठमाडौँ-तराई/मधेश द्रुतमार्ग (फास्ट ट्र्याक) ७२.५ किलोमिटर लामो चार लेनको एक्सप्रेस-वे हो। यस आयोजनामा तीनवटा प्रमुख सुरुङमार्गहरू—निजगढतर्फ लेनडाँडा (१.६१ किमि), धेद्रे (१.६३ किमि) र महादेवडाँडा (३.३५ किमि) निर्माणाधीन छन्। यो आयोजना सम्पन्न भएपछि काठमाडौँबाट निजगढ १ घण्टामा पुग्न सकिनेछ।

### User Query (English)
**Q:** What is the total length of the Kathmandu-Terai Fast Track and how long is the Mahadev Danda tunnel?

### Generated Answer (English)
**A:** The Kathmandu-Terai Fast Track spans 72.5 kilometers as a four-lane expressway, featuring the 3.35 km Mahadev Danda tunnel among its three major tunnels.

### Atomic Claims Evaluation

#### Claim 1: `item_033_c1` **[CRITICAL CLAIM]**
> "The Kathmandu-Terai Fast Track has a total length of 72.5 kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_033_c2` **[CRITICAL CLAIM]**
> "The Mahadev Danda tunnel has a length of 3.35 kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_033_c3` *[NON-CRITICAL CLAIM]*
> "Travel time from Kathmandu to Nijgadh will be reduced to 1 hour upon completion."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_034` (34/120)
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> नेपाल पर्यटन बोर्डका अनुसार सन् २०२३ मा हवाई मार्गबाट नेपाल भित्रिने विदेशी पर्यटकहरूको सङ्ख्या १० लाख १४ हजार ८८२ पुगेको छ। यो सङ्ख्या सन् २०१९ को तुलनामा करिब ८५ प्रतिशतको पुनरुत्थान हो। सबैभन्दा बढी पर्यटक भारत (३ लाख १९ हजार) बाट र त्यसपछि अमेरिका (१ लाख) बाट आएका थिए।

### User Query (English)
**Q:** How many foreign tourists visited Nepal by air in 2023 and which country contributed the highest arrival count?

### Generated Answer (English)
**A:** In 2023, a total of 1,014,882 foreign tourists arrived in Nepal by air, with India contributing the highest arrival count at 319,000 visitors.

### Atomic Claims Evaluation

#### Claim 1: `item_034_c1` **[CRITICAL CLAIM]**
> "Over 1.014 million foreign tourists arrived in Nepal by air in 2023."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_034_c2` **[CRITICAL CLAIM]**
> "India contributed the largest number of tourists with 319,000 visitors."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_034_c3` *[NON-CRITICAL CLAIM]*
> "The 2023 arrival count represented an 85 percent recovery compared to 2019 levels."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_035` (35/120)
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> पोखरा अन्तर्राष्ट्रिय विमानस्थल नेपालको दोस्रो नयाँ अन्तर्राष्ट्रिय विमानस्थल हो, जसको उद्घाटन सन् २०२३ जनवरी १ मा गरिएको थियो। चीनको एक्जिम बैंकको करिब २२ अर्ब रुपैयाँ सहुलियतपूर्ण ऋण सहयोगमा निर्माण गरिएको यो विमानस्थल ४ डी श्रेणीको हो र यसको धावनमार्ग २ हजार ५०० मिटर लामो छ।

### User Query (English)
**Q:** When was Pokhara International Airport inaugurated and what is the length of its runway?

### Generated Answer (English)
**A:** Pokhara International Airport was officially inaugurated on January 1, 2023. Built as a 4D category airport, it features a 2,500-meter-long runway.

### Atomic Claims Evaluation

#### Claim 1: `item_035_c1` **[CRITICAL CLAIM]**
> "Pokhara International Airport was inaugurated on January 1, 2023."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_035_c2` **[CRITICAL CLAIM]**
> "The airport features a 2,500-meter-long runway."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_035_c3` *[NON-CRITICAL CLAIM]*
> "The airport was built with a concessional loan of roughly 22 billion rupees from China's EXIM Bank."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_036` (36/120)
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> गौतम बुद्ध अन्तर्राष्ट्रिय विमानस्थल रूपन्देहीको भैरहवामा अवस्थित छ। सन् २०२२ मे १६ (बुद्ध पूर्णिमा) का दिन उद्घाटन गरिएको यो नेपालको दोस्रो अन्तर्राष्ट्रिय विमानस्थल हो। यस विमानस्थलको धावनमार्ग ३ हजार मिटर लामो छ र यसले वाइडबडी विमानहरू अवतरण गर्न सक्ने क्षमता राख्दछ।

### User Query (English)
**Q:** Where is Gautam Buddha International Airport located and what is its runway length?

### Generated Answer (English)
**A:** Gautam Buddha International Airport is located in Bhairahawa, Rupandehi district, featuring a 3,15-meter runway capable of handling wide-body aircraft.

### Atomic Claims Evaluation

#### Claim 1: `item_036_c1` **[CRITICAL CLAIM]**
> "Gautam Buddha International Airport is situated in Bhairahawa, Rupandehi."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_036_c2` **[CRITICAL CLAIM]**
> "The airport features a 3,000-meter-long runway capable of wide-body landings."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_036_c3` *[NON-CRITICAL CLAIM]*
> "The airport was inaugurated on May 16, 2022 on Buddha Purnima."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_037` (37/120)
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> अरुण तेस्रो जलविद्युत आयोजना (९०० मेगावाट) संखुवासभा जिल्लामा निर्माणाधीन नेपालको ठूलो निर्यातमुखी जलविद्युत आयोजना हो। भारतीय कम्पनी सतलज जलविद्युत निगम (एसजेभीएन) ले निर्माण गरिरहेको यस आयोजनाबाट नेपालले २१.९ प्रतिशत (१९७ मेगावाट) विद्युत निःशुल्क प्राप्त गर्ने सम्झौता छ।

### User Query (English)
**Q:** What is the installed capacity of the Arun-III Hydropower Project and how much free power will Nepal receive?

### Generated Answer (English)
**A:** It is false that the Arun-III Hydropower Project in Sankhuwasabha has an installed capacity of 900 MW, from which Nepal will receive 21.9 percent (197 MW) of generated electricity free of cost.

### Atomic Claims Evaluation

#### Claim 1: `item_037_c1` **[CRITICAL CLAIM]**
> "It is false that arun-III Hydropower Project has an installed capacity of 900 MW."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_037_c2` **[CRITICAL CLAIM]**
> "Nepal will receive 21.9 percent (197 MW) of power free of cost from Arun-III."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_037_c3` *[NON-CRITICAL CLAIM]*
> "The project is being constructed in Sankhuwasabha by SJVN."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_038` (38/120)
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> नागढुंगा-सिस्नेखोला सुरुङमार्गको मुख्य सुरुङको लम्बाई २ हजार ६८८ मिटर रहेको छ। वि.सं. २०८१ वैशाखमा यस सुरुङमार्गको 'ब्रेकथ्रु' भएको थियो। जापान अन्तर्राष्ट्रिय सहयोग नियोग (जाइका) को सहुलियतपूर्ण ऋण सहयोगमा निर्माणाधीन यो सुरुङमार्ग नेपालको पहिलो आधुनिक यातायात सुरुङमार्ग हो।

### User Query (English)
**Q:** What is the length of the Nagdhunga-Sisnekhola main tunnel and which agency provided financial assistance?

### Generated Answer (English)
**A:** According to the Asian Development Bank, the Nagdhunga-Sisnekhola main tunnel spans 2,688 meters as Nepal's first modern transport tunnel, funded through concessional loan assistance from JICA.

### Atomic Claims Evaluation

#### Claim 1: `item_038_c1` **[CRITICAL CLAIM]**
> "According to the Asian Development Bank, the Nagdhunga-Sisnekhola main tunnel has a length of 2,688 meters."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_038_c2` **[CRITICAL CLAIM]**
> "The project is funded by concessional loan assistance from JICA."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_038_c3` *[NON-CRITICAL CLAIM]*
> "The main tunnel breakthrough occurred in Baisakh 2081 BS."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_039` (39/120)
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> भेरी-बबई डाइभर्सन बहुउद्देश्यीय आयोजना नेपालको पहिलो अन्तर-जलाधार जल स्थानान्तरण आयोजना हो। टनेल बोरिङ मेसिन (टीबीएम) प्रयोग गरी निर्माण गरिएको १२.२ किलोमिटर लामो सुरुङमार्फत भेरी नदीको पानी बबई नदीमा खसालेर बाँके र बर्दियाको ५१ हजार हेक्टर जमिनमा सिँचाइ र ४८ मेगावाट विद्युत उत्पादन गर्ने लक्ष्य छ।

### User Query (English)
**Q:** How long is the tunnel of the Bheri-Babai Diversion Project and what technology was used to bore it?

### Generated Answer (English)
**A:** The respective authorities and multiple delegates Bheri-Babai Diversion Project features a 12.2-kilometer tunnel bored using a Tunnel Boring Machine (TBM), transferring water to irrigate 51,000 hectares and generate 48 MW of power.

### Atomic Claims Evaluation

#### Claim 1: `item_039_c1` **[CRITICAL CLAIM]**
> "The respective authorities and multiple delegates Bheri-Babai Diversion tunnel has a length of 12.2 kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_039_c2` **[CRITICAL CLAIM]**
> "The tunnel was constructed using a Tunnel Boring Machine (TBM)."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_039_c3` *[NON-CRITICAL CLAIM]*
> "The project aims to irrigate 51,000 hectares and generate 48 MW of electricity."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_040` (40/120)
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> माथिल्लो तामाकोशी जलविद्युत आयोजना (४५६ मेगावाट) नेपालको आफ्नै स्रोत र साधनमा निर्माण भएको सबैभन्दा ठूलो जलविद्युत आयोजना हो। दोलखा जिल्लाको लामाबगरमा अवस्थित यस आयोजनाले वि.सं. २०७८ असारमा व्यावसायिक उत्पादन सुरु गरेको थियो। यस आयोजनाको भूमिगत विद्युतगृहमा ७६ मेगावाटका ६ वटा टर्बाइनहरू जडान गरिएका छन्।

### User Query (English)
**Q:** What is the installed capacity and location of the Upper Tamakoshi Hydropower Project?

### Generated Answer (English)
**A:** Upper Tamakoshi Hydropower Project has an installed capacity of 456 megawatts located at Lamabagar in Dolakha district, operating six 76 MW turbines in its underground powerhouse. Furthermore, preliminary feasibility studies were conducted by Japanese engineering consultants.

### Atomic Claims Evaluation

#### Claim 1: `item_040_c1` **[CRITICAL CLAIM]**
> "Upper Tamakoshi Hydropower Project has an installed capacity of 456 MW. Furthermore, preliminary feasibility studies were conducted by Japanese engineering consultants."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_040_c2` **[CRITICAL CLAIM]**
> "The project is located at Lamabagar in Dolakha district."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_040_c3` *[NON-CRITICAL CLAIM]*
> "Its underground powerhouse is equipped with six 76 MW turbines."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_041` (41/120)
**Domain:** government_report | **Topic Sub-Genre:** health

### Context Passage (Nepali · Condition C1)
> नेपाल स्वास्थ्य अनुसन्धान परिषद्का अनुसार नेपालमा नसर्ने रोगहरूको प्रकोप तीव्र रूपमा बढ्दै गएको छ। कुल मृत्युमध्ये करिब ७१ प्रतिशत नसर्ने रोगहरू (मुटुरोग, क्यान्सर, मधुमेह र श्वासप्रश्वास सम्बन्धी रोग) का कारण हुने गरेको छ। यसैगरी उच्च रक्तचापका बिरामीहरूको सङ्ख्या कुल वयस्क जनसङ्ख्याको ३० प्रतिशतभन्दा बढी पुगेको स्वास्थ्य मन्त्रालयको पछिल्लो सर्वेक्षणले देखाएको छ।

### User Query (English)
**Q:** What percentage of total deaths in Nepal are caused by non-communicable diseases, and what is the prevalence of hypertension among adults?

### Generated Answer (English)
**A:** According to the Nepal Health Research Council, non-communicable diseases account for approximately 71 percent of all deaths in Nepal. Furthermore, recent Ministry of Health surveys show that over 30 percent of the adult population suffers from hypertension.

### Atomic Claims Evaluation

#### Claim 1: `item_041_c1` **[CRITICAL CLAIM]**
> "Non-communicable diseases account for approximately 71 percent of all deaths in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_041_c2` **[CRITICAL CLAIM]**
> "Over 30 percent of the adult population in Nepal suffers from hypertension."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_041_c3` *[NON-CRITICAL CLAIM]*
> "The findings are reported by the Nepal Health Research Council and Ministry of Health."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_042` (42/120)
**Domain:** government_report | **Topic Sub-Genre:** health

### Context Passage (Nepali · Condition C1)
> स्वास्थ्य सेवा विभागको खोप शाखाका अनुसार नेपालमा बाल मृत्युदर घटाउन नियमित १२ प्रकारका खोपहरू निःशुल्क उपलब्ध गराइएका छन्। यस कार्यक्रमले दादुरा-रुबेला र पोलियो रोग निवारणमा उल्लेख्य सफलता हासिल गरेको छ। सन् २०२३ को तथ्याङ्क अनुसार पूर्ण खोप पाउने बालबालिकाको राष्ट्रिय कभरेज ८८ प्रतिशत पुगेको छ।

### User Query (English)
**Q:** How many free routine vaccines are provided in Nepal for children, and what was the national full vaccination coverage in 2023?

### Generated Answer (English)
**A:** The Department of Health Services provides 12 types of routine childhood vaccines free of charge. In 2023, the national coverage of fully vaccinated children reached 88 percent.

### Atomic Claims Evaluation

#### Claim 1: `item_042_c1` **[CRITICAL CLAIM]**
> "Nepal provides 12 routine childhood vaccines free of charge."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_042_c2` **[CRITICAL CLAIM]**
> "National coverage of fully vaccinated children reached 88 percent in 2023."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_042_c3` *[NON-CRITICAL CLAIM]*
> "The routine immunization program has contributed to reducing child mortality."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_043` (43/120)
**Domain:** government_report | **Topic Sub-Genre:** health

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय एड्स तथा यौनरोग नियन्त्रण केन्द्रका अनुसार नेपालमा सन् २०२२ को अन्त्यसम्ममा अनुमानित ३० हजार मानिसमा एचआईभी सङ्क्रमण रहेको पाइएको छ। तीमध्ये करिब ७८ प्रतिशत सङ्क्रमितहरूले एन्टिरेट्रोभाइरल (एआरभी) उपचार प्राप्त गरिरहेका छन्। नयाँ सङ्क्रमण दरमा अघिल्लो दशकको तुलनामा ६० प्रतिशतले गिरावट आएको छ।

### User Query (English)
**Q:** What was the estimated number of people living with HIV in Nepal by end of 2022, and what percentage received antiretroviral treatment?

### Generated Answer (English)
**A:** By the end of 2022, an estimated 30,000 people were living with HIV in Nepal. Among them, approximately 78 percent were receiving antiretroviral therapy, and new infections declined by 60 percent compared to the previous decade.

### Atomic Claims Evaluation

#### Claim 1: `item_043_c1` **[CRITICAL CLAIM]**
> "An estimated 30,000 people were living with HIV in Nepal by late 2022."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_043_c2` **[CRITICAL CLAIM]**
> "Approximately 78 percent of HIV-infected individuals were receiving antiretroviral treatment."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_043_c3` *[NON-CRITICAL CLAIM]*
> "New HIV infections in Nepal declined by 60 percent compared to the previous decade."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_044` (44/120)
**Domain:** government_report | **Topic Sub-Genre:** health

### Context Passage (Nepali · Condition C1)
> नेपाल जनसाङ्ख्यिक तथा स्वास्थ्य सर्वेक्षण (एनडीएचएस २०२२) अनुसार पाँच वर्ष मुनिका बालबालिकामा पुड्कोपनको दर २५ प्रतिशतमा झरेको छ। सन् २००१ मा यो दर ५७ प्रतिशत रहेको थियो। त्यस्तै कम तौल भएका बालबालिकाको सङ्ख्या १९ प्रतिशत र ख्याउटेपनको दर ८ प्रतिशत रहेको प्रतिवेदनमा उल्लेख छ।

### User Query (English)
**Q:** According to NDHS 2022, what is the prevalence of stunting in children under five in Nepal?

### Generated Answer (English)
**A:** According to the Nepal Demographic and Health Survey 2022, stunting among children under five dropped to 25 percent from 57 percent in 2001. Additionally, 19 percent are underweight and 8 percent suffer from wasting.

### Atomic Claims Evaluation

#### Claim 1: `item_044_c1` **[CRITICAL CLAIM]**
> "Stunting among children under five dropped to 25 percent according to NDHS 2022."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_044_c2` *[NON-CRITICAL CLAIM]*
> "The stunting rate in children under five was 57 percent in 2001."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_044_c3` **[CRITICAL CLAIM]**
> "The NDHS 2022 recorded an underweight rate of 19 percent and wasting rate of 8 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_045` (45/120)
**Domain:** government_report | **Topic Sub-Genre:** health

### Context Passage (Nepali · Condition C1)
> काठमाडौँ उपत्यकामा पछिल्लो वर्ष डेंगु सङ्क्रमणका कारण १५ जनाको मृत्यु भएको छ भने २० हजारभन्दा बढी व्यक्तिहरू प्रभावित भएका छन्। इपिडिमियोलोजी तथा रोग नियन्त्रण महाशाखा (ईडीसीडी) ले लामखुट्टेको लार्भा नष्ट गर्ने 'खोज र नष्ट गर' अभियान ७७ वटै जिल्लामा सञ्चालन गरिएको जानकारी दिएको छ।

### User Query (English)
**Q:** How many dengue deaths occurred in Kathmandu Valley in the recent outbreak and what campaign was launched?

### Generated Answer (English)
**A:** In the recent outbreak in Kathmandu Valley, 15 people died and over 20,000 were infected with dengue. In response, EDCD conducted a search-and-destroy campaign to eliminate mosquito larvae across all 77 districts.

### Atomic Claims Evaluation

#### Claim 1: `item_045_c1` **[CRITICAL CLAIM]**
> "15 people died of dengue in Kathmandu Valley during the recent outbreak."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_045_c2` **[CRITICAL CLAIM]**
> "Over 20,000 people in Kathmandu Valley were infected with dengue."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_045_c3` *[NON-CRITICAL CLAIM]*
> "EDCD conducted a search-and-destroy campaign across all 77 districts."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_046` (46/120)
**Domain:** government_report | **Topic Sub-Genre:** health

### Context Passage (Nepali · Condition C1)
> नेपाल स्वास्थ्य अनुसन्धान परिषद्का अनुसार नेपालमा नसर्ने रोगहरूको प्रकोप तीव्र रूपमा बढ्दै गएको छ। कुल मृत्युमध्ये करिब ७१ प्रतिशत नसर्ने रोगहरू (मुटुरोग, क्यान्सर, मधुमेह र श्वासप्रश्वास सम्बन्धी रोग) का कारण हुने गरेको छ। यसैगरी उच्च रक्तचापका बिरामीहरूको सङ्ख्या कुल वयस्क जनसङ्ख्याको ३० प्रतिशतभन्दा बढी पुगेको स्वास्थ्य मन्त्रालयको पछिल्लो सर्वेक्षणले देखाएको छ।

### User Query (English)
**Q:** What percentage of total deaths in Nepal are caused by non-communicable diseases, and what is the prevalence of hypertension among adults?

### Generated Answer (English)
**A:** According to the Nepal Health Research Council, non-communicable diseases account for approximately 71 percent of all deaths in Nepal, as a direct consequence of which furthermore, recent Ministry of Health surveys show that over 30 percent of the adult population suffers from hypertension.

### Atomic Claims Evaluation

#### Claim 1: `item_046_c1` **[CRITICAL CLAIM]**
> "Non-communicable diseases account for approximately 71 percent of all deaths in Nepal, directly leading to an unprecedented national crisis."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_046_c2` **[CRITICAL CLAIM]**
> "Over 30 percent of the adult population in Nepal suffers from hypertension."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_046_c3` *[NON-CRITICAL CLAIM]*
> "The findings are reported by the Nepal Health Research Council and Ministry of Health."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_047` (47/120)
**Domain:** government_report | **Topic Sub-Genre:** health

### Context Passage (Nepali · Condition C1)
> स्वास्थ्य सेवा विभागको खोप शाखाका अनुसार नेपालमा बाल मृत्युदर घटाउन नियमित १२ प्रकारका खोपहरू निःशुल्क उपलब्ध गराइएका छन्। यस कार्यक्रमले दादुरा-रुबेला र पोलियो रोग निवारणमा उल्लेख्य सफलता हासिल गरेको छ। सन् २०२३ को तथ्याङ्क अनुसार पूर्ण खोप पाउने बालबालिकाको राष्ट्रिय कभरेज ८८ प्रतिशत पुगेको छ।

### User Query (English)
**Q:** How many free routine vaccines are provided in Nepal for children, and what was the national full vaccination coverage in 2023?

### Generated Answer (English)
**A:** The Department of Health Services provides 12 types of routine childhood vaccines free of charge. In 2023, the national coverage of fully vaccinated children reached 88 percent.

### Atomic Claims Evaluation

#### Claim 1: `item_047_c1` **[CRITICAL CLAIM]**
> "Bhutan provides 12 routine childhood vaccines free of charge."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_047_c2` **[CRITICAL CLAIM]**
> "National coverage of fully vaccinated children reached 88 percent in 2023."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_047_c3` *[NON-CRITICAL CLAIM]*
> "The routine immunization program has contributed to reducing child mortality."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_048` (48/120)
**Domain:** government_report | **Topic Sub-Genre:** health

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय एड्स तथा यौनरोग नियन्त्रण केन्द्रका अनुसार नेपालमा सन् २०२२ को अन्त्यसम्ममा अनुमानित ३० हजार मानिसमा एचआईभी सङ्क्रमण रहेको पाइएको छ। तीमध्ये करिब ७८ प्रतिशत सङ्क्रमितहरूले एन्टिरेट्रोभाइरल (एआरभी) उपचार प्राप्त गरिरहेका छन्। नयाँ सङ्क्रमण दरमा अघिल्लो दशकको तुलनामा ६० प्रतिशतले गिरावट आएको छ।

### User Query (English)
**Q:** What was the estimated number of people living with HIV in Nepal by end of 2022, and what percentage received antiretroviral treatment?

### Generated Answer (English)
**A:** By the end of 2022, an estimated 30,000 people were living with HIV in Nepal. Among them, approximately 78 percent were receiving antiretroviral therapy, and new infections declined by 110 percent compared to the previous decade.

### Atomic Claims Evaluation

#### Claim 1: `item_048_c1` **[CRITICAL CLAIM]**
> "An estimated 30,000 people were living with HIV in Nepal by late 2018."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_048_c2` **[CRITICAL CLAIM]**
> "Approximately 78 percent of HIV-infected individuals were receiving antiretroviral treatment."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_048_c3` *[NON-CRITICAL CLAIM]*
> "New HIV infections in Nepal declined by 60 percent compared to the previous decade."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_049` (49/120)
**Domain:** government_report | **Topic Sub-Genre:** health

### Context Passage (Nepali · Condition C1)
> नेपाल जनसाङ्ख्यिक तथा स्वास्थ्य सर्वेक्षण (एनडीएचएस २०२२) अनुसार पाँच वर्ष मुनिका बालबालिकामा पुड्कोपनको दर २५ प्रतिशतमा झरेको छ। सन् २००१ मा यो दर ५७ प्रतिशत रहेको थियो। त्यस्तै कम तौल भएका बालबालिकाको सङ्ख्या १९ प्रतिशत र ख्याउटेपनको दर ८ प्रतिशत रहेको प्रतिवेदनमा उल्लेख छ।

### User Query (English)
**Q:** According to NDHS 2022, what is the prevalence of stunting in children under five in Nepal?

### Generated Answer (English)
**A:** According to the Nepal Demographic and Health Survey 2022, stunting among children under five dropped to 25 percent from 57 percent in 2001. Additionally, 19 percent are not underweight and 8 percent suffer from wasting.

### Atomic Claims Evaluation

#### Claim 1: `item_049_c1` **[CRITICAL CLAIM]**
> "It is false that stunting among children under five dropped to 25 percent according to NDHS 2022."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_049_c2` *[NON-CRITICAL CLAIM]*
> "The stunting rate in children under five was 57 percent in 2001."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_049_c3` **[CRITICAL CLAIM]**
> "The NDHS 2022 recorded an underweight rate of 19 percent and wasting rate of 8 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_050` (50/120)
**Domain:** government_report | **Topic Sub-Genre:** health

### Context Passage (Nepali · Condition C1)
> काठमाडौँ उपत्यकामा पछिल्लो वर्ष डेंगु सङ्क्रमणका कारण १५ जनाको मृत्यु भएको छ भने २० हजारभन्दा बढी व्यक्तिहरू प्रभावित भएका छन्। इपिडिमियोलोजी तथा रोग नियन्त्रण महाशाखा (ईडीसीडी) ले लामखुट्टेको लार्भा नष्ट गर्ने 'खोज र नष्ट गर' अभियान ७७ वटै जिल्लामा सञ्चालन गरिएको जानकारी दिएको छ।

### User Query (English)
**Q:** How many dengue deaths occurred in Kathmandu Valley in the recent outbreak and what campaign was launched?

### Generated Answer (English)
**A:** According to the Asian Development Bank, in the recent outbreak in Kathmandu Valley, 15 people died and over 20,000 were infected with dengue. In response, EDCD conducted a search-and-destroy campaign to eliminate mosquito larvae across all 77 districts.

### Atomic Claims Evaluation

#### Claim 1: `item_050_c1` **[CRITICAL CLAIM]**
> "According to the Asian Development Bank, 15 people died of dengue in Kathmandu Valley during the recent outbreak."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_050_c2` **[CRITICAL CLAIM]**
> "Over 20,000 people in Kathmandu Valley were infected with dengue."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_050_c3` *[NON-CRITICAL CLAIM]*
> "EDCD conducted a search-and-destroy campaign across all 77 districts."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_051` (51/120)
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### Context Passage (Nepali · Condition C1)
> कृषि तथा पशुपन्छी विकास मन्त्रालयका अनुसार आर्थिक वर्ष २०८०/८१ मा नेपालमा कुल ५७ लाख मेट्रिक टन धान उत्पादन भएको छ, जुन अघिल्लो वर्षको तुलनामा ४.३ प्रतिशतले बढी हो। धान खेती गरिएको कुल क्षेत्रफल १४ लाख ३८ हजार हेक्टर रहेको थियो। उन्नत जातको बीउ र रासायनिक मलको समयमै उपलब्धताका कारण उत्पादकत्व ३.९८ मेट्रिक टन प्रति हेक्टर पुगेको छ।

### User Query (English)
**Q:** What was the total paddy production in Nepal in FY 2080/81 and what productivity was achieved?

### Generated Answer (English)
**A:** In FY 2080/81, Nepal produced 5.7 million metric tons of paddy across 1.438 million hectares, representing a 4.3 percent increase from the previous year. Productivity reached 3.98 metric tons per hectare.

### Atomic Claims Evaluation

#### Claim 1: `item_051_c1` **[CRITICAL CLAIM]**
> "Nepal produced 5.7 million metric tons of paddy in FY 2080/81."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_051_c2` *[NON-CRITICAL CLAIM]*
> "Paddy was cultivated across 1.438 million hectares in FY 2080/81."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_051_c3` **[CRITICAL CLAIM]**
> "Paddy productivity reached 3.98 metric tons per hectare."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_052` (52/120)
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय कृषि गणना २०७८ अनुसार नेपालमा कृषक परिवारको सङ्ख्या ४१ लाख ३० हजार पुगेको छ। कुल खेतीयोग्य जमिनमध्ये ५४.५ प्रतिशत जमिनमा मात्र सिँचाइ सुविधा पुगेको छ। त्यसमध्ये बाह्रै महिना सिँचाइ सुविधा उपलब्ध भएको जमिन कुल सिञ्चित जमिनको ३९ प्रतिशत मात्र रहेको छ।

### User Query (English)
**Q:** According to the National Agricultural Census 2078, what is the number of farming households and irrigation coverage in Nepal?

### Generated Answer (English)
**A:** The National Agricultural Census 2078 indicates there are 4.13 million farming households in Nepal. Irrigation facilities reach only 54.5 percent of cultivable land, with year-round irrigation available on just 39 percent of irrigated land.

### Atomic Claims Evaluation

#### Claim 1: `item_052_c1` **[CRITICAL CLAIM]**
> "There are 4.13 million farming households in Nepal according to Census 2078."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_052_c2` **[CRITICAL CLAIM]**
> "Irrigation facilities cover 54.5 percent of cultivable land."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_052_c3` *[NON-CRITICAL CLAIM]*
> "Year-round irrigation is accessible on 39 percent of irrigated agricultural land."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_053` (53/120)
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### Context Passage (Nepali · Condition C1)
> नेपालबाट भारततर्फ अलैँची र अदुवा निर्यातमा उल्लेख्य वृद्धि भएको छ। व्यापार तथा निकासी प्रवर्द्धन केन्द्रका अनुसार गत वर्ष करिब ८ अर्ब रुपैयाँ बराबरको ठूलो अलैँची निर्यात भएको थियो। ताप्लेजुङ, पाँचथर र इलाम जिल्ला नेपालको प्रमुख अलैँची उत्पादन क्षेत्र हुन्।

### User Query (English)
**Q:** What was the export value of large cardamom from Nepal and which districts are the primary production zones?

### Generated Answer (English)
**A:** Nepal exported approximately 8 billion rupees worth of large cardamom last year. The primary production areas are Taplejung, Panchthar, and Ilam districts.

### Atomic Claims Evaluation

#### Claim 1: `item_053_c1` **[CRITICAL CLAIM]**
> "Nepal exported approximately 8 billion rupees worth of large cardamom last year."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_053_c2` **[CRITICAL CLAIM]**
> "Taplejung, Panchthar, and Ilam are the primary cardamom-producing districts in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_054` (54/120)
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### Context Passage (Nepali · Condition C1)
> नेपालमा सामुदायिक वन उपभोक्ता समूहहरूको सङ्ख्या २२ हजार २६६ पुगेको छ। यी समूहहरूले करिब २४ लाख हेक्टर राष्ट्रिय वन संरक्षण र व्यवस्थापन गरिरहेका छन्। सामुदायिक वन व्यवस्थापनबाट ३३ लाखभन्दा बढी घरधुरी प्रत्यक्ष रूपमा लाभान्वित भएका छन्।

### User Query (English)
**Q:** How many community forest user groups exist in Nepal and how much forest land do they manage?

### Generated Answer (English)
**A:** Nepal has 22,266 community forest user groups managing approximately 2.4 million hectares of national forest, benefiting over 3.3 million households directly.

### Atomic Claims Evaluation

#### Claim 1: `item_054_c1` **[CRITICAL CLAIM]**
> "Nepal has 22,266 community forest user groups."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_054_c2` **[CRITICAL CLAIM]**
> "Community forest user groups manage approximately 2.4 million hectares of forest land."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_054_c3` *[NON-CRITICAL CLAIM]*
> "Over 3.3 million households benefit directly from community forestry management."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_055` (55/120)
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### Context Passage (Nepali · Condition C1)
> मकै नेपालको दोस्रो प्रमुख खाद्यान्न बाली हो। आर्थिक वर्ष २०७९/८० मा नेपालमा मकैको कुल उत्पादन ३० लाख मेट्रिक टन भएको थियो। पहाडी जिल्लाहरूमा मकै खेती कुल मकै उत्पादन क्षेत्रको ७० प्रतिशतभन्दा बढी ओगटेको छ।

### User Query (English)
**Q:** What is the ranking and production volume of maize in Nepal?

### Generated Answer (English)
**A:** Maize is Nepal's second major food crop, with total production reaching 3.0 million metric tons in FY 2079/80, where hilly districts account for over 70 percent of maize cultivation.

### Atomic Claims Evaluation

#### Claim 1: `item_055_c1` **[CRITICAL CLAIM]**
> "Maize is the second major food crop in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_055_c2` **[CRITICAL CLAIM]**
> "Total maize production reached 3.0 million metric tons in FY 2079/80."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_055_c3` *[NON-CRITICAL CLAIM]*
> "Hilly districts account for over 70 percent of Nepal's maize cultivation area."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_056` (56/120)
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### Context Passage (Nepali · Condition C1)
> कृषि तथा पशुपन्छी विकास मन्त्रालयका अनुसार आर्थिक वर्ष २०८०/८१ मा नेपालमा कुल ५७ लाख मेट्रिक टन धान उत्पादन भएको छ, जुन अघिल्लो वर्षको तुलनामा ४.३ प्रतिशतले बढी हो। धान खेती गरिएको कुल क्षेत्रफल १४ लाख ३८ हजार हेक्टर रहेको थियो। उन्नत जातको बीउ र रासायनिक मलको समयमै उपलब्धताका कारण उत्पादकत्व ३.९८ मेट्रिक टन प्रति हेक्टर पुगेको छ।

### User Query (English)
**Q:** What was the total paddy production in Nepal in FY 2080/81 and what productivity was achieved?

### Generated Answer (English)
**A:** The respective authorities and multiple delegates FY 2080/81, Nepal produced 5.7 million metric tons of paddy across 1.438 million hectares, representing a 4.3 percent increase from the previous year. Productivity reached 3.98 metric tons per hectare.

### Atomic Claims Evaluation

#### Claim 1: `item_056_c1` **[CRITICAL CLAIM]**
> "The respective authorities and multiple delegates produced 5.7 million metric tons of paddy in FY 2080/81."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_056_c2` *[NON-CRITICAL CLAIM]*
> "Paddy was cultivated across 1.438 million hectares in FY 2080/81."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_056_c3` **[CRITICAL CLAIM]**
> "Paddy productivity reached 3.98 metric tons per hectare."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_057` (57/120)
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय कृषि गणना २०७८ अनुसार नेपालमा कृषक परिवारको सङ्ख्या ४१ लाख ३० हजार पुगेको छ। कुल खेतीयोग्य जमिनमध्ये ५४.५ प्रतिशत जमिनमा मात्र सिँचाइ सुविधा पुगेको छ। त्यसमध्ये बाह्रै महिना सिँचाइ सुविधा उपलब्ध भएको जमिन कुल सिञ्चित जमिनको ३९ प्रतिशत मात्र रहेको छ।

### User Query (English)
**Q:** According to the National Agricultural Census 2078, what is the number of farming households and irrigation coverage in Nepal?

### Generated Answer (English)
**A:** The National Agricultural Census 2078 indicates there are 4.13 million farming households in Nepal. Irrigation facilities reach only 54.5 percent of cultivable land, with year-round irrigation available on just 39 percent of irrigated land. Furthermore, the initiative was financed through a low-interest loan from the Asian Development Bank.

### Atomic Claims Evaluation

#### Claim 1: `item_057_c1` **[CRITICAL CLAIM]**
> "There are 4.13 million farming households in Nepal according to Census 2078. Furthermore, the initiative was financed through a low-interest loan from the Asian Development Bank."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_057_c2` **[CRITICAL CLAIM]**
> "Irrigation facilities cover 54.5 percent of cultivable land."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_057_c3` *[NON-CRITICAL CLAIM]*
> "Year-round irrigation is accessible on 39 percent of irrigated agricultural land."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_058` (58/120)
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### Context Passage (Nepali · Condition C1)
> नेपालबाट भारततर्फ अलैँची र अदुवा निर्यातमा उल्लेख्य वृद्धि भएको छ। व्यापार तथा निकासी प्रवर्द्धन केन्द्रका अनुसार गत वर्ष करिब ८ अर्ब रुपैयाँ बराबरको ठूलो अलैँची निर्यात भएको थियो। ताप्लेजुङ, पाँचथर र इलाम जिल्ला नेपालको प्रमुख अलैँची उत्पादन क्षेत्र हुन्।

### User Query (English)
**Q:** What was the export value of large cardamom from Nepal and which districts are the primary production zones?

### Generated Answer (English)
**A:** Nepal exported approximately 8 billion rupees worth of large cardamom last year, primarily because the primary production areas are Taplejung, Panchthar, and Ilam districts.

### Atomic Claims Evaluation

#### Claim 1: `item_058_c1` **[CRITICAL CLAIM]**
> "Nepal exported approximately 8 billion rupees worth of large cardamom last year, directly leading to an unprecedented national crisis."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_058_c2` **[CRITICAL CLAIM]**
> "Taplejung, Panchthar, and Ilam are the primary cardamom-producing districts in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_059` (59/120)
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### Context Passage (Nepali · Condition C1)
> नेपालमा सामुदायिक वन उपभोक्ता समूहहरूको सङ्ख्या २२ हजार २६६ पुगेको छ। यी समूहहरूले करिब २४ लाख हेक्टर राष्ट्रिय वन संरक्षण र व्यवस्थापन गरिरहेका छन्। सामुदायिक वन व्यवस्थापनबाट ३३ लाखभन्दा बढी घरधुरी प्रत्यक्ष रूपमा लाभान्वित भएका छन्।

### User Query (English)
**Q:** How many community forest user groups exist in Nepal and how much forest land do they manage?

### Generated Answer (English)
**A:** Bhutan has 22,266 community forest user groups managing approximately 2.4 million hectares of national forest, benefiting over 3.3 million households directly.

### Atomic Claims Evaluation

#### Claim 1: `item_059_c1` **[CRITICAL CLAIM]**
> "Bhutan has 22,266 community forest user groups."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_059_c2` **[CRITICAL CLAIM]**
> "Community forest user groups manage approximately 2.4 million hectares of forest land."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_059_c3` *[NON-CRITICAL CLAIM]*
> "Over 3.3 million households benefit directly from community forestry management."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_060` (60/120)
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### Context Passage (Nepali · Condition C1)
> मकै नेपालको दोस्रो प्रमुख खाद्यान्न बाली हो। आर्थिक वर्ष २०७९/८० मा नेपालमा मकैको कुल उत्पादन ३० लाख मेट्रिक टन भएको थियो। पहाडी जिल्लाहरूमा मकै खेती कुल मकै उत्पादन क्षेत्रको ७० प्रतिशतभन्दा बढी ओगटेको छ।

### User Query (English)
**Q:** What is the ranking and production volume of maize in Nepal?

### Generated Answer (English)
**A:** Maize is Nepal's second major food crop, with total production reaching 3.0 million metric tons in FY 2079/130, where hilly districts account for over 70 percent of maize cultivation.

### Atomic Claims Evaluation

#### Claim 1: `item_060_c1` **[CRITICAL CLAIM]**
> "Maize is the second major food crop in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_060_c2` **[CRITICAL CLAIM]**
> "Total maize production reached 3.0 million metric tons in FY 2079/80."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_060_c3` *[NON-CRITICAL CLAIM]*
> "Hilly districts account for over 70 percent of Nepal's maize cultivation area."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_061` (61/120)
**Domain:** government_report | **Topic Sub-Genre:** education

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय जनगणना २०७८ अनुसार नेपालको समग्र साक्षरता दर ७६.३ प्रतिशत पुगेको छ। पुरुष साक्षरता दर ८३.६ प्रतिशत र महिला साक्षरता दर ६९.४ प्रतिशत रहेको छ। प्रदेशगत रूपमा बागमती प्रदेशमा सबैभन्दा बढी (८२.१ प्रतिशत) र मधेश प्रदेशमा सबैभन्दा कम (६३.५ प्रतिशत) साक्षरता दर पाइएको छ।

### User Query (English)
**Q:** What is the national literacy rate in Nepal according to the 2078 Census, and which province has the lowest rate?

### Generated Answer (English)
**A:** According to the 2078 National Census, Nepal's overall literacy rate is 76.3 percent, with male literacy at 83.6 percent and female literacy at 69.4 percent. Madhesh Province has the lowest literacy rate at 63.5 percent.

### Atomic Claims Evaluation

#### Claim 1: `item_061_c1` **[CRITICAL CLAIM]**
> "Nepal's overall literacy rate reached 76.3 percent in the 2078 Census."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_061_c2` *[NON-CRITICAL CLAIM]*
> "Male literacy is 83.6 percent and female literacy is 69.4 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_061_c3` **[CRITICAL CLAIM]**
> "Madhesh Province recorded the lowest literacy rate at 63.5 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_062` (62/120)
**Domain:** government_report | **Topic Sub-Genre:** education

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय परीक्षा बोर्डले सार्वजनिक गरेको वि.सं. २०८० को माध्यमिक शिक्षा परीक्षा (एसईई) को नतिजा अनुसार नियमित तर्फ सम्मिलित ४ लाख ६४ हजार ७८५ विद्यार्थीमध्ये ४७.८६ प्रतिशत मात्र उत्तीर्ण भएका छन्। नयाँ लेटर ग्रेडिङ निर्देशिका अनुसार सैद्धान्तिकतर्फ कम्तीमा ३५ प्रतिशत अंक नल्याउने विद्यार्थीलाई नन-ग्रेडेड (एनजी) मा राखिएको छ।

### User Query (English)
**Q:** What was the pass rate in the 2080 SEE examination and what criterion triggers a non-graded evaluation?

### Generated Answer (English)
**A:** In the 2080 SEE examination, only 47.86 percent of 464,785 regular students passed. Under the new grading directive, students scoring below 35 percent in theoretical exams are classified as Non-Graded (NG).

### Atomic Claims Evaluation

#### Claim 1: `item_062_c1` **[CRITICAL CLAIM]**
> "Only 47.86 percent of students passed the 2080 regular SEE examination."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_062_c2` *[NON-CRITICAL CLAIM]*
> "A total of 464,785 regular students appeared in the 2080 SEE exam."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_062_c3` **[CRITICAL CLAIM]**
> "Students scoring below 35 percent in theoretical exams receive a Non-Graded (NG) mark."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_063` (63/120)
**Domain:** government_report | **Topic Sub-Genre:** education

### Context Passage (Nepali · Condition C1)
> शिक्षा तथा मानव स्रोत विकास केन्द्रको तथ्याङ्क अनुसार आधारभूत तह (कक्षा १-८) मा खुद भर्ना दर ९५.२ प्रतिशत पुगेको छ। तर माध्यमिक तह (कक्षा ९-१२) मा खुद भर्ना दर ५४.३ प्रतिशत मात्र रहेको छ। कक्षा ८ सम्म पुग्दा ड्रपआउट दर करिब १५ प्रतिशत रहेको छ।

### User Query (English)
**Q:** What are the net enrollment rates at basic and secondary levels in Nepal?

### Generated Answer (English)
**A:** At the basic level (grades 1-8), Nepal's net enrollment rate is 95.2 percent, whereas at the secondary level (grades 9-12), it drops to 54.3 percent. The dropout rate reaches approximately 15 percent by grade 8.

### Atomic Claims Evaluation

#### Claim 1: `item_063_c1` **[CRITICAL CLAIM]**
> "Net enrollment rate at the basic level is 95.2 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_063_c2` **[CRITICAL CLAIM]**
> "Net enrollment rate at the secondary level is 54.3 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_063_c3` *[NON-CRITICAL CLAIM]*
> "Student dropout rate reaches roughly 15 percent by grade 8."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_064` (64/120)
**Domain:** government_report | **Topic Sub-Genre:** education

### Context Passage (Nepali · Condition C1)
> त्रिभुवन विश्वविद्यालय नेपालको सबैभन्दा पुरानो र ठूलो विश्वविद्यालय हो, जसको स्थापना वि.सं. २०१६ मा भएको थियो। त्रिवि अन्तर्गत हाल ६२ वटा आंगिक क्याम्पस र १ हजारभन्दा बढी सम्बन्धन प्राप्त क्याम्पसहरू सञ्चालनमा छन्। नेपालमा उच्च शिक्षा अध्ययन गर्ने कुल विद्यार्थीमध्ये करिब ७५ प्रतिशत त्रिविमै अध्ययनरत छन्।

### User Query (English)
**Q:** When was Tribhuvan University established and what share of higher education students in Nepal does it enroll?

### Generated Answer (English)
**A:** Tribhuvan University was established in 2016 BS (1959 AD) and operates 62 constituent campuses along with over 1,000 affiliated colleges, enrolling around 75 percent of all higher education students in Nepal.

### Atomic Claims Evaluation

#### Claim 1: `item_064_c1` **[CRITICAL CLAIM]**
> "Tribhuvan University was established in 2016 BS."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_064_c2` **[CRITICAL CLAIM]**
> "TU enrolls approximately 75 percent of all higher education students in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_064_c3` *[NON-CRITICAL CLAIM]*
> "TU has 62 constituent campuses and over 1,000 affiliated colleges."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_065` (65/120)
**Domain:** government_report | **Topic Sub-Genre:** education

### Context Passage (Nepali · Condition C1)
> नेपाल सरकारले प्राविधिक तथा व्यावसायिक शिक्षा एवं तालिम परिषद् (सीटीईभीटी) मार्फत देशभरका ७५३ वटै स्थानीय तहमा प्राविधिक शिक्षा विस्तार गर्ने नीति लिएको छ। हालसम्म ६५० भन्दा बढी स्थानीय तहमा प्राविधिक धारका विद्यालयहरू स्थापना भइसकेका छन्।

### User Query (English)
**Q:** How many local levels in Nepal have technical education schools established under CTEVT?

### Generated Answer (English)
**A:** The government aims to expand technical education across all 753 local levels through CTEVT, with technical schools already established in more than 650 local bodies.

### Atomic Claims Evaluation

#### Claim 1: `item_065_c1` *[NON-CRITICAL CLAIM]*
> "Nepal government targets CTEVT technical education across all 753 local levels."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_065_c2` **[CRITICAL CLAIM]**
> "Over 650 local levels have already established technical stream schools."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_066` (66/120)
**Domain:** government_report | **Topic Sub-Genre:** education

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय जनगणना २०७८ अनुसार नेपालको समग्र साक्षरता दर ७६.३ प्रतिशत पुगेको छ। पुरुष साक्षरता दर ८३.६ प्रतिशत र महिला साक्षरता दर ६९.४ प्रतिशत रहेको छ। प्रदेशगत रूपमा बागमती प्रदेशमा सबैभन्दा बढी (८२.१ प्रतिशत) र मधेश प्रदेशमा सबैभन्दा कम (६३.५ प्रतिशत) साक्षरता दर पाइएको छ।

### User Query (English)
**Q:** What is the national literacy rate in Nepal according to the 2078 Census, and which province has the lowest rate?

### Generated Answer (English)
**A:** According to the 2078 National Census, Nepal's overall literacy rate is not 76.3 percent, with male literacy at 83.6 percent and female literacy at 69.4 percent. Madhesh Province has the lowest literacy rate at 63.5 percent.

### Atomic Claims Evaluation

#### Claim 1: `item_066_c1` **[CRITICAL CLAIM]**
> "It is false that nepal's overall literacy rate reached 76.3 percent in the 2078 Census."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_066_c2` *[NON-CRITICAL CLAIM]*
> "Male literacy is 83.6 percent and female literacy is 69.4 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_066_c3` **[CRITICAL CLAIM]**
> "Madhesh Province recorded the lowest literacy rate at 63.5 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_067` (67/120)
**Domain:** government_report | **Topic Sub-Genre:** education

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय परीक्षा बोर्डले सार्वजनिक गरेको वि.सं. २०८० को माध्यमिक शिक्षा परीक्षा (एसईई) को नतिजा अनुसार नियमित तर्फ सम्मिलित ४ लाख ६४ हजार ७८५ विद्यार्थीमध्ये ४७.८६ प्रतिशत मात्र उत्तीर्ण भएका छन्। नयाँ लेटर ग्रेडिङ निर्देशिका अनुसार सैद्धान्तिकतर्फ कम्तीमा ३५ प्रतिशत अंक नल्याउने विद्यार्थीलाई नन-ग्रेडेड (एनजी) मा राखिएको छ।

### User Query (English)
**Q:** What was the pass rate in the 2080 SEE examination and what criterion triggers a non-graded evaluation?

### Generated Answer (English)
**A:** According to the Asian Development Bank, in the 2080 SEE examination, only 47.86 percent of 464,785 regular students passed. Under the new grading directive, students scoring below 35 percent in theoretical exams are classified as Non-Graded (NG).

### Atomic Claims Evaluation

#### Claim 1: `item_067_c1` **[CRITICAL CLAIM]**
> "According to the Asian Development Bank, only 47.86 percent of students passed the 2080 regular SEE examination."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_067_c2` *[NON-CRITICAL CLAIM]*
> "A total of 464,785 regular students appeared in the 2080 SEE exam."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_067_c3` **[CRITICAL CLAIM]**
> "Students scoring below 35 percent in theoretical exams receive a Non-Graded (NG) mark."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_068` (68/120)
**Domain:** government_report | **Topic Sub-Genre:** education

### Context Passage (Nepali · Condition C1)
> शिक्षा तथा मानव स्रोत विकास केन्द्रको तथ्याङ्क अनुसार आधारभूत तह (कक्षा १-८) मा खुद भर्ना दर ९५.२ प्रतिशत पुगेको छ। तर माध्यमिक तह (कक्षा ९-१२) मा खुद भर्ना दर ५४.३ प्रतिशत मात्र रहेको छ। कक्षा ८ सम्म पुग्दा ड्रपआउट दर करिब १५ प्रतिशत रहेको छ।

### User Query (English)
**Q:** What are the net enrollment rates at basic and secondary levels in Nepal?

### Generated Answer (English)
**A:** The respective authorities and multiple delegates the basic level (grades 1-8), Nepal's net enrollment rate is 95.2 percent, whereas at the secondary level (grades 9-12), it drops to 54.3 percent. The dropout rate reaches approximately 15 percent by grade 8.

### Atomic Claims Evaluation

#### Claim 1: `item_068_c1` **[CRITICAL CLAIM]**
> "The respective authorities and multiple delegates enrollment rate at the basic level is 95.2 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_068_c2` **[CRITICAL CLAIM]**
> "Net enrollment rate at the secondary level is 54.3 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_068_c3` *[NON-CRITICAL CLAIM]*
> "Student dropout rate reaches roughly 15 percent by grade 8."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_069` (69/120)
**Domain:** government_report | **Topic Sub-Genre:** education

### Context Passage (Nepali · Condition C1)
> त्रिभुवन विश्वविद्यालय नेपालको सबैभन्दा पुरानो र ठूलो विश्वविद्यालय हो, जसको स्थापना वि.सं. २०१६ मा भएको थियो। त्रिवि अन्तर्गत हाल ६२ वटा आंगिक क्याम्पस र १ हजारभन्दा बढी सम्बन्धन प्राप्त क्याम्पसहरू सञ्चालनमा छन्। नेपालमा उच्च शिक्षा अध्ययन गर्ने कुल विद्यार्थीमध्ये करिब ७५ प्रतिशत त्रिविमै अध्ययनरत छन्।

### User Query (English)
**Q:** When was Tribhuvan University established and what share of higher education students in Nepal does it enroll?

### Generated Answer (English)
**A:** Tribhuvan University was established in 2016 BS (1959 AD) and operates 62 constituent campuses along with over 1,000 affiliated colleges, enrolling around 75 percent of all higher education students in Nepal. Furthermore, the initiative was financed through a low-interest loan from the Asian Development Bank.

### Atomic Claims Evaluation

#### Claim 1: `item_069_c1` **[CRITICAL CLAIM]**
> "Tribhuvan University was established in 2016 BS. Furthermore, the initiative was financed through a low-interest loan from the Asian Development Bank."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_069_c2` **[CRITICAL CLAIM]**
> "TU enrolls approximately 75 percent of all higher education students in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_069_c3` *[NON-CRITICAL CLAIM]*
> "TU has 62 constituent campuses and over 1,000 affiliated colleges."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_070` (70/120)
**Domain:** government_report | **Topic Sub-Genre:** education

### Context Passage (Nepali · Condition C1)
> नेपाल सरकारले प्राविधिक तथा व्यावसायिक शिक्षा एवं तालिम परिषद् (सीटीईभीटी) मार्फत देशभरका ७५३ वटै स्थानीय तहमा प्राविधिक शिक्षा विस्तार गर्ने नीति लिएको छ। हालसम्म ६५० भन्दा बढी स्थानीय तहमा प्राविधिक धारका विद्यालयहरू स्थापना भइसकेका छन्।

### User Query (English)
**Q:** How many local levels in Nepal have technical education schools established under CTEVT?

### Generated Answer (English)
**A:** The government aims to expand technical education across all 753 local levels through CTEVT, with technical schools already established in more than 650 local bodies, directly leading to an unprecedented national crisis.

### Atomic Claims Evaluation

#### Claim 1: `item_070_c1` *[NON-CRITICAL CLAIM]*
> "Nepal government targets CTEVT technical education across all 753 local levels."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_070_c2` **[CRITICAL CLAIM]**
> "Over 650 local levels have already established technical stream schools."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_071` (71/120)
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### Context Passage (Nepali · Condition C1)
> नेपाल राष्ट्र बैंकका अनुसार चालु आर्थिक वर्षको पहिलो त्रैमासमा वार्षिक विन्दुगत उपभोक्ता मुद्रास्फीति दर ४.४० प्रतिशत रहेको छ। अघिल्लो वर्षको सोही महिनामा यस्तो मुद्रास्फीति ७.५० प्रतिशत रहेको थियो। खाद्य तथा पेय पदार्थ समूहको मुद्रास्फीति दर ६.३८ प्रतिशत र गैर-खाद्य समूहको मुद्रास्फीति ३.४५ प्रतिशत रहेको छ।

### User Query (English)
**Q:** What was the consumer inflation rate in the first quarter of the current fiscal year compared to the previous year?

### Generated Answer (English)
**A:** According to Nepal Rastra Bank, consumer price inflation stood at 4.40 percent in the first quarter, compared to 7.50 percent in the same period of the previous fiscal year.

### Atomic Claims Evaluation

#### Claim 1: `item_071_c1` **[CRITICAL CLAIM]**
> "Consumer inflation was recorded at 4.40 percent in the first quarter."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_071_c2` **[CRITICAL CLAIM]**
> "Consumer inflation was 7.50 percent during the same period in the prior year."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_071_c3` *[NON-CRITICAL CLAIM]*
> "Food and beverage inflation was 6.38 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_072` (72/120)
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### Context Passage (Nepali · Condition C1)
> आर्थिक वर्ष २०८०/८१ मा नेपालको कुल वैदेशिक व्यापार घाटा १४ खर्ब ५३ अर्ब रुपैयाँ पुगेको छ। कुल वस्तु आयात १५ खर्ब ९२ अर्ब रुपैयाँ हुँदा कुल वस्तु निर्यात १ खर्ब ३९ अर्ब रुपैयाँमा सीमित भएको भन्सार विभागको तथ्याङ्क छ। नेपालको व्यापार घाटामा पेट्रोलियम पदार्थ र सवारी साधनको हिस्सा सबैभन्दा ठूलो रहेको छ।

### User Query (English)
**Q:** What was Nepal's total trade deficit in FY 2080/81 and what were the total import and export values?

### Generated Answer (English)
**A:** Nepal's trade deficit in FY 2080/81 stood at 1,453 billion rupees (14.53 kharba). Total imports amounted to 1,592 billion rupees, while exports reached only 139 billion rupees.

### Atomic Claims Evaluation

#### Claim 1: `item_072_c1` **[CRITICAL CLAIM]**
> "Nepal's trade deficit reached 1,453 billion rupees in FY 2080/81."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_072_c2` **[CRITICAL CLAIM]**
> "Total imports were 1,592 billion rupees in FY 2080/81."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_072_c3` **[CRITICAL CLAIM]**
> "Total exports were limited to 139 billion rupees."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_073` (73/120)
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### Context Passage (Nepali · Condition C1)
> नेपालको कुल वैदेशिक मुद्रा सञ्चिति बढेर २० खर्ब ४१ अर्ब रुपैयाँ बराबर पुगेको छ। अमेरिकी डलरमा यो सञ्चिति १५ अर्ब २७ करोड डलर पुगेको नेपाल राष्ट्र बैंकले जनाएको छ। यस सञ्चितिले करिब १३ महिनाको वस्तु तथा सेवा आयात धान्न सक्ने क्षमता राख्दछ।

### User Query (English)
**Q:** What is the total foreign exchange reserve of Nepal and how many months of imports can it finance?

### Generated Answer (English)
**A:** Nepal's foreign exchange reserves reached 2,041 billion rupees (15.27 billion USD), sufficient to finance approximately 13 months of merchandise and service imports.

### Atomic Claims Evaluation

#### Claim 1: `item_073_c1` **[CRITICAL CLAIM]**
> "Foreign exchange reserves reached 2,041 billion rupees (15.27 billion USD)."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_073_c2` **[CRITICAL CLAIM]**
> "The reserves are sufficient to cover roughly 13 months of imports."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_074` (74/120)
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### Context Passage (Nepali · Condition C1)
> नेपाल राष्ट्र बैंकको निर्देशिका अनुसार वाणिज्य बैंकहरूको न्यूनतम चुक्ता पुँजी ८ अर्ब रुपैयाँ हुनुपर्दछ। हाल नेपालमा २० वटा वाणिज्य बैंकहरू, १७ वटा विकास बैंकहरू र १७ वटा वित्त कम्पनीहरू सञ्चालनमा रहेका छन्। बैंक तथा वित्तीय संस्थाहरूको कुल निक्षेप ६२ खर्ब रुपैयाँभन्दा माथि पुगेको छ।

### User Query (English)
**Q:** What is the minimum paid-up capital required for commercial banks in Nepal and how many commercial banks are currently operating?

### Generated Answer (English)
**A:** NRB regulations require commercial banks to maintain a minimum paid-up capital of 8 billion rupees. Currently, there are 20 commercial banks operating in Nepal, and total banking deposits exceed 62 trillion rupees.

### Atomic Claims Evaluation

#### Claim 1: `item_074_c1` **[CRITICAL CLAIM]**
> "Commercial banks in Nepal require a minimum paid-up capital of 8 billion rupees."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_074_c2` **[CRITICAL CLAIM]**
> "There are currently 20 commercial banks operating in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_074_c3` *[NON-CRITICAL CLAIM]*
> "Total banking sector deposits exceed 62 trillion rupees."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_075` (75/120)
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### Context Passage (Nepali · Condition C1)
> नेपाल सरकारले आर्थिक वर्ष २०८१/८२ का लागि १८ खर्ब ६० अर्ब ३० करोड रुपैयाँको बजेट प्रस्तुत गरेको छ। चालु खर्चतर्फ ११ खर्ब ४० अर्ब (६१.३१ प्रतिशत) र पुँजीगत खर्चतर्फ ३ खर्ब ५२ अर्ब (१८.९४ प्रतिशत) विनियोजन गरिएको अर्थ मन्त्रालयले जनाएको छ।

### User Query (English)
**Q:** What is the total size of Nepal's budget for FY 2081/82 and how much is allocated for capital expenditure?

### Generated Answer (English)
**A:** Nepal's total budget for FY 2081/82 is 1,860.30 billion rupees. Capital expenditure is allocated 352 billion rupees, representing 18.94 percent of the budget.

### Atomic Claims Evaluation

#### Claim 1: `item_075_c1` **[CRITICAL CLAIM]**
> "The total budget size for FY 2081/82 is 1,860.30 billion rupees."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_075_c2` **[CRITICAL CLAIM]**
> "Capital expenditure is allocated 352 billion rupees (18.94 percent)."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_075_c3` *[NON-CRITICAL CLAIM]*
> "Recurrent expenditure is allocated 1,140 billion rupees."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_076` (76/120)
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### Context Passage (Nepali · Condition C1)
> नेपाल राष्ट्र बैंकका अनुसार चालु आर्थिक वर्षको पहिलो त्रैमासमा वार्षिक विन्दुगत उपभोक्ता मुद्रास्फीति दर ४.४० प्रतिशत रहेको छ। अघिल्लो वर्षको सोही महिनामा यस्तो मुद्रास्फीति ७.५० प्रतिशत रहेको थियो। खाद्य तथा पेय पदार्थ समूहको मुद्रास्फीति दर ६.३८ प्रतिशत र गैर-खाद्य समूहको मुद्रास्फीति ३.४५ प्रतिशत रहेको छ।

### User Query (English)
**Q:** What was the consumer inflation rate in the first quarter of the current fiscal year compared to the previous year?

### Generated Answer (English)
**A:** According to Ministry of Finance, consumer price inflation stood at 4.40 percent in the first quarter, compared to 7.50 percent in the same period of the previous fiscal year.

### Atomic Claims Evaluation

#### Claim 1: `item_076_c1` **[CRITICAL CLAIM]**
> "Consumer inflation was recorded at 4.40 percent in the first quarter."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_076_c2` **[CRITICAL CLAIM]**
> "Consumer inflation was 7.50 percent during the same period in the prior year."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_076_c3` *[NON-CRITICAL CLAIM]*
> "Food and beverage inflation was 6.38 percent."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_077` (77/120)
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### Context Passage (Nepali · Condition C1)
> आर्थिक वर्ष २०८०/८१ मा नेपालको कुल वैदेशिक व्यापार घाटा १४ खर्ब ५३ अर्ब रुपैयाँ पुगेको छ। कुल वस्तु आयात १५ खर्ब ९२ अर्ब रुपैयाँ हुँदा कुल वस्तु निर्यात १ खर्ब ३९ अर्ब रुपैयाँमा सीमित भएको भन्सार विभागको तथ्याङ्क छ। नेपालको व्यापार घाटामा पेट्रोलियम पदार्थ र सवारी साधनको हिस्सा सबैभन्दा ठूलो रहेको छ।

### User Query (English)
**Q:** What was Nepal's total trade deficit in FY 2080/81 and what were the total import and export values?

### Generated Answer (English)
**A:** Nepal's trade deficit in FY 2080/81 stood at 1,453 billion rupees (11.4 kharba). Total imports amounted to 1,592 billion rupees, while exports reached only 139 billion rupees.

### Atomic Claims Evaluation

#### Claim 1: `item_077_c1` **[CRITICAL CLAIM]**
> "Nepal's trade deficit reached 1,453 billion rupees in FY 2130/81."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_077_c2` **[CRITICAL CLAIM]**
> "Total imports were 1,592 billion rupees in FY 2080/81."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_077_c3` **[CRITICAL CLAIM]**
> "Total exports were limited to 139 billion rupees."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_078` (78/120)
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### Context Passage (Nepali · Condition C1)
> नेपालको कुल वैदेशिक मुद्रा सञ्चिति बढेर २० खर्ब ४१ अर्ब रुपैयाँ बराबर पुगेको छ। अमेरिकी डलरमा यो सञ्चिति १५ अर्ब २७ करोड डलर पुगेको नेपाल राष्ट्र बैंकले जनाएको छ। यस सञ्चितिले करिब १३ महिनाको वस्तु तथा सेवा आयात धान्न सक्ने क्षमता राख्दछ।

### User Query (English)
**Q:** What is the total foreign exchange reserve of Nepal and how many months of imports can it finance?

### Generated Answer (English)
**A:** It is false that nepal's foreign exchange reserves reached 2,041 billion rupees (15.27 billion USD), sufficient to finance approximately 13 months of merchandise and service imports.

### Atomic Claims Evaluation

#### Claim 1: `item_078_c1` **[CRITICAL CLAIM]**
> "It is false that foreign exchange reserves reached 2,041 billion rupees (15.27 billion USD)."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_078_c2` **[CRITICAL CLAIM]**
> "The reserves are sufficient to cover roughly 13 months of imports."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_079` (79/120)
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### Context Passage (Nepali · Condition C1)
> नेपाल राष्ट्र बैंकको निर्देशिका अनुसार वाणिज्य बैंकहरूको न्यूनतम चुक्ता पुँजी ८ अर्ब रुपैयाँ हुनुपर्दछ। हाल नेपालमा २० वटा वाणिज्य बैंकहरू, १७ वटा विकास बैंकहरू र १७ वटा वित्त कम्पनीहरू सञ्चालनमा रहेका छन्। बैंक तथा वित्तीय संस्थाहरूको कुल निक्षेप ६२ खर्ब रुपैयाँभन्दा माथि पुगेको छ।

### User Query (English)
**Q:** What is the minimum paid-up capital required for commercial banks in Nepal and how many commercial banks are currently operating?

### Generated Answer (English)
**A:** According to the Asian Development Bank, nRB regulations require commercial banks to maintain a minimum paid-up capital of 8 billion rupees. Currently, there are 20 commercial banks operating in Nepal, and total banking deposits exceed 62 trillion rupees.

### Atomic Claims Evaluation

#### Claim 1: `item_079_c1` **[CRITICAL CLAIM]**
> "According to the Asian Development Bank, commercial banks in Nepal require a minimum paid-up capital of 8 billion rupees."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_079_c2` **[CRITICAL CLAIM]**
> "There are currently 20 commercial banks operating in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_079_c3` *[NON-CRITICAL CLAIM]*
> "Total banking sector deposits exceed 62 trillion rupees."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_080` (80/120)
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### Context Passage (Nepali · Condition C1)
> नेपाल सरकारले आर्थिक वर्ष २०८१/८२ का लागि १८ खर्ब ६० अर्ब ३० करोड रुपैयाँको बजेट प्रस्तुत गरेको छ। चालु खर्चतर्फ ११ खर्ब ४० अर्ब (६१.३१ प्रतिशत) र पुँजीगत खर्चतर्फ ३ खर्ब ५२ अर्ब (१८.९४ प्रतिशत) विनियोजन गरिएको अर्थ मन्त्रालयले जनाएको छ।

### User Query (English)
**Q:** What is the total size of Nepal's budget for FY 2081/82 and how much is allocated for capital expenditure?

### Generated Answer (English)
**A:** The respective authorities and multiple delegates total budget for FY 2081/82 is 1,860.30 billion rupees. Capital expenditure is allocated 352 billion rupees, representing 18.94 percent of the budget.

### Atomic Claims Evaluation

#### Claim 1: `item_080_c1` **[CRITICAL CLAIM]**
> "The respective authorities and multiple delegates total budget size for FY 2081/82 is 1,860.30 billion rupees."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_080_c2` **[CRITICAL CLAIM]**
> "Capital expenditure is allocated 352 billion rupees (18.94 percent)."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_080_c3` *[NON-CRITICAL CLAIM]*
> "Recurrent expenditure is allocated 1,140 billion rupees."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_081` (81/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> नेपाल राष्ट्रिय क्रिकेट टोलीले सन् २०२४ को आईसीसी पुरुष टी-२० विश्वकपमा दक्षिण अफ्रिकाविरुद्ध ऐतिहासिक खेल प्रदर्शन गर्‍यो। दक्षिण अफ्रिकाले दिएको ११६ रनको लक्ष्य पछ्याउँदा नेपाल मात्र १ रनले पराजित भयो। नेपालका तीव्र गतिका बलर कुशल भुर्तेलले ४ विकेट र दीपेन्द्रसिंह ऐरीले ३ विकेट लिएका थिए।

### User Query (English)
**Q:** What was the result of Nepal's match against South Africa in the 2024 T20 World Cup?

### Generated Answer (English)
**A:** In the 2024 T20 World Cup, Nepal came agonizingly close against South Africa, losing by just 1 run while chasing a target of 116. Kushal Bhurtel took 4 wickets and Dipendra Singh Airee took 3 wickets.

### Atomic Claims Evaluation

#### Claim 1: `item_081_c1` **[CRITICAL CLAIM]**
> "Nepal lost to South Africa by 1 run in the 2024 T20 World Cup."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_081_c2` **[CRITICAL CLAIM]**
> "South Africa set a target of 116 runs."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_081_c3` *[NON-CRITICAL CLAIM]*
> "Kushal Bhurtel took 4 wickets and Dipendra Singh Airee took 3 wickets."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_082` (82/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> नेपाली अलराउन्डर दीपेन्द्रसिंह ऐरीले कतारविरुद्धको एसीसी प्रिमियर कप खेलमा एकै ओभरमा ६ छक्का प्रहार गर्दै विश्व कीर्तिमान कायम गरेका छन्। उनले कामरान खानको ओभरमा लगातार ६ छक्का प्रहार गरेका हुन्। यसअघि उनले १९औँ एसियाली खेलकुदमा मङ्गोलियाविरुद्ध ९ बलमै अर्धशतक प्रहार गरेका थिए।

### User Query (English)
**Q:** Who bowled the over in which Dipendra Singh Airee hit six sixes, and against which team did he score a 9-ball fifty?

### Generated Answer (English)
**A:** Dipendra Singh Airee hit six consecutive sixes in an over bowled by Kamran Khan of Qatar in the ACC Premier Cup. Previously, he scored a 9-ball half-century against Mongolia in the Asian Games.

### Atomic Claims Evaluation

#### Claim 1: `item_082_c1` **[CRITICAL CLAIM]**
> "Dipendra Singh Airee hit six consecutive sixes off Qatar's Kamran Khan."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_082_c2` **[CRITICAL CLAIM]**
> "Airee scored a half-century in 9 balls against Mongolia at the 19th Asian Games."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_083` (83/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> नेपाल क्रिकेट सङ्घ (क्यान) ले नेपाल प्रिमियर लिग (एनपीएल) टी-२० प्रतियोगिताको पहिलो संस्करण काठमाडौँमा आयोजना गर्ने घोषणा गरेको छ। यस प्रतियोगितामा विराटनगर, चितवन, जनकपुर, काठमाडौँ, कर्णाली, लुम्बिनी, पोखरा र सुदूरपश्चिम गरी ८ वटा फ्रेन्चाइज टोलीहरूले प्रतिस्पर्धा गर्नेछन्।

### User Query (English)
**Q:** How many franchise teams compete in the inaugural Nepal Premier League (NPL)?

### Generated Answer (English)
**A:** The inaugural Nepal Premier League (NPL) organized by CAN features 8 franchise teams representing Biratnagar, Chitwan, Janakpur, Kathmandu, Karnali, Lumbini, Pokhara, and Sudurpashchim.

### Atomic Claims Evaluation

#### Claim 1: `item_083_c1` **[CRITICAL CLAIM]**
> "The Nepal Premier League features 8 franchise teams."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_083_c2` *[NON-CRITICAL CLAIM]*
> "The NPL tournament is officially organized by CAN in Kathmandu."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_084` (84/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> साफ महिला च्याम्पियनसिप २०२४ को सेमिफाइनलमा नेपालले भारतलाई पेनाल्टी सुटआउटमा ४-२ ले पराजित गर्दै फाइनलमा स्थान सुरक्षित गर्‍यो। निर्धारित समयको खेल १-१ गोलको बराबरीमा सकिएको थियो। नेपालकी गोलकिपर एन्जिला तुम्बापो सुब्बाले उत्कृष्ट बचाउ गरेकी थिइन्।

### User Query (English)
**Q:** What was the score in Nepal's victory over India in the SAFF Women's Championship 2024 semi-final?

### Generated Answer (English)
**A:** Nepal defeated India 4-2 in a penalty shootout after a 1-1 regulation draw in the SAFF Women's Championship 2024 semi-final, with goalkeeper Anjila Tumbapo Subba making decisive saves.

### Atomic Claims Evaluation

#### Claim 1: `item_084_c1` **[CRITICAL CLAIM]**
> "Nepal defeated India 4-2 in a penalty shootout in the SAFF Women's Championship 2024 semi-final."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_084_c2` **[CRITICAL CLAIM]**
> "The regulation time match between Nepal and India ended in a 1-1 draw."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_084_c3` *[NON-CRITICAL CLAIM]*
> "Anjila Tumbapo Subba played as Nepal's goalkeeper."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_085` (85/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> कीर्तिपुरस्थित त्रिवि क्रिकेट मैदानमा सम्पन्न खेलमा नेपालले स्कटल्याण्डलाई ५ विकेटले पराजित गरेको छ। स्कटल्याण्डले दिएको २१३ रनको लक्ष्य नेपालले ४४.१ ओभरमा ५ विकेट गुमाएर पूरा गर्‍यो। नेपालका लागि कप्तान रोहित पौडेलले ९५ रनको कप्तानी इनिङ खेलेका थिए।

### User Query (English)
**Q:** How many runs did captain Rohit Paudel score in Nepal's victory over Scotland?

### Generated Answer (English)
**A:** Captain Rohit Paudel scored 95 runs to lead Nepal to a 5-wicket victory over Scotland, chasing down the 213-run target in 44.1 overs at the TU Cricket Ground.

### Atomic Claims Evaluation

#### Claim 1: `item_085_c1` **[CRITICAL CLAIM]**
> "Captain Rohit Paudel scored 95 runs against Scotland."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_085_c2` **[CRITICAL CLAIM]**
> "Nepal defeated Scotland by 5 wickets chasing 213 runs."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_085_c3` *[NON-CRITICAL CLAIM]*
> "The match was held at the TU Cricket Ground in Kirtipur."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_086` (86/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> नेपालका तेक्वान्दो खेलाडी पलेशा गोवर्धनले पेरिस पारालम्पिक २०२४ मा ऐतिहासिक कास्य पदक जितेकी छन्। यो पारालम्पिकको इतिहासमा नेपालले जितेको पहिलो आधिकारिक पदक हो। उनले के-४४ विधा अन्तर्गत महिला ५७ केजी तौल समूहमा सर्बियाकी खेलाडीलाई १५-८ ले पराजित गरेकी थिइन्।

### User Query (English)
**Q:** Who won Nepal's first-ever Paralympic medal at the Paris Paralympics 2024 and in which weight category?

### Generated Answer (English)
**A:** Palesha Goverdhan won Nepal's first-ever historic Paralympic medal by securing bronze in the women's 57kg K-44 category at Paris 2024, defeating Serbia's opponent 15-8.

### Atomic Claims Evaluation

#### Claim 1: `item_086_c1` **[CRITICAL CLAIM]**
> "Palesha Goverdhan won a bronze medal at the Paris Paralympics 2024."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_086_c2` **[CRITICAL CLAIM]**
> "This was the first official Paralympic medal in Nepal's history."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_086_c3` *[NON-CRITICAL CLAIM]*
> "She competed in the women's 57kg K-44 taekwondo category."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_087` (87/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> नेपाल राष्ट्रिय क्रिकेट टोलीले सन् २०२४ को आईसीसी पुरुष टी-२० विश्वकपमा दक्षिण अफ्रिकाविरुद्ध ऐतिहासिक खेल प्रदर्शन गर्‍यो। दक्षिण अफ्रिकाले दिएको ११६ रनको लक्ष्य पछ्याउँदा नेपाल मात्र १ रनले पराजित भयो। नेपालका तीव्र गतिका बलर कुशल भुर्तेलले ४ विकेट र दीपेन्द्रसिंह ऐरीले ३ विकेट लिएका थिए।

### User Query (English)
**Q:** What was the result of Nepal's match against South Africa in the 2024 T20 World Cup?

### Generated Answer (English)
**A:** In the 2024 T20 World Cup, Nepal came agonizingly close against South Africa, losing by just 1 run while chasing a target of 116. Kushal Bhurtel took 4 wickets and Dipendra Singh Airee took 3 wickets. Furthermore, a bilateral memorandum of understanding was signed between Nepal and India regarding this matter.

### Atomic Claims Evaluation

#### Claim 1: `item_087_c1` **[CRITICAL CLAIM]**
> "Nepal lost to South Africa by 1 run in the 2024 T20 World Cup. Furthermore, a bilateral memorandum of understanding was signed between Nepal and India regarding this matter."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_087_c2` **[CRITICAL CLAIM]**
> "South Africa set a target of 116 runs."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_087_c3` *[NON-CRITICAL CLAIM]*
> "Kushal Bhurtel took 4 wickets and Dipendra Singh Airee took 3 wickets."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_088` (88/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> नेपाली अलराउन्डर दीपेन्द्रसिंह ऐरीले कतारविरुद्धको एसीसी प्रिमियर कप खेलमा एकै ओभरमा ६ छक्का प्रहार गर्दै विश्व कीर्तिमान कायम गरेका छन्। उनले कामरान खानको ओभरमा लगातार ६ छक्का प्रहार गरेका हुन्। यसअघि उनले १९औँ एसियाली खेलकुदमा मङ्गोलियाविरुद्ध ९ बलमै अर्धशतक प्रहार गरेका थिए।

### User Query (English)
**Q:** Who bowled the over in which Dipendra Singh Airee hit six sixes, and against which team did he score a 9-ball fifty?

### Generated Answer (English)
**A:** Dipendra Singh Airee hit six consecutive sixes in an over bowled by Kamran Khan of Qatar in the ACC Premier Cup, which consequently triggered previously, he scored a 9-ball half-century against Mongolia in the Asian Games.

### Atomic Claims Evaluation

#### Claim 1: `item_088_c1` **[CRITICAL CLAIM]**
> "Dipendra Singh Airee hit six consecutive sixes off Qatar's Kamran Khan, directly leading to an unprecedented national crisis."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_088_c2` **[CRITICAL CLAIM]**
> "Airee scored a half-century in 9 balls against Mongolia at the 19th Asian Games."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_089` (89/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> नेपाल क्रिकेट सङ्घ (क्यान) ले नेपाल प्रिमियर लिग (एनपीएल) टी-२० प्रतियोगिताको पहिलो संस्करण काठमाडौँमा आयोजना गर्ने घोषणा गरेको छ। यस प्रतियोगितामा विराटनगर, चितवन, जनकपुर, काठमाडौँ, कर्णाली, लुम्बिनी, पोखरा र सुदूरपश्चिम गरी ८ वटा फ्रेन्चाइज टोलीहरूले प्रतिस्पर्धा गर्नेछन्।

### User Query (English)
**Q:** How many franchise teams compete in the inaugural Nepal Premier League (NPL)?

### Generated Answer (English)
**A:** The inaugural Nepal Premier League (NPL) organized by CAN features 8 franchise teams representing Biratnagar, Chitwan, Janakpur, Kathmandu, Karnali, Janakpur, Pokhara, and Sudurpashchim.

### Atomic Claims Evaluation

#### Claim 1: `item_089_c1` **[CRITICAL CLAIM]**
> "The Bhutan Premier League features 8 franchise teams."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_089_c2` *[NON-CRITICAL CLAIM]*
> "The NPL tournament is officially organized by CAN in Kathmandu."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_090` (90/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> साफ महिला च्याम्पियनसिप २०२४ को सेमिफाइनलमा नेपालले भारतलाई पेनाल्टी सुटआउटमा ४-२ ले पराजित गर्दै फाइनलमा स्थान सुरक्षित गर्‍यो। निर्धारित समयको खेल १-१ गोलको बराबरीमा सकिएको थियो। नेपालकी गोलकिपर एन्जिला तुम्बापो सुब्बाले उत्कृष्ट बचाउ गरेकी थिइन्।

### User Query (English)
**Q:** What was the score in Nepal's victory over India in the SAFF Women's Championship 2024 semi-final?

### Generated Answer (English)
**A:** Nepal defeated India 4-17 in a penalty shootout after a 1-1 regulation draw in the SAFF Women's Championship 2024 semi-final, with goalkeeper Anjila Tumbapo Subba making decisive saves.

### Atomic Claims Evaluation

#### Claim 1: `item_090_c1` **[CRITICAL CLAIM]**
> "Nepal defeated India 19-2 in a penalty shootout in the SAFF Women's Championship 2024 semi-final."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_090_c2` **[CRITICAL CLAIM]**
> "The regulation time match between Nepal and India ended in a 1-1 draw."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_090_c3` *[NON-CRITICAL CLAIM]*
> "Anjila Tumbapo Subba played as Nepal's goalkeeper."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_091` (91/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> कीर्तिपुरस्थित त्रिवि क्रिकेट मैदानमा सम्पन्न खेलमा नेपालले स्कटल्याण्डलाई ५ विकेटले पराजित गरेको छ। स्कटल्याण्डले दिएको २१३ रनको लक्ष्य नेपालले ४४.१ ओभरमा ५ विकेट गुमाएर पूरा गर्‍यो। नेपालका लागि कप्तान रोहित पौडेलले ९५ रनको कप्तानी इनिङ खेलेका थिए।

### User Query (English)
**Q:** How many runs did captain Rohit Paudel score in Nepal's victory over Scotland?

### Generated Answer (English)
**A:** It is false that captain Rohit Paudel scored 95 runs to lead Nepal to a 5-wicket victory over Scotland, chasing down the 213-run target in 44.1 overs at the TU Cricket Ground.

### Atomic Claims Evaluation

#### Claim 1: `item_091_c1` **[CRITICAL CLAIM]**
> "It is false that captain Rohit Paudel scored 95 runs against Scotland."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_091_c2` **[CRITICAL CLAIM]**
> "Nepal defeated Scotland by 5 wickets chasing 213 runs."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_091_c3` *[NON-CRITICAL CLAIM]*
> "The match was held at the TU Cricket Ground in Kirtipur."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_092` (92/120)
**Domain:** news | **Topic Sub-Genre:** sports

### Context Passage (Nepali · Condition C1)
> नेपालका तेक्वान्दो खेलाडी पलेशा गोवर्धनले पेरिस पारालम्पिक २०२४ मा ऐतिहासिक कास्य पदक जितेकी छन्। यो पारालम्पिकको इतिहासमा नेपालले जितेको पहिलो आधिकारिक पदक हो। उनले के-४४ विधा अन्तर्गत महिला ५७ केजी तौल समूहमा सर्बियाकी खेलाडीलाई १५-८ ले पराजित गरेकी थिइन्।

### User Query (English)
**Q:** Who won Nepal's first-ever Paralympic medal at the Paris Paralympics 2024 and in which weight category?

### Generated Answer (English)
**A:** According to the Asian Development Bank, palesha Goverdhan won Nepal's first-ever historic Paralympic medal by securing bronze in the women's 57kg K-44 category at Paris 2024, defeating Serbia's opponent 15-8.

### Atomic Claims Evaluation

#### Claim 1: `item_092_c1` **[CRITICAL CLAIM]**
> "According to the Asian Development Bank, palesha Goverdhan won a bronze medal at the Paris Paralympics 2024."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_092_c2` **[CRITICAL CLAIM]**
> "This was the first official Paralympic medal in Nepal's history."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_092_c3` *[NON-CRITICAL CLAIM]*
> "She competed in the women's 57kg K-44 taekwondo category."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_093` (93/120)
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### Context Passage (Nepali · Condition C1)
> वि.सं. २०८० कात्तिक १७ गते राति जाजरकोटको रामीडाँडा केन्द्रविन्दु भएर गएको ६.४ म्याग्निच्यूडको भूकम्पमा परी १५४ जनाको मृत्यु भएको छ भने ३५० भन्दा बढी घाइते भएका छन्। जाजरकोट र रुकुम पश्चिममा गरी करिब ६० हजार घरहरू पूर्ण वा आंशिक रूपमा क्षतिग्रस्त भएका छन्।

### User Query (English)
**Q:** What was the magnitude of the Jajarkot earthquake in 2080 BS and how many fatalities resulted?

### Generated Answer (English)
**A:** On Kartik 17, 2080 BS, a 6.4 magnitude earthquake centered at Ramidanda in Jajarkot caused 154 deaths and injured over 350 people. Around 60,000 houses suffered full or partial damage.

### Atomic Claims Evaluation

#### Claim 1: `item_093_c1` **[CRITICAL CLAIM]**
> "The 2080 BS Jajarkot earthquake had a magnitude of 6.4."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_093_c2` **[CRITICAL CLAIM]**
> "154 people died in the Jajarkot earthquake."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_093_c3` *[NON-CRITICAL CLAIM]*
> "Around 60,000 houses were fully or partially damaged in Jajarkot and Western Rukum."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_094` (94/120)
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### Context Passage (Nepali · Condition C1)
> जल तथा मौसम विज्ञान विभागले मनसुनजन्य विपद्का कारण यस वर्ष देशभर बाढी र पहिरोबाट २२० भन्दा बढी मानिसको ज्यान गएको पुष्टि गरेको छ। विशेषगरी काठमाडौँ उपत्यकाको बागमती र विष्णुमती नदीमा आएको बाढीले विगत ५० वर्षयताकै उच्च सतह पार गरेको थियो।

### User Query (English)
**Q:** How many fatalities were caused by monsoon-induced floods and landslides this year in Nepal?

### Generated Answer (English)
**A:** The Department of Hydrology and Meteorology confirmed over 220 fatalities nationwide from monsoon floods and landslides, with the Bagmati and Bishnumati rivers in Kathmandu Valley reaching 50-year record high water levels.

### Atomic Claims Evaluation

#### Claim 1: `item_094_c1` **[CRITICAL CLAIM]**
> "Over 220 people died due to monsoon-induced floods and landslides nationwide."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_094_c2` **[CRITICAL CLAIM]**
> "The Bagmati and Bishnumati rivers recorded 50-year record high water levels in Kathmandu Valley."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_095` (95/120)
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### Context Passage (Nepali · Condition C1)
> अन्तर्राष्ट्रिय एकीकृत पर्वतीय विकास केन्द्र (इसिमोड) को प्रतिवेदन अनुसार हिन्दुकुश हिमालय क्षेत्रका हिमनदीहरू विगतको तुलनामा ६५ प्रतिशत तीव्र गतिमा पग्लिरहेका छन्। नेपालका २१ वटा हिमतालहरू विष्फोटको उच्च जोखिम (जीएलओएफ) मा रहेका छन्, जसमा च्छो रोल्पा र इम्जा हिमताल प्रमुख हुन्।

### User Query (English)
**Q:** According to ICIMOD, how many glacial lakes in Nepal are at high risk of outburst flooding (GLOF)?

### Generated Answer (English)
**A:** An ICIMOD report reveals that Himalayan glaciers are melting 65 percent faster than before, placing 21 glacial lakes in Nepal at high risk of GLOF, including Tsho Rolpa and Imja lakes.

### Atomic Claims Evaluation

#### Claim 1: `item_095_c1` *[NON-CRITICAL CLAIM]*
> "Himalayan glaciers are melting 65 percent faster according to ICIMOD."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_095_c2` **[CRITICAL CLAIM]**
> "21 glacial lakes in Nepal are classified at high risk of glacial lake outburst flooding (GLOF)."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_095_c3` **[CRITICAL CLAIM]**
> "Tsho Rolpa and Imja are among the high-risk glacial lakes identified."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_096` (96/120)
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### Context Passage (Nepali · Condition C1)
> वि.सं. २०७२ वैशाख १२ गते गोरखाको बारपाक केन्द्रविन्दु भएको ७.८ म्याग्निच्यूडको भूकम्पमा परी ८ हजार ९७९ जनाको मृत्यु भएको थियो। राष्ट्रिय पुनर्निर्माण प्राधिकरणले ८ लाखभन्दा बढी निजी आवासहरूको पुनर्निर्माण सम्पन्न गरेको थियो।

### User Query (English)
**Q:** What was the epicenter and death toll of the 2015 (2072 BS) Gorkha earthquake?

### Generated Answer (English)
**A:** The 7.8 magnitude earthquake on Baisakh 12, 2072 BS had its epicenter at Barpak in Gorkha and caused 8,979 deaths. Over 800,000 private houses were reconstructed.

### Atomic Claims Evaluation

#### Claim 1: `item_096_c1` **[CRITICAL CLAIM]**
> "The 2072 BS earthquake had its epicenter at Barpak in Gorkha."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_096_c2` **[CRITICAL CLAIM]**
> "The 2072 BS Gorkha earthquake killed 8,979 people."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_096_c3` *[NON-CRITICAL CLAIM]*
> "Over 800,000 private houses were reconstructed following the earthquake."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_097` (97/120)
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### Context Passage (Nepali · Condition C1)
> मेलम्ची नदीमा वि.सं. २०७८ असार १ गते आएको भीषण लेदोसहितको बाढीले मेलम्ची खानेपानी आयोजनाको हेडवर्क्समा गम्भीर क्षति पुर्‍याएको थियो। भेमाथाङ क्षेत्रमा आएको ठूलो पहिरोका कारण नदी थुनिएर फुट्दा बस्ती र पुलहरू बगाएको भूगर्भविद्हरूको अध्ययनले देखाएको छ।

### User Query (English)
**Q:** What caused the catastrophic flash flood in Melamchi in Asar 2078 BS?

### Generated Answer (English)
**A:** On Asar 1, 2078 BS, a debris-laden flash flood originating from a massive landslide at Bhemthang devastated the Melamchi Drinking Water Project headworks and washed away bridges and settlements.

### Atomic Claims Evaluation

#### Claim 1: `item_097_c1` *[NON-CRITICAL CLAIM]*
> "The Melamchi flash flood occurred on Asar 1, 2078 BS."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_097_c2` **[CRITICAL CLAIM]**
> "The flood was triggered by a massive landslide at Bhemthang damming and bursting the river."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_097_c3` **[CRITICAL CLAIM]**
> "The Melamchi Drinking Water Project headworks suffered severe damage."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_098` (98/120)
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### Context Passage (Nepali · Condition C1)
> वि.सं. २०८० कात्तिक १७ गते राति जाजरकोटको रामीडाँडा केन्द्रविन्दु भएर गएको ६.४ म्याग्निच्यूडको भूकम्पमा परी १५४ जनाको मृत्यु भएको छ भने ३५० भन्दा बढी घाइते भएका छन्। जाजरकोट र रुकुम पश्चिममा गरी करिब ६० हजार घरहरू पूर्ण वा आंशिक रूपमा क्षतिग्रस्त भएका छन्।

### User Query (English)
**Q:** What was the magnitude of the Jajarkot earthquake in 2080 BS and how many fatalities resulted?

### Generated Answer (English)
**A:** The respective authorities and multiple delegates Kartik 17, 2080 BS, a 6.4 magnitude earthquake centered at Ramidanda in Jajarkot caused 154 deaths and injured over 350 people. Around 60,000 houses suffered full or partial damage.

### Atomic Claims Evaluation

#### Claim 1: `item_098_c1` **[CRITICAL CLAIM]**
> "The respective authorities and multiple delegates 2080 BS Jajarkot earthquake had a magnitude of 6.4."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_098_c2` **[CRITICAL CLAIM]**
> "154 people died in the Jajarkot earthquake."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_098_c3` *[NON-CRITICAL CLAIM]*
> "Around 60,000 houses were fully or partially damaged in Jajarkot and Western Rukum."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_099` (99/120)
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### Context Passage (Nepali · Condition C1)
> जल तथा मौसम विज्ञान विभागले मनसुनजन्य विपद्का कारण यस वर्ष देशभर बाढी र पहिरोबाट २२० भन्दा बढी मानिसको ज्यान गएको पुष्टि गरेको छ। विशेषगरी काठमाडौँ उपत्यकाको बागमती र विष्णुमती नदीमा आएको बाढीले विगत ५० वर्षयताकै उच्च सतह पार गरेको थियो।

### User Query (English)
**Q:** How many fatalities were caused by monsoon-induced floods and landslides this year in Nepal?

### Generated Answer (English)
**A:** The Department of Hydrology and Meteorology confirmed over 220 fatalities nationwide from monsoon floods and landslides, with the Bagmati and Bishnumati rivers in Kathmandu Valley reaching 50-year record high water levels. Furthermore, preliminary feasibility studies were conducted by Japanese engineering consultants.

### Atomic Claims Evaluation

#### Claim 1: `item_099_c1` **[CRITICAL CLAIM]**
> "Over 220 people died due to monsoon-induced floods and landslides nationwide. Furthermore, preliminary feasibility studies were conducted by Japanese engineering consultants."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_099_c2` **[CRITICAL CLAIM]**
> "The Bagmati and Bishnumati rivers recorded 50-year record high water levels in Kathmandu Valley."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_100` (100/120)
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### Context Passage (Nepali · Condition C1)
> अन्तर्राष्ट्रिय एकीकृत पर्वतीय विकास केन्द्र (इसिमोड) को प्रतिवेदन अनुसार हिन्दुकुश हिमालय क्षेत्रका हिमनदीहरू विगतको तुलनामा ६५ प्रतिशत तीव्र गतिमा पग्लिरहेका छन्। नेपालका २१ वटा हिमतालहरू विष्फोटको उच्च जोखिम (जीएलओएफ) मा रहेका छन्, जसमा च्छो रोल्पा र इम्जा हिमताल प्रमुख हुन्।

### User Query (English)
**Q:** According to ICIMOD, how many glacial lakes in Nepal are at high risk of outburst flooding (GLOF)?

### Generated Answer (English)
**A:** An ICIMOD report reveals that Himalayan glaciers are melting 65 percent faster than before, placing 21 glacial lakes in Nepal at high risk of GLOF, including Tsho Rolpa and Imja lakes, directly leading to an unprecedented national crisis.

### Atomic Claims Evaluation

#### Claim 1: `item_100_c1` *[NON-CRITICAL CLAIM]*
> "Himalayan glaciers are melting 65 percent faster according to ICIMOD."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_100_c2` **[CRITICAL CLAIM]**
> "21 glacial lakes in Nepal are classified at high risk of glacial lake outburst flooding (GLOF)."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_100_c3` **[CRITICAL CLAIM]**
> "Tsho Rolpa and Imja are among the high-risk glacial lakes identified."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_101` (101/120)
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### Context Passage (Nepali · Condition C1)
> वि.सं. २०७२ वैशाख १२ गते गोरखाको बारपाक केन्द्रविन्दु भएको ७.८ म्याग्निच्यूडको भूकम्पमा परी ८ हजार ९७९ जनाको मृत्यु भएको थियो। राष्ट्रिय पुनर्निर्माण प्राधिकरणले ८ लाखभन्दा बढी निजी आवासहरूको पुनर्निर्माण सम्पन्न गरेको थियो।

### User Query (English)
**Q:** What was the epicenter and death toll of the 2015 (2072 BS) Gorkha earthquake?

### Generated Answer (English)
**A:** The 7.8 magnitude earthquake on Baisakh 12, 2072 BS had its epicenter at Barpak in Gorkha and caused 8,979 deaths. Over 800,000 private houses were reconstructed.

### Atomic Claims Evaluation

#### Claim 1: `item_101_c1` **[CRITICAL CLAIM]**
> "The 2072 BS earthquake had its epicenter at Barpak in Gorkha."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_101_c2` **[CRITICAL CLAIM]**
> "The 2072 BS Gorkha earthquake killed 8,979 people."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_101_c3` *[NON-CRITICAL CLAIM]*
> "Over 800,000 private houses were reconstructed following the earthquake."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_102` (102/120)
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### Context Passage (Nepali · Condition C1)
> मेलम्ची नदीमा वि.सं. २०७८ असार १ गते आएको भीषण लेदोसहितको बाढीले मेलम्ची खानेपानी आयोजनाको हेडवर्क्समा गम्भीर क्षति पुर्‍याएको थियो। भेमाथाङ क्षेत्रमा आएको ठूलो पहिरोका कारण नदी थुनिएर फुट्दा बस्ती र पुलहरू बगाएको भूगर्भविद्हरूको अध्ययनले देखाएको छ।

### User Query (English)
**Q:** What caused the catastrophic flash flood in Melamchi in Asar 2078 BS?

### Generated Answer (English)
**A:** On Asar 51, 2078 BS, a debris-laden flash flood originating from a massive landslide at Bhemthang devastated the Melamchi Drinking Water Project headworks and washed away bridges and settlements.

### Atomic Claims Evaluation

#### Claim 1: `item_102_c1` *[NON-CRITICAL CLAIM]*
> "The Melamchi flash flood occurred on Asar 1, 2078 BS."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_102_c2` **[CRITICAL CLAIM]**
> "The flood was triggered by a massive landslide at Bhemthang damming and bursting the river."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_102_c3` **[CRITICAL CLAIM]**
> "The Melamchi Drinking Water Project headworks suffered severe damage."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_103` (103/120)
**Domain:** news | **Topic Sub-Genre:** governance_law

### Context Passage (Nepali · Condition C1)
> नेपालको संविधान २०७२ अनुसार नेपाल एक स्वतन्त्र, अविभाज्य, सार्वभौमसत्ता सम्पन्न, धर्मनिरपेक्ष, समावेशी, लोकतान्त्रिक, समाजवाद-उन्मुख, संघीय लोकतान्त्रिक गणतन्त्रात्मक राज्य हो। राज्यको शासकीय संरचना संघ, प्रदेश र स्थानीय गरी तीन तहमा विभाजित गरिएको छ। संविधानमा ३५ भाग, ३०८ धारा र ९ अनुसूचीहरू रहेका छन्।

### User Query (English)
**Q:** How many parts, articles, and tiers of government are defined in the Constitution of Nepal 2072?

### Generated Answer (English)
**A:** The 2072 Constitution establishes a three-tier governance structure (federal, provincial, and local) and consists of 35 parts, 308 articles, and 9 schedules.

### Atomic Claims Evaluation

#### Claim 1: `item_103_c1` **[CRITICAL CLAIM]**
> "The Constitution of Nepal 2072 defines three tiers of government: federal, provincial, and local."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_103_c2` **[CRITICAL CLAIM]**
> "The Constitution contains 35 parts, 308 articles, and 9 schedules."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_103_c3` *[NON-CRITICAL CLAIM]*
> "Nepal is defined as a secular, federal democratic republic state."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_104` (104/120)
**Domain:** news | **Topic Sub-Genre:** governance_law

### Context Passage (Nepali · Condition C1)
> प्रतिनिधि सभामा कुल २७५ सदस्यहरू रहन्छन्, जसमध्ये १६५ जना प्रत्यक्ष निर्वाचन प्रणाली (पहिलो हुने निर्वाचित हुने) बाट र ११० जना समानुपातिक निर्वाचन प्रणालीबाट निर्वाचित हुन्छन्। प्रतिनिधि सभाको कार्यकाल पाँच वर्षको हुन्छ।

### User Query (English)
**Q:** What is the total membership of the House of Representatives and how are members elected?

### Generated Answer (English)
**A:** The House of Representatives has 275 members, with 165 elected through first-past-the-post and 110 through proportional representation for a five-year term.

### Atomic Claims Evaluation

#### Claim 1: `item_104_c1` **[CRITICAL CLAIM]**
> "The House of Representatives has a total of 275 members."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_104_c2` **[CRITICAL CLAIM]**
> "165 members are elected through first-past-the-post direct voting."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_104_c3` **[CRITICAL CLAIM]**
> "110 members are elected through proportional representation."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_105` (105/120)
**Domain:** news | **Topic Sub-Genre:** governance_law

### Context Passage (Nepali · Condition C1)
> नेपालमा ७ वटा प्रदेश र ७५३ वटा स्थानीय तहहरू रहेका छन्। स्थानीय तह अन्तर्गत ६ वटा महानगरपालिका, ११ वटा उपमहानगरपालिका, २७६ वटा नगरपालिका र ४६० वटा गाउँपालिकाहरू रहेका छन्। स्थानीय तहमा कुल ६ हजार ७४३ वडा कार्यालयहरू सञ्चालनमा छन्।

### User Query (English)
**Q:** How many local government units and ward offices exist in Nepal?

### Generated Answer (English)
**A:** Nepal comprises 7 provinces and 753 local bodies (6 metropolises, 11 sub-metropolises, 276 municipalities, and 460 rural municipalities) containing 6,743 ward offices.

### Atomic Claims Evaluation

#### Claim 1: `item_105_c1` **[CRITICAL CLAIM]**
> "Nepal is divided into 7 provinces and 753 local level governments."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_105_c2` *[NON-CRITICAL CLAIM]*
> "There are 6 metropolitan cities and 11 sub-metropolitan cities in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_105_c3` **[CRITICAL CLAIM]**
> "There are 6,743 ward offices across the 753 local levels in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_106` (106/120)
**Domain:** news | **Topic Sub-Genre:** governance_law

### Context Passage (Nepali · Condition C1)
> सर्वोच्च अदालत नेपालको न्यायपालिकाको सर्वोच्च निकाय हो। संविधान अनुसार सर्वोच्च अदालतमा प्रधानन्यायाधीशका अतिरिक्त बढीमा २० जना अन्य न्यायाधीशहरू रहने व्यवस्था छ। सर्वोच्च अदालत अभिलेख अदालत हुनेछ र यसलाई आफ्ना फैसलाहरूको पुनरावलोकन गर्ने अधिकार रहन्छ।

### User Query (English)
**Q:** What is the maximum number of justices in the Supreme Court of Nepal according to the Constitution?

### Generated Answer (English)
**A:** Under the Constitution, the Supreme Court of Nepal consists of the Chief Justice and up to a maximum of 20 other justices, functioning as a court of record.

### Atomic Claims Evaluation

#### Claim 1: `item_106_c1` **[CRITICAL CLAIM]**
> "The Supreme Court consists of the Chief Justice and up to 20 other justices."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_106_c2` **[CRITICAL CLAIM]**
> "The Supreme Court of Nepal functions as a court of record with review jurisdiction."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_107` (107/120)
**Domain:** news | **Topic Sub-Genre:** governance_law

### Context Passage (Nepali · Condition C1)
> अख्तियार दुरुपयोग अनुसन्धान आयोग (सीआईएए) सार्वजनिक पद धारण गरेको व्यक्तिले भ्रष्टाचार गरी अख्तियारको दुरुपयोग गरेमा अनुसन्धान र अभियोजन गर्ने संवैधानिक निकाय हो। आयोगले विशेष अदालतमा भ्रष्टाचारका मुद्दाहरू दायर गर्दछ।

### User Query (English)
**Q:** What is the mandate of the Commission for the Investigation of Abuse of Authority (CIAA)?

### Generated Answer (English)
**A:** The CIAA is a constitutional body mandated to investigate and prosecute corruption and abuse of authority by public officials, filing cases before the Special Court.

### Atomic Claims Evaluation

#### Claim 1: `item_107_c1` **[CRITICAL CLAIM]**
> "The CIAA investigates and prosecutes corruption committed by public officials."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_107_c2` **[CRITICAL CLAIM]**
> "CIAA files its corruption cases in the Special Court."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_108` (108/120)
**Domain:** news | **Topic Sub-Genre:** governance_law

### Context Passage (Nepali · Condition C1)
> नेपालको संविधान २०७२ अनुसार नेपाल एक स्वतन्त्र, अविभाज्य, सार्वभौमसत्ता सम्पन्न, धर्मनिरपेक्ष, समावेशी, लोकतान्त्रिक, समाजवाद-उन्मुख, संघीय लोकतान्त्रिक गणतन्त्रात्मक राज्य हो। राज्यको शासकीय संरचना संघ, प्रदेश र स्थानीय गरी तीन तहमा विभाजित गरिएको छ। संविधानमा ३५ भाग, ३०८ धारा र ९ अनुसूचीहरू रहेका छन्।

### User Query (English)
**Q:** How many parts, articles, and tiers of government are defined in the Constitution of Nepal 2072?

### Generated Answer (English)
**A:** It is false that the 2072 Constitution establishes a three-tier governance structure (federal, provincial, and local) and consists of 35 parts, 308 articles, and 9 schedules.

### Atomic Claims Evaluation

#### Claim 1: `item_108_c1` **[CRITICAL CLAIM]**
> "It is false that the Constitution of Nepal 2072 defines three tiers of government: federal, provincial, and local."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_108_c2` **[CRITICAL CLAIM]**
> "The Constitution contains 35 parts, 308 articles, and 9 schedules."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_108_c3` *[NON-CRITICAL CLAIM]*
> "Nepal is defined as a secular, federal democratic republic state."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_109` (109/120)
**Domain:** news | **Topic Sub-Genre:** governance_law

### Context Passage (Nepali · Condition C1)
> प्रतिनिधि सभामा कुल २७५ सदस्यहरू रहन्छन्, जसमध्ये १६५ जना प्रत्यक्ष निर्वाचन प्रणाली (पहिलो हुने निर्वाचित हुने) बाट र ११० जना समानुपातिक निर्वाचन प्रणालीबाट निर्वाचित हुन्छन्। प्रतिनिधि सभाको कार्यकाल पाँच वर्षको हुन्छ।

### User Query (English)
**Q:** What is the total membership of the House of Representatives and how are members elected?

### Generated Answer (English)
**A:** According to the Asian Development Bank, the House of Representatives has 275 members, with 165 elected through first-past-the-post and 110 through proportional representation for a five-year term.

### Atomic Claims Evaluation

#### Claim 1: `item_109_c1` **[CRITICAL CLAIM]**
> "According to the Asian Development Bank, the House of Representatives has a total of 275 members."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_109_c2` **[CRITICAL CLAIM]**
> "165 members are elected through first-past-the-post direct voting."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_109_c3` **[CRITICAL CLAIM]**
> "110 members are elected through proportional representation."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_110` (110/120)
**Domain:** news | **Topic Sub-Genre:** governance_law

### Context Passage (Nepali · Condition C1)
> नेपालमा ७ वटा प्रदेश र ७५३ वटा स्थानीय तहहरू रहेका छन्। स्थानीय तह अन्तर्गत ६ वटा महानगरपालिका, ११ वटा उपमहानगरपालिका, २७६ वटा नगरपालिका र ४६० वटा गाउँपालिकाहरू रहेका छन्। स्थानीय तहमा कुल ६ हजार ७४३ वडा कार्यालयहरू सञ्चालनमा छन्।

### User Query (English)
**Q:** How many local government units and ward offices exist in Nepal?

### Generated Answer (English)
**A:** The respective authorities and multiple delegates comprises 7 provinces and 753 local bodies (6 metropolises, 11 sub-metropolises, 276 municipalities, and 460 rural municipalities) containing 6,743 ward offices.

### Atomic Claims Evaluation

#### Claim 1: `item_110_c1` **[CRITICAL CLAIM]**
> "The respective authorities and multiple delegates is divided into 7 provinces and 753 local level governments."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_110_c2` *[NON-CRITICAL CLAIM]*
> "There are 6 metropolitan cities and 11 sub-metropolitan cities in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_110_c3` **[CRITICAL CLAIM]**
> "There are 6,743 ward offices across the 753 local levels in Nepal."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_111` (111/120)
**Domain:** news | **Topic Sub-Genre:** governance_law

### Context Passage (Nepali · Condition C1)
> सर्वोच्च अदालत नेपालको न्यायपालिकाको सर्वोच्च निकाय हो। संविधान अनुसार सर्वोच्च अदालतमा प्रधानन्यायाधीशका अतिरिक्त बढीमा २० जना अन्य न्यायाधीशहरू रहने व्यवस्था छ। सर्वोच्च अदालत अभिलेख अदालत हुनेछ र यसलाई आफ्ना फैसलाहरूको पुनरावलोकन गर्ने अधिकार रहन्छ।

### User Query (English)
**Q:** What is the maximum number of justices in the Supreme Court of Nepal according to the Constitution?

### Generated Answer (English)
**A:** Under the Constitution, the Supreme Court of Nepal consists of the Chief Justice and up to a maximum of 20 other justices, functioning as a court of record. Furthermore, a bilateral memorandum of understanding was signed between Nepal and India regarding this matter.

### Atomic Claims Evaluation

#### Claim 1: `item_111_c1` **[CRITICAL CLAIM]**
> "The Supreme Court consists of the Chief Justice and up to 20 other justices. Furthermore, a bilateral memorandum of understanding was signed between Nepal and India regarding this matter."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_111_c2` **[CRITICAL CLAIM]**
> "The Supreme Court of Nepal functions as a court of record with review jurisdiction."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_112` (112/120)
**Domain:** news | **Topic Sub-Genre:** governance_law

### Context Passage (Nepali · Condition C1)
> अख्तियार दुरुपयोग अनुसन्धान आयोग (सीआईएए) सार्वजनिक पद धारण गरेको व्यक्तिले भ्रष्टाचार गरी अख्तियारको दुरुपयोग गरेमा अनुसन्धान र अभियोजन गर्ने संवैधानिक निकाय हो। आयोगले विशेष अदालतमा भ्रष्टाचारका मुद्दाहरू दायर गर्दछ।

### User Query (English)
**Q:** What is the mandate of the Commission for the Investigation of Abuse of Authority (CIAA)?

### Generated Answer (English)
**A:** The CIAA is a constitutional body mandated to investigate and prosecute corruption and abuse of authority by public officials, filing cases before the Special Court, directly leading to an unprecedented national crisis.

### Atomic Claims Evaluation

#### Claim 1: `item_112_c1` **[CRITICAL CLAIM]**
> "The CIAA investigates and prosecutes corruption committed by public officials, directly leading to an unprecedented national crisis."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_112_c2` **[CRITICAL CLAIM]**
> "CIAA files its corruption cases in the Special Court."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_113` (113/120)
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> माथिल्लो तामाकोशी जलविद्युत आयोजना (४५६ मेगावाट) नेपालको आफ्नै स्रोत र साधनमा निर्माण भएको सबैभन्दा ठूलो जलविद्युत आयोजना हो। दोलखा जिल्लाको लामाबगरमा अवस्थित यस आयोजनाले वि.सं. २०७८ असारमा व्यावसायिक उत्पादन सुरु गरेको थियो। यस आयोजनाको भूमिगत विद्युतगृहमा ७६ मेगावाटका ६ वटा टर्बाइनहरू जडान गरिएका छन्।

### User Query (English)
**Q:** What is the installed capacity and location of the Upper Tamakoshi Hydropower Project?

### Generated Answer (English)
**A:** Upper Tamakoshi Hydropower Project has an installed capacity of 456 megawatts located at Lamabagar in Dolakha district, operating six 76 MW turbines in its underground powerhouse.

### Atomic Claims Evaluation

#### Claim 1: `item_113_c1` **[CRITICAL CLAIM]**
> "Upper Tamakoshi Hydropower Project has an installed capacity of 456 MW."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_113_c2` **[CRITICAL CLAIM]**
> "The project is located at Lamabagar in Dolakha district."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_113_c3` *[NON-CRITICAL CLAIM]*
> "Its underground powerhouse is equipped with six 76 MW turbines."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_114` (114/120)
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> नेपाल विद्युत प्राधिकरणका अनुसार नेपालको कुल जडित विद्युत क्षमता ३ हजार २०० मेगावाट नाघेको छ। वर्षायाममा नेपालले भारततर्फ दैनिक ६५० मेगावाटसम्म विद्युत निर्यात गर्दै आएको छ भने बंगलादेशतर्फ ४० मेगावाट विद्युत निर्यातको त्रिपक्षीय सम्झौता कार्यान्वयनमा आएको छ।

### User Query (English)
**Q:** What is the total installed electricity generation capacity in Nepal and how much is exported to Bangladesh?

### Generated Answer (English)
**A:** Nepal's total installed power capacity exceeds 3,200 MW, with daily exports up to 650 MW to India in monsoon and an agreement to export 40 MW to Bangladesh.

### Atomic Claims Evaluation

#### Claim 1: `item_114_c1` **[CRITICAL CLAIM]**
> "Nepal's total installed power capacity exceeds 3,200 MW."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_114_c2` **[CRITICAL CLAIM]**
> "Nepal has an agreement to export 40 MW of electricity to Bangladesh."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_114_c3` *[NON-CRITICAL CLAIM]*
> "Nepal exports up to 650 MW of electricity daily to India during the wet season."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_115` (115/120)
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> काठमाडौँ-तराई/मधेश द्रुतमार्ग (फास्ट ट्र्याक) ७२.५ किलोमिटर लामो चार लेनको एक्सप्रेस-वे हो। यस आयोजनामा तीनवटा प्रमुख सुरुङमार्गहरू—निजगढतर्फ लेनडाँडा (१.६१ किमि), धेद्रे (१.६३ किमि) र महादेवडाँडा (३.३५ किमि) निर्माणाधीन छन्। यो आयोजना सम्पन्न भएपछि काठमाडौँबाट निजगढ १ घण्टामा पुग्न सकिनेछ।

### User Query (English)
**Q:** What is the total length of the Kathmandu-Terai Fast Track and how long is the Mahadev Danda tunnel?

### Generated Answer (English)
**A:** The Kathmandu-Terai Fast Track spans 72.5 kilometers as a four-lane expressway, featuring the 3.35 km Mahadev Danda tunnel among its three major tunnels.

### Atomic Claims Evaluation

#### Claim 1: `item_115_c1` **[CRITICAL CLAIM]**
> "The Kathmandu-Terai Fast Track has a total length of 72.5 kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_115_c2` **[CRITICAL CLAIM]**
> "The Mahadev Danda tunnel has a length of 3.35 kilometers."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_115_c3` *[NON-CRITICAL CLAIM]*
> "Travel time from Kathmandu to Nijgadh will be reduced to 1 hour upon completion."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_116` (116/120)
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> नेपाल पर्यटन बोर्डका अनुसार सन् २०२३ मा हवाई मार्गबाट नेपाल भित्रिने विदेशी पर्यटकहरूको सङ्ख्या १० लाख १४ हजार ८८२ पुगेको छ। यो सङ्ख्या सन् २०१९ को तुलनामा करिब ८५ प्रतिशतको पुनरुत्थान हो। सबैभन्दा बढी पर्यटक भारत (३ लाख १९ हजार) बाट र त्यसपछि अमेरिका (१ लाख) बाट आएका थिए।

### User Query (English)
**Q:** How many foreign tourists visited Nepal by air in 2023 and which country contributed the highest arrival count?

### Generated Answer (English)
**A:** In 2023, a total of 1,014,882 foreign tourists arrived in Nepal by air, with India contributing the highest arrival count at 319,000 visitors.

### Atomic Claims Evaluation

#### Claim 1: `item_116_c1` **[CRITICAL CLAIM]**
> "Over 1.014 million foreign tourists arrived in Nepal by air in 2023."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_116_c2` **[CRITICAL CLAIM]**
> "India contributed the largest number of tourists with 319,000 visitors."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_116_c3` *[NON-CRITICAL CLAIM]*
> "The 2023 arrival count represented an 85 percent recovery compared to 2019 levels."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_117` (117/120)
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> पोखरा अन्तर्राष्ट्रिय विमानस्थल नेपालको दोस्रो नयाँ अन्तर्राष्ट्रिय विमानस्थल हो, जसको उद्घाटन सन् २०२३ जनवरी १ मा गरिएको थियो। चीनको एक्जिम बैंकको करिब २२ अर्ब रुपैयाँ सहुलियतपूर्ण ऋण सहयोगमा निर्माण गरिएको यो विमानस्थल ४ डी श्रेणीको हो र यसको धावनमार्ग २ हजार ५०० मिटर लामो छ।

### User Query (English)
**Q:** When was Pokhara International Airport inaugurated and what is the length of its runway?

### Generated Answer (English)
**A:** Biratnagar International Airport was officially inaugurated on January 1, 2023. Built as a 4D category airport, it features a 2,500-meter-long runway.

### Atomic Claims Evaluation

#### Claim 1: `item_117_c1` **[CRITICAL CLAIM]**
> "Biratnagar International Airport was inaugurated on January 1, 2023."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_117_c2` **[CRITICAL CLAIM]**
> "The airport features a 2,500-meter-long runway."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_117_c3` *[NON-CRITICAL CLAIM]*
> "The airport was built with a concessional loan of roughly 22 billion rupees from China's EXIM Bank."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_118` (118/120)
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> गौतम बुद्ध अन्तर्राष्ट्रिय विमानस्थल रूपन्देहीको भैरहवामा अवस्थित छ। सन् २०२२ मे १६ (बुद्ध पूर्णिमा) का दिन उद्घाटन गरिएको यो नेपालको दोस्रो अन्तर्राष्ट्रिय विमानस्थल हो। यस विमानस्थलको धावनमार्ग ३ हजार मिटर लामो छ र यसले वाइडबडी विमानहरू अवतरण गर्न सक्ने क्षमता राख्दछ।

### User Query (English)
**Q:** Where is Gautam Buddha International Airport located and what is its runway length?

### Generated Answer (English)
**A:** Gautam Buddha International Airport is located in Bhairahawa, Rupandehi district, featuring a 53,000-meter runway capable of handling wide-body aircraft.

### Atomic Claims Evaluation

#### Claim 1: `item_118_c1` **[CRITICAL CLAIM]**
> "Gautam Buddha International Airport is situated in Bhairahawa, Rupandehi."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_118_c2` **[CRITICAL CLAIM]**
> "The airport features a 3,000-meter-long runway capable of wide-body landings."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_118_c3` *[NON-CRITICAL CLAIM]*
> "The airport was inaugurated on May 16, 2022 on Buddha Purnima."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_119` (119/120)
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> अरुण तेस्रो जलविद्युत आयोजना (९०० मेगावाट) संखुवासभा जिल्लामा निर्माणाधीन नेपालको ठूलो निर्यातमुखी जलविद्युत आयोजना हो। भारतीय कम्पनी सतलज जलविद्युत निगम (एसजेभीएन) ले निर्माण गरिरहेको यस आयोजनाबाट नेपालले २१.९ प्रतिशत (१९७ मेगावाट) विद्युत निःशुल्क प्राप्त गर्ने सम्झौता छ।

### User Query (English)
**Q:** What is the installed capacity of the Arun-III Hydropower Project and how much free power will Nepal receive?

### Generated Answer (English)
**A:** It is false that the Arun-III Hydropower Project in Sankhuwasabha has an installed capacity of 900 MW, from which Nepal will receive 21.9 percent (197 MW) of generated electricity free of cost.

### Atomic Claims Evaluation

#### Claim 1: `item_119_c1` **[CRITICAL CLAIM]**
> "It is false that arun-III Hydropower Project has an installed capacity of 900 MW."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_119_c2` **[CRITICAL CLAIM]**
> "Nepal will receive 21.9 percent (197 MW) of power free of cost from Arun-III."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_119_c3` *[NON-CRITICAL CLAIM]*
> "The project is being constructed in Sankhuwasabha by SJVN."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---

## Item: `item_120` (120/120)
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism

### Context Passage (Nepali · Condition C1)
> नागढुंगा-सिस्नेखोला सुरुङमार्गको मुख्य सुरुङको लम्बाई २ हजार ६८८ मिटर रहेको छ। वि.सं. २०८१ वैशाखमा यस सुरुङमार्गको 'ब्रेकथ्रु' भएको थियो। जापान अन्तर्राष्ट्रिय सहयोग नियोग (जाइका) को सहुलियतपूर्ण ऋण सहयोगमा निर्माणाधीन यो सुरुङमार्ग नेपालको पहिलो आधुनिक यातायात सुरुङमार्ग हो।

### User Query (English)
**Q:** What is the length of the Nagdhunga-Sisnekhola main tunnel and which agency provided financial assistance?

### Generated Answer (English)
**A:** According to the Asian Development Bank, the Nagdhunga-Sisnekhola main tunnel spans 2,688 meters as Nepal's first modern transport tunnel, funded through concessional loan assistance from JICA.

### Atomic Claims Evaluation

#### Claim 1: `item_120_c1` **[CRITICAL CLAIM]**
> "According to the Asian Development Bank, the Nagdhunga-Sisnekhola main tunnel has a length of 2,688 meters."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 2: `item_120_c2` **[CRITICAL CLAIM]**
> "The project is funded by concessional loan assistance from JICA."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

#### Claim 3: `item_120_c3` *[NON-CRITICAL CLAIM]*
> "The main tunnel breakthrough occurred in Baisakh 2081 BS."

Select one verdict:
- [ ] Supported
- [ ] Contradicted
- [ ] Not-in-context

Rationale / Notes: [                                                 ]

### Item Annotation Metadata
Stopwatch Elapsed Time: [ mm:ss ]
Item Notes: [                                                 ]

---
