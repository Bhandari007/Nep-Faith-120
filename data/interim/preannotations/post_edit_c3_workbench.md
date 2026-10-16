# NepFaith-120 Condition C3 Post-Editing Workbench

**Version:** 1.0 (Locked Protocol)  
**Editor:** Human Bilingual Post-Editor  
**Target:** 61 Unique Reference Passages (spanning all 120 candidate items)  
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

## Passage 01 / 61
**Linked Candidate Items:** `item_001`, `item_009`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### 1. Source Passage (Nepali · Condition C1)
> काठमाडौँ उपत्यकाका सातवटा स्मारक क्षेत्रहरू सन् १९७९ मा युनेस्को विश्व सम्पदा सूचीमा सूचीकृत भएका थिए। ती क्षेत्रहरूमा काठमाडौँ दरबार स्क्वायर, पाटन दरबार स्क्वायर, भक्तपुर दरबार स्क्वायर, स्वयम्भूनाथ, बौद्धनाथ, पशुपतिनाथ मन्दिर र चाँगुनारायण मन्दिर पर्दछन्। यी सम्पदाहरूले उपत्यकाको मल्लकालीन कला र नेवारी वास्तुकलालाई प्रतिनिधित्व गर्दछन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Seven memorial areas in the Kathmandu Valley were listed on the UNESCO World Heritage List in 2001. These areas include Kathmandu Durbar Square, Patan Durbar Square, Bhaktapur Durbar Square, Swayambhunath, Boudhanath, Pashupatinath Temple, and Changunarayan Temple. These heritage sites represent the Malala period art and Newari architecture of the valley.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Seven memorial areas in the Kathmandu Valley were listed on the UNESCO World Heritage List in 2001. These areas include Kathmandu Durbar Square, Patan Durbar Square, Bhaktapur Durbar Square, Swayambhunath, Boudhanath, Pashupatinath Temple, and Changunarayan Temple. These heritage sites represent the Malala period art and Newari architecture of the valley.
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

## Passage 02 / 61
**Linked Candidate Items:** `item_002`, `item_010`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### 1. Source Passage (Nepali · Condition C1)
> पशुपतिनाथ मन्दिर बागमती नदीको किनारमा अवस्थित हिन्दूहरूको पवित्र तीर्थस्थल हो। यो मन्दिर प्यागोडा शैलीमा निर्माण गरिएको छ र यसको छाना दुई तहको सुनको जलप लगाइएको तामाबाट बनेको छ। वि.सं. १९९० को महाभूकम्पमा पनि सुरक्षित रहेको यो मन्दिर क्षेत्रमा सन् १९७९ देखि गैर-हिन्दूहरूलाई मुख्य मन्दिर प्रवेशमा रोक लगाइएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Pashupatinath Temple is a sacred pilgrimage site for Hindus located on the banks of the Bagmati River. The temple is built in pagoda style and its roof is made of two layers of gold-plated copper. Also protected in the Great Earthquake of the 20th century, non-Hindus have been barred from entering the main temple in this temple area since the 20th century.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Pashupatinath Temple is a sacred pilgrimage site for Hindus located on the banks of the Bagmati River. The temple is built in pagoda style and its roof is made of two layers of gold-plated copper. Also protected in the Great Earthquake of the 20th century, non-Hindus have been barred from entering the main temple in this temple area since the 20th century.
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

## Passage 03 / 61
**Linked Candidate Items:** `item_003`, `item_011`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### 1. Source Passage (Nepali · Condition C1)
> इन्द्रजात्रा काठमाडौँ उपत्यकाको नेवार समुदायले मनाउने सबैभन्दा ठूलो ऐतिहासिक जात्रा हो। यो जात्रा भाद्र शुक्ल द्वादशीका दिन हनुमानढोकामा लिंगो (इन्द्रध्वज) ठड्याएपछि सुरु हुन्छ र आठ दिनसम्म चल्दछ। जात्राको मुख्य दिन जीवित देवी कुमारी, गणेश र भैरवको रथ यात्रा गराइन्छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Indrajatra is the largest historical jatra celebrated by the Newar community of the Kathmandu Valley. The jatra begins on the day of Bhadra Shukla Dwadashi with the beating of the lingo ( Indradhwaj ) at Hanumandhoka and lasts for eight days. On the main day of the jatra, the chariot journey of the living goddess Kumari and Ganesha and Bhairav is undertaken.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Indrajatra is the largest historical jatra celebrated by the Newar community of the Kathmandu Valley. The jatra begins on the day of Bhadra Shukla Dwadashi with the beating of the lingo ( Indradhwaj ) at Hanumandhoka and lasts for eight days. On the main day of the jatra, the chariot journey of the living goddess Kumari and Ganesha and Bhairav is undertaken.
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

## Passage 04 / 61
**Linked Candidate Items:** `item_004`, `item_012`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### 1. Source Passage (Nepali · Condition C1)
> नेपाल संवत् राष्ट्रिय विभूति शंखधर साख्वाले वि.सं. ९३६ (सन् ८७९) मा सुरु गरेका थिए। उनले काठमाडौँका गरिब जनताको ऋण मोचन गरी यो संवत् चलाएका हुन्। नेपाल सरकारले वि.सं. २०६५ मा नेपाल संवत्लाई राष्ट्रिय संवत्को रूपमा मान्यता दिएको थियो।

### 2. Raw IndicTrans2 MT (Condition C2)
> Nepal Samvat was started by national icon Shankhdhar Sakhwa in 1965. He ran this Samvat by relieving the debt of the poor people of Kathmandu. The Government of Nepal recognized Nepal Samvat as a national Samvat in 1965.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Nepal Samvat was started by national icon Shankhdhar Sakhwa in 1965. He ran this Samvat by relieving the debt of the poor people of Kathmandu. The Government of Nepal recognized Nepal Samvat as a national Samvat in 1965.
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

## Passage 05 / 61
**Linked Candidate Items:** `item_005`, `item_013`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### 1. Source Passage (Nepali · Condition C1)
> चाँगुनारायण मन्दिर काठमाडौँ उपत्यकाको सबैभन्दा पुरानो हिन्दू मन्दिर मानिन्छ। यस मन्दिर परिसरमा वि.सं. ५२१ (सन् ४६४) को लिच्छवी राजा मानदेव प्रथमको शिलालेख फेला परेको छ, जुन नेपालको इतिहासको सबैभन्दा पुरानो प्रमाणिक अभिलेख हो। मन्दिर भक्तपुर जिल्लाको चाँगुनारायण नगरपालिकामा अवस्थित छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Changunarayan Temple is considered to be the oldest Hindu temple in the Kathmandu Valley. An inscription of the Licchavi King Mandev I of AD 1501 ( ) has been found in this temple complex, which is the oldest attested record in the history of Nepal. The temple is located in Changunarayan Municipality of Bhaktapur district.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Changunarayan Temple is considered to be the oldest Hindu temple in the Kathmandu Valley. An inscription of the Licchavi King Mandev I of AD 1501 ( ) has been found in this temple complex, which is the oldest attested record in the history of Nepal. The temple is located in Changunarayan Municipality of Bhaktapur district.
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

## Passage 06 / 61
**Linked Candidate Items:** `item_006`, `item_014`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### 1. Source Passage (Nepali · Condition C1)
> स्वयम्भूनाथ स्तूप काठमाडौँ उपत्यकाको पश्चिम भागमा एउटा पहाडी टाकुरामा अवस्थित छ। यसलाई 'मंकी टेम्पल' का नामले पनि चिनिन्छ। स्तूपको शीर्ष भागमा चारै दिशामा हेरिरहेका बुद्धका आँखाहरू कुँदिएका छन्, जसले सर्वव्यापी ज्ञान र करुणाको प्रतीक जनाउँछ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Swayambhunath Stupa is located on a hilltop in the western part of Kathmandu Valley. It is also known as'Monkey Temple '. The top of the Stupa is carved with the eyes of Buddha looking in all directions and symbolizes omnipresent knowledge and compassion.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Swayambhunath Stupa is located on a hilltop in the western part of Kathmandu Valley. It is also known as'Monkey Temple '. The top of the Stupa is carved with the eyes of Buddha looking in all directions and symbolizes omnipresent knowledge and compassion.
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

## Passage 07 / 61
**Linked Candidate Items:** `item_007`, `item_015`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### 1. Source Passage (Nepali · Condition C1)
> नेपालमा मनाइने छठ पर्व सूर्य देवता र छठी माताको उपासना गरिने प्रमुख चाड हो। चार दिनसम्म मनाइने यस पर्वमा अस्ताउँदो र उदाउँदो सूर्यलाई पवित्र नदी वा पोखरीको किनारमा अर्घ्य दिइन्छ। विशेषगरी तराई-मधेशमा मनाइने यो पर्व अहिले काठमाडौँ उपत्यका लगायत पहाडी क्षेत्रमा पनि लोकप्रिय भएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Chhath Puja, celebrated in Nepal, is a major festival that worships the sun god and the sixth mother. The four-day festival celebrates the rising and setting sun on the banks of a holy river or pond. This festival, especially celebrated in the Terai-Madhesh, has now become popular in the hilly regions including the Kathmandu Valley.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Chhath Puja, celebrated in Nepal, is a major festival that worships the sun god and the sixth mother. The four-day festival celebrates the rising and setting sun on the banks of a holy river or pond. This festival, especially celebrated in the Terai-Madhesh, has now become popular in the hilly regions including the Kathmandu Valley.
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

## Passage 08 / 61
**Linked Candidate Items:** `item_008`
**Domain:** wikipedia | **Topic Sub-Genre:** culture_heritage

