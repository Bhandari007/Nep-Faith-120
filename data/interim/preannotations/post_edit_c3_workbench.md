# NepFaith-120 Condition C3 Post-Editing Workbench

**Version:** 1.0 (Locked Protocol)  
**Editor:** Human Bilingual Post-Editor  
**Target:** 60 Unique Reference Passages (spanning all 120 candidate items)  
**Storage Protocol:** Save completed post-edits directly to `data/interim/preannotations/post_edit_c3_workbench.md`.

---

## Minimal-Pair Post-Editing Principles
The purpose of Condition $C3$ is to compute the pure Machine Translation Error Gap:
$$\Delta_{\text{MT}} = A(C3) - A(C2)$$
To ensure that $C3$ differs from $C2$ **only** by the absence of translation errors (and not by human stylistic embellishments), adhere strictly to these rules:

1. **Minimal Edit Distance**: Start with the Raw IndicTrans2 translation ($p_{c2}$) and edit **only** what is factually, syntactically, or semantically incorrect. Do not rephrase well-formed sentences simply to improve style or prose.
2. **Entity & Number Precision**: Fix mistranslated numbers, years, currencies, and proper nouns (e.g., if "सन् १९७९" was translated as "2001", fix it to "1979").
3. **Evidentials & Epistemic Stance**: Preserve evidential markers and modal qualifiers present in Nepali (e.g., "भनिन्छ", "दाबी गरिएको छ").
4. **Negation & Polarities**: Ensure negation particles (e.g., "छैन", "हुँदैन") are accurately reflected in English without polarity inversion.
5. **No Edit Needed**: If the raw MT is fluent, accurate, and contains no translation errors, leave the editable slot unchanged and check `[X] Clean / No edit needed`.
6. **Stopwatch Duration**: Record the elapsed time (`mm:ss`) spent on each passage.

---

## Passage 01 / 60
**Linked Candidate Items:** `item_001`, `item_009`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [पशुपतिनाथ मन्दिर](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A4%B6%E0%A5%81%E0%A4%AA%E0%A4%A4%E0%A4%BF%E0%A4%A8%E0%A4%BE%E0%A4%A5_%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%B0)

