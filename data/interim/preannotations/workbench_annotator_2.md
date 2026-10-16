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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [पशुपतिनाथ मन्दिर](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A4%B6%E0%A5%81%E0%A4%AA%E0%A4%A4%E0%A4%BF%E0%A4%A8%E0%A4%BE%E0%A4%A5_%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%B0)

### Context Passage (Nepali · Condition C1)
> पशुपतिनाथको मन्दिर काठमाडौँ जिल्लामा रहेको ऐतिहासिक, धार्मिक एवं पर्यटकीय दृष्टिले महत्त्वपूर्ण स्थल हो। यो मन्दिर काठमाडौँ महानगरपालिका वडा नम्बर ८ मा बागमती नदीको किनारमा रहेको छ। यो मन्दिर २४० हेक्टर जग्गामा फैलिएको छ। पशुपतिनाथको मन्दिर सांस्कृतिक सम्पदा अन्तर्गत युनेस्को विश्व सम्पदा क्षेत्रमा सूचीकृत छ। यो हिन्दूहरूको एक पवित्र तीर्थस्थल मानिन्छ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [चाँगुनारायण मन्दिर](https://ne.wikipedia.org/wiki/%E0%A4%9A%E0%A4%BE%E0%A4%81%E0%A4%97%E0%A5%81%E0%A4%A8%E0%A4%BE%E0%A4%B0%E0%A4%BE%E0%A4%AF%E0%A4%A3_%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%B0)

### Context Passage (Nepali · Condition C1)
> चाँगुनारायण मन्दिर नेपालको एक प्रसिद्ध मन्दिर हो। यो भक्तपुर जिल्लाको चाँगुनारायण नगरपालिकामा अवस्थित छ। यो काठमाडौँ उपत्यकाको प्राचीनतम मन्दिरहरू मध्ये एक मानिन्छ। यस मन्दिर परिसरमा वि.सं. ५२१ मा राजा मानदेव प्रथमले स्थापना गरेको ऐतिहासिक गरुडध्वज शिलालेख रहेको छ, जुन नेपालको इतिहासको सबैभन्दा पुरानो प्रमाणिक अभिलेख हो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [स्वयम्भूनाथ](https://ne.wikipedia.org/wiki/%E0%A4%B8%E0%A5%8D%E0%A4%B5%E0%A4%AF%E0%A4%AE%E0%A5%8D%E0%A4%AD%E0%A5%82%E0%A4%A8%E0%A4%BE%E0%A4%A5)

### Context Passage (Nepali · Condition C1)
> स्वयम्भूनाथ काठमाडौँ उपत्यकाको पश्चिममा अवस्थित एक प्रसिद्ध बौद्ध स्तूप हो। यसलाई नेवारी भाषामा 'सिङ्गु' भनिन्छ। यस स्तूपलाई विदेशीहरूले 'मङ्की टेम्पल' पनि भन्ने गर्दछन्। स्तूपको मुख्य भागमा चारै दिशामा तथागत बुद्धका आँखाहरू चित्रित गरिएका छन्, जसले सर्वव्यापी ज्ञान र करुणाको प्रतीक जनाउँछ। सन् १९७९ मा युनेस्कोले यसलाई विश्व सम्पदा सूचीमा समावेश गरेको थियो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [बौद्धनाथ](https://ne.wikipedia.org/wiki/%E0%A4%AC%E0%A5%8C%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%A8%E0%A4%BE%E0%A4%A5)

### Context Passage (Nepali · Condition C1)
> बौद्धनाथ काठमाडौँको पूर्वी भागमा अवस्थित प्रसिद्ध बौद्ध स्तूप तथा तीर्थस्थल हो। यो विश्वकै ठूला स्तूपहरू मध्ये एक मानिन्छ। तिब्बती बौद्ध धर्मावलम्बीहरूका लागि यो अत्यन्त पवित्र धार्मिक केन्द्र हो। सन् १९७९ मा बौद्धनाथ युनेस्को विश्व सम्पदा सूचीमा सूचीकृत भएको थियो। वि.सं. २०७२ को महाभूकम्पबाट क्षतिग्रस्त भएको यस स्तूपको पुनर्निर्माण सम्पन्न भइसकेको छ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [भक्तपुर दरबार क्षेत्र](https://ne.wikipedia.org/wiki/%E0%A4%AD%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%AA%E0%A5%81%E0%A4%B0_%E0%A4%A6%E0%A4%B0%E0%A4%AC%E0%A4%BE%E0%A4%B0_%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4%B0)

### Context Passage (Nepali · Condition C1)
> भक्तपुर दरबार क्षेत्र भक्तपुर नगरको मध्यभागमा अवस्थित ऐतिहासिक तथा सांस्कृतिक सम्पदा क्षेत्र हो। यहाँ मल्लकालीन ५५ झ्याले दरबार, न्यातपोल मन्दिर, भैरवनाथ मन्दिर र सुनढोका जस्ता उत्कृष्ट वास्तुकलाका नमुनाहरू रहेका छन्। राजा भूपतिन्द्र मल्लले निर्माण गर्न लगाएको न्यातपोल मन्दिर नेपालकै सबैभन्दा अग्लो पाँचतले प्यागोडा शैलीको मन्दिर हो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [पाटन दरबार क्षेत्र](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A4%BE%E0%A4%9F%E0%A4%A8_%E0%A4%A6%E0%A4%B0%E0%A4%AC%E0%A4%BE%E0%A4%B0_%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4%B0)

### Context Passage (Nepali · Condition C1)
> पाटन दरबार क्षेत्र ललितपुर महानगरपालिकाको केन्द्रमा अवस्थित ऐतिहासिक मल्लकालीन दरबार परिसर हो। यहाँ प्रसिद्ध कृष्ण मन्दिर, भीमसेन मन्दिर, विश्वनाथ मन्दिर र चार नारायण मन्दिरहरू रहेका छन्। राजा सिद्धिनरसिंह मल्लद्वारा निर्मित कृष्ण मन्दिर २१ वटा गजुर भएको शिखर शैलीको अनुपम ढुङ्गे कलाकृति हो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [लुम्बिनी](https://ne.wikipedia.org/wiki/%E0%A4%B2%E0%A5%81%E0%A4%AE%E0%A5%8D%E0%A4%AC%E0%A4%BF%E0%A4%A8%E0%A5%80)

### Context Passage (Nepali · Condition C1)
> लुम्बिनी रुपन्देही जिल्लामा अवस्थित गौतम बुद्धको जन्मस्थल हो। यो विश्वभरका बौद्ध धर्मावलम्बीहरूको प्रमुख तीर्थस्थल हो। यहाँ ईसापूर्व २४९ मा मौर्य सम्राट अशोकले स्थापना गरेको प्रसिद्ध अशोक स्तम्भ, मायादेवी मन्दिर, र पवित्र पुष्करिणी पोखरी रहेका छन्। सन् १९९७ मा लुम्बिनीलाई युनेस्कोले विश्व सम्पदा सूचीमा सूचीकृत गरेको थियो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [जानकी मन्दिर](https://ne.wikipedia.org/wiki/%E0%A4%9C%E0%A4%BE%E0%A4%A8%E0%A4%95%E0%A5%80_%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%B0)

### Context Passage (Nepali · Condition C1)
> जानकी मन्दिर धनुषा जिल्लाको जनकपुरधामको केन्द्रमा अवस्थित प्रसिद्ध हिन्दू मन्दिर हो। यो मन्दिर माता सीताको जन्मस्थलको सम्झनामा निर्माण गरिएको हो। सन् १९११ मा टिकमगढकी महारानी वृषभानु कुँवरीले नौ लाख चाँदीका असर्फी खर्चेर निर्माण गराएकाले यसलाई 'नौ लखा मन्दिर' पनि भनिन्छ। यो मन्दिर मुगल र राजपुत वास्तुकलाको सुन्दर सम्मिश्रण हो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [पशुपतिनाथ मन्दिर](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A4%B6%E0%A5%81%E0%A4%AA%E0%A4%A4%E0%A4%BF%E0%A4%A8%E0%A4%BE%E0%A4%A5_%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%B0)

### Context Passage (Nepali · Condition C1)
> पशुपतिनाथको मन्दिर काठमाडौँ जिल्लामा रहेको ऐतिहासिक, धार्मिक एवं पर्यटकीय दृष्टिले महत्त्वपूर्ण स्थल हो। यो मन्दिर काठमाडौँ महानगरपालिका वडा नम्बर ८ मा बागमती नदीको किनारमा रहेको छ। यो मन्दिर २४० हेक्टर जग्गामा फैलिएको छ। पशुपतिनाथको मन्दिर सांस्कृतिक सम्पदा अन्तर्गत युनेस्को विश्व सम्पदा क्षेत्रमा सूचीकृत छ। यो हिन्दूहरूको एक पवित्र तीर्थस्थल मानिन्छ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [चाँगुनारायण मन्दिर](https://ne.wikipedia.org/wiki/%E0%A4%9A%E0%A4%BE%E0%A4%81%E0%A4%97%E0%A5%81%E0%A4%A8%E0%A4%BE%E0%A4%B0%E0%A4%BE%E0%A4%AF%E0%A4%A3_%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%B0)

### Context Passage (Nepali · Condition C1)
> चाँगुनारायण मन्दिर नेपालको एक प्रसिद्ध मन्दिर हो। यो भक्तपुर जिल्लाको चाँगुनारायण नगरपालिकामा अवस्थित छ। यो काठमाडौँ उपत्यकाको प्राचीनतम मन्दिरहरू मध्ये एक मानिन्छ। यस मन्दिर परिसरमा वि.सं. ५२१ मा राजा मानदेव प्रथमले स्थापना गरेको ऐतिहासिक गरुडध्वज शिलालेख रहेको छ, जुन नेपालको इतिहासको सबैभन्दा पुरानो प्रमाणिक अभिलेख हो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [स्वयम्भूनाथ](https://ne.wikipedia.org/wiki/%E0%A4%B8%E0%A5%8D%E0%A4%B5%E0%A4%AF%E0%A4%AE%E0%A5%8D%E0%A4%AD%E0%A5%82%E0%A4%A8%E0%A4%BE%E0%A4%A5)

### Context Passage (Nepali · Condition C1)
> स्वयम्भूनाथ काठमाडौँ उपत्यकाको पश्चिममा अवस्थित एक प्रसिद्ध बौद्ध स्तूप हो। यसलाई नेवारी भाषामा 'सिङ्गु' भनिन्छ। यस स्तूपलाई विदेशीहरूले 'मङ्की टेम्पल' पनि भन्ने गर्दछन्। स्तूपको मुख्य भागमा चारै दिशामा तथागत बुद्धका आँखाहरू चित्रित गरिएका छन्, जसले सर्वव्यापी ज्ञान र करुणाको प्रतीक जनाउँछ। सन् १९७९ मा युनेस्कोले यसलाई विश्व सम्पदा सूचीमा समावेश गरेको थियो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [बौद्धनाथ](https://ne.wikipedia.org/wiki/%E0%A4%AC%E0%A5%8C%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%A8%E0%A4%BE%E0%A4%A5)

### Context Passage (Nepali · Condition C1)
> बौद्धनाथ काठमाडौँको पूर्वी भागमा अवस्थित प्रसिद्ध बौद्ध स्तूप तथा तीर्थस्थल हो। यो विश्वकै ठूला स्तूपहरू मध्ये एक मानिन्छ। तिब्बती बौद्ध धर्मावलम्बीहरूका लागि यो अत्यन्त पवित्र धार्मिक केन्द्र हो। सन् १९७९ मा बौद्धनाथ युनेस्को विश्व सम्पदा सूचीमा सूचीकृत भएको थियो। वि.सं. २०७२ को महाभूकम्पबाट क्षतिग्रस्त भएको यस स्तूपको पुनर्निर्माण सम्पन्न भइसकेको छ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [भक्तपुर दरबार क्षेत्र](https://ne.wikipedia.org/wiki/%E0%A4%AD%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%AA%E0%A5%81%E0%A4%B0_%E0%A4%A6%E0%A4%B0%E0%A4%AC%E0%A4%BE%E0%A4%B0_%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4%B0)

### Context Passage (Nepali · Condition C1)
> भक्तपुर दरबार क्षेत्र भक्तपुर नगरको मध्यभागमा अवस्थित ऐतिहासिक तथा सांस्कृतिक सम्पदा क्षेत्र हो। यहाँ मल्लकालीन ५५ झ्याले दरबार, न्यातपोल मन्दिर, भैरवनाथ मन्दिर र सुनढोका जस्ता उत्कृष्ट वास्तुकलाका नमुनाहरू रहेका छन्। राजा भूपतिन्द्र मल्लले निर्माण गर्न लगाएको न्यातपोल मन्दिर नेपालकै सबैभन्दा अग्लो पाँचतले प्यागोडा शैलीको मन्दिर हो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [पाटन दरबार क्षेत्र](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A4%BE%E0%A4%9F%E0%A4%A8_%E0%A4%A6%E0%A4%B0%E0%A4%AC%E0%A4%BE%E0%A4%B0_%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4%B0)

### Context Passage (Nepali · Condition C1)
> पाटन दरबार क्षेत्र ललितपुर महानगरपालिकाको केन्द्रमा अवस्थित ऐतिहासिक मल्लकालीन दरबार परिसर हो। यहाँ प्रसिद्ध कृष्ण मन्दिर, भीमसेन मन्दिर, विश्वनाथ मन्दिर र चार नारायण मन्दिरहरू रहेका छन्। राजा सिद्धिनरसिंह मल्लद्वारा निर्मित कृष्ण मन्दिर २१ वटा गजुर भएको शिखर शैलीको अनुपम ढुङ्गे कलाकृति हो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [लुम्बिनी](https://ne.wikipedia.org/wiki/%E0%A4%B2%E0%A5%81%E0%A4%AE%E0%A5%8D%E0%A4%AC%E0%A4%BF%E0%A4%A8%E0%A5%80)

### Context Passage (Nepali · Condition C1)
> लुम्बिनी रुपन्देही जिल्लामा अवस्थित गौतम बुद्धको जन्मस्थल हो। यो विश्वभरका बौद्ध धर्मावलम्बीहरूको प्रमुख तीर्थस्थल हो। यहाँ ईसापूर्व २४९ मा मौर्य सम्राट अशोकले स्थापना गरेको प्रसिद्ध अशोक स्तम्भ, मायादेवी मन्दिर, र पवित्र पुष्करिणी पोखरी रहेका छन्। सन् १९९७ मा लुम्बिनीलाई युनेस्कोले विश्व सम्पदा सूचीमा सूचीकृत गरेको थियो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [सगरमाथा राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B8%E0%A4%97%E0%A4%B0%E0%A4%AE%E0%A4%BE%E0%A4%A5%E0%A4%BE_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> सगरमाथा राष्ट्रिय निकुञ्ज पूर्वी नेपालको सोलुखुम्बु जिल्लामा अवस्थित छ। यस निकुञ्जको क्षेत्रफल १,१४८ वर्ग किलोमिटर रहेको छ। यस क्षेत्रमा विश्वको सर्वोच्च शिखर सगरमाथा (८,८४८.८६ मिटर) का साथै ल्होत्से, नुप्त्से, चोयु र आमादब्लम जस्ता हिमालहरू पर्दछन्। यहाँ दुर्लभ हिमचितुवा, कस्तुरी मृग र रातो पाण्डा पाइन्छन्। सन् १९७९ मा यो विश्व सम्पदा सूचीमा सूचीकृत भएको थियो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [चितवन राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%9A%E0%A4%BF%E0%A4%A4%E0%A4%B5%E0%A4%A8_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> चितवन राष्ट्रिय निकुञ्ज नेपालको पहिलो राष्ट्रिय निकुञ्ज हो, जसको स्थापना वि.सं. २०३० (सन् १९७३) मा भएको थियो। ९५२.६३ वर्ग किलोमिटर क्षेत्रफलमा फैलिएको यो निकुञ्ज एकसिंगे गैँडा, पाटे बाघ, घडियाल गोही र विभिन्न प्रजातिका चराचुरुङ्गीहरूको प्रमुख बासस्थान हो। जैविक विविधताको दृष्टिले महत्त्वपूर्ण यो निकुञ्ज सन् १९८४ मा युनेस्को विश्व सम्पदा सूचीमा समावेश गरिएको थियो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [बर्दिया राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%AC%E0%A4%B0%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%AF%E0%A4%BE_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> बर्दिया राष्ट्रिय निकुञ्ज तराई क्षेत्रमा अवस्थित नेपालको सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज हो, जसको क्षेत्रफल ९६८ वर्ग किलोमिटर रहेको छ। यो निकुञ्ज पाटे बाघ, जंगली हात्ती र एकसिंगे गैँडाको महत्त्वपूर्ण संरक्षण क्षेत्र हो। यहाँ बबई र कर्णाली नदीको तटीय क्षेत्रमा घडियाल गोही तथा डल्फिन समेत पाइन्छन्।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [रारा राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B0%E0%A4%BE%E0%A4%B0%E0%A4%BE_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> रारा राष्ट्रिय निकुञ्ज कर्णाली प्रदेशको मुगु र जुम्ला जिल्लामा अवस्थित नेपालको सबैभन्दा सानो राष्ट्रिय निकुञ्ज हो। यस निकुञ्जको मुख्य आकर्षण नेपालको सबैभन्दा ठूलो र गहिरो ताल 'रारा ताल' हो। समुद्र सतहबाट २,९९० मिटरको उचाइमा रहेको रारा तालको गहिराइ करिब १६७ मिटर रहेको छ। यहाँ कस्तुरी मृग र डाँफे चरा पाइन्छन्।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [शे-फोक्सुण्डो राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B6%E0%A5%87-%E0%A4%AB%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%B8%E0%A5%81%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A5%8B_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> शे-फोक्सुण्डो राष्ट्रिय निकुञ्ज नेपालको सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज हो, जसको क्षेत्रफल ३,५५५ वर्ग किलोमिटर रहेको छ। यो निकुञ्ज डोल्पा र मुगु जिल्लामा फैलिएको छ। यस निकुञ्जभित्र समुद्र सतहबाट ३,६११ मिटरको उचाइमा अवस्थित प्रसिद्ध गहिरो फोक्सुण्डो ताल रहेको छ। यहाँ तिब्बती पठारको हिमाली पारिस्थितिक प्रणाली र हिमचितुवा पाइन्छन्।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [लाङटाङ राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B2%E0%A4%BE%E0%A4%99%E0%A4%9F%E0%A4%BE%E0%A4%99_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> लाङटाङ राष्ट्रिय निकुञ्ज काठमाडौँ उपत्यकाको नजिक रहेको हिमाली निकुञ्ज हो, जुन रसुवा, नुवाकोट र सिन्धुपाल्चोक जिल्लामा फैलिएको छ। १,७१० वर्ग किलोमिटर क्षेत्रफल रहेको यस निकुञ्जमा लाङटाङ लिरुङ हिमाल, गोसाइँकुण्ड र लाङटाङ उपत्यका रहेका छन्। यो निकुञ्ज रातो पाण्डा (रेड पाण्डा) को प्रमुख बासस्थान मानिन्छ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [अन्नपूर्ण संरक्षण क्षेत्र](https://ne.wikipedia.org/wiki/%E0%A4%85%E0%A4%A8%E0%A5%8D%E0%A4%A8%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%A3_%E0%A4%B8%E0%A4%82%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%A3_%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4%B0)

### Context Passage (Nepali · Condition C1)
> अन्नपूर्ण संरक्षण क्षेत्र नेपालको सबैभन्दा ठूलो संरक्षित क्षेत्र हो, जसको क्षेत्रफल ७,६२९ वर्ग किलोमिटर रहेको छ। राष्ट्रिय प्रकृति संरक्षण कोष (एनटीएनसी) द्वारा समुदायमा आधारित व्यवस्थापन गरिएको यो क्षेत्र पदयात्राका लागि विश्वमै प्रसिद्ध छ। यहाँ अन्नपूर्ण हिमशृंखला, कालीगण्डकी गल्छी, र मुक्तिनाथ मन्दिर अवस्थित छन्।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [सगरमाथा राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B8%E0%A4%97%E0%A4%B0%E0%A4%AE%E0%A4%BE%E0%A4%A5%E0%A4%BE_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> सगरमाथा राष्ट्रिय निकुञ्ज पूर्वी नेपालको सोलुखुम्बु जिल्लामा अवस्थित छ। यस निकुञ्जको क्षेत्रफल १,१४८ वर्ग किलोमिटर रहेको छ। यस क्षेत्रमा विश्वको सर्वोच्च शिखर सगरमाथा (८,८४८.८६ मिटर) का साथै ल्होत्से, नुप्त्से, चोयु र आमादब्लम जस्ता हिमालहरू पर्दछन्। यहाँ दुर्लभ हिमचितुवा, कस्तुरी मृग र रातो पाण्डा पाइन्छन्। सन् १९७९ मा यो विश्व सम्पदा सूचीमा सूचीकृत भएको थियो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [चितवन राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%9A%E0%A4%BF%E0%A4%A4%E0%A4%B5%E0%A4%A8_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> चितवन राष्ट्रिय निकुञ्ज नेपालको पहिलो राष्ट्रिय निकुञ्ज हो, जसको स्थापना वि.सं. २०३० (सन् १९७३) मा भएको थियो। ९५२.६३ वर्ग किलोमिटर क्षेत्रफलमा फैलिएको यो निकुञ्ज एकसिंगे गैँडा, पाटे बाघ, घडियाल गोही र विभिन्न प्रजातिका चराचुरुङ्गीहरूको प्रमुख बासस्थान हो। जैविक विविधताको दृष्टिले महत्त्वपूर्ण यो निकुञ्ज सन् १९८४ मा युनेस्को विश्व सम्पदा सूचीमा समावेश गरिएको थियो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [बर्दिया राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%AC%E0%A4%B0%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%AF%E0%A4%BE_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> बर्दिया राष्ट्रिय निकुञ्ज तराई क्षेत्रमा अवस्थित नेपालको सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज हो, जसको क्षेत्रफल ९६८ वर्ग किलोमिटर रहेको छ। यो निकुञ्ज पाटे बाघ, जंगली हात्ती र एकसिंगे गैँडाको महत्त्वपूर्ण संरक्षण क्षेत्र हो। यहाँ बबई र कर्णाली नदीको तटीय क्षेत्रमा घडियाल गोही तथा डल्फिन समेत पाइन्छन्।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [रारा राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B0%E0%A4%BE%E0%A4%B0%E0%A4%BE_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> रारा राष्ट्रिय निकुञ्ज कर्णाली प्रदेशको मुगु र जुम्ला जिल्लामा अवस्थित नेपालको सबैभन्दा सानो राष्ट्रिय निकुञ्ज हो। यस निकुञ्जको मुख्य आकर्षण नेपालको सबैभन्दा ठूलो र गहिरो ताल 'रारा ताल' हो। समुद्र सतहबाट २,९९० मिटरको उचाइमा रहेको रारा तालको गहिराइ करिब १६७ मिटर रहेको छ। यहाँ कस्तुरी मृग र डाँफे चरा पाइन्छन्।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [शे-फोक्सुण्डो राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B6%E0%A5%87-%E0%A4%AB%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%B8%E0%A5%81%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A5%8B_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> शे-फोक्सुण्डो राष्ट्रिय निकुञ्ज नेपालको सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज हो, जसको क्षेत्रफल ३,५५५ वर्ग किलोमिटर रहेको छ। यो निकुञ्ज डोल्पा र मुगु जिल्लामा फैलिएको छ। यस निकुञ्जभित्र समुद्र सतहबाट ३,६११ मिटरको उचाइमा अवस्थित प्रसिद्ध गहिरो फोक्सुण्डो ताल रहेको छ। यहाँ तिब्बती पठारको हिमाली पारिस्थितिक प्रणाली र हिमचितुवा पाइन्छन्।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [लाङटाङ राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B2%E0%A4%BE%E0%A4%99%E0%A4%9F%E0%A4%BE%E0%A4%99_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> लाङटाङ राष्ट्रिय निकुञ्ज काठमाडौँ उपत्यकाको नजिक रहेको हिमाली निकुञ्ज हो, जुन रसुवा, नुवाकोट र सिन्धुपाल्चोक जिल्लामा फैलिएको छ। १,७१० वर्ग किलोमिटर क्षेत्रफल रहेको यस निकुञ्जमा लाङटाङ लिरुङ हिमाल, गोसाइँकुण्ड र लाङटाङ उपत्यका रहेका छन्। यो निकुञ्ज रातो पाण्डा (रेड पाण्डा) को प्रमुख बासस्थान मानिन्छ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [अन्नपूर्ण संरक्षण क्षेत्र](https://ne.wikipedia.org/wiki/%E0%A4%85%E0%A4%A8%E0%A5%8D%E0%A4%A8%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%A3_%E0%A4%B8%E0%A4%82%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%A3_%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4%B0)

### Context Passage (Nepali · Condition C1)
> अन्नपूर्ण संरक्षण क्षेत्र नेपालको सबैभन्दा ठूलो संरक्षित क्षेत्र हो, जसको क्षेत्रफल ७,६२९ वर्ग किलोमिटर रहेको छ। राष्ट्रिय प्रकृति संरक्षण कोष (एनटीएनसी) द्वारा समुदायमा आधारित व्यवस्थापन गरिएको यो क्षेत्र पदयात्राका लागि विश्वमै प्रसिद्ध छ। यहाँ अन्नपूर्ण हिमशृंखला, कालीगण्डकी गल्छी, र मुक्तिनाथ मन्दिर अवस्थित छन्।

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
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [सगरमाथा राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B8%E0%A4%97%E0%A4%B0%E0%A4%AE%E0%A4%BE%E0%A4%A5%E0%A4%BE_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### Context Passage (Nepali · Condition C1)
> सगरमाथा राष्ट्रिय निकुञ्ज पूर्वी नेपालको सोलुखुम्बु जिल्लामा अवस्थित छ। यस निकुञ्जको क्षेत्रफल १,१४८ वर्ग किलोमिटर रहेको छ। यस क्षेत्रमा विश्वको सर्वोच्च शिखर सगरमाथा (८,८४८.८६ मिटर) का साथै ल्होत्से, नुप्त्से, चोयु र आमादब्लम जस्ता हिमालहरू पर्दछन्। यहाँ दुर्लभ हिमचितुवा, कस्तुरी मृग र रातो पाण्डा पाइन्छन्। सन् १९७९ मा यो विश्व सम्पदा सूचीमा सूचीकृत भएको थियो।

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
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [सगरमाथा](https://ne.wikipedia.org/wiki/%E0%A4%B8%E0%A4%97%E0%A4%B0%E0%A4%AE%E0%A4%BE%E0%A4%A5%E0%A4%BE)

### Context Passage (Nepali · Condition C1)
> सगरमाथा विश्वको सर्वोच्च शिखर हो, जसको आधिकारिक उचाइ समुद्र सतहबाट ८,८४८.८६ मिटर (२९,०३१.७ फिट) रहेको छ। यो हिमाल नेपाल र चीन (तिब्बत) को सीमानामा महालङ्गूर हिमशृङ्खलामा अवस्थित छ। इतिहासमा पहिलो पटक सन् १९५३ मे २९ मा सर एडमन्ड हिलारी र तेन्जिङ नोर्गे शेर्पाले सगरमाथाको सफल आरोहण गरेका थिए।

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
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [पोखरा](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A5%8B%E0%A4%96%E0%A4%B0%E0%A4%BE)

### Context Passage (Nepali · Condition C1)
> पोखरा गण्डकी प्रदेशको राजधानी तथा नेपालको प्रमुख पर्यटकीय सहर हो। यो सहर फेवा ताल, बेगनास ताल, डेभिड फल्स, महेन्द्र गुफा र विन्ध्यवासिनी मन्दिरका लागि प्रसिद्ध छ। पोखराबाट माछापुच्छ्रे, अन्नपूर्ण र धौलागिरी हिमशृङ्खलाको मनोरम दृश्य नजिकबाट देख्न सकिन्छ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [कोशी नदी](https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A5%8B%E0%A4%B6%E0%A5%80_%E0%A4%A8%E0%A4%A6%E0%A5%80)

### Context Passage (Nepali · Condition C1)
> कोशी नदी नेपालको सबैभन्दा ठूलो नदी हो, जसलाई 'सप्तकोशी' पनि भनिन्छ। यो नदी सातवटा सहायक नदीहरू (सुनकोशी, भोटेकोशी, तामाकोशी, दुधकोशी, इन्द्रावती, अरुण र तमोर) मिलेर बनेको छ। चतराबाट तराई प्रवेश गर्ने यो नदी भारतको बिहार राज्यमा गङ्गा नदीमा गएर मिसिन्छ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [कालीगण्डकी नदी](https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A4%BE%E0%A4%B2%E0%A5%80%E0%A4%97%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A4%95%E0%A5%80_%E0%A4%A8%E0%A4%A6%E0%A5%80)

### Context Passage (Nepali · Condition C1)
> कालीगण्डकी नदी नेपालको एक प्रमुख तथा पवित्र नदी हो, जुन तिब्बती सीमा नजिकै दामोदर कुण्डबाट उत्पत्ति हुन्छ। यस नदीले धौलागिरी र अन्नपूर्ण हिमालको बीचमा विश्वकै सबैभन्दा गहिरो गल्छी (अन्ध गल्छी) बनाएको छ। हिन्दू धर्ममा पवित्र मानिने शालिग्राम शिला विश्वभरमा केवल कालीगण्डकी नदीमै फेला पर्दछ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [तिलिचो ताल](https://ne.wikipedia.org/wiki/%E0%A4%A4%E0%A4%BF%E0%A4%B2%E0%A4%BF%E0%A4%9A%E0%A5%8B_%E0%A4%A4%E0%A4%BE%E0%A4%B2)

### Context Passage (Nepali · Condition C1)
> तिलिचो ताल मनाङ जिल्लामा अन्नपूर्ण हिमशृङ्खलाको काखमा समुद्र सतहबाट ४,९१९ मिटरको उचाइमा अवस्थित नेपालको उच्च हिमाली ताल हो। यस तालको लम्बाइ करिब ४ किलोमिटर र चौडाइ १.२ किलोमिटर रहेको छ। वरिपरि हिउँले ढाकिएका पहाडहरूले घेरिएको यो ताल कठिन पदयात्रा तथा पर्यटकीय गन्तव्यको रूपमा परिचित छ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [सगरमाथा](https://ne.wikipedia.org/wiki/%E0%A4%B8%E0%A4%97%E0%A4%B0%E0%A4%AE%E0%A4%BE%E0%A4%A5%E0%A4%BE)

### Context Passage (Nepali · Condition C1)
> सगरमाथा विश्वको सर्वोच्च शिखर हो, जसको आधिकारिक उचाइ समुद्र सतहबाट ८,८४८.८६ मिटर (२९,०३१.७ फिट) रहेको छ। यो हिमाल नेपाल र चीन (तिब्बत) को सीमानामा महालङ्गूर हिमशृङ्खलामा अवस्थित छ। इतिहासमा पहिलो पटक सन् १९५३ मे २९ मा सर एडमन्ड हिलारी र तेन्जिङ नोर्गे शेर्पाले सगरमाथाको सफल आरोहण गरेका थिए।

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
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [पोखरा](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A5%8B%E0%A4%96%E0%A4%B0%E0%A4%BE)

### Context Passage (Nepali · Condition C1)
> पोखरा गण्डकी प्रदेशको राजधानी तथा नेपालको प्रमुख पर्यटकीय सहर हो। यो सहर फेवा ताल, बेगनास ताल, डेभिड फल्स, महेन्द्र गुफा र विन्ध्यवासिनी मन्दिरका लागि प्रसिद्ध छ। पोखराबाट माछापुच्छ्रे, अन्नपूर्ण र धौलागिरी हिमशृङ्खलाको मनोरम दृश्य नजिकबाट देख्न सकिन्छ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [कोशी नदी](https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A5%8B%E0%A4%B6%E0%A5%80_%E0%A4%A8%E0%A4%A6%E0%A5%80)

### Context Passage (Nepali · Condition C1)
> कोशी नदी नेपालको सबैभन्दा ठूलो नदी हो, जसलाई 'सप्तकोशी' पनि भनिन्छ। यो नदी सातवटा सहायक नदीहरू (सुनकोशी, भोटेकोशी, तामाकोशी, दुधकोशी, इन्द्रावती, अरुण र तमोर) मिलेर बनेको छ। चतराबाट तराई प्रवेश गर्ने यो नदी भारतको बिहार राज्यमा गङ्गा नदीमा गएर मिसिन्छ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [कालीगण्डकी नदी](https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A4%BE%E0%A4%B2%E0%A5%80%E0%A4%97%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A4%95%E0%A5%80_%E0%A4%A8%E0%A4%A6%E0%A5%80)

### Context Passage (Nepali · Condition C1)
> कालीगण्डकी नदी नेपालको एक प्रमुख तथा पवित्र नदी हो, जुन तिब्बती सीमा नजिकै दामोदर कुण्डबाट उत्पत्ति हुन्छ। यस नदीले धौलागिरी र अन्नपूर्ण हिमालको बीचमा विश्वकै सबैभन्दा गहिरो गल्छी (अन्ध गल्छी) बनाएको छ। हिन्दू धर्ममा पवित्र मानिने शालिग्राम शिला विश्वभरमा केवल कालीगण्डकी नदीमै फेला पर्दछ।

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
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [तिलिचो ताल](https://ne.wikipedia.org/wiki/%E0%A4%A4%E0%A4%BF%E0%A4%B2%E0%A4%BF%E0%A4%9A%E0%A5%8B_%E0%A4%A4%E0%A4%BE%E0%A4%B2)

### Context Passage (Nepali · Condition C1)
> तिलिचो ताल मनाङ जिल्लामा अन्नपूर्ण हिमशृङ्खलाको काखमा समुद्र सतहबाट ४,९१९ मिटरको उचाइमा अवस्थित नेपालको उच्च हिमाली ताल हो। यस तालको लम्बाइ करिब ४ किलोमिटर र चौडाइ १.२ किलोमिटर रहेको छ। वरिपरि हिउँले ढाकिएका पहाडहरूले घेरिएको यो ताल कठिन पदयात्रा तथा पर्यटकीय गन्तव्यको रूपमा परिचित छ।

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
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [गाभी उच्चस्तरीय टोलीसँग स्वास्थ्यमन्त्रीको छलफल: राष्ट्रिय खोप कार्यक्रम](https://gorkhapatraonline.com/news/207198)

### Context Passage (Nepali · Condition C1)
> स्वास्थ्य तथा जनसङ्ख्या मन्त्रालय र गाभी (ग्लोबल एलायन्स फर भ्याक्सिन्स एन्ड इम्युनाइजेसन) को उच्चस्तरीय टोलीबीच नेपालको राष्ट्रिय खोप कार्यक्रम सुदृढीकरणबारे छलफल भएको छ। नेपालमा बालबालिकालाई निःशुल्क रूपमा प्रदान गरिँदै आएको नियमित खोप कभरेज विस्तार गर्न र दुर्गम क्षेत्रमा खोप सेवा सुरक्षित रूपमा पुर्‍याउन सहयोग निरन्तर रहने गाभीले जनाएको छ। मन्त्रालयले दादुरा-रुबेला, पोलियो र एचपीभी खोप अभियानलाई प्राथमिकतामा राखेको जनाएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [स्वास्थ्य अनुसन्धान: क्यान्सर तथा नसर्ने रोग रोकथाम](https://www.gorkhapatraonline.com/news/111744)

### Context Passage (Nepali · Condition C1)
> स्वास्थ्य विज्ञहरूका अनुसार नेपालमा नसर्ने रोगहरू (मुटुरोग, क्यान्सर र मधुमेह) का कारण हुने मृत्युदर कुल मृत्युको ७० प्रतिशतभन्दा माथि पुगेको छ। अस्वस्थ खानपान, शारीरिक निष्क्रियता र सुर्तीजन्य पदार्थको प्रयोगले क्यान्सर तथा उच्च रक्तचापको जोखिम बढाएको अध्ययनले देखाएको छ। स्वास्थ्य सेवा विभागले नसर्ने रोगको रोकथाम तथा स्क्रिनिङका लागि प्राथमिक स्वास्थ्य केन्द्रस्तरमै विशेष कार्यक्रम सञ्चालन गर्नुपर्नेमा जोड दिएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [मातृ बाल मृत्युदर न्यूनीकरण: सुरक्षित मातृत्व कार्यक्रम](https://gorkhapatraonline.com/index.php/news/202136)

### Context Passage (Nepali · Condition C1)
> स्वास्थ्य तथा जनसङ्ख्या मन्त्रालयले सुरक्षित मातृत्व तथा मातृ बाल मृत्युदर न्यूनीकरणलाई मुख्य प्राथमिकता दिएको छ। राष्ट्रिय जनगणना २०७८ को अध्ययन अनुसार नेपालमा मातृ मृत्युदर प्रति लाख जीवित जन्ममा १५१ मा झरेको छ। सरकारी स्वास्थ्य संस्थाहरूमा निःशुल्क प्रसूति सेवा र यातायात खर्च उपलब्ध गराइएपछि संस्थागत सुत्केरी दरमा उल्लेख्य वृद्धि भएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [स्वास्थ्य मन्त्रालय डेंगु नियन्त्रण तथा लामखुट्टे रोकथाम निर्देशिका](https://www.onlinekhabar.com/2022/10/1206660/%E0%A4%B8%E0%A5%8D%E0%A4%B5%E0%A4%BE%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A5%8D%E0%A4%AF-%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%B2%E0%A4%AF%E0%A4%95%E0%A4%BE-%E0%A5%AB)

### Context Passage (Nepali · Condition C1)
> स्वास्थ्य तथा जनसङ्ख्या मन्त्रालयले डेंगु सङ्क्रमण तीव्र रूपमा फैलिएपछि देशव्यापी सतर्कता अपनाउन र लामखुट्टेको लार्भा नष्ट गर्ने 'खोज र नष्ट गर' अभियान चलाउन निर्देशन दिएको छ। एडिस प्रजातिको लामखुट्टेको टोकाइबाट सर्ने यो रोगका कारण हजारौँ नागरिक प्रभावित भएका छन्। स्वास्थ्य मन्त्रालयले सबै सरकारी अस्पतालहरूमा डेंगुका बिरामीका लागि निःशुल्क परामर्श तथा उपचार डेस्क स्थापना गरेको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [औषधि व्यवस्था विभाग: बजार अनुगमन तथा गुणस्तर नियन्त्रण](https://gorkhapatraonline.com/news/26125)

### Context Passage (Nepali · Condition C1)
> औषधि व्यवस्था विभागले बजारमा बिक्रीवितरण भइरहेका औषधिको गुणस्तर सुनिश्चित गर्न र अनुचित व्यापारिक क्रियाकलाप नियन्त्रण गर्न विशेष अनुगमन टोली परिचालन गरेको छ। सरकारले गुणस्तरहीन औषधि बिक्री गर्ने फार्मेसीहरूलाई कारबाही गर्ने र जीवनरक्षक औषधिको अभाव हुन नदिन आपूर्ति व्यवस्थापन कडा बनाएको जनाएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [गाभी उच्चस्तरीय टोलीसँग स्वास्थ्यमन्त्रीको छलफल: राष्ट्रिय खोप कार्यक्रम](https://gorkhapatraonline.com/news/207198)

### Context Passage (Nepali · Condition C1)
> स्वास्थ्य तथा जनसङ्ख्या मन्त्रालय र गाभी (ग्लोबल एलायन्स फर भ्याक्सिन्स एन्ड इम्युनाइजेसन) को उच्चस्तरीय टोलीबीच नेपालको राष्ट्रिय खोप कार्यक्रम सुदृढीकरणबारे छलफल भएको छ। नेपालमा बालबालिकालाई निःशुल्क रूपमा प्रदान गरिँदै आएको नियमित खोप कभरेज विस्तार गर्न र दुर्गम क्षेत्रमा खोप सेवा सुरक्षित रूपमा पुर्‍याउन सहयोग निरन्तर रहने गाभीले जनाएको छ। मन्त्रालयले दादुरा-रुबेला, पोलियो र एचपीभी खोप अभियानलाई प्राथमिकतामा राखेको जनाएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [स्वास्थ्य अनुसन्धान: क्यान्सर तथा नसर्ने रोग रोकथाम](https://www.gorkhapatraonline.com/news/111744)

### Context Passage (Nepali · Condition C1)
> स्वास्थ्य विज्ञहरूका अनुसार नेपालमा नसर्ने रोगहरू (मुटुरोग, क्यान्सर र मधुमेह) का कारण हुने मृत्युदर कुल मृत्युको ७० प्रतिशतभन्दा माथि पुगेको छ। अस्वस्थ खानपान, शारीरिक निष्क्रियता र सुर्तीजन्य पदार्थको प्रयोगले क्यान्सर तथा उच्च रक्तचापको जोखिम बढाएको अध्ययनले देखाएको छ। स्वास्थ्य सेवा विभागले नसर्ने रोगको रोकथाम तथा स्क्रिनिङका लागि प्राथमिक स्वास्थ्य केन्द्रस्तरमै विशेष कार्यक्रम सञ्चालन गर्नुपर्नेमा जोड दिएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [मातृ बाल मृत्युदर न्यूनीकरण: सुरक्षित मातृत्व कार्यक्रम](https://gorkhapatraonline.com/index.php/news/202136)

### Context Passage (Nepali · Condition C1)
> स्वास्थ्य तथा जनसङ्ख्या मन्त्रालयले सुरक्षित मातृत्व तथा मातृ बाल मृत्युदर न्यूनीकरणलाई मुख्य प्राथमिकता दिएको छ। राष्ट्रिय जनगणना २०७८ को अध्ययन अनुसार नेपालमा मातृ मृत्युदर प्रति लाख जीवित जन्ममा १५१ मा झरेको छ। सरकारी स्वास्थ्य संस्थाहरूमा निःशुल्क प्रसूति सेवा र यातायात खर्च उपलब्ध गराइएपछि संस्थागत सुत्केरी दरमा उल्लेख्य वृद्धि भएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [स्वास्थ्य मन्त्रालय डेंगु नियन्त्रण तथा लामखुट्टे रोकथाम निर्देशिका](https://www.onlinekhabar.com/2022/10/1206660/%E0%A4%B8%E0%A5%8D%E0%A4%B5%E0%A4%BE%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A5%8D%E0%A4%AF-%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%B2%E0%A4%AF%E0%A4%95%E0%A4%BE-%E0%A5%AB)

### Context Passage (Nepali · Condition C1)
> स्वास्थ्य तथा जनसङ्ख्या मन्त्रालयले डेंगु सङ्क्रमण तीव्र रूपमा फैलिएपछि देशव्यापी सतर्कता अपनाउन र लामखुट्टेको लार्भा नष्ट गर्ने 'खोज र नष्ट गर' अभियान चलाउन निर्देशन दिएको छ। एडिस प्रजातिको लामखुट्टेको टोकाइबाट सर्ने यो रोगका कारण हजारौँ नागरिक प्रभावित भएका छन्। स्वास्थ्य मन्त्रालयले सबै सरकारी अस्पतालहरूमा डेंगुका बिरामीका लागि निःशुल्क परामर्श तथा उपचार डेस्क स्थापना गरेको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [औषधि व्यवस्था विभाग: बजार अनुगमन तथा गुणस्तर नियन्त्रण](https://gorkhapatraonline.com/news/26125)

### Context Passage (Nepali · Condition C1)
> औषधि व्यवस्था विभागले बजारमा बिक्रीवितरण भइरहेका औषधिको गुणस्तर सुनिश्चित गर्न र अनुचित व्यापारिक क्रियाकलाप नियन्त्रण गर्न विशेष अनुगमन टोली परिचालन गरेको छ। सरकारले गुणस्तरहीन औषधि बिक्री गर्ने फार्मेसीहरूलाई कारबाही गर्ने र जीवनरक्षक औषधिको अभाव हुन नदिन आपूर्ति व्यवस्थापन कडा बनाएको जनाएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [कृषि मन्त्रालय: धान उत्पादन चार प्रतिशतले वृद्धि](https://gorkhapatraonline.com/news/137532)

### Context Passage (Nepali · Condition C1)
> कृषि तथा पशुपन्छी विकास मन्त्रालयका अनुसार चालु आर्थिक वर्ष २०८१/८२ मा धानको उत्पादन ४.०४ प्रतिशतले बढेर ५९ लाख ५५ हजार ४७६ मेट्रिक टन पुगेको छ। गत आर्थिक वर्षमा ५७ लाख २४ हजार मेट्रिक टन धान उत्पादन भएको थियो। समयमा रासायनिक मलको उपलब्धता, उन्नत बीउबिजन र अनुकूल वर्षाका कारण धानको उत्पादकत्व प्रतिहेक्टर ४.१९ मेट्रिक टन पुगेको मन्त्रालयले जनाएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [रासायनिक मल आपूर्ति तथा अनुदान व्यवस्थापन](https://gorkhapatraonline.com/news/71329)

### Context Passage (Nepali · Condition C1)
> सरकारले किसानलाई रासायनिक मलको अभाव हुन नदिन अनुदान नीतिलाई प्रभावकारी बनाएको छ। साल्ट ट्रेडिङ कर्पोरेसन र कृषि सामग्री कम्पनी लिमिटेडमार्फत युरिया, डीएपी र पोटास मलको आयात व्यवस्थित गरिएको छ। असारे धान रोपाइँका बेला मलको सहज उपलब्धता सुनिश्चित गर्न मन्त्रालयले अन्तरनिकाय समन्वय समिति गठन गरेको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [प्रधानमन्त्री कृषि आधुनिकीकरण परियोजना: झापा धान सुपरजोन](https://gorkhapatraonline.com/news/19549)

### Context Passage (Nepali · Condition C1)
> प्रधानमन्त्री कृषि आधुनिकीकरण परियोजना अन्तर्गत झापा जिल्लामा सञ्चालित धान सुपरजोन कार्यक्रममार्फत उत्पादकत्व उल्लेख्य रूपमा बढेको छ। परियोजना कार्यान्वयन एकाइका अनुसार आधुनिक कृषि यन्त्र, चक्लाबन्दी र सिँचाइ विस्तारका कारण पाँच वर्षअघि प्रतिहेक्टर ४.६९ मेट्रिक टन रहेको उत्पादकत्व बढेर ५.६ मेट्रिक टन पुगेको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [राष्ट्रिय चिया तथा कफी विकास बोर्ड: नेपाली चिया निर्यात समीक्षा](https://gorkhapatraonline.com/news/105422)

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय चिया तथा कफी विकास बोर्डका अनुसार नेपाली अर्थोडक्स चियाको अन्तर्राष्ट्रिय बजार विस्तारका लागि नयाँ रणनीति तय गरिएको छ। कुल चिया निर्यातमध्ये ठूलो हिस्सा छिमेकी भारतमा निकासी हुने गरेकोमा अब युरोपेली तथा अमेरिकी बजारमा प्रत्यक्ष निर्यात बढाउन गुणस्तर प्रमाणीकरण र ब्राण्डिङलाई प्राथमिकता दिइएको बोर्डले जनाएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [पशु सेवा विभाग: दुग्ध उत्पादन तथा आत्मनिर्भरता](https://gorkhapatraonline.com/index.php/news/79742)

### Context Passage (Nepali · Condition C1)
> पशु सेवा विभाग र राष्ट्रिय दुग्ध विकास बोर्डका अनुसार नेपाल दुग्ध उत्पादनमा आत्मनिर्भरतातर्फ अघि बढेको छ। ग्रामीण भेगका किसानहरूलाई उन्नत जातका गाईभैँसी पालनमा प्रोत्साहन, दाना अनुदान र चिस्यान केन्द्रको स्थापना गरिएपछि वार्षिक दूध उत्पादन २५ लाख मेट्रिक टन नाघेको छ। विद्यालयहरूमा दिवा खाजामा दूध समावेश गर्ने कार्यक्रम समेत सुरु गरिएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [कृषि मन्त्रालय: धान उत्पादन चार प्रतिशतले वृद्धि](https://gorkhapatraonline.com/news/137532)

### Context Passage (Nepali · Condition C1)
> कृषि तथा पशुपन्छी विकास मन्त्रालयका अनुसार चालु आर्थिक वर्ष २०८१/८२ मा धानको उत्पादन ४.०४ प्रतिशतले बढेर ५९ लाख ५५ हजार ४७६ मेट्रिक टन पुगेको छ। गत आर्थिक वर्षमा ५७ लाख २४ हजार मेट्रिक टन धान उत्पादन भएको थियो। समयमा रासायनिक मलको उपलब्धता, उन्नत बीउबिजन र अनुकूल वर्षाका कारण धानको उत्पादकत्व प्रतिहेक्टर ४.१९ मेट्रिक टन पुगेको मन्त्रालयले जनाएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [रासायनिक मल आपूर्ति तथा अनुदान व्यवस्थापन](https://gorkhapatraonline.com/news/71329)

### Context Passage (Nepali · Condition C1)
> सरकारले किसानलाई रासायनिक मलको अभाव हुन नदिन अनुदान नीतिलाई प्रभावकारी बनाएको छ। साल्ट ट्रेडिङ कर्पोरेसन र कृषि सामग्री कम्पनी लिमिटेडमार्फत युरिया, डीएपी र पोटास मलको आयात व्यवस्थित गरिएको छ। असारे धान रोपाइँका बेला मलको सहज उपलब्धता सुनिश्चित गर्न मन्त्रालयले अन्तरनिकाय समन्वय समिति गठन गरेको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [प्रधानमन्त्री कृषि आधुनिकीकरण परियोजना: झापा धान सुपरजोन](https://gorkhapatraonline.com/news/19549)

### Context Passage (Nepali · Condition C1)
> प्रधानमन्त्री कृषि आधुनिकीकरण परियोजना अन्तर्गत झापा जिल्लामा सञ्चालित धान सुपरजोन कार्यक्रममार्फत उत्पादकत्व उल्लेख्य रूपमा बढेको छ। परियोजना कार्यान्वयन एकाइका अनुसार आधुनिक कृषि यन्त्र, चक्लाबन्दी र सिँचाइ विस्तारका कारण पाँच वर्षअघि प्रतिहेक्टर ४.६९ मेट्रिक टन रहेको उत्पादकत्व बढेर ५.६ मेट्रिक टन पुगेको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [राष्ट्रिय चिया तथा कफी विकास बोर्ड: नेपाली चिया निर्यात समीक्षा](https://gorkhapatraonline.com/news/105422)

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय चिया तथा कफी विकास बोर्डका अनुसार नेपाली अर्थोडक्स चियाको अन्तर्राष्ट्रिय बजार विस्तारका लागि नयाँ रणनीति तय गरिएको छ। कुल चिया निर्यातमध्ये ठूलो हिस्सा छिमेकी भारतमा निकासी हुने गरेकोमा अब युरोपेली तथा अमेरिकी बजारमा प्रत्यक्ष निर्यात बढाउन गुणस्तर प्रमाणीकरण र ब्राण्डिङलाई प्राथमिकता दिइएको बोर्डले जनाएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [पशु सेवा विभाग: दुग्ध उत्पादन तथा आत्मनिर्भरता](https://gorkhapatraonline.com/index.php/news/79742)

### Context Passage (Nepali · Condition C1)
> पशु सेवा विभाग र राष्ट्रिय दुग्ध विकास बोर्डका अनुसार नेपाल दुग्ध उत्पादनमा आत्मनिर्भरतातर्फ अघि बढेको छ। ग्रामीण भेगका किसानहरूलाई उन्नत जातका गाईभैँसी पालनमा प्रोत्साहन, दाना अनुदान र चिस्यान केन्द्रको स्थापना गरिएपछि वार्षिक दूध उत्पादन २५ लाख मेट्रिक टन नाघेको छ। विद्यालयहरूमा दिवा खाजामा दूध समावेश गर्ने कार्यक्रम समेत सुरु गरिएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [राष्ट्रिय तथ्याङ्क कार्यालय जनगणना २०७८: साक्षरता दर प्रतिवेदन](https://gorkhapatraonline.com/news/65329)

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय तथ्याङ्क कार्यालयद्वारा सार्वजनिक राष्ट्रिय जनगणना २०७८ को नतिजा अनुसार नेपालको कुल साक्षरता दर ७६.३ प्रतिशत पुगेको छ। पुरुष साक्षरता दर ८३.६ प्रतिशत र महिला साक्षरता दर ६९.४ प्रतिशत रहेको छ। तथ्याङ्क अनुसार बागमती प्रदेशमा सबैभन्दा उच्च साक्षरता रहेको छ भने मधेश प्रदेशमा साक्षरता दर सबैभन्दा न्यून पाइएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [शिक्षा तथा मानव स्रोत विकास केन्द्र: सामुदायिक विद्यालय दिवा खाजा](https://gorkhapatraonline.com/news/183700)

### Context Passage (Nepali · Condition C1)
> शिक्षा तथा मानव स्रोत विकास केन्द्रका अनुसार देशभरका सामुदायिक विद्यालयमा सञ्चालित दिवा खाजा कार्यक्रमले विद्यार्थी भर्ना दर र टिकाउ दरमा सुधार ल्याएको छ। प्रारम्भिक बालविकासदेखि कक्षा ५ सम्मका विद्यार्थीलाई वार्षिक १८० दिनका लागि प्रति विद्यार्थी २० देखि २५ रुपैयाँका दरले खाजा रकम निकासा गरिएको छ। यस कार्यक्रमबाट देशभरका २९ लाखभन्दा बढी बालबालिका प्रत्यक्ष लाभान्वित भएका छन्।

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
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [प्राविधिक शिक्षा तथा व्यावसायिक तालिम परिषद् (सीटीईभीटी): सीप विकास](https://gorkhapatraonline.com/news/55391)

### Context Passage (Nepali · Condition C1)
> प्राविधिक शिक्षा तथा व्यावसायिक तालिम परिषद् (सीटीईभीटी) ले श्रम बजारको माग अनुसार दक्ष जनशक्ति उत्पादन गर्न ७७ वटै जिल्लामा प्राविधिक शिक्षालयको सञ्जाल विस्तार गरेको छ। इन्जिनियरिङ, स्वास्थ्य, कृषि र सूचना प्रविधिका डिप्लोमा तथा प्रि-डिप्लोमा तहका कार्यक्रममार्फत वार्षिक ६० हजारभन्दा बढी युवाहरूलाई सीपमूलक तालिम प्रदान गरिँदै आएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [राष्ट्रिय परीक्षा बोर्ड: माध्यमिक शिक्षा परीक्षा (एसईई) नतिजा](https://gorkhapatraonline.com/news/20316)

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय परीक्षा बोर्डले माध्यमिक शिक्षा परीक्षा (एसईई) को नतिजा सार्वजनिक गर्दै कुल परीक्षार्थीमध्ये ९ हजारभन्दा बढीले ३.६ देखि ४ जीपीए हासिल गरेको जनाएको छ। बोर्डले परीक्षामा ग्रेडिङ प्रणाली लागू गरी विद्यार्थीहरूको विषयगत दक्षता अभिवृद्धि गर्न नयाँ पाठ्यक्रम र उत्तरपुस्तिका परीक्षण मापदण्ड कार्यान्वयनमा ल्याएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [शिक्षा तथा मानव स्रोत विकास केन्द्र: विद्यालय शिक्षा फ्ल्यास प्रतिवेदन](https://cehrd.gov.np)

### Context Passage (Nepali · Condition C1)
> शिक्षा तथा मानव स्रोत विकास केन्द्र (सीईएचआरडी) को वार्षिक फ्ल्यास रिपोर्ट अनुसार नेपालमा आधारभूत तह (कक्षा १-८) को खुद भर्ना दर ९६ प्रतिशतभन्दा माथि पुगेको छ। सामुदायिक विद्यालयहरूमा सूचना प्रविधि प्रयोगशाला, निःशुल्क पाठ्यपुस्तक वितरण र छात्रवृत्ति कार्यक्रमले लैङ्गिक समानता हासिल गर्न सहयोग पुर्‍याएको प्रतिवेदनमा उल्लेख छ।

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
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [राष्ट्रिय तथ्याङ्क कार्यालय जनगणना २०७८: साक्षरता दर प्रतिवेदन](https://gorkhapatraonline.com/news/65329)

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय तथ्याङ्क कार्यालयद्वारा सार्वजनिक राष्ट्रिय जनगणना २०७८ को नतिजा अनुसार नेपालको कुल साक्षरता दर ७६.३ प्रतिशत पुगेको छ। पुरुष साक्षरता दर ८३.६ प्रतिशत र महिला साक्षरता दर ६९.४ प्रतिशत रहेको छ। तथ्याङ्क अनुसार बागमती प्रदेशमा सबैभन्दा उच्च साक्षरता रहेको छ भने मधेश प्रदेशमा साक्षरता दर सबैभन्दा न्यून पाइएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [शिक्षा तथा मानव स्रोत विकास केन्द्र: सामुदायिक विद्यालय दिवा खाजा](https://gorkhapatraonline.com/news/183700)

### Context Passage (Nepali · Condition C1)
> शिक्षा तथा मानव स्रोत विकास केन्द्रका अनुसार देशभरका सामुदायिक विद्यालयमा सञ्चालित दिवा खाजा कार्यक्रमले विद्यार्थी भर्ना दर र टिकाउ दरमा सुधार ल्याएको छ। प्रारम्भिक बालविकासदेखि कक्षा ५ सम्मका विद्यार्थीलाई वार्षिक १८० दिनका लागि प्रति विद्यार्थी २० देखि २५ रुपैयाँका दरले खाजा रकम निकासा गरिएको छ। यस कार्यक्रमबाट देशभरका २९ लाखभन्दा बढी बालबालिका प्रत्यक्ष लाभान्वित भएका छन्।

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
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [प्राविधिक शिक्षा तथा व्यावसायिक तालिम परिषद् (सीटीईभीटी): सीप विकास](https://gorkhapatraonline.com/news/55391)

### Context Passage (Nepali · Condition C1)
> प्राविधिक शिक्षा तथा व्यावसायिक तालिम परिषद् (सीटीईभीटी) ले श्रम बजारको माग अनुसार दक्ष जनशक्ति उत्पादन गर्न ७७ वटै जिल्लामा प्राविधिक शिक्षालयको सञ्जाल विस्तार गरेको छ। इन्जिनियरिङ, स्वास्थ्य, कृषि र सूचना प्रविधिका डिप्लोमा तथा प्रि-डिप्लोमा तहका कार्यक्रममार्फत वार्षिक ६० हजारभन्दा बढी युवाहरूलाई सीपमूलक तालिम प्रदान गरिँदै आएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [राष्ट्रिय परीक्षा बोर्ड: माध्यमिक शिक्षा परीक्षा (एसईई) नतिजा](https://gorkhapatraonline.com/news/20316)

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय परीक्षा बोर्डले माध्यमिक शिक्षा परीक्षा (एसईई) को नतिजा सार्वजनिक गर्दै कुल परीक्षार्थीमध्ये ९ हजारभन्दा बढीले ३.६ देखि ४ जीपीए हासिल गरेको जनाएको छ। बोर्डले परीक्षामा ग्रेडिङ प्रणाली लागू गरी विद्यार्थीहरूको विषयगत दक्षता अभिवृद्धि गर्न नयाँ पाठ्यक्रम र उत्तरपुस्तिका परीक्षण मापदण्ड कार्यान्वयनमा ल्याएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [शिक्षा तथा मानव स्रोत विकास केन्द्र: विद्यालय शिक्षा फ्ल्यास प्रतिवेदन](https://cehrd.gov.np)

### Context Passage (Nepali · Condition C1)
> शिक्षा तथा मानव स्रोत विकास केन्द्र (सीईएचआरडी) को वार्षिक फ्ल्यास रिपोर्ट अनुसार नेपालमा आधारभूत तह (कक्षा १-८) को खुद भर्ना दर ९६ प्रतिशतभन्दा माथि पुगेको छ। सामुदायिक विद्यालयहरूमा सूचना प्रविधि प्रयोगशाला, निःशुल्क पाठ्यपुस्तक वितरण र छात्रवृत्ति कार्यक्रमले लैङ्गिक समानता हासिल गर्न सहयोग पुर्‍याएको प्रतिवेदनमा उल्लेख छ।

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
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [अर्थ मन्त्रालय: वार्षिक बजेट वक्तव्य तथा आर्थिक विनियोजन](https://mof.gov.np/category/budget-speech)

### Context Passage (Nepali · Condition C1)
> अर्थ मन्त्रालयद्वारा प्रस्तुत वार्षिक बजेट वक्तव्यमा आर्थिक वृद्धि, उत्पादन वृद्धि र रोजगारी सिर्जनालाई प्रमुख प्राथमिकतामा राखिएको छ। सरकारले पुँजीगत खर्च बढाउन पूर्वाधार विकास आयोजनालाई समयमै बजेट निकासा गर्ने र वित्तीय अनुशासन कायम राख्ने नीति अवलम्बन गरेको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [मध्यमकालीन खर्च संरचना तथा सार्वजनिक वित्त व्यवस्थापन](https://gorkhapatraonline.com/news/61451)

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय योजना आयोग र अर्थ मन्त्रालयले सार्वजनिक स्रोतको समुचित उपयोगका लागि तीन वर्षे चक्रीय मध्यमकालीन खर्च संरचना (एमटीईएफ) कार्यान्वयन गरेका छन्। यस प्रणालीले आवधिक योजना र वार्षिक बजेटबीच तालमेल मिलाउँदै सार्वजनिक खर्चमा पारदर्शिता र वित्तीय अनुशासन कायम गर्न मद्दत पुर्‍याउँछ।

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
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [महालेखा नियन्त्रक कार्यालय: सरकारी राजस्व तथा बजेट खर्च स्थिति](https://www.gorkhapatraonline.com/news/89477)

### Context Passage (Nepali · Condition C1)
> महालेखा नियन्त्रक कार्यालयको तथ्याङ्क अनुसार चालु आर्थिक वर्षको पहिलो पाँच महिनामा सरकारको कुल आम्दानी ३ खर्ब ८३ अर्ब रुपैयाँ र कुल बजेट खर्च ४ खर्ब ५२ अर्ब रुपैयाँ पुगेको छ। सरकारले वार्षिक लक्ष्य अनुसार राजस्व संकलन बढाउन कर प्रणाली सुधार र भन्सार चुहावट नियन्त्रणमा कडाइ गरेको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [नेपाल खुद्रा व्यापार सङ्घ: उपभोक्ता मूल्य तथा मुद्रास्फीति](https://gorkhapatraonline.com/news/142145)

### Context Passage (Nepali · Condition C1)
> दैनिक उपभोग्य वस्तुहरूको बजार अनुगमन प्रतिवेदन अनुसार खाद्यान्न, खानेतेल र गेडागुडीको मूल्यमा सामान्य वृद्धि भएको छ। नेपाल खुद्रा व्यापार सङ्घ र वाणिज्य विभागले कृत्रिम अभाव र कालोबजारी नियन्त्रण गर्न संयुक्त बजार अनुगमनलाई तीव्रता दिएका छन्।

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
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [नेपाल राष्ट्र बैंक: मौद्रिक नीति तथा समष्टिगत आर्थिक समीक्षा](https://www.onlinekhabar.com/2024/07/1514858/rashtra-bank-passing-monetary-policy)

### Context Passage (Nepali · Condition C1)
> नेपाल राष्ट्र बैंकले चालु आर्थिक वर्षको मौद्रिक नीति सार्वजनिक गर्दै वित्तीय स्थायित्व र बाह्य क्षेत्र सन्तुलन कायम राख्ने नीति लिएको छ। बैंक तथा वित्तीय संस्थाहरूमा तरलता सहज बनाउन नीतिगत दर घटाउनुका साथै विदेशी विनिमय सञ्चिति २० खर्ब रुपैयाँ नाघेकाले अर्थतन्त्रको बाह्य क्षेत्र बलियो अवस्थामा रहेको केन्द्रीय बैंकले जनाएको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [अर्थ मन्त्रालय: वार्षिक बजेट वक्तव्य तथा आर्थिक विनियोजन](https://mof.gov.np/category/budget-speech)

### Context Passage (Nepali · Condition C1)
> अर्थ मन्त्रालयद्वारा प्रस्तुत वार्षिक बजेट वक्तव्यमा आर्थिक वृद्धि, उत्पादन वृद्धि र रोजगारी सिर्जनालाई प्रमुख प्राथमिकतामा राखिएको छ। सरकारले पुँजीगत खर्च बढाउन पूर्वाधार विकास आयोजनालाई समयमै बजेट निकासा गर्ने र वित्तीय अनुशासन कायम राख्ने नीति अवलम्बन गरेको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [मध्यमकालीन खर्च संरचना तथा सार्वजनिक वित्त व्यवस्थापन](https://gorkhapatraonline.com/news/61451)

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय योजना आयोग र अर्थ मन्त्रालयले सार्वजनिक स्रोतको समुचित उपयोगका लागि तीन वर्षे चक्रीय मध्यमकालीन खर्च संरचना (एमटीईएफ) कार्यान्वयन गरेका छन्। यस प्रणालीले आवधिक योजना र वार्षिक बजेटबीच तालमेल मिलाउँदै सार्वजनिक खर्चमा पारदर्शिता र वित्तीय अनुशासन कायम गर्न मद्दत पुर्‍याउँछ।

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
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [महालेखा नियन्त्रक कार्यालय: सरकारी राजस्व तथा बजेट खर्च स्थिति](https://www.gorkhapatraonline.com/news/89477)

### Context Passage (Nepali · Condition C1)
> महालेखा नियन्त्रक कार्यालयको तथ्याङ्क अनुसार चालु आर्थिक वर्षको पहिलो पाँच महिनामा सरकारको कुल आम्दानी ३ खर्ब ८३ अर्ब रुपैयाँ र कुल बजेट खर्च ४ खर्ब ५२ अर्ब रुपैयाँ पुगेको छ। सरकारले वार्षिक लक्ष्य अनुसार राजस्व संकलन बढाउन कर प्रणाली सुधार र भन्सार चुहावट नियन्त्रणमा कडाइ गरेको छ।

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
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [नेपाल खुद्रा व्यापार सङ्घ: उपभोक्ता मूल्य तथा मुद्रास्फीति](https://gorkhapatraonline.com/news/142145)

### Context Passage (Nepali · Condition C1)
> दैनिक उपभोग्य वस्तुहरूको बजार अनुगमन प्रतिवेदन अनुसार खाद्यान्न, खानेतेल र गेडागुडीको मूल्यमा सामान्य वृद्धि भएको छ। नेपाल खुद्रा व्यापार सङ्घ र वाणिज्य विभागले कृत्रिम अभाव र कालोबजारी नियन्त्रण गर्न संयुक्त बजार अनुगमनलाई तीव्रता दिएका छन्।

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
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [नेपाल राष्ट्र बैंक: मौद्रिक नीति तथा समष्टिगत आर्थिक समीक्षा](https://www.onlinekhabar.com/2024/07/1514858/rashtra-bank-passing-monetary-policy)

### Context Passage (Nepali · Condition C1)
> नेपाल राष्ट्र बैंकले चालु आर्थिक वर्षको मौद्रिक नीति सार्वजनिक गर्दै वित्तीय स्थायित्व र बाह्य क्षेत्र सन्तुलन कायम राख्ने नीति लिएको छ। बैंक तथा वित्तीय संस्थाहरूमा तरलता सहज बनाउन नीतिगत दर घटाउनुका साथै विदेशी विनिमय सञ्चिति २० खर्ब रुपैयाँ नाघेकाले अर्थतन्त्रको बाह्य क्षेत्र बलियो अवस्थामा रहेको केन्द्रीय बैंकले जनाएको छ।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [टी-२० विश्वकपका लागि नेपाली क्रिकेट टोलीको घोषणा](https://www.onlinekhabar.com/2026/01/1843313/these-are-the-15-nepali-players-who-will-play-in-the-t20-world-cup)

### Context Passage (Nepali · Condition C1)
> नेपाल क्रिकेट संघ (क्यान) ले आईसीसी पुरुष टी-२० विश्वकपका लागि १५ सदस्यीय राष्ट्रिय टोली घोषणा गरेको छ। युवा तथा अनुभवी खेलाडीहरूको समिश्रण रहेको नेपाली टोलीमा रोहित पौडेलले कप्तानी सम्हालेका छन् भने सोमपाल कामी, कुशल भुर्तेल र दीपेन्द्रसिंह ऐरी समावेश छन्। नेपाली टोलीले विश्वकपमा समूह चरणका खेलहरू प्रतिष्ठित अन्तर्राष्ट्रिय रंगशालामा खेल्ने तालिका छ।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [दीपेन्द्रसिंह ऐरी: ९ बलमा अर्धशतकको ऐतिहासिक विश्व कीर्तिमान](https://www.onlinekhabar.com/personality/dipendra-singh-airee)

### Context Passage (Nepali · Condition C1)
> नेपाली क्रिकेटका अलराउन्डर दीपेन्द्रसिंह ऐरीले अन्तर्राष्ट्रिय टी-२० क्रिकेटमा विश्वकै सबैभन्दा छिटो ९ बलमा अर्धशतक प्रहार गरी कीर्तिमान बनाएका छन्। चीनको हाङ्ग्जाउमा आयोजित १९औँ एसियाली खेलकुद अन्तर्गत मंगोलियाविरुद्धको खेलमा उनले यो दुर्लभ कीर्तिमान रचेका हुन्। यसैगरी उनले अन्तर्राष्ट्रिय खेलमा एकै ओभरमा ६ छक्का समेत प्रहार गरेका छन्।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [क्यानद्वारा नेपाल प्रिमियर लिग (एनपीएल) आयोजनाको तयारी](https://www.onlinekhabar.com/2020/01/826769/%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%A8-%E0%A4%86%E0%A4%AB%E0%A5%88%E0%A4%82%E0%A4%B2%E0%A5%87-%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2-%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AE)

### Context Passage (Nepali · Condition C1)
> नेपाल क्रिकेट संघ (क्यान) ले आधिकारिक फ्रेन्चाइज प्रतियोगिता नेपाल प्रिमियर लिग (एनपीएल) को औपचारिक तयारी सुरु गरेको छ। देशभरका प्रमुख सहरहरूलाई प्रतिनिधित्व गर्ने टोलीहरूमार्फत घरेलु क्रिकेटको व्यावसायिक विकास गर्ने र विदेशी खेलाडीहरूलाई समेत समावेश गरी प्रतियोगितालाई अन्तर्राष्ट्रिय स्तरको बनाउने क्यानको योजना छ।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [एन्फा राष्ट्रिय फुटबल लिग तथा सहिद स्मारक लिग समीक्षा](https://www.hamrokhelkud.com/football/170529.html)

### Context Passage (Nepali · Condition C1)
> अखिल नेपाल फुटबल संघ (एन्फा) ले राष्ट्रिय लिग तथा सहिद स्मारक फुटबल प्रतियोगितालाई व्यवस्थित गर्न नयाँ कार्यविधि कार्यान्वयनमा ल्याएको छ। क्लबहरूमा विदेशी खेलाडीहरूको श्रम स्वीकृति, खेलाडी सुरक्षा तथा पारिश्रमिक सम्झौताका मापदण्डहरू कडाइका साथ पालना गर्न एन्फाले सबै सहभागी क्लबहरूलाई निर्देशन दिएको छ।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [एसीसी प्रिमियर कप विजेता नेपाली क्रिकेट टोलीको स्वागत](https://www.onlinekhabar.com/2026/09/2016553/nepali-cricket-team-returns-home-after-winning-acc-premier-cup)

### Context Passage (Nepali · Condition C1)
> एसियाली क्रिकेट काउन्सिल (एसीसी) प्रिमियर कपको उपाधि जितेर एसिया कपमा छनोट भएको नेपाली राष्ट्रिय क्रिकेट टोली स्वदेश फर्किएको छ। कीर्तिपुरस्थित त्रिवि क्रिकेट मैदानमा सम्पन्न फाइनल खेलमा यूएईलाई हराउँदै नेपालले उपाधि हात पारेको थियो। त्रिभुवन अन्तर्राष्ट्रिय विमानस्थलमा सयौँ समर्थक र खेल अधिकारीहरूले टोलीको भव्य स्वागत गरे।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [१९औँ एसियाली खेलकुदमा नेपाली खेलाडीको सहभागिता](https://www.hamrokhelkud.com/featured/135943.html)

### Context Passage (Nepali · Condition C1)
> चीनको हाङझावमा सम्पन्न १९औँ एसियाली खेलकुदमा नेपालका २३४ खेलाडीहरूले २९ विभिन्न खेल विधामा सहभागिता जनाएका छन्। राष्ट्रिय खेलकुद परिषद् (राखेप) का अनुसार कराते र कबड्डी विधामा नेपाली खेलाडीहरूले ऐतिहासिक पदक जित्दै देशको नाम अन्तर्राष्ट्रिय मञ्चमा उच्च राखेका छन्।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [टी-२० विश्वकपका लागि नेपाली क्रिकेट टोलीको घोषणा](https://www.onlinekhabar.com/2026/01/1843313/these-are-the-15-nepali-players-who-will-play-in-the-t20-world-cup)

### Context Passage (Nepali · Condition C1)
> नेपाल क्रिकेट संघ (क्यान) ले आईसीसी पुरुष टी-२० विश्वकपका लागि १५ सदस्यीय राष्ट्रिय टोली घोषणा गरेको छ। युवा तथा अनुभवी खेलाडीहरूको समिश्रण रहेको नेपाली टोलीमा रोहित पौडेलले कप्तानी सम्हालेका छन् भने सोमपाल कामी, कुशल भुर्तेल र दीपेन्द्रसिंह ऐरी समावेश छन्। नेपाली टोलीले विश्वकपमा समूह चरणका खेलहरू प्रतिष्ठित अन्तर्राष्ट्रिय रंगशालामा खेल्ने तालिका छ।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [दीपेन्द्रसिंह ऐरी: ९ बलमा अर्धशतकको ऐतिहासिक विश्व कीर्तिमान](https://www.onlinekhabar.com/personality/dipendra-singh-airee)

### Context Passage (Nepali · Condition C1)
> नेपाली क्रिकेटका अलराउन्डर दीपेन्द्रसिंह ऐरीले अन्तर्राष्ट्रिय टी-२० क्रिकेटमा विश्वकै सबैभन्दा छिटो ९ बलमा अर्धशतक प्रहार गरी कीर्तिमान बनाएका छन्। चीनको हाङ्ग्जाउमा आयोजित १९औँ एसियाली खेलकुद अन्तर्गत मंगोलियाविरुद्धको खेलमा उनले यो दुर्लभ कीर्तिमान रचेका हुन्। यसैगरी उनले अन्तर्राष्ट्रिय खेलमा एकै ओभरमा ६ छक्का समेत प्रहार गरेका छन्।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [क्यानद्वारा नेपाल प्रिमियर लिग (एनपीएल) आयोजनाको तयारी](https://www.onlinekhabar.com/2020/01/826769/%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%A8-%E0%A4%86%E0%A4%AB%E0%A5%88%E0%A4%82%E0%A4%B2%E0%A5%87-%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2-%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AE)

### Context Passage (Nepali · Condition C1)
> नेपाल क्रिकेट संघ (क्यान) ले आधिकारिक फ्रेन्चाइज प्रतियोगिता नेपाल प्रिमियर लिग (एनपीएल) को औपचारिक तयारी सुरु गरेको छ। देशभरका प्रमुख सहरहरूलाई प्रतिनिधित्व गर्ने टोलीहरूमार्फत घरेलु क्रिकेटको व्यावसायिक विकास गर्ने र विदेशी खेलाडीहरूलाई समेत समावेश गरी प्रतियोगितालाई अन्तर्राष्ट्रिय स्तरको बनाउने क्यानको योजना छ।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [एन्फा राष्ट्रिय फुटबल लिग तथा सहिद स्मारक लिग समीक्षा](https://www.hamrokhelkud.com/football/170529.html)

### Context Passage (Nepali · Condition C1)
> अखिल नेपाल फुटबल संघ (एन्फा) ले राष्ट्रिय लिग तथा सहिद स्मारक फुटबल प्रतियोगितालाई व्यवस्थित गर्न नयाँ कार्यविधि कार्यान्वयनमा ल्याएको छ। क्लबहरूमा विदेशी खेलाडीहरूको श्रम स्वीकृति, खेलाडी सुरक्षा तथा पारिश्रमिक सम्झौताका मापदण्डहरू कडाइका साथ पालना गर्न एन्फाले सबै सहभागी क्लबहरूलाई निर्देशन दिएको छ।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [एसीसी प्रिमियर कप विजेता नेपाली क्रिकेट टोलीको स्वागत](https://www.onlinekhabar.com/2026/09/2016553/nepali-cricket-team-returns-home-after-winning-acc-premier-cup)

### Context Passage (Nepali · Condition C1)
> एसियाली क्रिकेट काउन्सिल (एसीसी) प्रिमियर कपको उपाधि जितेर एसिया कपमा छनोट भएको नेपाली राष्ट्रिय क्रिकेट टोली स्वदेश फर्किएको छ। कीर्तिपुरस्थित त्रिवि क्रिकेट मैदानमा सम्पन्न फाइनल खेलमा यूएईलाई हराउँदै नेपालले उपाधि हात पारेको थियो। त्रिभुवन अन्तर्राष्ट्रिय विमानस्थलमा सयौँ समर्थक र खेल अधिकारीहरूले टोलीको भव्य स्वागत गरे।

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
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [१९औँ एसियाली खेलकुदमा नेपाली खेलाडीको सहभागिता](https://www.hamrokhelkud.com/featured/135943.html)

### Context Passage (Nepali · Condition C1)
> चीनको हाङझावमा सम्पन्न १९औँ एसियाली खेलकुदमा नेपालका २३४ खेलाडीहरूले २९ विभिन्न खेल विधामा सहभागिता जनाएका छन्। राष्ट्रिय खेलकुद परिषद् (राखेप) का अनुसार कराते र कबड्डी विधामा नेपाली खेलाडीहरूले ऐतिहासिक पदक जित्दै देशको नाम अन्तर्राष्ट्रिय मञ्चमा उच्च राखेका छन्।

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
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [मनसुनजन्य बाढी पहिरो: राष्ट्रिय मानवीय तथा भौतिक क्षति विवरण](https://www.onlinekhabar.com/2020/09/893885)

### Context Passage (Nepali · Condition C1)
> गृह मन्त्रालयको राष्ट्रिय विपद् जोखिम न्यूनीकरण तथा व्यवस्थापन प्राधिकरणका अनुसार यस वर्षको मनसुनमा आएको बाढी र पहिरोबाट २६० भन्दा बढी नागरिकले ज्यान गुमाएका छन्। सिन्धुपाल्चोक, म्याग्दी र कालिकोट जिल्लामा पहिरोले ठूलो मानवीय क्षति पुर्‍याएको छ। सरकारले प्रभावित परिवारलाई तत्काल राहत सामग्री र अस्थायी आवास निर्माणका लागि अनुदान उपलब्ध गराएको छ।

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
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [जल तथा मौसम विज्ञान विभाग: पूर्वी पहाडी जिल्लामा भारी वर्षा](https://www.onlinekhabar.com/2023/06/1324916/%E0%A4%A6%E0%A5%87%E0%A4%B6%E0%A4%AD%E0%A4%B0-%E0%A4%AE%E0%A4%A8%E0%A4%B8%E0%A5%81%E0%A4%A8-%E0%A4%A8%E0%A4%AB%E0%A5%88%E0%A4%B2%E0%A4%BF%E0%A4%81%E0%A4%A6%E0%A5%88-%E0%A4%95%E0%A4%BF%E0%A4%A8)

### Context Passage (Nepali · Condition C1)
> जल तथा मौसम विज्ञान विभागका अनुसार मनसुन सक्रिय भएसँगै पूर्वी नेपालका सङ्खुवासभा, पाँचथर र ताप्लेजुङ जिल्लामा भारी वर्षाका कारण आकस्मिक बाढी आएको छ। खोलाहरूमा पानीको बहाव खतराको तह नाघेपछि तटीय क्षेत्रका बासिन्दालाई सुरक्षित स्थानमा सर्न मौसम पूर्वानुमान महाशाखाले विशेष बुलेटिन जारी गरेको छ।

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
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [जलवायु परिवर्तन र उच्च हिमाली क्षेत्रमा हिमताल विस्फोटको जोखिम](https://www.onlinekhabar.com/2026/09/2014165/can-the-risk-of-glacial-lake-outburst-floods-and-landslides-be-reduced)

### Context Passage (Nepali · Condition C1)
> वातावरणविद्हरूका अनुसार विश्वव्यापी तापमान वृद्धिका कारण हिमालय क्षेत्रका हिमनदीहरू तीव्र गतिमा पग्लिरहेका छन्। इम्जा, छोरोल्पा र ठुलागी जस्ता जोखिमपूर्ण हिमतालहरूमा पानीको सतह बढेकाले सम्भावित हिमताल विस्फोट (जीएलओएफ) को पूर्वसूचना प्रणाली जडान गरी तल्लो तटीय बस्तीहरूको संरक्षण गर्न सरकारले पहल थालेको छ।

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
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [विपद् जोखिम न्यूनीकरण: नदी नियन्त्रण तथा तटबन्ध निर्माण](https://www.onlinekhabar.com/2021/06/967950/%E0%A4%AC%E0%A4%BE%E0%A4%A2%E0%A5%80-%E0%A4%AA%E0%A4%B9%E0%A4%BF%E0%A4%B0%E0%A5%8B%E0%A4%AC%E0%A4%BE%E0%A4%9F-%E0%A5%A7%E0%A5%AE-%E0%A4%B2%E0%A4%BE%E0%A4%96-%E0%A4%AC%E0%A4%BE%E0%A4%B8)

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय विपद् प्राधिकरणका अनुसार नेपालका तराई तथा चुरे क्षेत्रमा वर्षेनि नदी कटान र बाढीका कारण लाखौँ नागरिक प्रभावित हुने गरेका छन्। कोशी, गण्डकी, कर्णाली र महाकाली नदी नियन्त्रणका लागि दिगो जैविक तटबन्ध निर्माण र स्थानीय समुदायलाई उद्धार सामग्रीसहित तालिम दिने कार्य अघि बढाइएको छ।

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
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [इलाम बाढी पहिरो: राहत वितरण तथा पुनर्स्थापना](https://www.onlinekhabar.com/2025/10/1777417/chief-minister-reaches-ilam-with-relief-supplies-three-days-after-floods-and-landslides)

### Context Passage (Nepali · Condition C1)
> अविरल वर्षाका कारण पूर्वी पहाडी जिल्ला इलाममा गएको पहिरोबाट विस्थापित नागरिकहरूका लागि प्रदेश सरकारले खाद्यान्न, त्रिपाल र औषधिजन्य राहत सामग्री पठाएको छ। अवरुद्ध सडक सञ्जाल खुलाउन र खानेपानी आपूर्ति पुनर्स्थापना गर्न नेपाली सेना र नेपाल प्रहरीको टोली परिचालन गरिएको छ।

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
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [मनसुनजन्य बाढी पहिरो: राष्ट्रिय मानवीय तथा भौतिक क्षति विवरण](https://www.onlinekhabar.com/2020/09/893885)

### Context Passage (Nepali · Condition C1)
> गृह मन्त्रालयको राष्ट्रिय विपद् जोखिम न्यूनीकरण तथा व्यवस्थापन प्राधिकरणका अनुसार यस वर्षको मनसुनमा आएको बाढी र पहिरोबाट २६० भन्दा बढी नागरिकले ज्यान गुमाएका छन्। सिन्धुपाल्चोक, म्याग्दी र कालिकोट जिल्लामा पहिरोले ठूलो मानवीय क्षति पुर्‍याएको छ। सरकारले प्रभावित परिवारलाई तत्काल राहत सामग्री र अस्थायी आवास निर्माणका लागि अनुदान उपलब्ध गराएको छ।

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
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [जल तथा मौसम विज्ञान विभाग: पूर्वी पहाडी जिल्लामा भारी वर्षा](https://www.onlinekhabar.com/2023/06/1324916/%E0%A4%A6%E0%A5%87%E0%A4%B6%E0%A4%AD%E0%A4%B0-%E0%A4%AE%E0%A4%A8%E0%A4%B8%E0%A5%81%E0%A4%A8-%E0%A4%A8%E0%A4%AB%E0%A5%88%E0%A4%B2%E0%A4%BF%E0%A4%81%E0%A4%A6%E0%A5%88-%E0%A4%95%E0%A4%BF%E0%A4%A8)

### Context Passage (Nepali · Condition C1)
> जल तथा मौसम विज्ञान विभागका अनुसार मनसुन सक्रिय भएसँगै पूर्वी नेपालका सङ्खुवासभा, पाँचथर र ताप्लेजुङ जिल्लामा भारी वर्षाका कारण आकस्मिक बाढी आएको छ। खोलाहरूमा पानीको बहाव खतराको तह नाघेपछि तटीय क्षेत्रका बासिन्दालाई सुरक्षित स्थानमा सर्न मौसम पूर्वानुमान महाशाखाले विशेष बुलेटिन जारी गरेको छ।

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
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [जलवायु परिवर्तन र उच्च हिमाली क्षेत्रमा हिमताल विस्फोटको जोखिम](https://www.onlinekhabar.com/2026/09/2014165/can-the-risk-of-glacial-lake-outburst-floods-and-landslides-be-reduced)

### Context Passage (Nepali · Condition C1)
> वातावरणविद्हरूका अनुसार विश्वव्यापी तापमान वृद्धिका कारण हिमालय क्षेत्रका हिमनदीहरू तीव्र गतिमा पग्लिरहेका छन्। इम्जा, छोरोल्पा र ठुलागी जस्ता जोखिमपूर्ण हिमतालहरूमा पानीको सतह बढेकाले सम्भावित हिमताल विस्फोट (जीएलओएफ) को पूर्वसूचना प्रणाली जडान गरी तल्लो तटीय बस्तीहरूको संरक्षण गर्न सरकारले पहल थालेको छ।

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
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [विपद् जोखिम न्यूनीकरण: नदी नियन्त्रण तथा तटबन्ध निर्माण](https://www.onlinekhabar.com/2021/06/967950/%E0%A4%AC%E0%A4%BE%E0%A4%A2%E0%A5%80-%E0%A4%AA%E0%A4%B9%E0%A4%BF%E0%A4%B0%E0%A5%8B%E0%A4%AC%E0%A4%BE%E0%A4%9F-%E0%A5%A7%E0%A5%AE-%E0%A4%B2%E0%A4%BE%E0%A4%96-%E0%A4%AC%E0%A4%BE%E0%A4%B8)

### Context Passage (Nepali · Condition C1)
> राष्ट्रिय विपद् प्राधिकरणका अनुसार नेपालका तराई तथा चुरे क्षेत्रमा वर्षेनि नदी कटान र बाढीका कारण लाखौँ नागरिक प्रभावित हुने गरेका छन्। कोशी, गण्डकी, कर्णाली र महाकाली नदी नियन्त्रणका लागि दिगो जैविक तटबन्ध निर्माण र स्थानीय समुदायलाई उद्धार सामग्रीसहित तालिम दिने कार्य अघि बढाइएको छ।

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
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [इलाम बाढी पहिरो: राहत वितरण तथा पुनर्स्थापना](https://www.onlinekhabar.com/2025/10/1777417/chief-minister-reaches-ilam-with-relief-supplies-three-days-after-floods-and-landslides)

### Context Passage (Nepali · Condition C1)
> अविरल वर्षाका कारण पूर्वी पहाडी जिल्ला इलाममा गएको पहिरोबाट विस्थापित नागरिकहरूका लागि प्रदेश सरकारले खाद्यान्न, त्रिपाल र औषधिजन्य राहत सामग्री पठाएको छ। अवरुद्ध सडक सञ्जाल खुलाउन र खानेपानी आपूर्ति पुनर्स्थापना गर्न नेपाली सेना र नेपाल प्रहरीको टोली परिचालन गरिएको छ।

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
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [सर्वोच्च अदालत संवैधानिक इजलास: न्यायिक क्षेत्राधिकार र फैसला](https://www.onlinekhabar.com/2021/09/1008845/%E0%A4%B8%E0%A4%82%E0%A4%B5%E0%A5%88%E0%A4%A7%E0%A4%BE%E0%A4%A8%E0%A4%BF%E0%A4%95-%E0%A4%87%E0%A4%9C%E0%A4%B2%E0%A4%BE%E0%A4%B8-%E0%A4%B0%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A6%E0%A5%88-%E0%A4%8F)

### Context Passage (Nepali · Condition C1)
> सर्वोच्च अदालतको प्रधानन्यायाधीशको नेतृत्वमा रहने पाँच सदस्यीय संवैधानिक इजलासले गम्भीर संवैधानिक व्याख्या सम्बन्धी विवादहरूको निरुपण गर्दै आएको छ। संविधानको धारा १३७ बमोजिम संघ, प्रदेश र स्थानीय तहबीचको अधिकार क्षेत्र विवाद तथा मौलिक हकको हनन सम्बन्धी महत्त्वपूर्ण रिटहरूमा इजलासले आदेश जारी गरेको छ।

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
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [निर्वाचन आयोग: प्रतिनिधि सभा तथा प्रदेश सभा निर्वाचन व्यवस्थापन](https://www.onlinekhabar.com/2025/12/1836350/these-are-the-provisional-voters-who-will-vote-for-members-of-the-house-of-representatives)

### Context Passage (Nepali · Condition C1)
> निर्वाचन आयोग नेपालले प्रतिनिधि सभा तथा प्रदेश सभा सदस्य निर्वाचनका लागि मतदाता नामावली अद्यावधिक गर्ने र मतदान केन्द्रहरूको सुरक्षा सुदृढ बनाउने कार्य सम्पन्न गरेको छ। आयोगका अनुसार प्रत्यक्ष र समानुपातिक निर्वाचन प्रणालीमार्फत कुल २७५ प्रतिनिधि सभा सदस्यहरू चयन हुने संवैधानिक व्यवस्था छ।

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
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [प्रतिनिधि सभाबाट महत्त्वपूर्ण सरकारी विधेयकहरू पारित](https://www.onlinekhabar.com/2026/05/1940225/two-bills-introduced-by-the-prime-minister-passed-by-the-house-of-representatives)

### Context Passage (Nepali · Condition C1)
> संघीय संसद्को प्रतिनिधि सभाले सुशासन, आर्थिक पारदर्शिता र सेवा प्रवाह सुधार सम्बन्धी दुई महत्त्वपूर्ण सरकारी विधेयकहरू बहुमतले पारित गरेको छ। संसद्मा दफावार छलफलपछि पारित भएका विधेयकहरू राष्ट्रिय सभामा पठाइएको र प्रमाणीकरणपछि कानुनको रूपमा लागू हुने संसद् सचिवालयले जनाएको छ।

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
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [राष्ट्रपतिद्वारा सत्य निरुपण तथा मेलमिलाप (टीआरसी) विधेयक प्रमाणीकरण](https://www.onlinekhabar.com/2024/08/1531575/the-president-assented-to-the-trc-bill)

### Context Passage (Nepali · Condition C1)
> राष्ट्रपतिले संघीय संसद्का दुवै सदनबाट पारित भएको बेपत्ता पारिएका व्यक्तिको छानबिन, सत्य निरुपण तथा मेलमिलाप आयोग ऐन संशोधन विधेयक प्रमाणीकरण गर्नुभएको छ। यससँगै नेपालको शान्ति प्रक्रियाको बाँकी रहेको सङ्क्रमणकालीन न्यायको कार्यभार टुङ्गोमा पुर्‍याउने कानुनी बाटो खुलेको छ।

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
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [नेपाल नागरिकता ऐन संशोधन तथा सर्वोच्च अदालतको आदेश](https://www.onlinekhabar.com/2023/06/1319932)

### Context Passage (Nepali · Condition C1)
> सर्वोच्च अदालतले नेपाल नागरिकता ऐन संशोधन सम्बन्धी रिट निवेदनमाथि सुनुवाइ गर्दै जन्मसिद्ध नागरिकका सन्तानलाई वंशजको आधारमा नागरिकता दिने कानुनी बाटो खुला गरेको छ। यस आदेशसँगै हजारौँ योग्य नेपाली नागरिकहरूले जिल्ला प्रशासन कार्यालयमार्फत नागरिकता प्रमाणपत्र प्राप्त गर्ने सुनिश्चित भएको छ।

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
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [सर्वोच्च अदालत संवैधानिक इजलास: न्यायिक क्षेत्राधिकार र फैसला](https://www.onlinekhabar.com/2021/09/1008845/%E0%A4%B8%E0%A4%82%E0%A4%B5%E0%A5%88%E0%A4%A7%E0%A4%BE%E0%A4%A8%E0%A4%BF%E0%A4%95-%E0%A4%87%E0%A4%9C%E0%A4%B2%E0%A4%BE%E0%A4%B8-%E0%A4%B0%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A6%E0%A5%88-%E0%A4%8F)

### Context Passage (Nepali · Condition C1)
> सर्वोच्च अदालतको प्रधानन्यायाधीशको नेतृत्वमा रहने पाँच सदस्यीय संवैधानिक इजलासले गम्भीर संवैधानिक व्याख्या सम्बन्धी विवादहरूको निरुपण गर्दै आएको छ। संविधानको धारा १३७ बमोजिम संघ, प्रदेश र स्थानीय तहबीचको अधिकार क्षेत्र विवाद तथा मौलिक हकको हनन सम्बन्धी महत्त्वपूर्ण रिटहरूमा इजलासले आदेश जारी गरेको छ।

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
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [निर्वाचन आयोग: प्रतिनिधि सभा तथा प्रदेश सभा निर्वाचन व्यवस्थापन](https://www.onlinekhabar.com/2025/12/1836350/these-are-the-provisional-voters-who-will-vote-for-members-of-the-house-of-representatives)

### Context Passage (Nepali · Condition C1)
> निर्वाचन आयोग नेपालले प्रतिनिधि सभा तथा प्रदेश सभा सदस्य निर्वाचनका लागि मतदाता नामावली अद्यावधिक गर्ने र मतदान केन्द्रहरूको सुरक्षा सुदृढ बनाउने कार्य सम्पन्न गरेको छ। आयोगका अनुसार प्रत्यक्ष र समानुपातिक निर्वाचन प्रणालीमार्फत कुल २७५ प्रतिनिधि सभा सदस्यहरू चयन हुने संवैधानिक व्यवस्था छ।

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
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [प्रतिनिधि सभाबाट महत्त्वपूर्ण सरकारी विधेयकहरू पारित](https://www.onlinekhabar.com/2026/05/1940225/two-bills-introduced-by-the-prime-minister-passed-by-the-house-of-representatives)

### Context Passage (Nepali · Condition C1)
> संघीय संसद्को प्रतिनिधि सभाले सुशासन, आर्थिक पारदर्शिता र सेवा प्रवाह सुधार सम्बन्धी दुई महत्त्वपूर्ण सरकारी विधेयकहरू बहुमतले पारित गरेको छ। संसद्मा दफावार छलफलपछि पारित भएका विधेयकहरू राष्ट्रिय सभामा पठाइएको र प्रमाणीकरणपछि कानुनको रूपमा लागू हुने संसद् सचिवालयले जनाएको छ।

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
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [राष्ट्रपतिद्वारा सत्य निरुपण तथा मेलमिलाप (टीआरसी) विधेयक प्रमाणीकरण](https://www.onlinekhabar.com/2024/08/1531575/the-president-assented-to-the-trc-bill)

### Context Passage (Nepali · Condition C1)
> राष्ट्रपतिले संघीय संसद्का दुवै सदनबाट पारित भएको बेपत्ता पारिएका व्यक्तिको छानबिन, सत्य निरुपण तथा मेलमिलाप आयोग ऐन संशोधन विधेयक प्रमाणीकरण गर्नुभएको छ। यससँगै नेपालको शान्ति प्रक्रियाको बाँकी रहेको सङ्क्रमणकालीन न्यायको कार्यभार टुङ्गोमा पुर्‍याउने कानुनी बाटो खुलेको छ।

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
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [नेपाल नागरिकता ऐन संशोधन तथा सर्वोच्च अदालतको आदेश](https://www.onlinekhabar.com/2023/06/1319932)

### Context Passage (Nepali · Condition C1)
> सर्वोच्च अदालतले नेपाल नागरिकता ऐन संशोधन सम्बन्धी रिट निवेदनमाथि सुनुवाइ गर्दै जन्मसिद्ध नागरिकका सन्तानलाई वंशजको आधारमा नागरिकता दिने कानुनी बाटो खुला गरेको छ। यस आदेशसँगै हजारौँ योग्य नेपाली नागरिकहरूले जिल्ला प्रशासन कार्यालयमार्फत नागरिकता प्रमाणपत्र प्राप्त गर्ने सुनिश्चित भएको छ।

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
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [काठमाडौं-तराई द्रुतमार्ग (फास्ट ट्रयाक) निर्माण प्रगति](https://www.onlinekhabar.com/2018/01/653008/%E0%A4%AB%E0%A4%BE%E0%A4%B8%E0%A5%8D%E0%A4%9F-%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%AF%E0%A4%BE%E0%A4%95%E0%A4%AE%E0%A4%BE-%E0%A4%B8%E0%A5%87%E0%A4%A8%E0%A4%BE%E0%A4%B2%E0%A5%87-%E0%A4%95%E0%A5%87)

### Context Passage (Nepali · Condition C1)
> नेपाली सेनाको व्यवस्थापनमा निर्माणाधीन ७०.९७ किलोमिटर लामो काठमाडौं-तराई मधेस द्रुतमार्ग (फास्ट ट्रयाक) को सुरुङमार्ग र पुल निर्माण कार्य तीव्र गतिमा अघि बढेको छ। महादेवडाँडा, धेद्रे र लेनडाँडामा सुरुङ छेड्ने काम सम्पन्न भएसँगै काठमाडौं उपत्यकालाई तराईसँग १ घण्टाको यात्रा दूरीमा जोड्ने राष्ट्रिय गौरवको आयोजनाले गति लिएको छ।

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
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [माथिल्लो तामाकोशी ४५६ मेगावाट जलविद्युत आयोजना](https://www.onlinekhabar.com/2021/07/978999/%E0%A4%A4%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%95%E0%A5%8B%E0%A4%B6%E0%A5%80-%E0%A4%9C%E0%A4%B2%E0%A4%B5%E0%A4%BF%E0%A4%A6%E0%A5%8D%E0%A4%AF%E0%A5%81%E0%A4%A4-%E0%A4%86%E0%A4%AF%E0%A5%8B%E0%A4%9C%E0%A4%A8)

### Context Passage (Nepali · Condition C1)
> दोलखा जिल्लामा स्वदेशी लगानीमा निर्मित ४५६ मेगावाट क्षमताको माथिल्लो तामाकोशी जलविद्युत आयोजना राष्ट्रिय प्रसारण प्रणालीमा जोडिएको छ। यस आयोजनाले हिउँदको समयमा हुने बिजुलीको अभाव घटाउन र नेपाललाई वर्षायाममा छिमेकी देशहरूमा जलविद्युत निर्यात गर्ने राष्ट्रको रूपमा स्थापित गर्न कोशेढुङ्गा साबित भएको छ।

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
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [पोखरा अन्तर्राष्ट्रिय विमानस्थल: उडान सञ्चालन तथा पर्यटन विकास](https://www.onlinekhabar.com/2026/03/1882796/9-international-flights-and-landings-at-pokhara-airport-in-a-month-74-passengers)

### Context Passage (Nepali · Condition C1)
> पोखरा अन्तर्राष्ट्रिय विमानस्थलमा अन्तर्राष्ट्रिय चार्टर्ड तथा नियमित उडानहरू विस्तार गर्न नागरिक उड्डयन प्राधिकरणले प्रोत्साहन प्याकेज घोषणा गरेको छ। विमानस्थल सञ्चालनसँगै गण्डकी प्रदेशमा साहसिक खेलकुद तथा पदयात्राका लागि आउने विदेशी पर्यटकहरूको आवागमन सहज भएको पर्यटन व्यवसायीहरूले बताएका छन्।

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
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [नेपाल पर्यटन बोर्ड: वार्षिक १० लाखभन्दा बढी विदेशी पर्यटक आगमन](https://www.onlinekhabar.com?p=1932505)

### Context Passage (Nepali · Condition C1)
> नेपाल पर्यटन बोर्डको तथ्याङ्क अनुसार हवाई मार्ग हुँदै नेपाल भ्रमणमा आउने विदेशी पर्यटकहरूको सङ्ख्या वार्षिक १० लाख नाघेको छ। भारत, अमेरिका, चीन, बेलायत र अस्ट्रेलियाबाट आउने पर्यटकहरूको सङ्ख्यामा उल्लेख्य वृद्धि भएको छ। बोर्डले पदयात्रा, पर्वतारोहण र सांस्कृतिक सम्पदा पर्यटन प्रवर्द्धनका लागि अन्तर्राष्ट्रिय पर्यटन मेलाहरूमा सहभागिता जनाएको छ।

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
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [काठमाडौं-तराई द्रुतमार्ग (फास्ट ट्रयाक) निर्माण प्रगति](https://www.onlinekhabar.com/2018/01/653008/%E0%A4%AB%E0%A4%BE%E0%A4%B8%E0%A5%8D%E0%A4%9F-%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%AF%E0%A4%BE%E0%A4%95%E0%A4%AE%E0%A4%BE-%E0%A4%B8%E0%A5%87%E0%A4%A8%E0%A4%BE%E0%A4%B2%E0%A5%87-%E0%A4%95%E0%A5%87)

### Context Passage (Nepali · Condition C1)
> नेपाली सेनाको व्यवस्थापनमा निर्माणाधीन ७०.९७ किलोमिटर लामो काठमाडौं-तराई मधेस द्रुतमार्ग (फास्ट ट्रयाक) को सुरुङमार्ग र पुल निर्माण कार्य तीव्र गतिमा अघि बढेको छ। महादेवडाँडा, धेद्रे र लेनडाँडामा सुरुङ छेड्ने काम सम्पन्न भएसँगै काठमाडौं उपत्यकालाई तराईसँग १ घण्टाको यात्रा दूरीमा जोड्ने राष्ट्रिय गौरवको आयोजनाले गति लिएको छ।

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
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [माथिल्लो तामाकोशी ४५६ मेगावाट जलविद्युत आयोजना](https://www.onlinekhabar.com/2021/07/978999/%E0%A4%A4%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%95%E0%A5%8B%E0%A4%B6%E0%A5%80-%E0%A4%9C%E0%A4%B2%E0%A4%B5%E0%A4%BF%E0%A4%A6%E0%A5%8D%E0%A4%AF%E0%A5%81%E0%A4%A4-%E0%A4%86%E0%A4%AF%E0%A5%8B%E0%A4%9C%E0%A4%A8)

### Context Passage (Nepali · Condition C1)
> दोलखा जिल्लामा स्वदेशी लगानीमा निर्मित ४५६ मेगावाट क्षमताको माथिल्लो तामाकोशी जलविद्युत आयोजना राष्ट्रिय प्रसारण प्रणालीमा जोडिएको छ। यस आयोजनाले हिउँदको समयमा हुने बिजुलीको अभाव घटाउन र नेपाललाई वर्षायाममा छिमेकी देशहरूमा जलविद्युत निर्यात गर्ने राष्ट्रको रूपमा स्थापित गर्न कोशेढुङ्गा साबित भएको छ।

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
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [पोखरा अन्तर्राष्ट्रिय विमानस्थल: उडान सञ्चालन तथा पर्यटन विकास](https://www.onlinekhabar.com/2026/03/1882796/9-international-flights-and-landings-at-pokhara-airport-in-a-month-74-passengers)

### Context Passage (Nepali · Condition C1)
> पोखरा अन्तर्राष्ट्रिय विमानस्थलमा अन्तर्राष्ट्रिय चार्टर्ड तथा नियमित उडानहरू विस्तार गर्न नागरिक उड्डयन प्राधिकरणले प्रोत्साहन प्याकेज घोषणा गरेको छ। विमानस्थल सञ्चालनसँगै गण्डकी प्रदेशमा साहसिक खेलकुद तथा पदयात्राका लागि आउने विदेशी पर्यटकहरूको आवागमन सहज भएको पर्यटन व्यवसायीहरूले बताएका छन्।

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
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [नेपाल पर्यटन बोर्ड: वार्षिक १० लाखभन्दा बढी विदेशी पर्यटक आगमन](https://www.onlinekhabar.com?p=1932505)

### Context Passage (Nepali · Condition C1)
> नेपाल पर्यटन बोर्डको तथ्याङ्क अनुसार हवाई मार्ग हुँदै नेपाल भ्रमणमा आउने विदेशी पर्यटकहरूको सङ्ख्या वार्षिक १० लाख नाघेको छ। भारत, अमेरिका, चीन, बेलायत र अस्ट्रेलियाबाट आउने पर्यटकहरूको सङ्ख्यामा उल्लेख्य वृद्धि भएको छ। बोर्डले पदयात्रा, पर्वतारोहण र सांस्कृतिक सम्पदा पर्यटन प्रवर्द्धनका लागि अन्तर्राष्ट्रिय पर्यटन मेलाहरूमा सहभागिता जनाएको छ।

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