### 1. Source Passage (Nepali · Condition C1)
> भक्तपुर दरबार स्क्वायरलाई '५५ झ्याले दरबार' र 'न्यातपोल मन्दिर' का लागि चिनिन्छ। राजा भूपतिन्द्र मल्लले निर्माण गर्न लगाएको न्यातपोल मन्दिर पाँच तल्ला भएको नेपालकै सबैभन्दा अग्लो प्यागोडा मन्दिर हो, जसको उचाइ करिब ३० मिटर रहेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Bhaktapur Durbar Square is known for'Jhyale Durbar'and'Nyatpole Temple '. The Nyatpole Temple commissioned by King Bhupatindra Malla is the highest pagoda temple in Nepal with five storeys and is about 303 meters high.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Bhaktapur Durbar Square is known for'Jhyale Durbar'and'Nyatpole Temple '. The Nyatpole Temple commissioned by King Bhupatindra Malla is the highest pagoda temple in Nepal with five storeys and is about 303 meters high.
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

## Passage 09 / 61
**Linked Candidate Items:** `item_016`, `item_024`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### 1. Source Passage (Nepali · Condition C1)
> सगरमाथा राष्ट्रिय निकुञ्ज सन् १९७६ मा स्थापना भएको हो र सन् १९७९ मा युनेस्को विश्व प्राकृतिक सम्पदा सूचीमा सूचीकृत भएको थियो। १ हजार १४८ वर्ग किलोमिटरमा फैलिएको यस निकुञ्जमा विश्वको सर्वोच्च शिखर सगरमाथा (८,८४८.८६ मिटर) सहित ल्होत्से, नुप्त्से, चो ओयु र आमादब्लम जस्ता प्रमुख हिमालहरू पर्दछन्। यहाँ हिमचितुवा र कस्तुरी मृग पाइन्छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Sagarmatha National Park was established in 1991 and was listed on the UNESCO World Natural Heritage List in 2001. The park covers major mountains such as Lhotse, Nuptse, Cho Oyu, and Amadblam, including the world's highest peak Sagarmatha (   .   ), which is spread over 1,000 square kilometres. Snow leopards and musk deer are found here.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Sagarmatha National Park was established in 1991 and was listed on the UNESCO World Natural Heritage List in 2001. The park covers major mountains such as Lhotse, Nuptse, Cho Oyu, and Amadblam, including the world's highest peak Sagarmatha (   .   ), which is spread over 1,000 square kilometres. Snow leopards and musk deer are found here.
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

## Passage 10 / 61
**Linked Candidate Items:** `item_017`, `item_025`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### 1. Source Passage (Nepali · Condition C1)
> सन् २०२२ को राष्ट्रिय बाघ गणना अनुसार नेपालमा पाटे बाघको सङ्ख्या बढेर ३५५ पुगेको छ। सन् २०१० मा सेन्ट पिटर्सबर्ग सम्मेलनमा नेपालले गरेको बाघको सङ्ख्या दोब्बर बनाउने प्रतिबद्धता (१२१ बाट २४२) पूरा गरी नेपाल विश्वमै बाघको सङ्ख्या दोब्बर बनाउने पहिलो देश बनेको थियो। सबैभन्दा बढी बाघ चितवन राष्ट्रिय निकुञ्ज (१२८ वटा) मा रहेका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the National Tiger Census of 2015, the total tiger population in Nepal has increased to 455. Nepal became the first country in the world to double its tiger population by fulfilling the commitment of doubling its tiger population ( from 212 to 232 ) made by Nepal at the St. Petersburg Conference in 2019. The highest number of tigers are in Chitwan National Park ( 212 ).

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the National Tiger Census of 2015, the total tiger population in Nepal has increased to 455. Nepal became the first country in the world to double its tiger population by fulfilling the commitment of doubling its tiger population ( from 212 to 232 ) made by Nepal at the St. Petersburg Conference in 2019. The highest number of tigers are in Chitwan National Park ( 212 ).
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

## Passage 11 / 61
**Linked Candidate Items:** `item_018`, `item_026`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### 1. Source Passage (Nepali · Condition C1)
> बर्दिया राष्ट्रिय निकुञ्ज नेपालको तराई क्षेत्रमा अवस्थित सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज हो, जसको क्षेत्रफल ९६८ वर्ग किलोमिटर छ। यो निकुञ्ज कर्णाली नदीको पूर्वी किनारमा फैलिएको छ र यहाँ एकसिङ्गे गैँडा, पाटे बाघ र एसियाली हात्तीहरू पाइन्छन्। बर्दियामा १२५ वटा पाटे बाघ रहेका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Bardiya National Park is the largest national park located in the Terai region of Nepal and covers an area of 14 square kilometres. The park extends along the eastern bank of the Karnali River and is home to the one-horned rhinoceros and the Asiatic elephant. Bardia is home to twenty-six species of tigers.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Bardiya National Park is the largest national park located in the Terai region of Nepal and covers an area of 14 square kilometres. The park extends along the eastern bank of the Karnali River and is home to the one-horned rhinoceros and the Asiatic elephant. Bardia is home to twenty-six species of tigers.
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

## Passage 12 / 61
**Linked Candidate Items:** `item_019`, `item_027`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### 1. Source Passage (Nepali · Condition C1)
> रारा ताल नेपालको सबैभन्दा ठूलो र गहिरो ताल हो। यो कर्णाली प्रदेशको मुगु जिल्लामा समुद्र सतहबाट २ हजार ९९० मिटरको उचाइमा अवस्थित छ। यस तालको लम्बाइ करिब ५.१ किलोमिटर, चौडाइ २.७ किलोमिटर र अधिकतम गहिराइ १६७ मिटर रहेको छ। रारा ताल रारा राष्ट्रिय निकुञ्जभित्र पर्दछ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Rara Lake is the largest and deepest lake in Nepal. It is located in Mugu district of Karnali Province at an altitude of 2, 500 meters above sea level. It is about 5, 51 kilometers long, 2, 22 kilometers wide, and has a maximum depth of 4, 00 meters. Rara Lake falls within Rara National Park.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Rara Lake is the largest and deepest lake in Nepal. It is located in Mugu district of Karnali Province at an altitude of 2, 500 meters above sea level. It is about 5, 51 kilometers long, 2, 22 kilometers wide, and has a maximum depth of 4, 00 meters. Rara Lake falls within Rara National Park.
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

## Passage 13 / 61
**Linked Candidate Items:** `item_020`, `item_028`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### 1. Source Passage (Nepali · Condition C1)
> अन्नपूर्ण संरक्षण क्षेत्र नेपालको सबैभन्दा ठूलो संरक्षण क्षेत्र हो, जसको क्षेत्रफल ७ हजार ६२९ वर्ग किलोमिटर छ। यो गण्डकी प्रदेशका कास्की, लमजुङ, म्याग्दी, मनाङ र मुस्ताङ जिल्लामा फैलिएको छ। यस क्षेत्रलाई राष्ट्रिय प्रकृति संरक्षण कोष (एनटीएनसी) ले स्थानीय समुदायको सहभागितामा व्यवस्थापन गर्दै आएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Annapurna Conservation Area is the largest conservation area in Nepal with an area of 6000 square kilometers. It is spread over Kaski, Lamjung, Myagdi, Manang and Mustang districts of Gandaki Province. The area has been managed by the National Nature Conservation Fund ( NTNC ) with the participation of the local community.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Annapurna Conservation Area is the largest conservation area in Nepal with an area of 6000 square kilometers. It is spread over Kaski, Lamjung, Myagdi, Manang and Mustang districts of Gandaki Province. The area has been managed by the National Nature Conservation Fund ( NTNC ) with the participation of the local community.
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

## Passage 14 / 61
**Linked Candidate Items:** `item_021`, `item_029`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### 1. Source Passage (Nepali · Condition C1)
> लाङटाङ राष्ट्रिय निकुञ्ज नेपालको पहिलो हिमाली राष्ट्रिय निकुञ्ज हो, जुन सन् १९७६ मा स्थापना भएको थियो। १ हजार ७१० वर्ग किलोमिटरमा फैलिएको यस निकुञ्जले रसुवा, नुवाकोट र सिन्धुपाल्चोक जिल्लालाई ओगटेको छ। निकुञ्जभित्र पवित्र गोसाइँकुण्ड ताल अवस्थित छ, जहाँ जनैपूर्णिमाका दिन ठूलो मेला लाग्दछ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Langtang National Park is the first Himalayan National Park in Nepal, established in the year 2001. The park covers Rasuwa, Nuwakot and Sindhupalchok districts. Within the park lies the sacred Gosainkund Lake, where a large fair is held on the day of Janapurnima.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Langtang National Park is the first Himalayan National Park in Nepal, established in the year 2001. The park covers Rasuwa, Nuwakot and Sindhupalchok districts. Within the park lies the sacred Gosainkund Lake, where a large fair is held on the day of Janapurnima.
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

## Passage 15 / 61
**Linked Candidate Items:** `item_022`, `item_030`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### 1. Source Passage (Nepali · Condition C1)
> नेपालमा हालसम्म ८८६ प्रजातिका चराहरू अभिलेखीकरण गरिएका छन्, जुन विश्वको कुल चरा प्रजातिको करिब ९ प्रतिशत हो। कोशी टप्पु वन्यजन्तु आरक्ष नेपालको प्रमुख चरा अवलोकन क्षेत्र हो, जहाँ ५२६ भन्दा बढी प्रजातिका चराहरू पाइन्छन्। काँडे भ्याकुर नेपालमा मात्र पाइने रैथाने चरा हो।