### 1. Source Passage (Nepali · Condition C1)
> पशुपतिनाथको मन्दिर काठमाडौँ जिल्लामा रहेको ऐतिहासिक, धार्मिक एवं पर्यटकीय दृष्टिले महत्त्वपूर्ण स्थल हो। यो मन्दिर काठमाडौँ महानगरपालिका वडा नम्बर ८ मा बागमती नदीको किनारमा रहेको छ। यो मन्दिर २४० हेक्टर जग्गामा फैलिएको छ। पशुपतिनाथको मन्दिर सांस्कृतिक सम्पदा अन्तर्गत युनेस्को विश्व सम्पदा क्षेत्रमा सूचीकृत छ। यो हिन्दूहरूको एक पवित्र तीर्थस्थल मानिन्छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Temple of Pashupatinath is a historically and religiously and touristly important site in Kathmandu district. The temple is located on the banks of the Bagmati River in Kathmandu Metropolitan City Ward No. 8. The temple is spread over an area of eighty hectares. The Temple of Pashupatinath is listed in the UNESCO World Heritage Site under the Cultural Heritage. It is considered a holy pilgrimage site for Hindus.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Temple of Pashupatinath is a historically and religiously and touristly important site in Kathmandu district. The temple is located on the banks of the Bagmati River in Kathmandu Metropolitan City Ward No. 8. The temple is spread over an area of eighty hectares. The Temple of Pashupatinath is listed in the UNESCO World Heritage Site under the Cultural Heritage. It is considered a holy pilgrimage site for Hindus.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 02 / 60
**Linked Candidate Items:** `item_002`, `item_010`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [चाँगुनारायण मन्दिर](https://ne.wikipedia.org/wiki/%E0%A4%9A%E0%A4%BE%E0%A4%81%E0%A4%97%E0%A5%81%E0%A4%A8%E0%A4%BE%E0%A4%B0%E0%A4%BE%E0%A4%AF%E0%A4%A3_%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%B0)

### 1. Source Passage (Nepali · Condition C1)
> चाँगुनारायण मन्दिर नेपालको एक प्रसिद्ध मन्दिर हो। यो भक्तपुर जिल्लाको चाँगुनारायण नगरपालिकामा अवस्थित छ। यो काठमाडौँ उपत्यकाको प्राचीनतम मन्दिरहरू मध्ये एक मानिन्छ। यस मन्दिर परिसरमा वि.सं. ५२१ मा राजा मानदेव प्रथमले स्थापना गरेको ऐतिहासिक गरुडध्वज शिलालेख रहेको छ, जुन नेपालको इतिहासको सबैभन्दा पुरानो प्रमाणिक अभिलेख हो।

### 2. Raw IndicTrans2 MT (Condition C2)
> Changunarayan Temple is a famous temple in Nepal. It is located in Changunarayan Municipality of Bhaktapur District. It is considered to be one of the oldest temples in Kathmandu Valley. The temple complex contains the historic Garudbhaj inscription installed by King Mandev I in 1611 CE, which is the oldest authentic record in the history of Nepal.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Changunarayan Temple is a famous temple in Nepal. It is located in Changunarayan Municipality of Bhaktapur District. It is considered to be one of the oldest temples in Kathmandu Valley. The temple complex contains the historic Garudbhaj inscription installed by King Mandev I in 1611 CE, which is the oldest authentic record in the history of Nepal.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 03 / 60
**Linked Candidate Items:** `item_003`, `item_011`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [स्वयम्भूनाथ](https://ne.wikipedia.org/wiki/%E0%A4%B8%E0%A5%8D%E0%A4%B5%E0%A4%AF%E0%A4%AE%E0%A5%8D%E0%A4%AD%E0%A5%82%E0%A4%A8%E0%A4%BE%E0%A4%A5)

### 1. Source Passage (Nepali · Condition C1)
> स्वयम्भूनाथ काठमाडौँ उपत्यकाको पश्चिममा अवस्थित एक प्रसिद्ध बौद्ध स्तूप हो। यसलाई नेवारी भाषामा 'सिङ्गु' भनिन्छ। यस स्तूपलाई विदेशीहरूले 'मङ्की टेम्पल' पनि भन्ने गर्दछन्। स्तूपको मुख्य भागमा चारै दिशामा तथागत बुद्धका आँखाहरू चित्रित गरिएका छन्, जसले सर्वव्यापी ज्ञान र करुणाको प्रतीक जनाउँछ। सन् १९७९ मा युनेस्कोले यसलाई विश्व सम्पदा सूचीमा समावेश गरेको थियो।

### 2. Raw IndicTrans2 MT (Condition C2)
> Swayambhunath is a famous Buddhist stupa located in the west of Kathmandu Valley. It is called'Singu'in Newari language. This stupa is also called'Monkey Temple'by foreigners. The main part of the stupa has the eyes of Tathagata Buddha painted on all four sides, symbolizing the omnipresent knowledge and compassion. In the year 1550, UNESCO included it in the World Heritage List.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Swayambhunath is a famous Buddhist stupa located in the west of Kathmandu Valley. It is called'Singu'in Newari language. This stupa is also called'Monkey Temple'by foreigners. The main part of the stupa has the eyes of Tathagata Buddha painted on all four sides, symbolizing the omnipresent knowledge and compassion. In the year 1550, UNESCO included it in the World Heritage List.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 04 / 60
**Linked Candidate Items:** `item_004`, `item_012`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [बौद्धनाथ](https://ne.wikipedia.org/wiki/%E0%A4%AC%E0%A5%8C%E0%A4%A6%E0%A5%8D%E0%A4%A7%E0%A4%A8%E0%A4%BE%E0%A4%A5)

### 1. Source Passage (Nepali · Condition C1)
> बौद्धनाथ काठमाडौँको पूर्वी भागमा अवस्थित प्रसिद्ध बौद्ध स्तूप तथा तीर्थस्थल हो। यो विश्वकै ठूला स्तूपहरू मध्ये एक मानिन्छ। तिब्बती बौद्ध धर्मावलम्बीहरूका लागि यो अत्यन्त पवित्र धार्मिक केन्द्र हो। सन् १९७९ मा बौद्धनाथ युनेस्को विश्व सम्पदा सूचीमा सूचीकृत भएको थियो। वि.सं. २०७२ को महाभूकम्पबाट क्षतिग्रस्त भएको यस स्तूपको पुनर्निर्माण सम्पन्न भइसकेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Boudhanath is a famous Buddhist stupa and pilgrimage site located in the eastern part of Kathmandu. It is considered to be one of the largest stupas in the world. It is a very holy religious center for Tibetan Buddhists. Boudhanath was listed on the UNESCO World Heritage List in the year 1511. The reconstruction of this stupa, which was damaged by the Great Earthquake of the year 2050, has been completed.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Boudhanath is a famous Buddhist stupa and pilgrimage site located in the eastern part of Kathmandu. It is considered to be one of the largest stupas in the world. It is a very holy religious center for Tibetan Buddhists. Boudhanath was listed on the UNESCO World Heritage List in the year 1511. The reconstruction of this stupa, which was damaged by the Great Earthquake of the year 2050, has been completed.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 05 / 60
**Linked Candidate Items:** `item_005`, `item_013`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [भक्तपुर दरबार क्षेत्र](https://ne.wikipedia.org/wiki/%E0%A4%AD%E0%A4%95%E0%A5%8D%E0%A4%A4%E0%A4%AA%E0%A5%81%E0%A4%B0_%E0%A4%A6%E0%A4%B0%E0%A4%AC%E0%A4%BE%E0%A4%B0_%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4%B0)

### 1. Source Passage (Nepali · Condition C1)
> भक्तपुर दरबार क्षेत्र भक्तपुर नगरको मध्यभागमा अवस्थित ऐतिहासिक तथा सांस्कृतिक सम्पदा क्षेत्र हो। यहाँ मल्लकालीन ५५ झ्याले दरबार, न्यातपोल मन्दिर, भैरवनाथ मन्दिर र सुनढोका जस्ता उत्कृष्ट वास्तुकलाका नमुनाहरू रहेका छन्। राजा भूपतिन्द्र मल्लले निर्माण गर्न लगाएको न्यातपोल मन्दिर नेपालकै सबैभन्दा अग्लो पाँचतले प्यागोडा शैलीको मन्दिर हो।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Bhaktapur Palace area is a historical and cultural heritage area located in the central part of Bhaktapur city. It has fine architectural specimens such as the Malla-era Jhyale Palace, the Nayapole Temple, the Bhairavnath Temple, and the Sundoka. The Nayapole Temple, commissioned by King Bhupatindra Malla, is the tallest five-storey pagoda-style temple in Nepal.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Bhaktapur Palace area is a historical and cultural heritage area located in the central part of Bhaktapur city. It has fine architectural specimens such as the Malla-era Jhyale Palace, the Nayapole Temple, the Bhairavnath Temple, and the Sundoka. The Nayapole Temple, commissioned by King Bhupatindra Malla, is the tallest five-storey pagoda-style temple in Nepal.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 06 / 60
**Linked Candidate Items:** `item_006`, `item_014`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [पाटन दरबार क्षेत्र](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A4%BE%E0%A4%9F%E0%A4%A8_%E0%A4%A6%E0%A4%B0%E0%A4%AC%E0%A4%BE%E0%A4%B0_%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4%B0)

### 1. Source Passage (Nepali · Condition C1)
> पाटन दरबार क्षेत्र ललितपुर महानगरपालिकाको केन्द्रमा अवस्थित ऐतिहासिक मल्लकालीन दरबार परिसर हो। यहाँ प्रसिद्ध कृष्ण मन्दिर, भीमसेन मन्दिर, विश्वनाथ मन्दिर र चार नारायण मन्दिरहरू रहेका छन्। राजा सिद्धिनरसिंह मल्लद्वारा निर्मित कृष्ण मन्दिर २१ वटा गजुर भएको शिखर शैलीको अनुपम ढुङ्गे कलाकृति हो।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Patan Palace area is the historic Malla period palace complex located in the centre of Lalitpur Metropolitan City. It houses the famous Krishna temple, Bhimsen temple, Vishwanath temple and four Narayan temples. The Krishna temple built by Raja Siddhinsinh Malla is a unique rock art in the Shikhara style with 21 gajur.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Patan Palace area is the historic Malla period palace complex located in the centre of Lalitpur Metropolitan City. It houses the famous Krishna temple, Bhimsen temple, Vishwanath temple and four Narayan temples. The Krishna temple built by Raja Siddhinsinh Malla is a unique rock art in the Shikhara style with 21 gajur.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 07 / 60
**Linked Candidate Items:** `item_007`, `item_015`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [लुम्बिनी](https://ne.wikipedia.org/wiki/%E0%A4%B2%E0%A5%81%E0%A4%AE%E0%A5%8D%E0%A4%AC%E0%A4%BF%E0%A4%A8%E0%A5%80)

### 1. Source Passage (Nepali · Condition C1)
> लुम्बिनी रुपन्देही जिल्लामा अवस्थित गौतम बुद्धको जन्मस्थल हो। यो विश्वभरका बौद्ध धर्मावलम्बीहरूको प्रमुख तीर्थस्थल हो। यहाँ ईसापूर्व २४९ मा मौर्य सम्राट अशोकले स्थापना गरेको प्रसिद्ध अशोक स्तम्भ, मायादेवी मन्दिर, र पवित्र पुष्करिणी पोखरी रहेका छन्। सन् १९९७ मा लुम्बिनीलाई युनेस्कोले विश्व सम्पदा सूचीमा सूचीकृत गरेको थियो।

### 2. Raw IndicTrans2 MT (Condition C2)
> Lumbini is the birthplace of Gautama Buddha, located in the Rupandehi district. It is a major pilgrimage site for Buddhists from all over the world. It houses the famous Ashoka Pillar, Mayadevi Temple, and Holy Pool, established by the Mauryan Emperor Ashoka in 34 BC. Lumbini was listed as a World Heritage Site by UNESCO in the same year.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Lumbini is the birthplace of Gautama Buddha, located in the Rupandehi district. It is a major pilgrimage site for Buddhists from all over the world. It houses the famous Ashoka Pillar, Mayadevi Temple, and Holy Pool, established by the Mauryan Emperor Ashoka in 34 BC. Lumbini was listed as a World Heritage Site by UNESCO in the same year.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 08 / 60
**Linked Candidate Items:** `item_008`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage | **Source:** [जानकी मन्दिर](https://ne.wikipedia.org/wiki/%E0%A4%9C%E0%A4%BE%E0%A4%A8%E0%A4%95%E0%A5%80_%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%B0)

### 1. Source Passage (Nepali · Condition C1)
> जानकी मन्दिर धनुषा जिल्लाको जनकपुरधामको केन्द्रमा अवस्थित प्रसिद्ध हिन्दू मन्दिर हो। यो मन्दिर माता सीताको जन्मस्थलको सम्झनामा निर्माण गरिएको हो। सन् १९११ मा टिकमगढकी महारानी वृषभानु कुँवरीले नौ लाख चाँदीका असर्फी खर्चेर निर्माण गराएकाले यसलाई 'नौ लखा मन्दिर' पनि भनिन्छ। यो मन्दिर मुगल र राजपुत वास्तुकलाको सुन्दर सम्मिश्रण हो।

### 2. Raw IndicTrans2 MT (Condition C2)
> Janaki Mandir is a famous Hindu temple located in the center of Janakpurdham in Dhanusha district. The temple is built to commemorate the birthplace of Mata Sita. It is also known as'Naunu Lakha Mandir'as it was built by Maharani Vrishabhanu Kunwari of Tikamgarh in 2181 AD at a cost of nine lakh rupees. The temple is a beautiful blend of Mughal and Rajput architecture.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Janaki Mandir is a famous Hindu temple located in the center of Janakpurdham in Dhanusha district. The temple is built to commemorate the birthplace of Mata Sita. It is also known as'Naunu Lakha Mandir'as it was built by Maharani Vrishabhanu Kunwari of Tikamgarh in 2181 AD at a cost of nine lakh rupees. The temple is a beautiful blend of Mughal and Rajput architecture.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 09 / 60
**Linked Candidate Items:** `item_016`, `item_023`, `item_030`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [सगरमाथा राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B8%E0%A4%97%E0%A4%B0%E0%A4%AE%E0%A4%BE%E0%A4%A5%E0%A4%BE_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### 1. Source Passage (Nepali · Condition C1)
> सगरमाथा राष्ट्रिय निकुञ्ज पूर्वी नेपालको सोलुखुम्बु जिल्लामा अवस्थित छ। यस निकुञ्जको क्षेत्रफल १,१४८ वर्ग किलोमिटर रहेको छ। यस क्षेत्रमा विश्वको सर्वोच्च शिखर सगरमाथा (८,८४८.८६ मिटर) का साथै ल्होत्से, नुप्त्से, चोयु र आमादब्लम जस्ता हिमालहरू पर्दछन्। यहाँ दुर्लभ हिमचितुवा, कस्तुरी मृग र रातो पाण्डा पाइन्छन्। सन् १९७९ मा यो विश्व सम्पदा सूचीमा सूचीकृत भएको थियो।

### 2. Raw IndicTrans2 MT (Condition C2)
> Sagarmatha National Park is located in Solukhumbu district in eastern Nepal. The park covers an area of 1,800 square kilometres. The area includes the world's highest peak Sagarmatha ( 1.86 m ) as well as mountains such as Lhotse, Nuptsay, Choyu and Amadablam. It is home to rare snow leopards, musk deer and red panda. It was listed on the World Heritage List in 1992.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Sagarmatha National Park is located in Solukhumbu district in eastern Nepal. The park covers an area of 1,800 square kilometres. The area includes the world's highest peak Sagarmatha ( 1.86 m ) as well as mountains such as Lhotse, Nuptsay, Choyu and Amadablam. It is home to rare snow leopards, musk deer and red panda. It was listed on the World Heritage List in 1992.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 10 / 60
**Linked Candidate Items:** `item_017`, `item_024`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [चितवन राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%9A%E0%A4%BF%E0%A4%A4%E0%A4%B5%E0%A4%A8_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### 1. Source Passage (Nepali · Condition C1)
> चितवन राष्ट्रिय निकुञ्ज नेपालको पहिलो राष्ट्रिय निकुञ्ज हो, जसको स्थापना वि.सं. २०३० (सन् १९७३) मा भएको थियो। ९५२.६३ वर्ग किलोमिटर क्षेत्रफलमा फैलिएको यो निकुञ्ज एकसिंगे गैँडा, पाटे बाघ, घडियाल गोही र विभिन्न प्रजातिका चराचुरुङ्गीहरूको प्रमुख बासस्थान हो। जैविक विविधताको दृष्टिले महत्त्वपूर्ण यो निकुञ्ज सन् १९८४ मा युनेस्को विश्व सम्पदा सूचीमा समावेश गरिएको थियो।

### 2. Raw IndicTrans2 MT (Condition C2)
> Chitwan National Park is the first national park of Nepal established in 1999. Spread over an area of 952,633 square kilometres, the park is a major habitat for the one-horned rhinoceros, tiger, gharial, and a variety of birds. The park, which is important from the point of view of biodiversity, was inscribed on the UNESCO World Heritage List in 1999.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Chitwan National Park is the first national park of Nepal established in 1999. Spread over an area of 952,633 square kilometres, the park is a major habitat for the one-horned rhinoceros, tiger, gharial, and a variety of birds. The park, which is important from the point of view of biodiversity, was inscribed on the UNESCO World Heritage List in 1999.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 11 / 60
**Linked Candidate Items:** `item_018`, `item_025`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [बर्दिया राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%AC%E0%A4%B0%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%AF%E0%A4%BE_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### 1. Source Passage (Nepali · Condition C1)
> बर्दिया राष्ट्रिय निकुञ्ज तराई क्षेत्रमा अवस्थित नेपालको सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज हो, जसको क्षेत्रफल ९६८ वर्ग किलोमिटर रहेको छ। यो निकुञ्ज पाटे बाघ, जंगली हात्ती र एकसिंगे गैँडाको महत्त्वपूर्ण संरक्षण क्षेत्र हो। यहाँ बबई र कर्णाली नदीको तटीय क्षेत्रमा घडियाल गोही तथा डल्फिन समेत पाइन्छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Bardiya National Park is the largest national park in Nepal located in the Terai region and covers an area of 8.9 square kilometres. The park is an important conservation area for the spotted tiger, wild elephant and unicorn. It also hosts gharial goats and dolphins along the banks of the Babai and Karnali rivers.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Bardiya National Park is the largest national park in Nepal located in the Terai region and covers an area of 8.9 square kilometres. The park is an important conservation area for the spotted tiger, wild elephant and unicorn. It also hosts gharial goats and dolphins along the banks of the Babai and Karnali rivers.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 12 / 60
**Linked Candidate Items:** `item_019`, `item_026`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [रारा राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B0%E0%A4%BE%E0%A4%B0%E0%A4%BE_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### 1. Source Passage (Nepali · Condition C1)
> रारा राष्ट्रिय निकुञ्ज कर्णाली प्रदेशको मुगु र जुम्ला जिल्लामा अवस्थित नेपालको सबैभन्दा सानो राष्ट्रिय निकुञ्ज हो। यस निकुञ्जको मुख्य आकर्षण नेपालको सबैभन्दा ठूलो र गहिरो ताल 'रारा ताल' हो। समुद्र सतहबाट २,९९० मिटरको उचाइमा रहेको रारा तालको गहिराइ करिब १६७ मिटर रहेको छ। यहाँ कस्तुरी मृग र डाँफे चरा पाइन्छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Rara National Park is the smallest national park in Nepal, located in Mugu and Jumla districts of Karnali province. The main attraction of this park is the largest and deepest lake in Nepal, Lake Rara, at an altitude of 2,902 metres above sea level, has a depth of about 3,560 metres. It is home to musk deer and dolphins.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Rara National Park is the smallest national park in Nepal, located in Mugu and Jumla districts of Karnali province. The main attraction of this park is the largest and deepest lake in Nepal, Lake Rara, at an altitude of 2,902 metres above sea level, has a depth of about 3,560 metres. It is home to musk deer and dolphins.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 13 / 60
**Linked Candidate Items:** `item_020`, `item_027`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [शे-फोक्सुण्डो राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B6%E0%A5%87-%E0%A4%AB%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%B8%E0%A5%81%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A5%8B_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### 1. Source Passage (Nepali · Condition C1)
> शे-फोक्सुण्डो राष्ट्रिय निकुञ्ज नेपालको सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज हो, जसको क्षेत्रफल ३,५५५ वर्ग किलोमिटर रहेको छ। यो निकुञ्ज डोल्पा र मुगु जिल्लामा फैलिएको छ। यस निकुञ्जभित्र समुद्र सतहबाट ३,६११ मिटरको उचाइमा अवस्थित प्रसिद्ध गहिरो फोक्सुण्डो ताल रहेको छ। यहाँ तिब्बती पठारको हिमाली पारिस्थितिक प्रणाली र हिमचितुवा पाइन्छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Shey-Foksundo National Park is the largest national park in Nepal with an area of 3,555 square kilometres. The park is spread over the Dolpa and Mugu districts. The park contains the famous deep Phoksundo Lake, located at an altitude of 3,650 metres above sea level. It hosts the Himalayan ecosystem of the Tibetan Plateau and snow leopards.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Shey-Foksundo National Park is the largest national park in Nepal with an area of 3,555 square kilometres. The park is spread over the Dolpa and Mugu districts. The park contains the famous deep Phoksundo Lake, located at an altitude of 3,650 metres above sea level. It hosts the Himalayan ecosystem of the Tibetan Plateau and snow leopards.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 14 / 60
**Linked Candidate Items:** `item_021`, `item_028`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [लाङटाङ राष्ट्रिय निकुञ्ज](https://ne.wikipedia.org/wiki/%E0%A4%B2%E0%A4%BE%E0%A4%99%E0%A4%9F%E0%A4%BE%E0%A4%99_%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%A8%E0%A4%BF%E0%A4%95%E0%A5%81%E0%A4%9E%E0%A5%8D%E0%A4%9C)

### 1. Source Passage (Nepali · Condition C1)
> लाङटाङ राष्ट्रिय निकुञ्ज काठमाडौँ उपत्यकाको नजिक रहेको हिमाली निकुञ्ज हो, जुन रसुवा, नुवाकोट र सिन्धुपाल्चोक जिल्लामा फैलिएको छ। १,७१० वर्ग किलोमिटर क्षेत्रफल रहेको यस निकुञ्जमा लाङटाङ लिरुङ हिमाल, गोसाइँकुण्ड र लाङटाङ उपत्यका रहेका छन्। यो निकुञ्ज रातो पाण्डा (रेड पाण्डा) को प्रमुख बासस्थान मानिन्छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Langtang National Park is a Himalayan park close to the Kathmandu Valley, spread over the districts of Rasuwa, Nuwakot, and Sindhupalchok. The park covers an area of 1 ⁄ 4 square kilometres, comprising the Langtang Lirung Mountains, Gosainkund, and the Langtang Valley. The park is considered the prime habitat of the red panda ( Rade Panda ).

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Langtang National Park is a Himalayan park close to the Kathmandu Valley, spread over the districts of Rasuwa, Nuwakot, and Sindhupalchok. The park covers an area of 1 ⁄ 4 square kilometres, comprising the Langtang Lirung Mountains, Gosainkund, and the Langtang Valley. The park is considered the prime habitat of the red panda ( Rade Panda ).
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 15 / 60
**Linked Candidate Items:** `item_022`, `item_029`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks | **Source:** [अन्नपूर्ण संरक्षण क्षेत्र](https://ne.wikipedia.org/wiki/%E0%A4%85%E0%A4%A8%E0%A5%8D%E0%A4%A8%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%A3_%E0%A4%B8%E0%A4%82%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%A3_%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A5%87%E0%A4%A4%E0%A5%8D%E0%A4%B0)

### 1. Source Passage (Nepali · Condition C1)
> अन्नपूर्ण संरक्षण क्षेत्र नेपालको सबैभन्दा ठूलो संरक्षित क्षेत्र हो, जसको क्षेत्रफल ७,६२९ वर्ग किलोमिटर रहेको छ। राष्ट्रिय प्रकृति संरक्षण कोष (एनटीएनसी) द्वारा समुदायमा आधारित व्यवस्थापन गरिएको यो क्षेत्र पदयात्राका लागि विश्वमै प्रसिद्ध छ। यहाँ अन्नपूर्ण हिमशृंखला, कालीगण्डकी गल्छी, र मुक्तिनाथ मन्दिर अवस्थित छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Annapurna Conservation Area is the largest protected area in Nepal with an area of 672 km2. Managed by the National Nature Conservation Fund ( NTNC ), the area is world-renowned for trekking. The Annapurna Glacier, Kaligandi Glacier, and Muktinath Temple are located here.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Annapurna Conservation Area is the largest protected area in Nepal with an area of 672 km2. Managed by the National Nature Conservation Fund ( NTNC ), the area is world-renowned for trekking. The Annapurna Glacier, Kaligandi Glacier, and Muktinath Temple are located here.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 16 / 60
**Linked Candidate Items:** `item_031`, `item_036`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [सगरमाथा](https://ne.wikipedia.org/wiki/%E0%A4%B8%E0%A4%97%E0%A4%B0%E0%A4%AE%E0%A4%BE%E0%A4%A5%E0%A4%BE)

### 1. Source Passage (Nepali · Condition C1)
> सगरमाथा विश्वको सर्वोच्च शिखर हो, जसको आधिकारिक उचाइ समुद्र सतहबाट ८,८४८.८६ मिटर (२९,०३१.७ फिट) रहेको छ। यो हिमाल नेपाल र चीन (तिब्बत) को सीमानामा महालङ्गूर हिमशृङ्खलामा अवस्थित छ। इतिहासमा पहिलो पटक सन् १९५३ मे २९ मा सर एडमन्ड हिलारी र तेन्जिङ नोर्गे शेर्पाले सगरमाथाको सफल आरोहण गरेका थिए।

### 2. Raw IndicTrans2 MT (Condition C2)
> Sagarmatha is the highest peak in the world, with an official elevation of 8.8 m ( 23.8 m ) above sea level. The mountain is located in the Mahalangur Range on the border of Nepal and China ( Tibet ). For the first time in history, Sir Edmund Hillary and Tenzing Norgay Sherpa successfully climbed Mount Everest in May.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Sagarmatha is the highest peak in the world, with an official elevation of 8.8 m ( 23.8 m ) above sea level. The mountain is located in the Mahalangur Range on the border of Nepal and China ( Tibet ). For the first time in history, Sir Edmund Hillary and Tenzing Norgay Sherpa successfully climbed Mount Everest in May.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 17 / 60
**Linked Candidate Items:** `item_032`, `item_037`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [पोखरा](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A5%8B%E0%A4%96%E0%A4%B0%E0%A4%BE)

### 1. Source Passage (Nepali · Condition C1)
> पोखरा गण्डकी प्रदेशको राजधानी तथा नेपालको प्रमुख पर्यटकीय सहर हो। यो सहर फेवा ताल, बेगनास ताल, डेभिड फल्स, महेन्द्र गुफा र विन्ध्यवासिनी मन्दिरका लागि प्रसिद्ध छ। पोखराबाट माछापुच्छ्रे, अन्नपूर्ण र धौलागिरी हिमशृङ्खलाको मनोरम दृश्य नजिकबाट देख्न सकिन्छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Pokhara is the capital of Gandaki Province and a major tourist city in Nepal. The city is famous for Phewa Lake, Beganas Lake, David Falls, Mahendra Caves, and Vindhyavasini Temple. From Pokhara, one can have a panoramic view of the fishing and Annapurna and Dhaulagiri snow ranges.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Pokhara is the capital of Gandaki Province and a major tourist city in Nepal. The city is famous for Phewa Lake, Beganas Lake, David Falls, Mahendra Caves, and Vindhyavasini Temple. From Pokhara, one can have a panoramic view of the fishing and Annapurna and Dhaulagiri snow ranges.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 18 / 60
**Linked Candidate Items:** `item_033`, `item_038`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [कोशी नदी](https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A5%8B%E0%A4%B6%E0%A5%80_%E0%A4%A8%E0%A4%A6%E0%A5%80)

### 1. Source Passage (Nepali · Condition C1)
> कोशी नदी नेपालको सबैभन्दा ठूलो नदी हो, जसलाई 'सप्तकोशी' पनि भनिन्छ। यो नदी सातवटा सहायक नदीहरू (सुनकोशी, भोटेकोशी, तामाकोशी, दुधकोशी, इन्द्रावती, अरुण र तमोर) मिलेर बनेको छ। चतराबाट तराई प्रवेश गर्ने यो नदी भारतको बिहार राज्यमा गङ्गा नदीमा गएर मिसिन्छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Koshi River is the largest river in Nepal and is also known as the'Saptakoshi '. The river is composed of seven tributaries ( Sunakoshi, Bhotekoshi, Tamakoshi, Dudhkoshi, Indravati, Arun and Tamor ). The river enters the Terai from Chatra and merges with the Ganges River in the Indian state of Bihar.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Koshi River is the largest river in Nepal and is also known as the'Saptakoshi '. The river is composed of seven tributaries ( Sunakoshi, Bhotekoshi, Tamakoshi, Dudhkoshi, Indravati, Arun and Tamor ). The river enters the Terai from Chatra and merges with the Ganges River in the Indian state of Bihar.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 19 / 60
**Linked Candidate Items:** `item_034`, `item_039`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [कालीगण्डकी नदी](https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A4%BE%E0%A4%B2%E0%A5%80%E0%A4%97%E0%A4%A3%E0%A5%8D%E0%A4%A1%E0%A4%95%E0%A5%80_%E0%A4%A8%E0%A4%A6%E0%A5%80)

### 1. Source Passage (Nepali · Condition C1)
> कालीगण्डकी नदी नेपालको एक प्रमुख तथा पवित्र नदी हो, जुन तिब्बती सीमा नजिकै दामोदर कुण्डबाट उत्पत्ति हुन्छ। यस नदीले धौलागिरी र अन्नपूर्ण हिमालको बीचमा विश्वकै सबैभन्दा गहिरो गल्छी (अन्ध गल्छी) बनाएको छ। हिन्दू धर्ममा पवित्र मानिने शालिग्राम शिला विश्वभरमा केवल कालीगण्डकी नदीमै फेला पर्दछ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Kaligandaki River is a major and sacred river in Nepal, originating from the Damodar Kund near the Tibetan border. The river forms the world's deepest gorge ( Andh Galchi ) between the Dhaulagiri and Annapurna mountains. The Shaligram rock, considered sacred in Hinduism, is found only in the Kaligandaki River worldwide.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Kaligandaki River is a major and sacred river in Nepal, originating from the Damodar Kund near the Tibetan border. The river forms the world's deepest gorge ( Andh Galchi ) between the Dhaulagiri and Annapurna mountains. The Shaligram rock, considered sacred in Hinduism, is found only in the Kaligandaki River worldwide.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 20 / 60
**Linked Candidate Items:** `item_035`, `item_040`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [तिलिचो ताल](https://ne.wikipedia.org/wiki/%E0%A4%A4%E0%A4%BF%E0%A4%B2%E0%A4%BF%E0%A4%9A%E0%A5%8B_%E0%A4%A4%E0%A4%BE%E0%A4%B2)

### 1. Source Passage (Nepali · Condition C1)
> तिलिचो ताल मनाङ जिल्लामा अन्नपूर्ण हिमशृङ्खलाको काखमा समुद्र सतहबाट ४,९१९ मिटरको उचाइमा अवस्थित नेपालको उच्च हिमाली ताल हो। यस तालको लम्बाइ करिब ४ किलोमिटर र चौडाइ १.२ किलोमिटर रहेको छ। वरिपरि हिउँले ढाकिएका पहाडहरूले घेरिएको यो ताल कठिन पदयात्रा तथा पर्यटकीय गन्तव्यको रूपमा परिचित छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Tilicho Lake is the highest Himalayan lake in Nepal, located at an altitude of 430 m above sea level in the foothills of Annapurna Glacier in Manang district. The lake is about 4 km in length and 1.2 km in width. Surrounded by snow-clad mountains, the lake is known as a difficult trekking and tourist destination.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Tilicho Lake is the highest Himalayan lake in Nepal, located at an altitude of 430 m above sea level in the foothills of Annapurna Glacier in Manang district. The lake is about 4 km in length and 1.2 km in width. Surrounded by snow-clad mountains, the lake is known as a difficult trekking and tourist destination.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 21 / 60
**Linked Candidate Items:** `item_041`, `item_046`
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [गाभी उच्चस्तरीय टोलीसँग स्वास्थ्यमन्त्रीको छलफल: राष्ट्रिय खोप कार्यक्रम](https://gorkhapatraonline.com/news/207198)

### 1. Source Passage (Nepali · Condition C1)
> स्वास्थ्य तथा जनसङ्ख्या मन्त्रालय र गाभी (ग्लोबल एलायन्स फर भ्याक्सिन्स एन्ड इम्युनाइजेसन) को उच्चस्तरीय टोलीबीच नेपालको राष्ट्रिय खोप कार्यक्रम सुदृढीकरणबारे छलफल भएको छ। नेपालमा बालबालिकालाई निःशुल्क रूपमा प्रदान गरिँदै आएको नियमित खोप कभरेज विस्तार गर्न र दुर्गम क्षेत्रमा खोप सेवा सुरक्षित रूपमा पुर्‍याउन सहयोग निरन्तर रहने गाभीले जनाएको छ। मन्त्रालयले दादुरा-रुबेला, पोलियो र एचपीभी खोप अभियानलाई प्राथमिकतामा राखेको जनाएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The high-level team of the Ministry of Health and Population and Gavi ( Global Alliance for Vaccines and Immunization ) discussed strengthening Nepal's national vaccination program. Gavi said that it will continue to support the expansion of regular vaccination coverage to children in Nepal, which is being provided free of charge, and the safe delivery of vaccination services in remote areas. The ministry has prioritized the polio and HPV vaccination campaign in Dadra and Rubella.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The high-level team of the Ministry of Health and Population and Gavi ( Global Alliance for Vaccines and Immunization ) discussed strengthening Nepal's national vaccination program. Gavi said that it will continue to support the expansion of regular vaccination coverage to children in Nepal, which is being provided free of charge, and the safe delivery of vaccination services in remote areas. The ministry has prioritized the polio and HPV vaccination campaign in Dadra and Rubella.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 22 / 60
**Linked Candidate Items:** `item_042`, `item_047`
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [स्वास्थ्य अनुसन्धान: क्यान्सर तथा नसर्ने रोग रोकथाम](https://www.gorkhapatraonline.com/news/111744)

### 1. Source Passage (Nepali · Condition C1)
> स्वास्थ्य विज्ञहरूका अनुसार नेपालमा नसर्ने रोगहरू (मुटुरोग, क्यान्सर र मधुमेह) का कारण हुने मृत्युदर कुल मृत्युको ७० प्रतिशतभन्दा माथि पुगेको छ। अस्वस्थ खानपान, शारीरिक निष्क्रियता र सुर्तीजन्य पदार्थको प्रयोगले क्यान्सर तथा उच्च रक्तचापको जोखिम बढाएको अध्ययनले देखाएको छ। स्वास्थ्य सेवा विभागले नसर्ने रोगको रोकथाम तथा स्क्रिनिङका लागि प्राथमिक स्वास्थ्य केन्द्रस्तरमै विशेष कार्यक्रम सञ्चालन गर्नुपर्नेमा जोड दिएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to health experts, the mortality rate due to non-communicable diseases ( heart disease, cancer and diabetes ) in Nepal has reached over 20 % of the total deaths. Studies have shown that unhealthy eating habits and physical inactivity and tobacco use increase the risk of cancer and hypertension. The Department of Health Services has stressed on special programs at the primary health centre level for the prevention and screening of non-communicable diseases.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to health experts, the mortality rate due to non-communicable diseases ( heart disease, cancer and diabetes ) in Nepal has reached over 20 % of the total deaths. Studies have shown that unhealthy eating habits and physical inactivity and tobacco use increase the risk of cancer and hypertension. The Department of Health Services has stressed on special programs at the primary health centre level for the prevention and screening of non-communicable diseases.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 23 / 60
**Linked Candidate Items:** `item_043`, `item_048`
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [मातृ बाल मृत्युदर न्यूनीकरण: सुरक्षित मातृत्व कार्यक्रम](https://gorkhapatraonline.com/index.php/news/202136)

### 1. Source Passage (Nepali · Condition C1)
> स्वास्थ्य तथा जनसङ्ख्या मन्त्रालयले सुरक्षित मातृत्व तथा मातृ बाल मृत्युदर न्यूनीकरणलाई मुख्य प्राथमिकता दिएको छ। राष्ट्रिय जनगणना २०७८ को अध्ययन अनुसार नेपालमा मातृ मृत्युदर प्रति लाख जीवित जन्ममा १५१ मा झरेको छ। सरकारी स्वास्थ्य संस्थाहरूमा निःशुल्क प्रसूति सेवा र यातायात खर्च उपलब्ध गराइएपछि संस्थागत सुत्केरी दरमा उल्लेख्य वृद्धि भएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Ministry of Health and Population has made safe motherhood and maternal mortality reduction a top priority. According to a study by the National Census Bureau, the maternal mortality rate in Nepal has fallen to eight per million live births. The institutional delivery rate has increased significantly since free maternity services and transportation costs are provided in government health institutions.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Ministry of Health and Population has made safe motherhood and maternal mortality reduction a top priority. According to a study by the National Census Bureau, the maternal mortality rate in Nepal has fallen to eight per million live births. The institutional delivery rate has increased significantly since free maternity services and transportation costs are provided in government health institutions.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 24 / 60
**Linked Candidate Items:** `item_044`, `item_049`
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [स्वास्थ्य मन्त्रालय डेंगु नियन्त्रण तथा लामखुट्टे रोकथाम निर्देशिका](https://www.onlinekhabar.com/2022/10/1206660/%E0%A4%B8%E0%A5%8D%E0%A4%B5%E0%A4%BE%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A5%8D%E0%A4%AF-%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%B2%E0%A4%AF%E0%A4%95%E0%A4%BE-%E0%A5%AB)

### 1. Source Passage (Nepali · Condition C1)
> स्वास्थ्य तथा जनसङ्ख्या मन्त्रालयले डेंगु सङ्क्रमण तीव्र रूपमा फैलिएपछि देशव्यापी सतर्कता अपनाउन र लामखुट्टेको लार्भा नष्ट गर्ने 'खोज र नष्ट गर' अभियान चलाउन निर्देशन दिएको छ। एडिस प्रजातिको लामखुट्टेको टोकाइबाट सर्ने यो रोगका कारण हजारौँ नागरिक प्रभावित भएका छन्। स्वास्थ्य मन्त्रालयले सबै सरकारी अस्पतालहरूमा डेंगुका बिरामीका लागि निःशुल्क परामर्श तथा उपचार डेस्क स्थापना गरेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Ministry of Health and Population has directed to adopt nationwide vigilance and conduct a'Search and Destroy'campaign to destroy mosquito larvae following the rapid spread of dengue infection. Thousands of citizens have been affected due to this disease transmitted by the bite of Aedes species of mosquitoes. The Ministry of Health has set up free consultation and treatment desks for dengue patients in all government hospitals.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Ministry of Health and Population has directed to adopt nationwide vigilance and conduct a'Search and Destroy'campaign to destroy mosquito larvae following the rapid spread of dengue infection. Thousands of citizens have been affected due to this disease transmitted by the bite of Aedes species of mosquitoes. The Ministry of Health has set up free consultation and treatment desks for dengue patients in all government hospitals.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 25 / 60
**Linked Candidate Items:** `item_045`, `item_050`
**Domain:** government_report | **Topic Sub-Genre:** health | **Source:** [औषधि व्यवस्था विभाग: बजार अनुगमन तथा गुणस्तर नियन्त्रण](https://gorkhapatraonline.com/news/26125)

### 1. Source Passage (Nepali · Condition C1)
> औषधि व्यवस्था विभागले बजारमा बिक्रीवितरण भइरहेका औषधिको गुणस्तर सुनिश्चित गर्न र अनुचित व्यापारिक क्रियाकलाप नियन्त्रण गर्न विशेष अनुगमन टोली परिचालन गरेको छ। सरकारले गुणस्तरहीन औषधि बिक्री गर्ने फार्मेसीहरूलाई कारबाही गर्ने र जीवनरक्षक औषधिको अभाव हुन नदिन आपूर्ति व्यवस्थापन कडा बनाएको जनाएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Department of Drug Administration has deployed special monitoring teams to ensure the quality of the drugs being sold in the market and to control unfair trade practices. The government has said that it will take action against pharmacies selling substandard drugs and tighten supply management to prevent a shortage of life-saving drugs.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Department of Drug Administration has deployed special monitoring teams to ensure the quality of the drugs being sold in the market and to control unfair trade practices. The government has said that it will take action against pharmacies selling substandard drugs and tighten supply management to prevent a shortage of life-saving drugs.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 26 / 60
**Linked Candidate Items:** `item_051`, `item_056`
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [कृषि मन्त्रालय: धान उत्पादन चार प्रतिशतले वृद्धि](https://gorkhapatraonline.com/news/137532)

### 1. Source Passage (Nepali · Condition C1)
> कृषि तथा पशुपन्छी विकास मन्त्रालयका अनुसार चालु आर्थिक वर्ष २०८१/८२ मा धानको उत्पादन ४.०४ प्रतिशतले बढेर ५९ लाख ५५ हजार ४७६ मेट्रिक टन पुगेको छ। गत आर्थिक वर्षमा ५७ लाख २४ हजार मेट्रिक टन धान उत्पादन भएको थियो। समयमा रासायनिक मलको उपलब्धता, उन्नत बीउबिजन र अनुकूल वर्षाका कारण धानको उत्पादकत्व प्रतिहेक्टर ४.१९ मेट्रिक टन पुगेको मन्त्रालयले जनाएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Ministry of Agriculture and Livestock Development, the rice production in the current financial year has increased by 4. 4 percent to reach 6. 00 million metric tons. Last financial year, rice production was 13. 00 million metric tons. The availability of chemical fertilizers in time and improved sowing and favorable rainfall have increased the rice productivity to 4. 03 metric tons per hectare.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Ministry of Agriculture and Livestock Development, the rice production in the current financial year has increased by 4. 4 percent to reach 6. 00 million metric tons. Last financial year, rice production was 13. 00 million metric tons. The availability of chemical fertilizers in time and improved sowing and favorable rainfall have increased the rice productivity to 4. 03 metric tons per hectare.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 27 / 60
**Linked Candidate Items:** `item_052`, `item_057`
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [रासायनिक मल आपूर्ति तथा अनुदान व्यवस्थापन](https://gorkhapatraonline.com/news/71329)

### 1. Source Passage (Nepali · Condition C1)
> सरकारले किसानलाई रासायनिक मलको अभाव हुन नदिन अनुदान नीतिलाई प्रभावकारी बनाएको छ। साल्ट ट्रेडिङ कर्पोरेसन र कृषि सामग्री कम्पनी लिमिटेडमार्फत युरिया, डीएपी र पोटास मलको आयात व्यवस्थित गरिएको छ। असारे धान रोपाइँका बेला मलको सहज उपलब्धता सुनिश्चित गर्न मन्त्रालयले अन्तरनिकाय समन्वय समिति गठन गरेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The government has made the subsidy policy effective to prevent farmers from facing shortage of chemical fertilizers. Import of urea and DAP and potash fertilizers has been arranged through Salt Trading Corporation and Agricultural Materials Company Limited. To ensure smooth availability of fertilizers during the sowing of rice, the ministry has formed an Inter-Agency Coordination Committee.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The government has made the subsidy policy effective to prevent farmers from facing shortage of chemical fertilizers. Import of urea and DAP and potash fertilizers has been arranged through Salt Trading Corporation and Agricultural Materials Company Limited. To ensure smooth availability of fertilizers during the sowing of rice, the ministry has formed an Inter-Agency Coordination Committee.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 28 / 60
**Linked Candidate Items:** `item_053`, `item_058`
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [प्रधानमन्त्री कृषि आधुनिकीकरण परियोजना: झापा धान सुपरजोन](https://gorkhapatraonline.com/news/19549)

### 1. Source Passage (Nepali · Condition C1)
> प्रधानमन्त्री कृषि आधुनिकीकरण परियोजना अन्तर्गत झापा जिल्लामा सञ्चालित धान सुपरजोन कार्यक्रममार्फत उत्पादकत्व उल्लेख्य रूपमा बढेको छ। परियोजना कार्यान्वयन एकाइका अनुसार आधुनिक कृषि यन्त्र, चक्लाबन्दी र सिँचाइ विस्तारका कारण पाँच वर्षअघि प्रतिहेक्टर ४.६९ मेट्रिक टन रहेको उत्पादकत्व बढेर ५.६ मेट्रिक टन पुगेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The rice superzone program in Jhapa district under the Pradhan Mantri Krishi Modernization Project has significantly increased productivity. According to the project implementation unit, modern agricultural machinery and irrigation expansion have increased the productivity from 4. 6 metric tons per hectare five years ago to 5. 6 metric tons.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The rice superzone program in Jhapa district under the Pradhan Mantri Krishi Modernization Project has significantly increased productivity. According to the project implementation unit, modern agricultural machinery and irrigation expansion have increased the productivity from 4. 6 metric tons per hectare five years ago to 5. 6 metric tons.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 29 / 60
**Linked Candidate Items:** `item_054`, `item_059`
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [राष्ट्रिय चिया तथा कफी विकास बोर्ड: नेपाली चिया निर्यात समीक्षा](https://gorkhapatraonline.com/news/105422)

### 1. Source Passage (Nepali · Condition C1)
> राष्ट्रिय चिया तथा कफी विकास बोर्डका अनुसार नेपाली अर्थोडक्स चियाको अन्तर्राष्ट्रिय बजार विस्तारका लागि नयाँ रणनीति तय गरिएको छ। कुल चिया निर्यातमध्ये ठूलो हिस्सा छिमेकी भारतमा निकासी हुने गरेकोमा अब युरोपेली तथा अमेरिकी बजारमा प्रत्यक्ष निर्यात बढाउन गुणस्तर प्रमाणीकरण र ब्राण्डिङलाई प्राथमिकता दिइएको बोर्डले जनाएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the National Tea and Coffee Development Board, a new strategy has been formulated to expand the international market of Nepali Orthodox tea. With a large part of the total tea exports going to neighbouring India, quality certification and branding have now been prioritized to increase direct exports to European and American markets.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the National Tea and Coffee Development Board, a new strategy has been formulated to expand the international market of Nepali Orthodox tea. With a large part of the total tea exports going to neighbouring India, quality certification and branding have now been prioritized to increase direct exports to European and American markets.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 30 / 60
**Linked Candidate Items:** `item_055`, `item_060`
**Domain:** government_report | **Topic Sub-Genre:** agriculture | **Source:** [पशु सेवा विभाग: दुग्ध उत्पादन तथा आत्मनिर्भरता](https://gorkhapatraonline.com/index.php/news/79742)

### 1. Source Passage (Nepali · Condition C1)
> पशु सेवा विभाग र राष्ट्रिय दुग्ध विकास बोर्डका अनुसार नेपाल दुग्ध उत्पादनमा आत्मनिर्भरतातर्फ अघि बढेको छ। ग्रामीण भेगका किसानहरूलाई उन्नत जातका गाईभैँसी पालनमा प्रोत्साहन, दाना अनुदान र चिस्यान केन्द्रको स्थापना गरिएपछि वार्षिक दूध उत्पादन २५ लाख मेट्रिक टन नाघेको छ। विद्यालयहरूमा दिवा खाजामा दूध समावेश गर्ने कार्यक्रम समेत सुरु गरिएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Department of Animal Services and the National Dairy Development Board, Nepal has moved towards self-sufficiency in dairy production. Farmers in rural areas have been encouraged to raise improved breeds of cattle. Annual milk production has exceeded 5 million metric tons since the establishment of the Grain Subsidy and Irrigation Centre. A programme to include milk in the day meals in schools has also been launched.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Department of Animal Services and the National Dairy Development Board, Nepal has moved towards self-sufficiency in dairy production. Farmers in rural areas have been encouraged to raise improved breeds of cattle. Annual milk production has exceeded 5 million metric tons since the establishment of the Grain Subsidy and Irrigation Centre. A programme to include milk in the day meals in schools has also been launched.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 31 / 60
**Linked Candidate Items:** `item_061`, `item_066`
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [राष्ट्रिय तथ्याङ्क कार्यालय जनगणना २०७८: साक्षरता दर प्रतिवेदन](https://gorkhapatraonline.com/news/65329)

### 1. Source Passage (Nepali · Condition C1)
> राष्ट्रिय तथ्याङ्क कार्यालयद्वारा सार्वजनिक राष्ट्रिय जनगणना २०७८ को नतिजा अनुसार नेपालको कुल साक्षरता दर ७६.३ प्रतिशत पुगेको छ। पुरुष साक्षरता दर ८३.६ प्रतिशत र महिला साक्षरता दर ६९.४ प्रतिशत रहेको छ। तथ्याङ्क अनुसार बागमती प्रदेशमा सबैभन्दा उच्च साक्षरता रहेको छ भने मधेश प्रदेशमा साक्षरता दर सबैभन्दा न्यून पाइएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the results of the National Census published by the National Statistics Office, the total literacy rate of Nepal has reached 53.33 %. Male literacy rate is 66.6 % and female literacy rate is 74.4 %. According to the data, Bagmati Province has the highest literacy rate while Madhesh Province has the lowest literacy rate.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the results of the National Census published by the National Statistics Office, the total literacy rate of Nepal has reached 53.33 %. Male literacy rate is 66.6 % and female literacy rate is 74.4 %. According to the data, Bagmati Province has the highest literacy rate while Madhesh Province has the lowest literacy rate.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 32 / 60
**Linked Candidate Items:** `item_062`, `item_067`
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [शिक्षा तथा मानव स्रोत विकास केन्द्र: सामुदायिक विद्यालय दिवा खाजा](https://gorkhapatraonline.com/news/183700)

### 1. Source Passage (Nepali · Condition C1)
> शिक्षा तथा मानव स्रोत विकास केन्द्रका अनुसार देशभरका सामुदायिक विद्यालयमा सञ्चालित दिवा खाजा कार्यक्रमले विद्यार्थी भर्ना दर र टिकाउ दरमा सुधार ल्याएको छ। प्रारम्भिक बालविकासदेखि कक्षा ५ सम्मका विद्यार्थीलाई वार्षिक १८० दिनका लागि प्रति विद्यार्थी २० देखि २५ रुपैयाँका दरले खाजा रकम निकासा गरिएको छ। यस कार्यक्रमबाट देशभरका २९ लाखभन्दा बढी बालबालिका प्रत्यक्ष लाभान्वित भएका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Center for Education and Human Resource Development, the day-lunch program in community schools across the country has improved student enrolment rates and sustainability rates. A lunch amount of 20 to 55 rupees per student has been released to provide annual tuition to students from early childhood development to grade 5. More than half a million children across the country have directly benefited from this program.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Center for Education and Human Resource Development, the day-lunch program in community schools across the country has improved student enrolment rates and sustainability rates. A lunch amount of 20 to 55 rupees per student has been released to provide annual tuition to students from early childhood development to grade 5. More than half a million children across the country have directly benefited from this program.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 33 / 60
**Linked Candidate Items:** `item_063`, `item_068`
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [प्राविधिक शिक्षा तथा व्यावसायिक तालिम परिषद् (सीटीईभीटी): सीप विकास](https://gorkhapatraonline.com/news/55391)

### 1. Source Passage (Nepali · Condition C1)
> प्राविधिक शिक्षा तथा व्यावसायिक तालिम परिषद् (सीटीईभीटी) ले श्रम बजारको माग अनुसार दक्ष जनशक्ति उत्पादन गर्न ७७ वटै जिल्लामा प्राविधिक शिक्षालयको सञ्जाल विस्तार गरेको छ। इन्जिनियरिङ, स्वास्थ्य, कृषि र सूचना प्रविधिका डिप्लोमा तथा प्रि-डिप्लोमा तहका कार्यक्रममार्फत वार्षिक ६० हजारभन्दा बढी युवाहरूलाई सीपमूलक तालिम प्रदान गरिँदै आएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Council for Technical Education and Vocational Training ( CTEVT ) has expanded the network of technical schools in all the districts to produce skilled manpower as per the demand of the labour market.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Council for Technical Education and Vocational Training ( CTEVT ) has expanded the network of technical schools in all the districts to produce skilled manpower as per the demand of the labour market.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 34 / 60
**Linked Candidate Items:** `item_064`, `item_069`
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [राष्ट्रिय परीक्षा बोर्ड: माध्यमिक शिक्षा परीक्षा (एसईई) नतिजा](https://gorkhapatraonline.com/news/20316)

### 1. Source Passage (Nepali · Condition C1)
> राष्ट्रिय परीक्षा बोर्डले माध्यमिक शिक्षा परीक्षा (एसईई) को नतिजा सार्वजनिक गर्दै कुल परीक्षार्थीमध्ये ९ हजारभन्दा बढीले ३.६ देखि ४ जीपीए हासिल गरेको जनाएको छ। बोर्डले परीक्षामा ग्रेडिङ प्रणाली लागू गरी विद्यार्थीहरूको विषयगत दक्षता अभिवृद्धि गर्न नयाँ पाठ्यक्रम र उत्तरपुस्तिका परीक्षण मापदण्ड कार्यान्वयनमा ल्याएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The National Board of Examinations ( NBE ) has released the results of the Secondary Education Examination ( SSEE ), stating that out of the total candidates, more than 6000 have achieved GPAs ranging from 3 to 4. The Board has implemented a grading system in the examination to enhance the subjective skills of the students by implementing new syllabus and answer book test standards.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The National Board of Examinations ( NBE ) has released the results of the Secondary Education Examination ( SSEE ), stating that out of the total candidates, more than 6000 have achieved GPAs ranging from 3 to 4. The Board has implemented a grading system in the examination to enhance the subjective skills of the students by implementing new syllabus and answer book test standards.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 35 / 60
**Linked Candidate Items:** `item_065`, `item_070`
**Domain:** government_report | **Topic Sub-Genre:** education | **Source:** [शिक्षा तथा मानव स्रोत विकास केन्द्र: विद्यालय शिक्षा फ्ल्यास प्रतिवेदन](https://cehrd.gov.np)

### 1. Source Passage (Nepali · Condition C1)
> शिक्षा तथा मानव स्रोत विकास केन्द्र (सीईएचआरडी) को वार्षिक फ्ल्यास रिपोर्ट अनुसार नेपालमा आधारभूत तह (कक्षा १-८) को खुद भर्ना दर ९६ प्रतिशतभन्दा माथि पुगेको छ। सामुदायिक विद्यालयहरूमा सूचना प्रविधि प्रयोगशाला, निःशुल्क पाठ्यपुस्तक वितरण र छात्रवृत्ति कार्यक्रमले लैङ्गिक समानता हासिल गर्न सहयोग पुर्‍याएको प्रतिवेदनमा उल्लेख छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the annual flash report of the Centre for Education and Human Resource Development ( CEHRD ), the self-enrolment rate of basic level ( classes 1 to 1 ) in Nepal has reached above 14 %. The report states that information technology laboratories in community schools and free textbook distribution and scholarship programs have helped achieve gender equality.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the annual flash report of the Centre for Education and Human Resource Development ( CEHRD ), the self-enrolment rate of basic level ( classes 1 to 1 ) in Nepal has reached above 14 %. The report states that information technology laboratories in community schools and free textbook distribution and scholarship programs have helped achieve gender equality.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 36 / 60
**Linked Candidate Items:** `item_071`, `item_076`
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [अर्थ मन्त्रालय: वार्षिक बजेट वक्तव्य तथा आर्थिक विनियोजन](https://mof.gov.np/category/budget-speech)

### 1. Source Passage (Nepali · Condition C1)
> अर्थ मन्त्रालयद्वारा प्रस्तुत वार्षिक बजेट वक्तव्यमा आर्थिक वृद्धि, उत्पादन वृद्धि र रोजगारी सिर्जनालाई प्रमुख प्राथमिकतामा राखिएको छ। सरकारले पुँजीगत खर्च बढाउन पूर्वाधार विकास आयोजनालाई समयमै बजेट निकासा गर्ने र वित्तीय अनुशासन कायम राख्ने नीति अवलम्बन गरेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The annual budget statement presented by the Ministry of Finance places economic growth, increased productivity and job creation as key priorities. The government has adopted a policy of timely budgeting and maintaining fiscal discipline to organize infrastructure development to increase capital expenditure.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The annual budget statement presented by the Ministry of Finance places economic growth, increased productivity and job creation as key priorities. The government has adopted a policy of timely budgeting and maintaining fiscal discipline to organize infrastructure development to increase capital expenditure.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 37 / 60
**Linked Candidate Items:** `item_072`, `item_077`
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [मध्यमकालीन खर्च संरचना तथा सार्वजनिक वित्त व्यवस्थापन](https://gorkhapatraonline.com/news/61451)

### 1. Source Passage (Nepali · Condition C1)
> राष्ट्रिय योजना आयोग र अर्थ मन्त्रालयले सार्वजनिक स्रोतको समुचित उपयोगका लागि तीन वर्षे चक्रीय मध्यमकालीन खर्च संरचना (एमटीईएफ) कार्यान्वयन गरेका छन्। यस प्रणालीले आवधिक योजना र वार्षिक बजेटबीच तालमेल मिलाउँदै सार्वजनिक खर्चमा पारदर्शिता र वित्तीय अनुशासन कायम गर्न मद्दत पुर्‍याउँछ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The National Planning Commission and the Ministry of Finance have implemented a three-year Cyclical Medium Term Expenditure Framework ( MTEF ) for proper utilization of public resources. This system helps in maintaining transparency and fiscal discipline in public expenditure by harmonizing periodic planning and annual budgets.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The National Planning Commission and the Ministry of Finance have implemented a three-year Cyclical Medium Term Expenditure Framework ( MTEF ) for proper utilization of public resources. This system helps in maintaining transparency and fiscal discipline in public expenditure by harmonizing periodic planning and annual budgets.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 38 / 60
**Linked Candidate Items:** `item_073`, `item_078`
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [महालेखा नियन्त्रक कार्यालय: सरकारी राजस्व तथा बजेट खर्च स्थिति](https://www.gorkhapatraonline.com/news/89477)

### 1. Source Passage (Nepali · Condition C1)
> महालेखा नियन्त्रक कार्यालयको तथ्याङ्क अनुसार चालु आर्थिक वर्षको पहिलो पाँच महिनामा सरकारको कुल आम्दानी ३ खर्ब ८३ अर्ब रुपैयाँ र कुल बजेट खर्च ४ खर्ब ५२ अर्ब रुपैयाँ पुगेको छ। सरकारले वार्षिक लक्ष्य अनुसार राजस्व संकलन बढाउन कर प्रणाली सुधार र भन्सार चुहावट नियन्त्रणमा कडाइ गरेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the data of the Comptroller and Auditor General's Office, the total revenue of the government in the first five months of the current financial year has reached 3 trillion rupees and the total budget expenditure has reached 4 trillion rupees. The government has reformed the tax system and tightened the control of customs leaks to increase revenue collection according to the annual target.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the data of the Comptroller and Auditor General's Office, the total revenue of the government in the first five months of the current financial year has reached 3 trillion rupees and the total budget expenditure has reached 4 trillion rupees. The government has reformed the tax system and tightened the control of customs leaks to increase revenue collection according to the annual target.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 39 / 60
**Linked Candidate Items:** `item_074`, `item_079`
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [नेपाल खुद्रा व्यापार सङ्घ: उपभोक्ता मूल्य तथा मुद्रास्फीति](https://gorkhapatraonline.com/news/142145)

### 1. Source Passage (Nepali · Condition C1)
> दैनिक उपभोग्य वस्तुहरूको बजार अनुगमन प्रतिवेदन अनुसार खाद्यान्न, खानेतेल र गेडागुडीको मूल्यमा सामान्य वृद्धि भएको छ। नेपाल खुद्रा व्यापार सङ्घ र वाणिज्य विभागले कृत्रिम अभाव र कालोबजारी नियन्त्रण गर्न संयुक्त बजार अनुगमनलाई तीव्रता दिएका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Daily Consumer Market Monitoring Report, there has been a general increase in the prices of food and edible oils and gedagudi. The Nepal Retail Trade Association and the Department of Commerce have intensified joint market monitoring to control artificial shortages and black marketing.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Daily Consumer Market Monitoring Report, there has been a general increase in the prices of food and edible oils and gedagudi. The Nepal Retail Trade Association and the Department of Commerce have intensified joint market monitoring to control artificial shortages and black marketing.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 40 / 60
**Linked Candidate Items:** `item_075`, `item_080`
**Domain:** government_report | **Topic Sub-Genre:** economy_finance | **Source:** [नेपाल राष्ट्र बैंक: मौद्रिक नीति तथा समष्टिगत आर्थिक समीक्षा](https://www.onlinekhabar.com/2024/07/1514858/rashtra-bank-passing-monetary-policy)

### 1. Source Passage (Nepali · Condition C1)
> नेपाल राष्ट्र बैंकले चालु आर्थिक वर्षको मौद्रिक नीति सार्वजनिक गर्दै वित्तीय स्थायित्व र बाह्य क्षेत्र सन्तुलन कायम राख्ने नीति लिएको छ। बैंक तथा वित्तीय संस्थाहरूमा तरलता सहज बनाउन नीतिगत दर घटाउनुका साथै विदेशी विनिमय सञ्चिति २० खर्ब रुपैयाँ नाघेकाले अर्थतन्त्रको बाह्य क्षेत्र बलियो अवस्थामा रहेको केन्द्रीय बैंकले जनाएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Nepal Rastra Bank has released its monetary policy for the current fiscal year and adopted a policy of maintaining financial stability and external sector balance. The central bank said that the external sector of the economy is in a strong position due to the reduction in policy rates to facilitate liquidity in banks and financial institutions, as well as the foreign exchange reserves exceeding 20 trillion rupees.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Nepal Rastra Bank has released its monetary policy for the current fiscal year and adopted a policy of maintaining financial stability and external sector balance. The central bank said that the external sector of the economy is in a strong position due to the reduction in policy rates to facilitate liquidity in banks and financial institutions, as well as the foreign exchange reserves exceeding 20 trillion rupees.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 41 / 60
**Linked Candidate Items:** `item_081`, `item_087`
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [टी-२० विश्वकपका लागि नेपाली क्रिकेट टोलीको घोषणा](https://www.onlinekhabar.com/2026/01/1843313/these-are-the-15-nepali-players-who-will-play-in-the-t20-world-cup)

### 1. Source Passage (Nepali · Condition C1)
> नेपाल क्रिकेट संघ (क्यान) ले आईसीसी पुरुष टी-२० विश्वकपका लागि १५ सदस्यीय राष्ट्रिय टोली घोषणा गरेको छ। युवा तथा अनुभवी खेलाडीहरूको समिश्रण रहेको नेपाली टोलीमा रोहित पौडेलले कप्तानी सम्हालेका छन् भने सोमपाल कामी, कुशल भुर्तेल र दीपेन्द्रसिंह ऐरी समावेश छन्। नेपाली टोलीले विश्वकपमा समूह चरणका खेलहरू प्रतिष्ठित अन्तर्राष्ट्रिय रंगशालामा खेल्ने तालिका छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Cricket Association of Nepal ( CAN ) has announced a fifteen-member national team for the ICC Men's T20 World Cup. The Nepali team is a combination of young and experienced players, captained by Rohit Poudel, with Sompal Kami, Kushal Bhurtel, and Dipendra Singh Ayri. The Nepali team will play its group stage matches in the World Cup at the prestigious international stadium.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Cricket Association of Nepal ( CAN ) has announced a fifteen-member national team for the ICC Men's T20 World Cup. The Nepali team is a combination of young and experienced players, captained by Rohit Poudel, with Sompal Kami, Kushal Bhurtel, and Dipendra Singh Ayri. The Nepali team will play its group stage matches in the World Cup at the prestigious international stadium.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 42 / 60
**Linked Candidate Items:** `item_082`, `item_088`
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [दीपेन्द्रसिंह ऐरी: ९ बलमा अर्धशतकको ऐतिहासिक विश्व कीर्तिमान](https://www.onlinekhabar.com/personality/dipendra-singh-airee)

### 1. Source Passage (Nepali · Condition C1)
> नेपाली क्रिकेटका अलराउन्डर दीपेन्द्रसिंह ऐरीले अन्तर्राष्ट्रिय टी-२० क्रिकेटमा विश्वकै सबैभन्दा छिटो ९ बलमा अर्धशतक प्रहार गरी कीर्तिमान बनाएका छन्। चीनको हाङ्ग्जाउमा आयोजित १९औँ एसियाली खेलकुद अन्तर्गत मंगोलियाविरुद्धको खेलमा उनले यो दुर्लभ कीर्तिमान रचेका हुन्। यसैगरी उनले अन्तर्राष्ट्रिय खेलमा एकै ओभरमा ६ छक्का समेत प्रहार गरेका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Nepali cricket all-rounder Dipendrasinh Ayri holds the record for the fastest half-century in international T20I cricket. He also hit six sixes in an over in an international match against Mongolia at the 16th Asian Games in Hangzhou, China.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Nepali cricket all-rounder Dipendrasinh Ayri holds the record for the fastest half-century in international T20I cricket. He also hit six sixes in an over in an international match against Mongolia at the 16th Asian Games in Hangzhou, China.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 43 / 60
**Linked Candidate Items:** `item_083`, `item_089`
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [क्यानद्वारा नेपाल प्रिमियर लिग (एनपीएल) आयोजनाको तयारी](https://www.onlinekhabar.com/2020/01/826769/%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%A8-%E0%A4%86%E0%A4%AB%E0%A5%88%E0%A4%82%E0%A4%B2%E0%A5%87-%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2-%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AE)

### 1. Source Passage (Nepali · Condition C1)
> नेपाल क्रिकेट संघ (क्यान) ले आधिकारिक फ्रेन्चाइज प्रतियोगिता नेपाल प्रिमियर लिग (एनपीएल) को औपचारिक तयारी सुरु गरेको छ। देशभरका प्रमुख सहरहरूलाई प्रतिनिधित्व गर्ने टोलीहरूमार्फत घरेलु क्रिकेटको व्यावसायिक विकास गर्ने र विदेशी खेलाडीहरूलाई समेत समावेश गरी प्रतियोगितालाई अन्तर्राष्ट्रिय स्तरको बनाउने क्यानको योजना छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Cricket Association of Nepal ( CAN ) has begun formal preparations for the official franchise competition, the Nepal Premier League ( NPL ). CAN plans to develop domestic cricket professionally through teams representing major cities across the country and make the competition international by including foreign players.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Cricket Association of Nepal ( CAN ) has begun formal preparations for the official franchise competition, the Nepal Premier League ( NPL ). CAN plans to develop domestic cricket professionally through teams representing major cities across the country and make the competition international by including foreign players.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 44 / 60
**Linked Candidate Items:** `item_084`, `item_090`
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [एन्फा राष्ट्रिय फुटबल लिग तथा सहिद स्मारक लिग समीक्षा](https://www.hamrokhelkud.com/football/170529.html)

### 1. Source Passage (Nepali · Condition C1)
> अखिल नेपाल फुटबल संघ (एन्फा) ले राष्ट्रिय लिग तथा सहिद स्मारक फुटबल प्रतियोगितालाई व्यवस्थित गर्न नयाँ कार्यविधि कार्यान्वयनमा ल्याएको छ। क्लबहरूमा विदेशी खेलाडीहरूको श्रम स्वीकृति, खेलाडी सुरक्षा तथा पारिश्रमिक सम्झौताका मापदण्डहरू कडाइका साथ पालना गर्न एन्फाले सबै सहभागी क्लबहरूलाई निर्देशन दिएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The All Nepal Football Association ( ANFA ) has implemented new procedures to organize the National League and Martyrs'Memorial Football Tournament. ANFA has directed all participating clubs to strictly follow the standards of foreign players'labour clearance and player safety and remuneration agreements in clubs.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The All Nepal Football Association ( ANFA ) has implemented new procedures to organize the National League and Martyrs'Memorial Football Tournament. ANFA has directed all participating clubs to strictly follow the standards of foreign players'labour clearance and player safety and remuneration agreements in clubs.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 45 / 60
**Linked Candidate Items:** `item_085`, `item_091`
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [एसीसी प्रिमियर कप विजेता नेपाली क्रिकेट टोलीको स्वागत](https://www.onlinekhabar.com/2026/09/2016553/nepali-cricket-team-returns-home-after-winning-acc-premier-cup)

### 1. Source Passage (Nepali · Condition C1)
> एसियाली क्रिकेट काउन्सिल (एसीसी) प्रिमियर कपको उपाधि जितेर एसिया कपमा छनोट भएको नेपाली राष्ट्रिय क्रिकेट टोली स्वदेश फर्किएको छ। कीर्तिपुरस्थित त्रिवि क्रिकेट मैदानमा सम्पन्न फाइनल खेलमा यूएईलाई हराउँदै नेपालले उपाधि हात पारेको थियो। त्रिभुवन अन्तर्राष्ट्रिय विमानस्थलमा सयौँ समर्थक र खेल अधिकारीहरूले टोलीको भव्य स्वागत गरे।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Nepali national cricket team, which qualified for the Asia Cup by winning the Asian Cricket Council ( ACC ) Premier Cup title, has returned home. Nepal won the title by defeating UAE in the final match held at the Triveni Cricket Ground in Kirtipur. The team was given a grand welcome by hundreds of supporters and sports officials at Tribhuvan International Airport.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Nepali national cricket team, which qualified for the Asia Cup by winning the Asian Cricket Council ( ACC ) Premier Cup title, has returned home. Nepal won the title by defeating UAE in the final match held at the Triveni Cricket Ground in Kirtipur. The team was given a grand welcome by hundreds of supporters and sports officials at Tribhuvan International Airport.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 46 / 60
**Linked Candidate Items:** `item_086`, `item_092`
**Domain:** news | **Topic Sub-Genre:** sports | **Source:** [१९औँ एसियाली खेलकुदमा नेपाली खेलाडीको सहभागिता](https://www.hamrokhelkud.com/featured/135943.html)

### 1. Source Passage (Nepali · Condition C1)
> चीनको हाङझावमा सम्पन्न १९औँ एसियाली खेलकुदमा नेपालका २३४ खेलाडीहरूले २९ विभिन्न खेल विधामा सहभागिता जनाएका छन्। राष्ट्रिय खेलकुद परिषद् (राखेप) का अनुसार कराते र कबड्डी विधामा नेपाली खेलाडीहरूले ऐतिहासिक पदक जित्दै देशको नाम अन्तर्राष्ट्रिय मञ्चमा उच्च राखेका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Twenty-seven players from Nepal have participated in various sports disciplines at the 16th Asian Games held in Hangzhou, China. According to the National Sports Council ( abbreviated ), Nepali players in karate and kabaddi disciplines have made the country proud on the international stage by winning historic medals.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Twenty-seven players from Nepal have participated in various sports disciplines at the 16th Asian Games held in Hangzhou, China. According to the National Sports Council ( abbreviated ), Nepali players in karate and kabaddi disciplines have made the country proud on the international stage by winning historic medals.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 47 / 60
**Linked Candidate Items:** `item_093`, `item_098`
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [मनसुनजन्य बाढी पहिरो: राष्ट्रिय मानवीय तथा भौतिक क्षति विवरण](https://www.onlinekhabar.com/2020/09/893885)

### 1. Source Passage (Nepali · Condition C1)
> गृह मन्त्रालयको राष्ट्रिय विपद् जोखिम न्यूनीकरण तथा व्यवस्थापन प्राधिकरणका अनुसार यस वर्षको मनसुनमा आएको बाढी र पहिरोबाट २६० भन्दा बढी नागरिकले ज्यान गुमाएका छन्। सिन्धुपाल्चोक, म्याग्दी र कालिकोट जिल्लामा पहिरोले ठूलो मानवीय क्षति पुर्‍याएको छ। सरकारले प्रभावित परिवारलाई तत्काल राहत सामग्री र अस्थायी आवास निर्माणका लागि अनुदान उपलब्ध गराएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the National Disaster Risk Reduction and Management Authority of the Ministry of Home Affairs, more than 200 civilians have lost their lives in this year's monsoon floods and landslides. Landslides in Sindhupalchok and Myagdi and Calicut districts have caused significant human losses. The government has provided immediate relief materials and grants for the construction of temporary housing for the affected families.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the National Disaster Risk Reduction and Management Authority of the Ministry of Home Affairs, more than 200 civilians have lost their lives in this year's monsoon floods and landslides. Landslides in Sindhupalchok and Myagdi and Calicut districts have caused significant human losses. The government has provided immediate relief materials and grants for the construction of temporary housing for the affected families.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 48 / 60
**Linked Candidate Items:** `item_094`, `item_099`
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [जल तथा मौसम विज्ञान विभाग: पूर्वी पहाडी जिल्लामा भारी वर्षा](https://www.onlinekhabar.com/2023/06/1324916/%E0%A4%A6%E0%A5%87%E0%A4%B6%E0%A4%AD%E0%A4%B0-%E0%A4%AE%E0%A4%A8%E0%A4%B8%E0%A5%81%E0%A4%A8-%E0%A4%A8%E0%A4%AB%E0%A5%88%E0%A4%B2%E0%A4%BF%E0%A4%81%E0%A4%A6%E0%A5%88-%E0%A4%95%E0%A4%BF%E0%A4%A8)

### 1. Source Passage (Nepali · Condition C1)
> जल तथा मौसम विज्ञान विभागका अनुसार मनसुन सक्रिय भएसँगै पूर्वी नेपालका सङ्खुवासभा, पाँचथर र ताप्लेजुङ जिल्लामा भारी वर्षाका कारण आकस्मिक बाढी आएको छ। खोलाहरूमा पानीको बहाव खतराको तह नाघेपछि तटीय क्षेत्रका बासिन्दालाई सुरक्षित स्थानमा सर्न मौसम पूर्वानुमान महाशाखाले विशेष बुलेटिन जारी गरेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Department of Water and Meteorology, heavy rains triggered flash floods in Sankhuwasabha and Taplejung districts of eastern Nepal as the monsoon became active. The Meteorological Forecasting Division has issued a special bulletin to evacuate residents of the coastal areas after the water flow in the streams crossed the danger level.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Department of Water and Meteorology, heavy rains triggered flash floods in Sankhuwasabha and Taplejung districts of eastern Nepal as the monsoon became active. The Meteorological Forecasting Division has issued a special bulletin to evacuate residents of the coastal areas after the water flow in the streams crossed the danger level.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 49 / 60
**Linked Candidate Items:** `item_095`, `item_100`
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [जलवायु परिवर्तन र उच्च हिमाली क्षेत्रमा हिमताल विस्फोटको जोखिम](https://www.onlinekhabar.com/2026/09/2014165/can-the-risk-of-glacial-lake-outburst-floods-and-landslides-be-reduced)

### 1. Source Passage (Nepali · Condition C1)
> वातावरणविद्हरूका अनुसार विश्वव्यापी तापमान वृद्धिका कारण हिमालय क्षेत्रका हिमनदीहरू तीव्र गतिमा पग्लिरहेका छन्। इम्जा, छोरोल्पा र ठुलागी जस्ता जोखिमपूर्ण हिमतालहरूमा पानीको सतह बढेकाले सम्भावित हिमताल विस्फोट (जीएलओएफ) को पूर्वसूचना प्रणाली जडान गरी तल्लो तटीय बस्तीहरूको संरक्षण गर्न सरकारले पहल थालेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to environmentalists, glaciers in the Himalayan region are melting rapidly due to global warming. The government has taken initiatives to protect low-lying coastal settlements by installing a potential glacial eruption ( GLOF ) early warning system as the water level in dangerous glaciers such as Chorolpa and Thulagi has risen.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to environmentalists, glaciers in the Himalayan region are melting rapidly due to global warming. The government has taken initiatives to protect low-lying coastal settlements by installing a potential glacial eruption ( GLOF ) early warning system as the water level in dangerous glaciers such as Chorolpa and Thulagi has risen.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 50 / 60
**Linked Candidate Items:** `item_096`, `item_101`
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [विपद् जोखिम न्यूनीकरण: नदी नियन्त्रण तथा तटबन्ध निर्माण](https://www.onlinekhabar.com/2021/06/967950/%E0%A4%AC%E0%A4%BE%E0%A4%A2%E0%A5%80-%E0%A4%AA%E0%A4%B9%E0%A4%BF%E0%A4%B0%E0%A5%8B%E0%A4%AC%E0%A4%BE%E0%A4%9F-%E0%A5%A7%E0%A5%AE-%E0%A4%B2%E0%A4%BE%E0%A4%96-%E0%A4%AC%E0%A4%BE%E0%A4%B8)

### 1. Source Passage (Nepali · Condition C1)
> राष्ट्रिय विपद् प्राधिकरणका अनुसार नेपालका तराई तथा चुरे क्षेत्रमा वर्षेनि नदी कटान र बाढीका कारण लाखौँ नागरिक प्रभावित हुने गरेका छन्। कोशी, गण्डकी, कर्णाली र महाकाली नदी नियन्त्रणका लागि दिगो जैविक तटबन्ध निर्माण र स्थानीय समुदायलाई उद्धार सामग्रीसहित तालिम दिने कार्य अघि बढाइएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the National Disaster Authority, millions of citizens are affected by river erosion and flooding in the Terai and Chure regions of Nepal annually.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the National Disaster Authority, millions of citizens are affected by river erosion and flooding in the Terai and Chure regions of Nepal annually.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 51 / 60
**Linked Candidate Items:** `item_097`, `item_102`
**Domain:** news | **Topic Sub-Genre:** disaster_geography | **Source:** [इलाम बाढी पहिरो: राहत वितरण तथा पुनर्स्थापना](https://www.onlinekhabar.com/2025/10/1777417/chief-minister-reaches-ilam-with-relief-supplies-three-days-after-floods-and-landslides)

### 1. Source Passage (Nepali · Condition C1)
> अविरल वर्षाका कारण पूर्वी पहाडी जिल्ला इलाममा गएको पहिरोबाट विस्थापित नागरिकहरूका लागि प्रदेश सरकारले खाद्यान्न, त्रिपाल र औषधिजन्य राहत सामग्री पठाएको छ। अवरुद्ध सडक सञ्जाल खुलाउन र खानेपानी आपूर्ति पुनर्स्थापना गर्न नेपाली सेना र नेपाल प्रहरीको टोली परिचालन गरिएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The provincial government has sent food and medical relief supplies to the citizens displaced by landslides in the eastern hilly district of Ilam due to incessant rains. Teams of the Nepali Army and Nepal Police have been deployed to open the blocked road network and restore drinking water supply.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The provincial government has sent food and medical relief supplies to the citizens displaced by landslides in the eastern hilly district of Ilam due to incessant rains. Teams of the Nepali Army and Nepal Police have been deployed to open the blocked road network and restore drinking water supply.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 52 / 60
**Linked Candidate Items:** `item_103`, `item_108`
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [सर्वोच्च अदालत संवैधानिक इजलास: न्यायिक क्षेत्राधिकार र फैसला](https://www.onlinekhabar.com/2021/09/1008845/%E0%A4%B8%E0%A4%82%E0%A4%B5%E0%A5%88%E0%A4%A7%E0%A4%BE%E0%A4%A8%E0%A4%BF%E0%A4%95-%E0%A4%87%E0%A4%9C%E0%A4%B2%E0%A4%BE%E0%A4%B8-%E0%A4%B0%E0%A5%8B%E0%A4%95%E0%A5%8D%E0%A4%A6%E0%A5%88-%E0%A4%8F)

### 1. Source Passage (Nepali · Condition C1)
> सर्वोच्च अदालतको प्रधानन्यायाधीशको नेतृत्वमा रहने पाँच सदस्यीय संवैधानिक इजलासले गम्भीर संवैधानिक व्याख्या सम्बन्धी विवादहरूको निरुपण गर्दै आएको छ। संविधानको धारा १३७ बमोजिम संघ, प्रदेश र स्थानीय तहबीचको अधिकार क्षेत्र विवाद तथा मौलिक हकको हनन सम्बन्धी महत्त्वपूर्ण रिटहरूमा इजलासले आदेश जारी गरेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> A five-member constitutional bench headed by the Chief Justice of the Supreme Court has been adjudicating disputes relating to serious constitutional interpretation.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
A five-member constitutional bench headed by the Chief Justice of the Supreme Court has been adjudicating disputes relating to serious constitutional interpretation.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 53 / 60
**Linked Candidate Items:** `item_104`, `item_109`
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [निर्वाचन आयोग: प्रतिनिधि सभा तथा प्रदेश सभा निर्वाचन व्यवस्थापन](https://www.onlinekhabar.com/2025/12/1836350/these-are-the-provisional-voters-who-will-vote-for-members-of-the-house-of-representatives)

### 1. Source Passage (Nepali · Condition C1)
> निर्वाचन आयोग नेपालले प्रतिनिधि सभा तथा प्रदेश सभा सदस्य निर्वाचनका लागि मतदाता नामावली अद्यावधिक गर्ने र मतदान केन्द्रहरूको सुरक्षा सुदृढ बनाउने कार्य सम्पन्न गरेको छ। आयोगका अनुसार प्रत्यक्ष र समानुपातिक निर्वाचन प्रणालीमार्फत कुल २७५ प्रतिनिधि सभा सदस्यहरू चयन हुने संवैधानिक व्यवस्था छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Election Commission Nepal has completed the work of updating the electoral rolls and strengthening the security of the polling stations for the election of the members of the House of Representatives and the Provincial Assembly. According to the commission, there is a constitutional provision for a total of 55 members of the House of Representatives to be elected through a direct and proportional election system.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Election Commission Nepal has completed the work of updating the electoral rolls and strengthening the security of the polling stations for the election of the members of the House of Representatives and the Provincial Assembly. According to the commission, there is a constitutional provision for a total of 55 members of the House of Representatives to be elected through a direct and proportional election system.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 54 / 60
**Linked Candidate Items:** `item_105`, `item_110`
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [प्रतिनिधि सभाबाट महत्त्वपूर्ण सरकारी विधेयकहरू पारित](https://www.onlinekhabar.com/2026/05/1940225/two-bills-introduced-by-the-prime-minister-passed-by-the-house-of-representatives)

### 1. Source Passage (Nepali · Condition C1)
> संघीय संसद्को प्रतिनिधि सभाले सुशासन, आर्थिक पारदर्शिता र सेवा प्रवाह सुधार सम्बन्धी दुई महत्त्वपूर्ण सरकारी विधेयकहरू बहुमतले पारित गरेको छ। संसद्मा दफावार छलफलपछि पारित भएका विधेयकहरू राष्ट्रिय सभामा पठाइएको र प्रमाणीकरणपछि कानुनको रूपमा लागू हुने संसद् सचिवालयले जनाएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The House of Representatives of the Federal Parliament has passed by a majority two important government bills on good governance, economic transparency and improving service delivery. The bills passed after due deliberations in the Parliament have been sent to the National Assembly and will come into force as law after certification, the Parliament Secretariat said.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The House of Representatives of the Federal Parliament has passed by a majority two important government bills on good governance, economic transparency and improving service delivery. The bills passed after due deliberations in the Parliament have been sent to the National Assembly and will come into force as law after certification, the Parliament Secretariat said.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 55 / 60
**Linked Candidate Items:** `item_106`, `item_111`
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [राष्ट्रपतिद्वारा सत्य निरुपण तथा मेलमिलाप (टीआरसी) विधेयक प्रमाणीकरण](https://www.onlinekhabar.com/2024/08/1531575/the-president-assented-to-the-trc-bill)

### 1. Source Passage (Nepali · Condition C1)
> राष्ट्रपतिले संघीय संसद्का दुवै सदनबाट पारित भएको बेपत्ता पारिएका व्यक्तिको छानबिन, सत्य निरुपण तथा मेलमिलाप आयोग ऐन संशोधन विधेयक प्रमाणीकरण गर्नुभएको छ। यससँगै नेपालको शान्ति प्रक्रियाको बाँकी रहेको सङ्क्रमणकालीन न्यायको कार्यभार टुङ्गोमा पुर्‍याउने कानुनी बाटो खुलेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The President has certified the Missing Persons Investigation and Fact-Finding and Reconciliation Commission Act Amendment Bill passed by both houses of the federal parliament, opening the legal way for the transitional justice responsibilities of Nepal's peace process to be terminated.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The President has certified the Missing Persons Investigation and Fact-Finding and Reconciliation Commission Act Amendment Bill passed by both houses of the federal parliament, opening the legal way for the transitional justice responsibilities of Nepal's peace process to be terminated.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 56 / 60
**Linked Candidate Items:** `item_107`, `item_112`
**Domain:** news | **Topic Sub-Genre:** governance_law | **Source:** [नेपाल नागरिकता ऐन संशोधन तथा सर्वोच्च अदालतको आदेश](https://www.onlinekhabar.com/2023/06/1319932)

### 1. Source Passage (Nepali · Condition C1)
> सर्वोच्च अदालतले नेपाल नागरिकता ऐन संशोधन सम्बन्धी रिट निवेदनमाथि सुनुवाइ गर्दै जन्मसिद्ध नागरिकका सन्तानलाई वंशजको आधारमा नागरिकता दिने कानुनी बाटो खुला गरेको छ। यस आदेशसँगै हजारौँ योग्य नेपाली नागरिकहरूले जिल्ला प्रशासन कार्यालयमार्फत नागरिकता प्रमाणपत्र प्राप्त गर्ने सुनिश्चित भएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Supreme Court of Nepal, while hearing a writ petition regarding the amendment of the Nepal Citizenship Act, has opened the legal way to grant citizenship to the children of born citizens on the basis of descent. With this order, thousands of eligible Nepali citizens have been ensured to obtain citizenship certificates through the District Administration Office.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Supreme Court of Nepal, while hearing a writ petition regarding the amendment of the Nepal Citizenship Act, has opened the legal way to grant citizenship to the children of born citizens on the basis of descent. With this order, thousands of eligible Nepali citizens have been ensured to obtain citizenship certificates through the District Administration Office.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 57 / 60
**Linked Candidate Items:** `item_113`, `item_117`
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [काठमाडौं-तराई द्रुतमार्ग (फास्ट ट्रयाक) निर्माण प्रगति](https://www.onlinekhabar.com/2018/01/653008/%E0%A4%AB%E0%A4%BE%E0%A4%B8%E0%A5%8D%E0%A4%9F-%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%AF%E0%A4%BE%E0%A4%95%E0%A4%AE%E0%A4%BE-%E0%A4%B8%E0%A5%87%E0%A4%A8%E0%A4%BE%E0%A4%B2%E0%A5%87-%E0%A4%95%E0%A5%87)

### 1. Source Passage (Nepali · Condition C1)
> नेपाली सेनाको व्यवस्थापनमा निर्माणाधीन ७०.९७ किलोमिटर लामो काठमाडौं-तराई मधेस द्रुतमार्ग (फास्ट ट्रयाक) को सुरुङमार्ग र पुल निर्माण कार्य तीव्र गतिमा अघि बढेको छ। महादेवडाँडा, धेद्रे र लेनडाँडामा सुरुङ छेड्ने काम सम्पन्न भएसँगै काठमाडौं उपत्यकालाई तराईसँग १ घण्टाको यात्रा दूरीमा जोड्ने राष्ट्रिय गौरवको आयोजनाले गति लिएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The construction of the tunnel and bridge of the 215.5 km long Kathmandu-Tarai Madhes Expressway ( Fast Track ), under construction under the management of the Nepali Army, has progressed rapidly. With the completion of the tunnel work at Mahadevdanda Dhedra and Landanda, the National Pride event connecting the Kathmandu Valley with the Terai has gained momentum.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The construction of the tunnel and bridge of the 215.5 km long Kathmandu-Tarai Madhes Expressway ( Fast Track ), under construction under the management of the Nepali Army, has progressed rapidly. With the completion of the tunnel work at Mahadevdanda Dhedra and Landanda, the National Pride event connecting the Kathmandu Valley with the Terai has gained momentum.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 58 / 60
**Linked Candidate Items:** `item_114`, `item_118`
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [माथिल्लो तामाकोशी ४५६ मेगावाट जलविद्युत आयोजना](https://www.onlinekhabar.com/2021/07/978999/%E0%A4%A4%E0%A4%BE%E0%A4%AE%E0%A4%BE%E0%A4%95%E0%A5%8B%E0%A4%B6%E0%A5%80-%E0%A4%9C%E0%A4%B2%E0%A4%B5%E0%A4%BF%E0%A4%A6%E0%A5%8D%E0%A4%AF%E0%A5%81%E0%A4%A4-%E0%A4%86%E0%A4%AF%E0%A5%8B%E0%A4%9C%E0%A4%A8)

### 1. Source Passage (Nepali · Condition C1)
> दोलखा जिल्लामा स्वदेशी लगानीमा निर्मित ४५६ मेगावाट क्षमताको माथिल्लो तामाकोशी जलविद्युत आयोजना राष्ट्रिय प्रसारण प्रणालीमा जोडिएको छ। यस आयोजनाले हिउँदको समयमा हुने बिजुलीको अभाव घटाउन र नेपाललाई वर्षायाममा छिमेकी देशहरूमा जलविद्युत निर्यात गर्ने राष्ट्रको रूपमा स्थापित गर्न कोशेढुङ्गा साबित भएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The 65 MW Upper Tamakoshi Hydropower Project, built with indigenous investment in Dolakha district, is connected to the national transmission system. This event has proved to be a milestone in reducing the power shortage during winter and establishing Nepal as a nation that exports hydroelectricity to neighbouring countries during the rainy season.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The 65 MW Upper Tamakoshi Hydropower Project, built with indigenous investment in Dolakha district, is connected to the national transmission system. This event has proved to be a milestone in reducing the power shortage during winter and establishing Nepal as a nation that exports hydroelectricity to neighbouring countries during the rainy season.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 59 / 60
**Linked Candidate Items:** `item_115`, `item_119`
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [पोखरा अन्तर्राष्ट्रिय विमानस्थल: उडान सञ्चालन तथा पर्यटन विकास](https://www.onlinekhabar.com/2026/03/1882796/9-international-flights-and-landings-at-pokhara-airport-in-a-month-74-passengers)

### 1. Source Passage (Nepali · Condition C1)
> पोखरा अन्तर्राष्ट्रिय विमानस्थलमा अन्तर्राष्ट्रिय चार्टर्ड तथा नियमित उडानहरू विस्तार गर्न नागरिक उड्डयन प्राधिकरणले प्रोत्साहन प्याकेज घोषणा गरेको छ। विमानस्थल सञ्चालनसँगै गण्डकी प्रदेशमा साहसिक खेलकुद तथा पदयात्राका लागि आउने विदेशी पर्यटकहरूको आवागमन सहज भएको पर्यटन व्यवसायीहरूले बताएका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Civil Aviation Authority has announced an incentive package to expand international chartered and regular flights at Pokhara International Airport. Tourism professionals have said that with the airport's operation, the movement of foreign tourists to Gandaki Province for adventure sports and trekking has become easier.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Civil Aviation Authority has announced an incentive package to expand international chartered and regular flights at Pokhara International Airport. Tourism professionals have said that with the airport's operation, the movement of foreign tourists to Gandaki Province for adventure sports and trekking has become easier.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---

## Passage 60 / 60
**Linked Candidate Items:** `item_116`, `item_120`
**Domain:** news | **Topic Sub-Genre:** infrastructure_tourism | **Source:** [नेपाल पर्यटन बोर्ड: वार्षिक १० लाखभन्दा बढी विदेशी पर्यटक आगमन](https://www.onlinekhabar.com?p=1932505)

### 1. Source Passage (Nepali · Condition C1)
> नेपाल पर्यटन बोर्डको तथ्याङ्क अनुसार हवाई मार्ग हुँदै नेपाल भ्रमणमा आउने विदेशी पर्यटकहरूको सङ्ख्या वार्षिक १० लाख नाघेको छ। भारत, अमेरिका, चीन, बेलायत र अस्ट्रेलियाबाट आउने पर्यटकहरूको सङ्ख्यामा उल्लेख्य वृद्धि भएको छ। बोर्डले पदयात्रा, पर्वतारोहण र सांस्कृतिक सम्पदा पर्यटन प्रवर्द्धनका लागि अन्तर्राष्ट्रिय पर्यटन मेलाहरूमा सहभागिता जनाएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Nepal Tourism Board data, the number of foreign tourists visiting Nepal by air has crossed 1 million annually. There has been a significant increase in the number of tourists from India, USA, China, UK and Australia. The board has participated in international tourism fairs to promote trekking and mountaineering and cultural heritage tourism.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Nepal Tourism Board data, the number of foreign tourists visiting Nepal by air has crossed 1 million annually. There has been a significant increase in the number of tourists from India, USA, China, UK and Australia. The board has participated in international tourism fairs to promote trekking and mountaineering and cultural heritage tourism.
```

### 4. Post-Editing Metadata
**Stopwatch Elapsed Time:** `[ mm:ss ]`

**Error Types Corrected in this Passage (Select all that apply):**
- [ ] Entity / Proper Noun mistranslation
- [ ] Number / Date / Metric distortion
- [ ] Omission / Dropped clauses
- [ ] Polarity / Negation flip
- [ ] Tense / Aspect collapse
- [ ] Evidential / Epistemic stance distortion
- [ ] Clean / No edit needed (Raw MT is faithful and accurate)

**Editor Notes / Justification:** `[                                                 ]`

---