### 2. Raw IndicTrans2 MT (Condition C2)
> Sixty-six species of birds have been recorded in Nepal so far, accounting for about 1 % of the total bird species in the world. Koshi Tappu Wildlife Reserve is the major bird watching area in Nepal, where more than sixty-six species of birds are found. Kande Vakur is the only raithane bird found in Nepal.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Sixty-six species of birds have been recorded in Nepal so far, accounting for about 1 % of the total bird species in the world. Koshi Tappu Wildlife Reserve is the major bird watching area in Nepal, where more than sixty-six species of birds are found. Kande Vakur is the only raithane bird found in Nepal.
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

## Passage 16 / 61
**Linked Candidate Items:** `item_023`
**Domain:** wikipedia | **Topic Sub-Genre:** biodiversity_parks

### 1. Source Passage (Nepali · Condition C1)
> शुक्लाफाँटा राष्ट्रिय निकुञ्ज सुदूरपश्चिम प्रदेशको कञ्चनपुर जिल्लामा अवस्थित छ। यस निकुञ्जको क्षेत्रफल ३०५ वर्ग किलोमिटर छ। यहाँ विश्वकै सबैभन्दा ठूलो बाह्रसिङ्गा (स्वम्प डियर) को बथान पाइन्छ, जसको सङ्ख्या २ हजारभन्दा बढी रहेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Shuklaphanta National Park is located in the Kanchanpur district of the Far-Western Provinces. The park has an area of 30,555 square kilometres. It is home to the world's largest herd of swamp deer, numbering over 2,000.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Shuklaphanta National Park is located in the Kanchanpur district of the Far-Western Provinces. The park has an area of 30,555 square kilometres. It is home to the world's largest herd of swamp deer, numbering over 2,000.
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

## Passage 17 / 61
**Linked Candidate Items:** `item_031`, `item_040`, `item_113`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### 1. Source Passage (Nepali · Condition C1)
> माथिल्लो तामाकोशी जलविद्युत आयोजना (४५६ मेगावाट) नेपालको आफ्नै स्रोत र साधनमा निर्माण भएको सबैभन्दा ठूलो जलविद्युत आयोजना हो। दोलखा जिल्लाको लामाबगरमा अवस्थित यस आयोजनाले वि.सं. २०७८ असारमा व्यावसायिक उत्पादन सुरु गरेको थियो। यस आयोजनाको भूमिगत विद्युतगृहमा ७६ मेगावाटका ६ वटा टर्बाइनहरू जडान गरिएका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Upper Tamakoshi Hydropower Project ( 46 MW ) is the largest hydroelectric project built in Nepal with its own resources and resources. Located in Lamabagar, Dolakha District, the project started commercial production in 2018. Six megawatts of turbines are installed in the underground power plant of the project.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Upper Tamakoshi Hydropower Project ( 46 MW ) is the largest hydroelectric project built in Nepal with its own resources and resources. Located in Lamabagar, Dolakha District, the project started commercial production in 2018. Six megawatts of turbines are installed in the underground power plant of the project.
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

## Passage 18 / 61
**Linked Candidate Items:** `item_032`, `item_114`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### 1. Source Passage (Nepali · Condition C1)
> नेपाल विद्युत प्राधिकरणका अनुसार नेपालको कुल जडित विद्युत क्षमता ३ हजार २०० मेगावाट नाघेको छ। वर्षायाममा नेपालले भारततर्फ दैनिक ६५० मेगावाटसम्म विद्युत निर्यात गर्दै आएको छ भने बंगलादेशतर्फ ४० मेगावाट विद्युत निर्यातको त्रिपक्षीय सम्झौता कार्यान्वयनमा आएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Nepal Electricity Authority, Nepal's total connected power capacity has exceeded 3,200 MW. During the rainy season, Nepal has been exporting up to 430 MW of power per day to India, while a tripartite agreement to export 40 MW of power to Bangladesh has come into effect.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Nepal Electricity Authority, Nepal's total connected power capacity has exceeded 3,200 MW. During the rainy season, Nepal has been exporting up to 430 MW of power per day to India, while a tripartite agreement to export 40 MW of power to Bangladesh has come into effect.
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

## Passage 19 / 61
**Linked Candidate Items:** `item_033`, `item_115`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### 1. Source Passage (Nepali · Condition C1)
> काठमाडौँ-तराई/मधेश द्रुतमार्ग (फास्ट ट्र्याक) ७२.५ किलोमिटर लामो चार लेनको एक्सप्रेस-वे हो। यस आयोजनामा तीनवटा प्रमुख सुरुङमार्गहरू—निजगढतर्फ लेनडाँडा (१.६१ किमि), धेद्रे (१.६३ किमि) र महादेवडाँडा (३.३५ किमि) निर्माणाधीन छन्। यो आयोजना सम्पन्न भएपछि काठमाडौँबाट निजगढ १ घण्टामा पुग्न सकिनेछ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Kathmandu-Tarai / Madhesh Expressway ( Fast Track ) is a four-lane expressway with a length of.55 km. Three major tunnel routes are under construction in the project, namely Lendanda (.651 km ), Dhedre (.633 km ) and Mahadevdanda (.333.55 km ) towards Jhunjhunjhunjhunjhunjhunjhunjhunj. Once completed, the project will be able to reach Nijgadh from Kathmandu in 1 hour.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Kathmandu-Tarai / Madhesh Expressway ( Fast Track ) is a four-lane expressway with a length of.55 km. Three major tunnel routes are under construction in the project, namely Lendanda (.651 km ), Dhedre (.633 km ) and Mahadevdanda (.333.55 km ) towards Jhunjhunjhunjhunjhunjhunjhunjhunj. Once completed, the project will be able to reach Nijgadh from Kathmandu in 1 hour.
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

## Passage 20 / 61
**Linked Candidate Items:** `item_034`, `item_116`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### 1. Source Passage (Nepali · Condition C1)
> नेपाल पर्यटन बोर्डका अनुसार सन् २०२३ मा हवाई मार्गबाट नेपाल भित्रिने विदेशी पर्यटकहरूको सङ्ख्या १० लाख १४ हजार ८८२ पुगेको छ। यो सङ्ख्या सन् २०१९ को तुलनामा करिब ८५ प्रतिशतको पुनरुत्थान हो। सबैभन्दा बढी पर्यटक भारत (३ लाख १९ हजार) बाट र त्यसपछि अमेरिका (१ लाख) बाट आएका थिए।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Nepal Tourism Board, the number of foreign tourists entering Nepal by air in 2003 reached 1 million 1 million 2 million. This figure is a revival of about 5 percent compared to the previous year. The largest number of tourists came from India ( 3 million 4 thousand ), followed by the United States ( 1 million ).

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Nepal Tourism Board, the number of foreign tourists entering Nepal by air in 2003 reached 1 million 1 million 2 million. This figure is a revival of about 5 percent compared to the previous year. The largest number of tourists came from India ( 3 million 4 thousand ), followed by the United States ( 1 million ).
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

## Passage 21 / 61
**Linked Candidate Items:** `item_035`, `item_117`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### 1. Source Passage (Nepali · Condition C1)
> पोखरा अन्तर्राष्ट्रिय विमानस्थल नेपालको दोस्रो नयाँ अन्तर्राष्ट्रिय विमानस्थल हो, जसको उद्घाटन सन् २०२३ जनवरी १ मा गरिएको थियो। चीनको एक्जिम बैंकको करिब २२ अर्ब रुपैयाँ सहुलियतपूर्ण ऋण सहयोगमा निर्माण गरिएको यो विमानस्थल ४ डी श्रेणीको हो र यसको धावनमार्ग २ हजार ५०० मिटर लामो छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Pokhara International Airport is the second new international airport in Nepal and was inaugurated on 1 January 2003. Built with a concessional loan assistance of about 2 billion rupees from the Exim Bank of China, the airport is of 4D category and has a runway length of 2,500 meters.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Pokhara International Airport is the second new international airport in Nepal and was inaugurated on 1 January 2003. Built with a concessional loan assistance of about 2 billion rupees from the Exim Bank of China, the airport is of 4D category and has a runway length of 2,500 meters.
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

## Passage 22 / 61
**Linked Candidate Items:** `item_036`, `item_118`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### 1. Source Passage (Nepali · Condition C1)
> गौतम बुद्ध अन्तर्राष्ट्रिय विमानस्थल रूपन्देहीको भैरहवामा अवस्थित छ। सन् २०२२ मे १६ (बुद्ध पूर्णिमा) का दिन उद्घाटन गरिएको यो नेपालको दोस्रो अन्तर्राष्ट्रिय विमानस्थल हो। यस विमानस्थलको धावनमार्ग ३ हजार मिटर लामो छ र यसले वाइडबडी विमानहरू अवतरण गर्न सक्ने क्षमता राख्दछ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Gautam Buddha International Airport is located in Bhairahawa, Rupandehi. It is the second international airport in Nepal to be inaugurated on 16 May ( Buddha Purnima ). The runway of the airport is 3,000 meters long and has the capacity to land widebody aircraft.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Gautam Buddha International Airport is located in Bhairahawa, Rupandehi. It is the second international airport in Nepal to be inaugurated on 16 May ( Buddha Purnima ). The runway of the airport is 3,000 meters long and has the capacity to land widebody aircraft.
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

## Passage 23 / 61
**Linked Candidate Items:** `item_037`, `item_119`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### 1. Source Passage (Nepali · Condition C1)
> अरुण तेस्रो जलविद्युत आयोजना (९०० मेगावाट) संखुवासभा जिल्लामा निर्माणाधीन नेपालको ठूलो निर्यातमुखी जलविद्युत आयोजना हो। भारतीय कम्पनी सतलज जलविद्युत निगम (एसजेभीएन) ले निर्माण गरिरहेको यस आयोजनाबाट नेपालले २१.९ प्रतिशत (१९७ मेगावाट) विद्युत निःशुल्क प्राप्त गर्ने सम्झौता छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Arun III Hydropower Project ( 100 MW ) is Nepal's largest export-oriented hydroelectric project under construction in Sankhuwasabha district. Nepal has an agreement to receive 21.1 % ( 13.8 MW ) of electricity free of charge from the project, which is being constructed by the Indian company Sutlej Hydroelectric Power Corporation ( SJVN ).

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Arun III Hydropower Project ( 100 MW ) is Nepal's largest export-oriented hydroelectric project under construction in Sankhuwasabha district. Nepal has an agreement to receive 21.1 % ( 13.8 MW ) of electricity free of charge from the project, which is being constructed by the Indian company Sutlej Hydroelectric Power Corporation ( SJVN ).
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

## Passage 24 / 61
**Linked Candidate Items:** `item_038`, `item_120`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### 1. Source Passage (Nepali · Condition C1)
> नागढुंगा-सिस्नेखोला सुरुङमार्गको मुख्य सुरुङको लम्बाई २ हजार ६८८ मिटर रहेको छ। वि.सं. २०८१ वैशाखमा यस सुरुङमार्गको 'ब्रेकथ्रु' भएको थियो। जापान अन्तर्राष्ट्रिय सहयोग नियोग (जाइका) को सहुलियतपूर्ण ऋण सहयोगमा निर्माणाधीन यो सुरुङमार्ग नेपालको पहिलो आधुनिक यातायात सुरुङमार्ग हो।

### 2. Raw IndicTrans2 MT (Condition C2)
> The main tunnel of the Nagdunga-Sisnekhola tunnel has a length of 2,000 metres. The tunnel was'broken'in 2021 CE. The tunnel is the first modern transport tunnel in Nepal under construction with a concessional loan assistance from the Japan International Cooperation Agency ( JICA ).

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The main tunnel of the Nagdunga-Sisnekhola tunnel has a length of 2,000 metres. The tunnel was'broken'in 2021 CE. The tunnel is the first modern transport tunnel in Nepal under construction with a concessional loan assistance from the Japan International Cooperation Agency ( JICA ).
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

## Passage 25 / 61
**Linked Candidate Items:** `item_039`
**Domain:** wikipedia | **Topic Sub-Genre:** infrastructure_tourism

### 1. Source Passage (Nepali · Condition C1)
> भेरी-बबई डाइभर्सन बहुउद्देश्यीय आयोजना नेपालको पहिलो अन्तर-जलाधार जल स्थानान्तरण आयोजना हो। टनेल बोरिङ मेसिन (टीबीएम) प्रयोग गरी निर्माण गरिएको १२.२ किलोमिटर लामो सुरुङमार्फत भेरी नदीको पानी बबई नदीमा खसालेर बाँके र बर्दियाको ५१ हजार हेक्टर जमिनमा सिँचाइ र ४८ मेगावाट विद्युत उत्पादन गर्ने लक्ष्य छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Bheri-Babai Diversion Multipurpose Project is Nepal's first inter-stream water transfer project. The 8.2 km long tunnel constructed using Tunnel Boring Machine ( TBM ) aims to divert the water of the Bheri River into the Babai River to irrigate thousands of hectares of land in Banke and Bardiya and generate 8 MW of electricity.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Bheri-Babai Diversion Multipurpose Project is Nepal's first inter-stream water transfer project. The 8.2 km long tunnel constructed using Tunnel Boring Machine ( TBM ) aims to divert the water of the Bheri River into the Babai River to irrigate thousands of hectares of land in Banke and Bardiya and generate 8 MW of electricity.
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

## Passage 26 / 61
**Linked Candidate Items:** `item_041`, `item_046`
**Domain:** government_report | **Topic Sub-Genre:** health

### 1. Source Passage (Nepali · Condition C1)
> नेपाल स्वास्थ्य अनुसन्धान परिषद्का अनुसार नेपालमा नसर्ने रोगहरूको प्रकोप तीव्र रूपमा बढ्दै गएको छ। कुल मृत्युमध्ये करिब ७१ प्रतिशत नसर्ने रोगहरू (मुटुरोग, क्यान्सर, मधुमेह र श्वासप्रश्वास सम्बन्धी रोग) का कारण हुने गरेको छ। यसैगरी उच्च रक्तचापका बिरामीहरूको सङ्ख्या कुल वयस्क जनसङ्ख्याको ३० प्रतिशतभन्दा बढी पुगेको स्वास्थ्य मन्त्रालयको पछिल्लो सर्वेक्षणले देखाएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Nepal Health Research Council, the incidence of non-communicable diseases is increasing rapidly in Nepal. About forty percent of the total deaths are due to non-communicable diseases ( heart disease, cancer, diabetes, and respiratory diseases ). Similarly, the number of patients with hypertension has increased to more than thirty-three percent of the total adult population, according to the latest survey by the Ministry of Health.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Nepal Health Research Council, the incidence of non-communicable diseases is increasing rapidly in Nepal. About forty percent of the total deaths are due to non-communicable diseases ( heart disease, cancer, diabetes, and respiratory diseases ). Similarly, the number of patients with hypertension has increased to more than thirty-three percent of the total adult population, according to the latest survey by the Ministry of Health.
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

## Passage 27 / 61
**Linked Candidate Items:** `item_042`, `item_047`
**Domain:** government_report | **Topic Sub-Genre:** health

### 1. Source Passage (Nepali · Condition C1)
> स्वास्थ्य सेवा विभागको खोप शाखाका अनुसार नेपालमा बाल मृत्युदर घटाउन नियमित १२ प्रकारका खोपहरू निःशुल्क उपलब्ध गराइएका छन्। यस कार्यक्रमले दादुरा-रुबेला र पोलियो रोग निवारणमा उल्लेख्य सफलता हासिल गरेको छ। सन् २०२३ को तथ्याङ्क अनुसार पूर्ण खोप पाउने बालबालिकाको राष्ट्रिय कभरेज ८८ प्रतिशत पुगेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Immunization Branch of the Department of Health Services, eight regular types of vaccines have been made available free of charge to reduce child mortality in Nepal. The program has achieved significant success in the prevention of measles-rubella and polio. The national coverage of fully vaccinated children has reached five percent as of 2013.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Immunization Branch of the Department of Health Services, eight regular types of vaccines have been made available free of charge to reduce child mortality in Nepal. The program has achieved significant success in the prevention of measles-rubella and polio. The national coverage of fully vaccinated children has reached five percent as of 2013.
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

## Passage 28 / 61
**Linked Candidate Items:** `item_043`, `item_048`
**Domain:** government_report | **Topic Sub-Genre:** health

### 1. Source Passage (Nepali · Condition C1)
> राष्ट्रिय एड्स तथा यौनरोग नियन्त्रण केन्द्रका अनुसार नेपालमा सन् २०२२ को अन्त्यसम्ममा अनुमानित ३० हजार मानिसमा एचआईभी सङ्क्रमण रहेको पाइएको छ। तीमध्ये करिब ७८ प्रतिशत सङ्क्रमितहरूले एन्टिरेट्रोभाइरल (एआरभी) उपचार प्राप्त गरिरहेका छन्। नयाँ सङ्क्रमण दरमा अघिल्लो दशकको तुलनामा ६० प्रतिशतले गिरावट आएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the National AIDS and Sexually Transmitted Diseases Control Center, an estimated 303,000 people in Nepal have been diagnosed with HIV by the end of the year. About 50 % of those infected are receiving antiretroviral ( ARV ) treatment. The new infection rate has fallen by 600 % compared to the previous decade.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the National AIDS and Sexually Transmitted Diseases Control Center, an estimated 303,000 people in Nepal have been diagnosed with HIV by the end of the year. About 50 % of those infected are receiving antiretroviral ( ARV ) treatment. The new infection rate has fallen by 600 % compared to the previous decade.
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

## Passage 29 / 61
**Linked Candidate Items:** `item_044`, `item_049`
**Domain:** government_report | **Topic Sub-Genre:** health

### 1. Source Passage (Nepali · Condition C1)
> नेपाल जनसाङ्ख्यिक तथा स्वास्थ्य सर्वेक्षण (एनडीएचएस २०२२) अनुसार पाँच वर्ष मुनिका बालबालिकामा पुड्कोपनको दर २५ प्रतिशतमा झरेको छ। सन् २००१ मा यो दर ५७ प्रतिशत रहेको थियो। त्यस्तै कम तौल भएका बालबालिकाको सङ्ख्या १९ प्रतिशत र ख्याउटेपनको दर ८ प्रतिशत रहेको प्रतिवेदनमा उल्लेख छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Nepal Demographic and Health Survey ( NDHS ), the fertility rate among children under the age of five has dropped to 5 %. The rate was 6 % in 2015. Similarly, the number of underweight children is 16 % and the rate of obesity is 8 %.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Nepal Demographic and Health Survey ( NDHS ), the fertility rate among children under the age of five has dropped to 5 %. The rate was 6 % in 2015. Similarly, the number of underweight children is 16 % and the rate of obesity is 8 %.
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

## Passage 30 / 61
**Linked Candidate Items:** `item_045`, `item_050`
**Domain:** government_report | **Topic Sub-Genre:** health

### 1. Source Passage (Nepali · Condition C1)
> काठमाडौँ उपत्यकामा पछिल्लो वर्ष डेंगु सङ्क्रमणका कारण १५ जनाको मृत्यु भएको छ भने २० हजारभन्दा बढी व्यक्तिहरू प्रभावित भएका छन्। इपिडिमियोलोजी तथा रोग नियन्त्रण महाशाखा (ईडीसीडी) ले लामखुट्टेको लार्भा नष्ट गर्ने 'खोज र नष्ट गर' अभियान ७७ वटै जिल्लामा सञ्चालन गरिएको जानकारी दिएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Fifteen people have died and more than 20,000 people have been affected due to dengue infection in the Kathmandu Valley in the last year. The Epidemiology and Disease Control Division ( EDCD ) has informed that the'Search and Destroy'campaign to destroy mosquito larvae has been carried out in all the districts.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Fifteen people have died and more than 20,000 people have been affected due to dengue infection in the Kathmandu Valley in the last year. The Epidemiology and Disease Control Division ( EDCD ) has informed that the'Search and Destroy'campaign to destroy mosquito larvae has been carried out in all the districts.
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

## Passage 31 / 61
**Linked Candidate Items:** `item_051`, `item_056`
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### 1. Source Passage (Nepali · Condition C1)
> कृषि तथा पशुपन्छी विकास मन्त्रालयका अनुसार आर्थिक वर्ष २०८०/८१ मा नेपालमा कुल ५७ लाख मेट्रिक टन धान उत्पादन भएको छ, जुन अघिल्लो वर्षको तुलनामा ४.३ प्रतिशतले बढी हो। धान खेती गरिएको कुल क्षेत्रफल १४ लाख ३८ हजार हेक्टर रहेको थियो। उन्नत जातको बीउ र रासायनिक मलको समयमै उपलब्धताका कारण उत्पादकत्व ३.९८ मेट्रिक टन प्रति हेक्टर पुगेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Ministry of Agriculture and Livestock Development, in the financial year 20â € " 21, Nepal has produced a total of 13.6 million metric tons of rice, which is 4.33 percent more than the previous year. The total area under rice cultivation was 13.5 million hectares. Due to the timely availability of advanced varieties of seeds and chemical fertilizers, the productivity has reached 3.9 million metric tons per hectare.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Ministry of Agriculture and Livestock Development, in the financial year 20â € " 21, Nepal has produced a total of 13.6 million metric tons of rice, which is 4.33 percent more than the previous year. The total area under rice cultivation was 13.5 million hectares. Due to the timely availability of advanced varieties of seeds and chemical fertilizers, the productivity has reached 3.9 million metric tons per hectare.
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

## Passage 32 / 61
**Linked Candidate Items:** `item_052`, `item_057`
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### 1. Source Passage (Nepali · Condition C1)
> राष्ट्रिय कृषि गणना २०७८ अनुसार नेपालमा कृषक परिवारको सङ्ख्या ४१ लाख ३० हजार पुगेको छ। कुल खेतीयोग्य जमिनमध्ये ५४.५ प्रतिशत जमिनमा मात्र सिँचाइ सुविधा पुगेको छ। त्यसमध्ये बाह्रै महिना सिँचाइ सुविधा उपलब्ध भएको जमिन कुल सिञ्चित जमिनको ३९ प्रतिशत मात्र रहेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the National Census of Agriculture, the number of farming families in Nepal has reached four million and thirty-three thousand. Out of the total cultivable land, only four and a half percent of the land has access to irrigation. Out of this, the land that has access to irrigation for twelve months is only one percent of the total irrigated land.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the National Census of Agriculture, the number of farming families in Nepal has reached four million and thirty-three thousand. Out of the total cultivable land, only four and a half percent of the land has access to irrigation. Out of this, the land that has access to irrigation for twelve months is only one percent of the total irrigated land.
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

## Passage 33 / 61
**Linked Candidate Items:** `item_053`, `item_058`
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### 1. Source Passage (Nepali · Condition C1)
> नेपालबाट भारततर्फ अलैँची र अदुवा निर्यातमा उल्लेख्य वृद्धि भएको छ। व्यापार तथा निकासी प्रवर्द्धन केन्द्रका अनुसार गत वर्ष करिब ८ अर्ब रुपैयाँ बराबरको ठूलो अलैँची निर्यात भएको थियो। ताप्लेजुङ, पाँचथर र इलाम जिल्ला नेपालको प्रमुख अलैँची उत्पादन क्षेत्र हुन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Cardamom and ginger exports from Nepal to India have increased significantly. According to the Trade and Export Promotion Centre, a large amount of cardamom worth about 8 billion rupees was exported last year. Taplejung and Ilam districts are the major cardamom producing areas of Nepal.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Cardamom and ginger exports from Nepal to India have increased significantly. According to the Trade and Export Promotion Centre, a large amount of cardamom worth about 8 billion rupees was exported last year. Taplejung and Ilam districts are the major cardamom producing areas of Nepal.
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

## Passage 34 / 61
**Linked Candidate Items:** `item_054`, `item_059`
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### 1. Source Passage (Nepali · Condition C1)
> नेपालमा सामुदायिक वन उपभोक्ता समूहहरूको सङ्ख्या २२ हजार २६६ पुगेको छ। यी समूहहरूले करिब २४ लाख हेक्टर राष्ट्रिय वन संरक्षण र व्यवस्थापन गरिरहेका छन्। सामुदायिक वन व्यवस्थापनबाट ३३ लाखभन्दा बढी घरधुरी प्रत्यक्ष रूपमा लाभान्वित भएका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> The number of community forest consumer groups in Nepal has reached 14,026. These groups are conserving and managing about 3.4 million hectares of national forests. Community forest management has directly benefited more than 5 million households.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The number of community forest consumer groups in Nepal has reached 14,026. These groups are conserving and managing about 3.4 million hectares of national forests. Community forest management has directly benefited more than 5 million households.
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

## Passage 35 / 61
**Linked Candidate Items:** `item_055`, `item_060`
**Domain:** government_report | **Topic Sub-Genre:** agriculture

### 1. Source Passage (Nepali · Condition C1)
> मकै नेपालको दोस्रो प्रमुख खाद्यान्न बाली हो। आर्थिक वर्ष २०७९/८० मा नेपालमा मकैको कुल उत्पादन ३० लाख मेट्रिक टन भएको थियो। पहाडी जिल्लाहरूमा मकै खेती कुल मकै उत्पादन क्षेत्रको ७० प्रतिशतभन्दा बढी ओगटेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Maize is the second major food crop in Nepal. The total production of maize in Nepal was 30.3 million metric tons in the financial year 2019-20. Maize cultivation in the hill districts accounts for more than 20 % of the total maize production area.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Maize is the second major food crop in Nepal. The total production of maize in Nepal was 30.3 million metric tons in the financial year 2019-20. Maize cultivation in the hill districts accounts for more than 20 % of the total maize production area.
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

## Passage 36 / 61
**Linked Candidate Items:** `item_061`, `item_066`
**Domain:** government_report | **Topic Sub-Genre:** education

### 1. Source Passage (Nepali · Condition C1)
> राष्ट्रिय जनगणना २०७८ अनुसार नेपालको समग्र साक्षरता दर ७६.३ प्रतिशत पुगेको छ। पुरुष साक्षरता दर ८३.६ प्रतिशत र महिला साक्षरता दर ६९.४ प्रतिशत रहेको छ। प्रदेशगत रूपमा बागमती प्रदेशमा सबैभन्दा बढी (८२.१ प्रतिशत) र मधेश प्रदेशमा सबैभन्दा कम (६३.५ प्रतिशत) साक्षरता दर पाइएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the national census, the overall literacy rate of Nepal has reached 83.3 %. The male literacy rate is 66.6 % and the female literacy rate is 74.4 %. Bagmati Province has the highest literacy rate provincially ( 72.2 % ) and Madhesh Province has the lowest ( 65.35 % ).

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the national census, the overall literacy rate of Nepal has reached 83.3 %. The male literacy rate is 66.6 % and the female literacy rate is 74.4 %. Bagmati Province has the highest literacy rate provincially ( 72.2 % ) and Madhesh Province has the lowest ( 65.35 % ).
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

## Passage 37 / 61
**Linked Candidate Items:** `item_062`, `item_067`
**Domain:** government_report | **Topic Sub-Genre:** education

### 1. Source Passage (Nepali · Condition C1)
> राष्ट्रिय परीक्षा बोर्डले सार्वजनिक गरेको वि.सं. २०८० को माध्यमिक शिक्षा परीक्षा (एसईई) को नतिजा अनुसार नियमित तर्फ सम्मिलित ४ लाख ६४ हजार ७८५ विद्यार्थीमध्ये ४७.८६ प्रतिशत मात्र उत्तीर्ण भएका छन्। नयाँ लेटर ग्रेडिङ निर्देशिका अनुसार सैद्धान्तिकतर्फ कम्तीमा ३५ प्रतिशत अंक नल्याउने विद्यार्थीलाई नन-ग्रेडेड (एनजी) मा राखिएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the results of the Secondary Education Examination ( SEE ) for the year 2020 released by the National Board of Examinations, out of 400,000 students enrolled on the regular side, only 8.8 % have passed. According to the new letter grading guidelines, students who do not score at least 6 % on the theoretical side are placed in the non-graded ( NG ) category.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the results of the Secondary Education Examination ( SEE ) for the year 2020 released by the National Board of Examinations, out of 400,000 students enrolled on the regular side, only 8.8 % have passed. According to the new letter grading guidelines, students who do not score at least 6 % on the theoretical side are placed in the non-graded ( NG ) category.
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

## Passage 38 / 61
**Linked Candidate Items:** `item_063`, `item_068`
**Domain:** government_report | **Topic Sub-Genre:** education

### 1. Source Passage (Nepali · Condition C1)
> शिक्षा तथा मानव स्रोत विकास केन्द्रको तथ्याङ्क अनुसार आधारभूत तह (कक्षा १-८) मा खुद भर्ना दर ९५.२ प्रतिशत पुगेको छ। तर माध्यमिक तह (कक्षा ९-१२) मा खुद भर्ना दर ५४.३ प्रतिशत मात्र रहेको छ। कक्षा ८ सम्म पुग्दा ड्रपआउट दर करिब १५ प्रतिशत रहेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the data of the Education and Human Resource Development Center, the self-enrolment rate at the basic level ( classes 1-8 ) has reached 95.2 %. But at the secondary level ( classes 1-8 ), the self-enrolment rate is only 44.33 %. By the time the dropout rate reaches class 8, it is about 15 %.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the data of the Education and Human Resource Development Center, the self-enrolment rate at the basic level ( classes 1-8 ) has reached 95.2 %. But at the secondary level ( classes 1-8 ), the self-enrolment rate is only 44.33 %. By the time the dropout rate reaches class 8, it is about 15 %.
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

## Passage 39 / 61
**Linked Candidate Items:** `item_064`, `item_069`
**Domain:** government_report | **Topic Sub-Genre:** education

### 1. Source Passage (Nepali · Condition C1)
> त्रिभुवन विश्वविद्यालय नेपालको सबैभन्दा पुरानो र ठूलो विश्वविद्यालय हो, जसको स्थापना वि.सं. २०१६ मा भएको थियो। त्रिवि अन्तर्गत हाल ६२ वटा आंगिक क्याम्पस र १ हजारभन्दा बढी सम्बन्धन प्राप्त क्याम्पसहरू सञ्चालनमा छन्। नेपालमा उच्च शिक्षा अध्ययन गर्ने कुल विद्यार्थीमध्ये करिब ७५ प्रतिशत त्रिविमै अध्ययनरत छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Tribhuvan University is the oldest and largest university in Nepal and was established in 1999. Currently, there are 12 organic campuses and more than 1000 affiliated campuses operating under Triveni. About 44 % of the total students studying higher education in Nepal are studying in Triveni.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Tribhuvan University is the oldest and largest university in Nepal and was established in 1999. Currently, there are 12 organic campuses and more than 1000 affiliated campuses operating under Triveni. About 44 % of the total students studying higher education in Nepal are studying in Triveni.
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

## Passage 40 / 61
**Linked Candidate Items:** `item_065`, `item_070`
**Domain:** government_report | **Topic Sub-Genre:** education

### 1. Source Passage (Nepali · Condition C1)
> नेपाल सरकारले प्राविधिक तथा व्यावसायिक शिक्षा एवं तालिम परिषद् (सीटीईभीटी) मार्फत देशभरका ७५३ वटै स्थानीय तहमा प्राविधिक शिक्षा विस्तार गर्ने नीति लिएको छ। हालसम्म ६५० भन्दा बढी स्थानीय तहमा प्राविधिक धारका विद्यालयहरू स्थापना भइसकेका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Government of Nepal, through the Council for Technical and Vocational Education and Training ( CTEVT ), has taken a policy of expanding technical education to all 43 local levels across the country. So far, more than 40 schools of technical streams have been established at local levels.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Government of Nepal, through the Council for Technical and Vocational Education and Training ( CTEVT ), has taken a policy of expanding technical education to all 43 local levels across the country. So far, more than 40 schools of technical streams have been established at local levels.
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

## Passage 41 / 61
**Linked Candidate Items:** `item_071`, `item_076`
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### 1. Source Passage (Nepali · Condition C1)
> नेपाल राष्ट्र बैंकका अनुसार चालु आर्थिक वर्षको पहिलो त्रैमासमा वार्षिक विन्दुगत उपभोक्ता मुद्रास्फीति दर ४.४० प्रतिशत रहेको छ। अघिल्लो वर्षको सोही महिनामा यस्तो मुद्रास्फीति ७.५० प्रतिशत रहेको थियो। खाद्य तथा पेय पदार्थ समूहको मुद्रास्फीति दर ६.३८ प्रतिशत र गैर-खाद्य समूहको मुद्रास्फीति ३.४५ प्रतिशत रहेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Nepal Rastra Bank, the annual point-to-point consumer inflation rate for the first quarter of the current financial year is 4.40 %. The corresponding month of the previous year, such inflation was 7.40 %. The inflation rate for the food and beverage group is 6.33 % and for the non-food group is 3.45 %.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Nepal Rastra Bank, the annual point-to-point consumer inflation rate for the first quarter of the current financial year is 4.40 %. The corresponding month of the previous year, such inflation was 7.40 %. The inflation rate for the food and beverage group is 6.33 % and for the non-food group is 3.45 %.
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

## Passage 42 / 61
**Linked Candidate Items:** `item_072`, `item_077`
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### 1. Source Passage (Nepali · Condition C1)
> आर्थिक वर्ष २०८०/८१ मा नेपालको कुल वैदेशिक व्यापार घाटा १४ खर्ब ५३ अर्ब रुपैयाँ पुगेको छ। कुल वस्तु आयात १५ खर्ब ९२ अर्ब रुपैयाँ हुँदा कुल वस्तु निर्यात १ खर्ब ३९ अर्ब रुपैयाँमा सीमित भएको भन्सार विभागको तथ्याङ्क छ। नेपालको व्यापार घाटामा पेट्रोलियम पदार्थ र सवारी साधनको हिस्सा सबैभन्दा ठूलो रहेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Nepal's total foreign trade deficit in FY2019 / 2018 has reached one trillion rupees. The total goods exports are limited to one trillion rupees as per the customs department's data. Petroleum products and vehicles account for the largest share of Nepal's trade deficit.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Nepal's total foreign trade deficit in FY2019 / 2018 has reached one trillion rupees. The total goods exports are limited to one trillion rupees as per the customs department's data. Petroleum products and vehicles account for the largest share of Nepal's trade deficit.
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

## Passage 43 / 61
**Linked Candidate Items:** `item_073`, `item_078`
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### 1. Source Passage (Nepali · Condition C1)
> नेपालको कुल वैदेशिक मुद्रा सञ्चिति बढेर २० खर्ब ४१ अर्ब रुपैयाँ बराबर पुगेको छ। अमेरिकी डलरमा यो सञ्चिति १५ अर्ब २७ करोड डलर पुगेको नेपाल राष्ट्र बैंकले जनाएको छ। यस सञ्चितिले करिब १३ महिनाको वस्तु तथा सेवा आयात धान्न सक्ने क्षमता राख्दछ।

### 2. Raw IndicTrans2 MT (Condition C2)
> Nepal's total foreign exchange reserves have increased to 20 trillion rupees. In US dollars, the reserves have reached $ 15 billion, according to the Nepal Rastra Bank. The reserves have the potential to handle about thirteen months'worth of goods and services imports.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Nepal's total foreign exchange reserves have increased to 20 trillion rupees. In US dollars, the reserves have reached $ 15 billion, according to the Nepal Rastra Bank. The reserves have the potential to handle about thirteen months'worth of goods and services imports.
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

## Passage 44 / 61
**Linked Candidate Items:** `item_074`, `item_079`
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### 1. Source Passage (Nepali · Condition C1)
> नेपाल राष्ट्र बैंकको निर्देशिका अनुसार वाणिज्य बैंकहरूको न्यूनतम चुक्ता पुँजी ८ अर्ब रुपैयाँ हुनुपर्दछ। हाल नेपालमा २० वटा वाणिज्य बैंकहरू, १७ वटा विकास बैंकहरू र १७ वटा वित्त कम्पनीहरू सञ्चालनमा रहेका छन्। बैंक तथा वित्तीय संस्थाहरूको कुल निक्षेप ६२ खर्ब रुपैयाँभन्दा माथि पुगेको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the guidelines of the Nepal Rastra Bank, the minimum paid-up capital of commercial banks should be 8 billion rupees. Currently, there are 20 commercial banks, 20 development banks, and 20 finance companies operating in Nepal. The total deposits of banks and financial institutions exceed one trillion rupees in a year.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the guidelines of the Nepal Rastra Bank, the minimum paid-up capital of commercial banks should be 8 billion rupees. Currently, there are 20 commercial banks, 20 development banks, and 20 finance companies operating in Nepal. The total deposits of banks and financial institutions exceed one trillion rupees in a year.
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

## Passage 45 / 61
**Linked Candidate Items:** `item_075`, `item_080`
**Domain:** government_report | **Topic Sub-Genre:** economy_finance

### 1. Source Passage (Nepali · Condition C1)
> नेपाल सरकारले आर्थिक वर्ष २०८१/८२ का लागि १८ खर्ब ६० अर्ब ३० करोड रुपैयाँको बजेट प्रस्तुत गरेको छ। चालु खर्चतर्फ ११ खर्ब ४० अर्ब (६१.३१ प्रतिशत) र पुँजीगत खर्चतर्फ ३ खर्ब ५२ अर्ब (१८.९४ प्रतिशत) विनियोजन गरिएको अर्थ मन्त्रालयले जनाएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Government of Nepal has presented a budget for the financial year 2018 / 202 with a budget of â'1 7 trillion â'3 billion. The Ministry of Finance has stated that â'1 4 trillion ( 611.33 billion ) has been allocated towards current expenditure and â'1 3 trillion ( 13.4 billion ) towards capital expenditure.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Government of Nepal has presented a budget for the financial year 2018 / 202 with a budget of â'1 7 trillion â'3 billion. The Ministry of Finance has stated that â'1 4 trillion ( 611.33 billion ) has been allocated towards current expenditure and â'1 3 trillion ( 13.4 billion ) towards capital expenditure.
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

## Passage 46 / 61
**Linked Candidate Items:** `item_081`, `item_087`
**Domain:** news | **Topic Sub-Genre:** sports

### 1. Source Passage (Nepali · Condition C1)
> नेपाल राष्ट्रिय क्रिकेट टोलीले सन् २०२४ को आईसीसी पुरुष टी-२० विश्वकपमा दक्षिण अफ्रिकाविरुद्ध ऐतिहासिक खेल प्रदर्शन गर्‍यो। दक्षिण अफ्रिकाले दिएको ११६ रनको लक्ष्य पछ्याउँदा नेपाल मात्र १ रनले पराजित भयो। नेपालका तीव्र गतिका बलर कुशल भुर्तेलले ४ विकेट र दीपेन्द्रसिंह ऐरीले ३ विकेट लिएका थिए।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Nepal national cricket team played a historic match against South Africa in the ICC Men's T20 World Cup 2018. Nepal were defeated by just 1 run in pursuit of a target of 16 runs set by South Africa. Nepal's fast bowler Kushal Bhurtel took 4 wickets and Dipendrasinh Ayri took 3 wickets.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Nepal national cricket team played a historic match against South Africa in the ICC Men's T20 World Cup 2018. Nepal were defeated by just 1 run in pursuit of a target of 16 runs set by South Africa. Nepal's fast bowler Kushal Bhurtel took 4 wickets and Dipendrasinh Ayri took 3 wickets.
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

## Passage 47 / 61
**Linked Candidate Items:** `item_082`, `item_088`
**Domain:** news | **Topic Sub-Genre:** sports

### 1. Source Passage (Nepali · Condition C1)
> नेपाली अलराउन्डर दीपेन्द्रसिंह ऐरीले कतारविरुद्धको एसीसी प्रिमियर कप खेलमा एकै ओभरमा ६ छक्का प्रहार गर्दै विश्व कीर्तिमान कायम गरेका छन्। उनले कामरान खानको ओभरमा लगातार ६ छक्का प्रहार गरेका हुन्। यसअघि उनले १९औँ एसियाली खेलकुदमा मङ्गोलियाविरुद्ध ९ बलमै अर्धशतक प्रहार गरेका थिए।

### 2. Raw IndicTrans2 MT (Condition C2)
> Nepali all-rounder Dipendrasinh Ayri holds the world record for hitting six sixes in an over in the ACC Premier Cup match against Qatar. He hit six consecutive sixes in Kamran Khan's over. Earlier, he had scored a half-century in the same ball against Mongolia in the 16th Asian Games.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Nepali all-rounder Dipendrasinh Ayri holds the world record for hitting six sixes in an over in the ACC Premier Cup match against Qatar. He hit six consecutive sixes in Kamran Khan's over. Earlier, he had scored a half-century in the same ball against Mongolia in the 16th Asian Games.
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

## Passage 48 / 61
**Linked Candidate Items:** `item_083`, `item_089`
**Domain:** news | **Topic Sub-Genre:** sports

### 1. Source Passage (Nepali · Condition C1)
> नेपाल क्रिकेट सङ्घ (क्यान) ले नेपाल प्रिमियर लिग (एनपीएल) टी-२० प्रतियोगिताको पहिलो संस्करण काठमाडौँमा आयोजना गर्ने घोषणा गरेको छ। यस प्रतियोगितामा विराटनगर, चितवन, जनकपुर, काठमाडौँ, कर्णाली, लुम्बिनी, पोखरा र सुदूरपश्चिम गरी ८ वटा फ्रेन्चाइज टोलीहरूले प्रतिस्पर्धा गर्नेछन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Cricket Association of Nepal ( CAN ) has announced that the first edition of the Nepal Premier League ( NPL ) T20 tournament will be held in Kathmandu. The tournament will feature eight franchise teams : Biratnagar, Chitwan, Janakpur, Kathmandu, Karnali, Lumbini, Pokhara and Far East.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Cricket Association of Nepal ( CAN ) has announced that the first edition of the Nepal Premier League ( NPL ) T20 tournament will be held in Kathmandu. The tournament will feature eight franchise teams : Biratnagar, Chitwan, Janakpur, Kathmandu, Karnali, Lumbini, Pokhara and Far East.
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

## Passage 49 / 61
**Linked Candidate Items:** `item_084`, `item_090`
**Domain:** news | **Topic Sub-Genre:** sports

### 1. Source Passage (Nepali · Condition C1)
> साफ महिला च्याम्पियनसिप २०२४ को सेमिफाइनलमा नेपालले भारतलाई पेनाल्टी सुटआउटमा ४-२ ले पराजित गर्दै फाइनलमा स्थान सुरक्षित गर्‍यो। निर्धारित समयको खेल १-१ गोलको बराबरीमा सकिएको थियो। नेपालकी गोलकिपर एन्जिला तुम्बापो सुब्बाले उत्कृष्ट बचाउ गरेकी थिइन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> In the semi-finals of the SAFF Women's Championship, Nepal defeated India in a penalty shootout 4-2 to secure a place in the final. The match ended in a 1-1 draw. Nepal goalkeeper Angela Tumbapo Subba made an excellent save.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
In the semi-finals of the SAFF Women's Championship, Nepal defeated India in a penalty shootout 4-2 to secure a place in the final. The match ended in a 1-1 draw. Nepal goalkeeper Angela Tumbapo Subba made an excellent save.
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

## Passage 50 / 61
**Linked Candidate Items:** `item_085`, `item_091`
**Domain:** news | **Topic Sub-Genre:** sports

### 1. Source Passage (Nepali · Condition C1)
> कीर्तिपुरस्थित त्रिवि क्रिकेट मैदानमा सम्पन्न खेलमा नेपालले स्कटल्याण्डलाई ५ विकेटले पराजित गरेको छ। स्कटल्याण्डले दिएको २१३ रनको लक्ष्य नेपालले ४४.१ ओभरमा ५ विकेट गुमाएर पूरा गर्‍यो। नेपालका लागि कप्तान रोहित पौडेलले ९५ रनको कप्तानी इनिङ खेलेका थिए।

### 2. Raw IndicTrans2 MT (Condition C2)
> Nepal defeated Scotland by 5 wickets in the match held at the Triveni Cricket Ground in Kirtipur. Nepal completed the target of 213 runs given by Scotland by losing 5 wickets in.1 overs. Captain Rohit Poudel played a captain's innings of 55 runs for Nepal.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Nepal defeated Scotland by 5 wickets in the match held at the Triveni Cricket Ground in Kirtipur. Nepal completed the target of 213 runs given by Scotland by losing 5 wickets in.1 overs. Captain Rohit Poudel played a captain's innings of 55 runs for Nepal.
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

## Passage 51 / 61
**Linked Candidate Items:** `item_086`, `item_092`
**Domain:** news | **Topic Sub-Genre:** sports

### 1. Source Passage (Nepali · Condition C1)
> नेपालका तेक्वान्दो खेलाडी पलेशा गोवर्धनले पेरिस पारालम्पिक २०२४ मा ऐतिहासिक कास्य पदक जितेकी छन्। यो पारालम्पिकको इतिहासमा नेपालले जितेको पहिलो आधिकारिक पदक हो। उनले के-४४ विधा अन्तर्गत महिला ५७ केजी तौल समूहमा सर्बियाकी खेलाडीलाई १५-८ ले पराजित गरेकी थिइन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Nepal's taekwondo player Palesha Govardhan has won a historic bronze medal at the Paris Paralympic Games. This is the first official medal won by Nepal in the history of the Paralympics. She defeated a Serbian player 15-8 in the women's 3kg weight category under the K-4 category.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Nepal's taekwondo player Palesha Govardhan has won a historic bronze medal at the Paris Paralympic Games. This is the first official medal won by Nepal in the history of the Paralympics. She defeated a Serbian player 15-8 in the women's 3kg weight category under the K-4 category.
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

## Passage 52 / 61
**Linked Candidate Items:** `item_093`, `item_098`
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### 1. Source Passage (Nepali · Condition C1)
> वि.सं. २०८० कात्तिक १७ गते राति जाजरकोटको रामीडाँडा केन्द्रविन्दु भएर गएको ६.४ म्याग्निच्यूडको भूकम्पमा परी १५४ जनाको मृत्यु भएको छ भने ३५० भन्दा बढी घाइते भएका छन्। जाजरकोट र रुकुम पश्चिममा गरी करिब ६० हजार घरहरू पूर्ण वा आंशिक रूपमा क्षतिग्रस्त भएका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Sixty-four people have been killed and more than 50,000 injured in a 6.4 magnitude earthquake that struck the Ramidanda epicentre of Jajarkot on the night of 20 November. About 500,000 houses have been completely or partially damaged in Jajarkot and Rukum West.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Sixty-four people have been killed and more than 50,000 injured in a 6.4 magnitude earthquake that struck the Ramidanda epicentre of Jajarkot on the night of 20 November. About 500,000 houses have been completely or partially damaged in Jajarkot and Rukum West.
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

## Passage 53 / 61
**Linked Candidate Items:** `item_094`, `item_099`
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### 1. Source Passage (Nepali · Condition C1)
> जल तथा मौसम विज्ञान विभागले मनसुनजन्य विपद्का कारण यस वर्ष देशभर बाढी र पहिरोबाट २२० भन्दा बढी मानिसको ज्यान गएको पुष्टि गरेको छ। विशेषगरी काठमाडौँ उपत्यकाको बागमती र विष्णुमती नदीमा आएको बाढीले विगत ५० वर्षयताकै उच्च सतह पार गरेको थियो।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Department of Water and Meteorology has confirmed that more than ten people have lost their lives due to floods and landslides across the country this year due to monsoon-related disasters. Floods, especially in the Bagmati and Vishnumati rivers of the Kathmandu Valley, have crossed the highest level in the last 50 years.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Department of Water and Meteorology has confirmed that more than ten people have lost their lives due to floods and landslides across the country this year due to monsoon-related disasters. Floods, especially in the Bagmati and Vishnumati rivers of the Kathmandu Valley, have crossed the highest level in the last 50 years.
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

## Passage 54 / 61
**Linked Candidate Items:** `item_095`, `item_100`
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### 1. Source Passage (Nepali · Condition C1)
> अन्तर्राष्ट्रिय एकीकृत पर्वतीय विकास केन्द्र (इसिमोड) को प्रतिवेदन अनुसार हिन्दुकुश हिमालय क्षेत्रका हिमनदीहरू विगतको तुलनामा ६५ प्रतिशत तीव्र गतिमा पग्लिरहेका छन्। नेपालका २१ वटा हिमतालहरू विष्फोटको उच्च जोखिम (जीएलओएफ) मा रहेका छन्, जसमा च्छो रोल्पा र इम्जा हिमताल प्रमुख हुन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to a report by the International Centre for Integrated Mountain Development ( ICIMOD ), glaciers in the Hindu Kush Himalayan region are melting at a four-tenths of a percent faster rate than in the past. Sixteen glaciers in Nepal are at high risk of eruptions ( GLOF ), with the Chho Rolpa and Imja glaciers being the main ones.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to a report by the International Centre for Integrated Mountain Development ( ICIMOD ), glaciers in the Hindu Kush Himalayan region are melting at a four-tenths of a percent faster rate than in the past. Sixteen glaciers in Nepal are at high risk of eruptions ( GLOF ), with the Chho Rolpa and Imja glaciers being the main ones.
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

## Passage 55 / 61
**Linked Candidate Items:** `item_096`, `item_101`
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### 1. Source Passage (Nepali · Condition C1)
> वि.सं. २०७२ वैशाख १२ गते गोरखाको बारपाक केन्द्रविन्दु भएको ७.८ म्याग्निच्यूडको भूकम्पमा परी ८ हजार ९७९ जनाको मृत्यु भएको थियो। राष्ट्रिय पुनर्निर्माण प्राधिकरणले ८ लाखभन्दा बढी निजी आवासहरूको पुनर्निर्माण सम्पन्न गरेको थियो।

### 2. Raw IndicTrans2 MT (Condition C2)
> On the 8th of September, 8000 people were killed in an earthquake with a magnitude of 8000, centered in Barpak, Gorkha. The National Reconstruction Authority had completed the reconstruction of more than 800,000 private houses.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
On the 8th of September, 8000 people were killed in an earthquake with a magnitude of 8000, centered in Barpak, Gorkha. The National Reconstruction Authority had completed the reconstruction of more than 800,000 private houses.
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

## Passage 56 / 61
**Linked Candidate Items:** `item_097`, `item_102`
**Domain:** news | **Topic Sub-Genre:** disaster_geography

### 1. Source Passage (Nepali · Condition C1)
> मेलम्ची नदीमा वि.सं. २०७८ असार १ गते आएको भीषण लेदोसहितको बाढीले मेलम्ची खानेपानी आयोजनाको हेडवर्क्समा गम्भीर क्षति पुर्‍याएको थियो। भेमाथाङ क्षेत्रमा आएको ठूलो पहिरोका कारण नदी थुनिएर फुट्दा बस्ती र पुलहरू बगाएको भूगर्भविद्हरूको अध्ययनले देखाएको छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Melamchi River was severely damaged in the headworks of the Melamchi Drinking Water Project by a severe flash flood on 1 September 2019. A study by geologists has shown that the massive landslide in the Vemathang area caused the river to overflow and overflow settlements and bridges.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Melamchi River was severely damaged in the headworks of the Melamchi Drinking Water Project by a severe flash flood on 1 September 2019. A study by geologists has shown that the massive landslide in the Vemathang area caused the river to overflow and overflow settlements and bridges.
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

## Passage 57 / 61
**Linked Candidate Items:** `item_103`, `item_108`
**Domain:** news | **Topic Sub-Genre:** governance_law

### 1. Source Passage (Nepali · Condition C1)
> नेपालको संविधान २०७२ अनुसार नेपाल एक स्वतन्त्र, अविभाज्य, सार्वभौमसत्ता सम्पन्न, धर्मनिरपेक्ष, समावेशी, लोकतान्त्रिक, समाजवाद-उन्मुख, संघीय लोकतान्त्रिक गणतन्त्रात्मक राज्य हो। राज्यको शासकीय संरचना संघ, प्रदेश र स्थानीय गरी तीन तहमा विभाजित गरिएको छ। संविधानमा ३५ भाग, ३०८ धारा र ९ अनुसूचीहरू रहेका छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> According to the Constitution of Nepal, Nepal is an independent, indivisible, sovereign, secular, inclusive, democratic, socialist, federal, democratic republican state. The state's administrative structure is divided into three tiers : federal, provincial, and local. The constitution consists of six parts, thirty-three articles, and a schedule.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
According to the Constitution of Nepal, Nepal is an independent, indivisible, sovereign, secular, inclusive, democratic, socialist, federal, democratic republican state. The state's administrative structure is divided into three tiers : federal, provincial, and local. The constitution consists of six parts, thirty-three articles, and a schedule.
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

## Passage 58 / 61
**Linked Candidate Items:** `item_104`, `item_109`
**Domain:** news | **Topic Sub-Genre:** governance_law

### 1. Source Passage (Nepali · Condition C1)
> प्रतिनिधि सभामा कुल २७५ सदस्यहरू रहन्छन्, जसमध्ये १६५ जना प्रत्यक्ष निर्वाचन प्रणाली (पहिलो हुने निर्वाचित हुने) बाट र ११० जना समानुपातिक निर्वाचन प्रणालीबाट निर्वाचित हुन्छन्। प्रतिनिधि सभाको कार्यकाल पाँच वर्षको हुन्छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The House of Representatives has a total of 55 members, of which 100 are elected by direct election ( the first to be elected ) and 40 by proportional election. The term of office of the House of Representatives is five years.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The House of Representatives has a total of 55 members, of which 100 are elected by direct election ( the first to be elected ) and 40 by proportional election. The term of office of the House of Representatives is five years.
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

## Passage 59 / 61
**Linked Candidate Items:** `item_105`, `item_110`
**Domain:** news | **Topic Sub-Genre:** governance_law

### 1. Source Passage (Nepali · Condition C1)
> नेपालमा ७ वटा प्रदेश र ७५३ वटा स्थानीय तहहरू रहेका छन्। स्थानीय तह अन्तर्गत ६ वटा महानगरपालिका, ११ वटा उपमहानगरपालिका, २७६ वटा नगरपालिका र ४६० वटा गाउँपालिकाहरू रहेका छन्। स्थानीय तहमा कुल ६ हजार ७४३ वडा कार्यालयहरू सञ्चालनमा छन्।

### 2. Raw IndicTrans2 MT (Condition C2)
> Nepal has seven provinces and thirty-three local levels. There are six metropolitan cities, eleven sub-metropolises, sixty-six municipalities and thirty-six villages under the local level. A total of six thousand thirty-three ward offices are functioning at the local level.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
Nepal has seven provinces and thirty-three local levels. There are six metropolitan cities, eleven sub-metropolises, sixty-six municipalities and thirty-six villages under the local level. A total of six thousand thirty-three ward offices are functioning at the local level.
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

## Passage 60 / 61
**Linked Candidate Items:** `item_106`, `item_111`
**Domain:** news | **Topic Sub-Genre:** governance_law

### 1. Source Passage (Nepali · Condition C1)
> सर्वोच्च अदालत नेपालको न्यायपालिकाको सर्वोच्च निकाय हो। संविधान अनुसार सर्वोच्च अदालतमा प्रधानन्यायाधीशका अतिरिक्त बढीमा २० जना अन्य न्यायाधीशहरू रहने व्यवस्था छ। सर्वोच्च अदालत अभिलेख अदालत हुनेछ र यसलाई आफ्ना फैसलाहरूको पुनरावलोकन गर्ने अधिकार रहन्छ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Supreme Court is the highest body of the judiciary in Nepal. According to the constitution, the Supreme Court has a maximum of 20 other judges in addition to the Chief Justice. The Supreme Court will be the court of record and has the power to review its decisions.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Supreme Court is the highest body of the judiciary in Nepal. According to the constitution, the Supreme Court has a maximum of 20 other judges in addition to the Chief Justice. The Supreme Court will be the court of record and has the power to review its decisions.
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

## Passage 61 / 61
**Linked Candidate Items:** `item_107`, `item_112`
**Domain:** news | **Topic Sub-Genre:** governance_law

### 1. Source Passage (Nepali · Condition C1)
> अख्तियार दुरुपयोग अनुसन्धान आयोग (सीआईएए) सार्वजनिक पद धारण गरेको व्यक्तिले भ्रष्टाचार गरी अख्तियारको दुरुपयोग गरेमा अनुसन्धान र अभियोजन गर्ने संवैधानिक निकाय हो। आयोगले विशेष अदालतमा भ्रष्टाचारका मुद्दाहरू दायर गर्दछ।

### 2. Raw IndicTrans2 MT (Condition C2)
> The Commission for the Investigation of Abuse of Authority ( CIAA ) is the constitutional body that investigates and prosecutes corruption and abuse of authority by persons holding public office. The commission files corruption cases in special courts.

### 3. Human Post-Edited Translation (Condition C3 Slot)
> *Edit the text below to fix translation errors while preserving phrasing:*
```text
The Commission for the Investigation of Abuse of Authority ( CIAA ) is the constitutional body that investigates and prosecutes corruption and abuse of authority by persons holding public office. The commission files corruption cases in special courts.
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
