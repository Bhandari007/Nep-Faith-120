# NepFaith-120: Human Adjudication Queue

**Status:** Awaiting Lead Researcher Adjudication  
**Reference Rubric:** `docs/RUBRIC_V1.md`  
**Total Discordant Claims Requiring Adjudication:** 19  

> [!IMPORTANT]
> For each discordant claim below, the lead researcher reviews the Nepali passage ($p_{ne}$) and English claim,
> makes the definitive determination (`Supported`, `Contradicted`, or `Not-in-context`), and records the verdict.
> Once finalized, these become part of the official gold benchmark committed to `data/raw/labels/gold_labels_120.jsonl`.

---

## Discrepancy 1/19 · `item_002_c3` (`item_002`)
- **Criticality:** `NON-CRITICAL`
- **Domain / Sub-Genre:** `wikipedia` / `culture_heritage`
- **Source:** [पशुपतिनाथ मन्दिर](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A4%B6%E0%A5%81%E0%A4%AA%E0%A4%A4%E0%A4%BF%E0%A4%A8%E0%A4%BE%E0%A4%A5_%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%B0)

### Nepali Context Passage ($p_{ne}$):
> पशुपतिनाथ मन्दिर बागमती नदीको किनारमा अवस्थित हिन्दूहरूको पवित्र तीर्थस्थल हो। यो मन्दिर प्यागोडा शैलीमा निर्माण गरिएको छ र यसको छाना दुई तहको सुनको जलप लगाइएको तामाबाट बनेको छ। वि.सं. १९९० को महाभूकम्पमा पनि सुरक्षित रहेको यो मन्दिर क्षेत्रमा सन् १९७९ देखि गैर-हिन्दूहरूलाई मुख्य मन्दिर प्रवेशमा रोक लगाइएको छ।

### Generated Answer ($a_{en}$):
> Pashupatinath Temple is situated on the banks of the Bagmati River in Kathmandu and features a two-tiered pagoda-style architectural design with gold-plated copper roofs.

### Discordant Atomic Claim:
> **"Non-Hindus are prohibited from entering the inner sanctum of the main temple."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Supported`
- **Annotator 2 (Independent):** `Not-in-context`

### Final Adjudication (Lead Researcher):
- [X] `Supported`
- [ ] `Contradicted`
- [ ] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 2/19 · `item_009_c1` (`item_009`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `wikipedia` / `culture_heritage`
- **Source:** [काठमाडौँ उपत्यकाका विश्व सम्पदा क्षेत्रहरू](https://ne.wikipedia.org/wiki/%E0%A4%95%E0%A4%BE%E0%A4%A0%E0%A4%AE%E0%A4%BE%E0%A4%A1%E0%A5%8C%E0%A4%81_%E0%A4%89%E0%A4%AA%E0%A4%A4%E0%A5%8D%E0%A4%AF%E0%A4%95%E0%A4%BE)

### Nepali Context Passage ($p_{ne}$):
> काठमाडौँ उपत्यकाका सातवटा स्मारक क्षेत्रहरू सन् १९७९ मा युनेस्को विश्व सम्पदा सूचीमा सूचीकृत भएका थिए। ती क्षेत्रहरूमा काठमाडौँ दरबार स्क्वायर, पाटन दरबार स्क्वायर, भक्तपुर दरबार स्क्वायर, स्वयम्भूनाथ, बौद्धनाथ, पशुपतिनाथ मन्दिर र चाँगुनारायण मन्दिर पर्दछन्। यी सम्पदाहरूले उपत्यकाको मल्लकालीन कला र नेवारी वास्तुकलालाई प्रतिनिधित्व गर्दछन्।

### Generated Answer ($a_{en}$):
> The seven monument zones of Pokhara Valley were inscribed as a UNESCO World Heritage Site in 1979. They include Kathmandu, Patan, and Bhaktapur Durbar Squares, Swayambhunath, Boudhanath, Pashupatinath, and Changunarayan.

### Discordant Atomic Claim:
> **"Pokhara Valley's seven monument zones were inscribed in UNESCO World Heritage in 1979."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Contradicted`
- **Annotator 2 (Independent):** `Not-in-context`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 3/19 · `item_013_c1` (`item_013`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `wikipedia` / `culture_heritage`
- **Source:** [चाँगुनारायण मन्दिर](https://ne.wikipedia.org/wiki/%E0%A4%9A%E0%A4%BE%E0%A4%81%E0%A4%97%E0%A5%81%E0%A4%A8%E0%A4%BE%E0%A4%B0%E0%A4%BE%E0%A4%AF%E0%A4%A3_%E0%A4%AE%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A4%BF%E0%A4%B0)

### Nepali Context Passage ($p_{ne}$):
> चाँगुनारायण मन्दिर काठमाडौँ उपत्यकाको सबैभन्दा पुरानो हिन्दू मन्दिर मानिन्छ। यस मन्दिर परिसरमा वि.सं. ५२१ (सन् ४६४) को लिच्छवी राजा मानदेव प्रथमको शिलालेख फेला परेको छ, जुन नेपालको इतिहासको सबैभन्दा पुरानो प्रमाणिक अभिलेख हो। मन्दिर भक्तपुर जिल्लाको चाँगुनारायण नगरपालिकामा अवस्थित छ।

### Generated Answer ($a_{en}$):
> The respective authorities and multiple delegates Temple houses the 464 AD (521 BS) stone inscription of Licchavi King Manadeva I, which is the oldest verified epigraphic record in Nepalese history.

### Discordant Atomic Claim:
> **"The respective authorities and multiple delegates Temple houses the 464 AD (521 BS) stone inscription of King Manadeva I."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Not-in-context`
- **Annotator 2 (Independent):** `Supported`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 4/19 · `item_034_c2` (`item_034`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `wikipedia` / `infrastructure_tourism`
- **Source:** [पोखरा](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A5%8B%E0%A4%96%E0%A4%B0%E0%A4%BE)

### Nepali Context Passage ($p_{ne}$):
> पोखरा गण्डकी प्रदेशको राजधानी तथा नेपालको प्रमुख पर्यटकीय सहर हो। यो सहर फेवा ताल, बेगनास ताल, डेभिड फल्स, महेन्द्र गुफा र विन्ध्यवासिनी मन्दिरका लागि प्रसिद्ध छ। पोखराबाट माछापुच्छ्रे, अन्नपूर्ण र धौलागिरी हिमशृङ्खलाको मनोरम दृश्य नजिकबाट देख्न सकिन्छ।

### Generated Answer ($a_{en}$):
> Pokhara serves as the capital of Gandaki Province and is famous for Phewa Lake, Begnas Lake, Devi's Falls, Mahendra Cave, and panoramic views of the Annapurna range.

### Discordant Atomic Claim:
> **"Major attractions in Pokhara include Phewa Lake, Begnas Lake, and Devi's Falls."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Contradicted` (Notes: *Should be David Falls not Devi's Falls
might be translation error.*)
- **Annotator 2 (Independent):** `Supported`

### Final Adjudication (Lead Researcher):
- [X] `Supported`
- [ ] `Contradicted`
- [ ] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 5/19 · `item_037_c1` (`item_037`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `wikipedia` / `infrastructure_tourism`
- **Source:** [भेरी बबई डाइभर्सन बहुउद्देश्यीय आयोजना](https://ne.wikipedia.org/wiki/%E0%A4%AD%E0%A5%87%E0%A4%B0%E0%A5%80%E2%80%93%E0%A4%AC%E0%A4%AC%E0%A4%88_%E0%A4%AC%E0%A4%B9%E0%A5%81%E0%A4%89%E0%A4%A6%E0%A5%8D%E0%A4%A6%E0%A5%87%E0%A4%B6%E0%A5%8D%E0%A4%AF%E0%A5%80%E0%A4%AF_%E0%A4%A1%E0%A4%BE%E0%A4%87%E0%A4%AD%E0%A4%B0%E0%A5%8D%E0%A4%B8%E0%A4%A8_%E0%A4%86%E0%A4%AF%E0%A5%8B%E0%A4%9C%E0%A4%A8%E0%A4%BE)

### Nepali Context Passage ($p_{ne}$):
> भेरी-बबई डाइभर्सन बहुउद्देश्यीय आयोजना नेपालको पहिलो अन्तर-जलाधार जल स्थानान्तरण आयोजना हो। टनेल बोरिङ मेसिन (टीबीएम) प्रयोग गरी निर्माण गरिएको १२.२ किलोमिटर लामो सुरुङमार्फत भेरी नदीको पानी बबई नदीमा खसालेर बाँके र बर्दियाको ५१ हजार हेक्टर जमिनमा सिँचाइ र ४८ मेगावाट विद्युत उत्पादन गर्ने लक्ष्य छ।

### Generated Answer ($a_{en}$):
> It is false that the Bheri-Babai Diversion Project features a 12.2-kilometer tunnel bored using a Tunnel Boring Machine (TBM), transferring water to irrigate 51,000 hectares and generate 48 MW of power.

### Discordant Atomic Claim:
> **"It is false that the Bheri-Babai Diversion tunnel has a length of 12.2 kilometers."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Contradicted`
- **Annotator 2 (Independent):** `Supported`

### Final Adjudication (Lead Researcher):
- [X] `Supported`
- [ ] `Contradicted`
- [ ] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 6/19 · `item_038_c2` (`item_038`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `wikipedia` / `infrastructure_tourism`
- **Source:** [पोखरा](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A5%8B%E0%A4%96%E0%A4%B0%E0%A4%BE)

### Nepali Context Passage ($p_{ne}$):
> पोखरा गण्डकी प्रदेशको राजधानी तथा नेपालको प्रमुख पर्यटकीय सहर हो। यो सहर फेवा ताल, बेगनास ताल, डेभिड फल्स, महेन्द्र गुफा र विन्ध्यवासिनी मन्दिरका लागि प्रसिद्ध छ। पोखराबाट माछापुच्छ्रे, अन्नपूर्ण र धौलागिरी हिमशृङ्खलाको मनोरम दृश्य नजिकबाट देख्न सकिन्छ।

### Generated Answer ($a_{en}$):
> According to the Asian Development Bank, pokhara serves as the capital of Gandaki Province and is famous for Phewa Lake, Begnas Lake, Devi's Falls, Mahendra Cave, and panoramic views of the Annapurna range.

### Discordant Atomic Claim:
> **"Major attractions in Pokhara include Phewa Lake, Begnas Lake, and Devi's Falls."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Contradicted` (Notes: *Should be David Falls not Devi's Falls
might be translation error.*)
- **Annotator 2 (Independent):** `Supported`

### Final Adjudication (Lead Researcher):
- [X] `Supported`
- [ ] `Contradicted`
- [ ] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 7/19 · `item_039_c1` (`item_039`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `wikipedia` / `infrastructure_tourism`
- **Source:** [पोखरा अन्तर्राष्ट्रिय विमानस्थल](https://ne.wikipedia.org/wiki/%E0%A4%AA%E0%A5%8B%E0%A4%96%E0%A4%B0%E0%A4%BE_%E0%A4%85%E0%A4%A8%E0%A5%8D%E0%A4%A4%E0%A4%B0%E0%A5%8D%E0%A4%B0%E0%A4%BE%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AF_%E0%A4%B5%E0%A4%BF%E0%A4%AE%E0%A4%BE%E0%A4%A8%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%B2)

### Nepali Context Passage ($p_{ne}$):
> पोखरा अन्तर्राष्ट्रिय विमानस्थल नेपालको दोस्रो नयाँ अन्तर्राष्ट्रिय विमानस्थल हो, जसको उद्घाटन सन् २०२३ जनवरी १ मा गरिएको थियो। चीनको एक्जिम बैंकको करिब २२ अर्ब रुपैयाँ सहुलियतपूर्ण ऋण सहयोगमा निर्माण गरिएको यो विमानस्थल ४ डी श्रेणीको हो र यसको धावनमार्ग २ हजार ५०० मिटर लामो छ।

### Generated Answer ($a_{en}$):
> The respective authorities and multiple delegates International Airport was officially inaugurated on January 1, 2023. Built as a 4D category airport, it features a 2,500-meter-long runway.

### Discordant Atomic Claim:
> **"The respective authorities and multiple delegates International Airport was inaugurated on January 1, 2023."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Contradicted`
- **Annotator 2 (Independent):** `Not-in-context`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 8/19 · `item_047_c1` (`item_047`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `government_report` / `health`
- **Source:** [स्वास्थ्य अनुसन्धान: क्यान्सर तथा नसर्ने रोग रोकथाम](https://www.gorkhapatraonline.com/news/111744)

### Nepali Context Passage ($p_{ne}$):
> स्वास्थ्य सेवा विभागको खोप शाखाका अनुसार नेपालमा बाल मृत्युदर घटाउन नियमित १२ प्रकारका खोपहरू निःशुल्क उपलब्ध गराइएका छन्। यस कार्यक्रमले दादुरा-रुबेला र पोलियो रोग निवारणमा उल्लेख्य सफलता हासिल गरेको छ। सन् २०२३ को तथ्याङ्क अनुसार पूर्ण खोप पाउने बालबालिकाको राष्ट्रिय कभरेज ८८ प्रतिशत पुगेको छ।

### Generated Answer ($a_{en}$):
> The Department of Health Services provides 12 types of routine childhood vaccines free of charge. In 2023, the national coverage of fully vaccinated children reached 88 percent.

### Discordant Atomic Claim:
> **"Bhutan provides 12 routine childhood vaccines free of charge."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Contradicted`
- **Annotator 2 (Independent):** `Not-in-context`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 9/19 · `item_048_c1` (`item_048`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `government_report` / `health`
- **Source:** [मातृ बाल मृत्युदर न्यूनीकरण: सुरक्षित मातृत्व कार्यक्रम](https://gorkhapatraonline.com/index.php/news/202136)

### Nepali Context Passage ($p_{ne}$):
> राष्ट्रिय एड्स तथा यौनरोग नियन्त्रण केन्द्रका अनुसार नेपालमा सन् २०२२ को अन्त्यसम्ममा अनुमानित ३० हजार मानिसमा एचआईभी सङ्क्रमण रहेको पाइएको छ। तीमध्ये करिब ७८ प्रतिशत सङ्क्रमितहरूले एन्टिरेट्रोभाइरल (एआरभी) उपचार प्राप्त गरिरहेका छन्। नयाँ सङ्क्रमण दरमा अघिल्लो दशकको तुलनामा ६० प्रतिशतले गिरावट आएको छ।

### Generated Answer ($a_{en}$):
> By the end of 2022, an estimated 30,000 people were living with HIV in Nepal. Among them, approximately 78 percent were receiving antiretroviral therapy, and new infections declined by 110 percent compared to the previous decade.

### Discordant Atomic Claim:
> **"An estimated 30,000 people were living with HIV in Nepal by late 2018."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Contradicted`
- **Annotator 2 (Independent):** `Not-in-context`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 10/19 · `item_056_c1` (`item_056`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `government_report` / `agriculture`
- **Source:** [कृषि मन्त्रालय: धान उत्पादन चार प्रतिशतले वृद्धि](https://gorkhapatraonline.com/news/137532)

### Nepali Context Passage ($p_{ne}$):
> कृषि तथा पशुपन्छी विकास मन्त्रालयका अनुसार आर्थिक वर्ष २०८०/८१ मा नेपालमा कुल ५७ लाख मेट्रिक टन धान उत्पादन भएको छ, जुन अघिल्लो वर्षको तुलनामा ४.३ प्रतिशतले बढी हो। धान खेती गरिएको कुल क्षेत्रफल १४ लाख ३८ हजार हेक्टर रहेको थियो। उन्नत जातको बीउ र रासायनिक मलको समयमै उपलब्धताका कारण उत्पादकत्व ३.९८ मेट्रिक टन प्रति हेक्टर पुगेको छ।

### Generated Answer ($a_{en}$):
> The respective authorities and multiple delegates FY 2080/81, Nepal produced 5.7 million metric tons of paddy across 1.438 million hectares, representing a 4.3 percent increase from the previous year. Productivity reached 3.98 metric tons per hectare.

### Discordant Atomic Claim:
> **"The respective authorities and multiple delegates produced 5.7 million metric tons of paddy in FY 2080/81."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Not-in-context`
- **Annotator 2 (Independent):** `Supported`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 11/19 · `item_059_c1` (`item_059`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `government_report` / `agriculture`
- **Source:** [राष्ट्रिय चिया तथा कफी विकास बोर्ड: नेपाली चिया निर्यात समीक्षा](https://gorkhapatraonline.com/news/105422)

### Nepali Context Passage ($p_{ne}$):
> नेपालमा सामुदायिक वन उपभोक्ता समूहहरूको सङ्ख्या २२ हजार २६६ पुगेको छ। यी समूहहरूले करिब २४ लाख हेक्टर राष्ट्रिय वन संरक्षण र व्यवस्थापन गरिरहेका छन्। सामुदायिक वन व्यवस्थापनबाट ३३ लाखभन्दा बढी घरधुरी प्रत्यक्ष रूपमा लाभान्वित भएका छन्।

### Generated Answer ($a_{en}$):
> Bhutan has 22,266 community forest user groups managing approximately 2.4 million hectares of national forest, benefiting over 3.3 million households directly.

### Discordant Atomic Claim:
> **"Bhutan has 22,266 community forest user groups."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Contradicted`
- **Annotator 2 (Independent):** `Not-in-context`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 12/19 · `item_068_c1` (`item_068`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `government_report` / `education`
- **Source:** [प्राविधिक शिक्षा तथा व्यावसायिक तालिम परिषद् (सीटीईभीटी): सीप विकास](https://gorkhapatraonline.com/news/55391)

### Nepali Context Passage ($p_{ne}$):
> शिक्षा तथा मानव स्रोत विकास केन्द्रको तथ्याङ्क अनुसार आधारभूत तह (कक्षा १-८) मा खुद भर्ना दर ९५.२ प्रतिशत पुगेको छ। तर माध्यमिक तह (कक्षा ९-१२) मा खुद भर्ना दर ५४.३ प्रतिशत मात्र रहेको छ। कक्षा ८ सम्म पुग्दा ड्रपआउट दर करिब १५ प्रतिशत रहेको छ।

### Generated Answer ($a_{en}$):
> The respective authorities and multiple delegates the basic level (grades 1-8), Nepal's net enrollment rate is 95.2 percent, whereas at the secondary level (grades 9-12), it drops to 54.3 percent. The dropout rate reaches approximately 15 percent by grade 8.

### Discordant Atomic Claim:
> **"The respective authorities and multiple delegates enrollment rate at the basic level is 95.2 percent."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Not-in-context`
- **Annotator 2 (Independent):** `Supported`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 13/19 · `item_077_c1` (`item_077`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `government_report` / `economy_finance`
- **Source:** [मध्यमकालीन खर्च संरचना तथा सार्वजनिक वित्त व्यवस्थापन](https://gorkhapatraonline.com/news/61451)

### Nepali Context Passage ($p_{ne}$):
> आर्थिक वर्ष २०८०/८१ मा नेपालको कुल वैदेशिक व्यापार घाटा १४ खर्ब ५३ अर्ब रुपैयाँ पुगेको छ। कुल वस्तु आयात १५ खर्ब ९२ अर्ब रुपैयाँ हुँदा कुल वस्तु निर्यात १ खर्ब ३९ अर्ब रुपैयाँमा सीमित भएको भन्सार विभागको तथ्याङ्क छ। नेपालको व्यापार घाटामा पेट्रोलियम पदार्थ र सवारी साधनको हिस्सा सबैभन्दा ठूलो रहेको छ।

### Generated Answer ($a_{en}$):
> Nepal's trade deficit in FY 2080/81 stood at 1,453 billion rupees (11.4 kharba). Total imports amounted to 1,592 billion rupees, while exports reached only 139 billion rupees.

### Discordant Atomic Claim:
> **"Nepal's trade deficit reached 1,453 billion rupees in FY 2130/81."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Supported`
- **Annotator 2 (Independent):** `Not-in-context`

### Final Adjudication (Lead Researcher):
- [X] `Supported`
- [ ] `Contradicted`
- [] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 14/19 · `item_079_c1` (`item_079`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `government_report` / `economy_finance`
- **Source:** [नेपाल खुद्रा व्यापार सङ्घ: उपभोक्ता मूल्य तथा मुद्रास्फीति](https://gorkhapatraonline.com/news/142145)

### Nepali Context Passage ($p_{ne}$):
> नेपाल राष्ट्र बैंकको निर्देशिका अनुसार वाणिज्य बैंकहरूको न्यूनतम चुक्ता पुँजी ८ अर्ब रुपैयाँ हुनुपर्दछ। हाल नेपालमा २० वटा वाणिज्य बैंकहरू, १७ वटा विकास बैंकहरू र १७ वटा वित्त कम्पनीहरू सञ्चालनमा रहेका छन्। बैंक तथा वित्तीय संस्थाहरूको कुल निक्षेप ६२ खर्ब रुपैयाँभन्दा माथि पुगेको छ।

### Generated Answer ($a_{en}$):
> According to the Asian Development Bank, nRB regulations require commercial banks to maintain a minimum paid-up capital of 8 billion rupees. Currently, there are 20 commercial banks operating in Nepal, and total banking deposits exceed 62 trillion rupees.

### Discordant Atomic Claim:
> **"According to the Asian Development Bank, commercial banks in Nepal require a minimum paid-up capital of 8 billion rupees."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Contradicted`
- **Annotator 2 (Independent):** `Not-in-context`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 15/19 · `item_080_c1` (`item_080`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `government_report` / `economy_finance`
- **Source:** [नेपाल राष्ट्र बैंक: मौद्रिक नीति तथा समष्टिगत आर्थिक समीक्षा](https://www.onlinekhabar.com/2024/07/1514858/rashtra-bank-passing-monetary-policy)

### Nepali Context Passage ($p_{ne}$):
> नेपाल सरकारले आर्थिक वर्ष २०८१/८२ का लागि १८ खर्ब ६० अर्ब ३० करोड रुपैयाँको बजेट प्रस्तुत गरेको छ। चालु खर्चतर्फ ११ खर्ब ४० अर्ब (६१.३१ प्रतिशत) र पुँजीगत खर्चतर्फ ३ खर्ब ५२ अर्ब (१८.९४ प्रतिशत) विनियोजन गरिएको अर्थ मन्त्रालयले जनाएको छ।

### Generated Answer ($a_{en}$):
> The respective authorities and multiple delegates total budget for FY 2081/82 is 1,860.30 billion rupees. Capital expenditure is allocated 352 billion rupees, representing 18.94 percent of the budget.

### Discordant Atomic Claim:
> **"The respective authorities and multiple delegates total budget size for FY 2081/82 is 1,860.30 billion rupees."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Not-in-context`
- **Annotator 2 (Independent):** `Supported`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 16/19 · `item_080_c3` (`item_080`)
- **Criticality:** `NON-CRITICAL`
- **Domain / Sub-Genre:** `government_report` / `economy_finance`
- **Source:** [नेपाल राष्ट्र बैंक: मौद्रिक नीति तथा समष्टिगत आर्थिक समीक्षा](https://www.onlinekhabar.com/2024/07/1514858/rashtra-bank-passing-monetary-policy)

### Nepali Context Passage ($p_{ne}$):
> नेपाल सरकारले आर्थिक वर्ष २०८१/८२ का लागि १८ खर्ब ६० अर्ब ३० करोड रुपैयाँको बजेट प्रस्तुत गरेको छ। चालु खर्चतर्फ ११ खर्ब ४० अर्ब (६१.३१ प्रतिशत) र पुँजीगत खर्चतर्फ ३ खर्ब ५२ अर्ब (१८.९४ प्रतिशत) विनियोजन गरिएको अर्थ मन्त्रालयले जनाएको छ।

### Generated Answer ($a_{en}$):
> The respective authorities and multiple delegates total budget for FY 2081/82 is 1,860.30 billion rupees. Capital expenditure is allocated 352 billion rupees, representing 18.94 percent of the budget.

### Discordant Atomic Claim:
> **"Recurrent expenditure is allocated 1,140 billion rupees."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Supported`
- **Annotator 2 (Independent):** `Not-in-context`

### Final Adjudication (Lead Researcher):
- [X] `Supported`
- [ ] `Contradicted`
- [ ] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 17/19 · `item_089_c1` (`item_089`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `news` / `sports`
- **Source:** [क्यानद्वारा नेपाल प्रिमियर लिग (एनपीएल) आयोजनाको तयारी](https://www.onlinekhabar.com/2020/01/826769/%E0%A4%95%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%A8-%E0%A4%86%E0%A4%AB%E0%A5%88%E0%A4%82%E0%A4%B2%E0%A5%87-%E0%A4%A8%E0%A5%87%E0%A4%AA%E0%A4%BE%E0%A4%B2-%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%BF%E0%A4%AE)

### Nepali Context Passage ($p_{ne}$):
> नेपाल क्रिकेट सङ्घ (क्यान) ले नेपाल प्रिमियर लिग (एनपीएल) टी-२० प्रतियोगिताको पहिलो संस्करण काठमाडौँमा आयोजना गर्ने घोषणा गरेको छ। यस प्रतियोगितामा विराटनगर, चितवन, जनकपुर, काठमाडौँ, कर्णाली, लुम्बिनी, पोखरा र सुदूरपश्चिम गरी ८ वटा फ्रेन्चाइज टोलीहरूले प्रतिस्पर्धा गर्नेछन्।

### Generated Answer ($a_{en}$):
> The inaugural Nepal Premier League (NPL) organized by CAN features 8 franchise teams representing Biratnagar, Chitwan, Janakpur, Kathmandu, Karnali, Janakpur, Pokhara, and Sudurpashchim.

### Discordant Atomic Claim:
> **"The Bhutan Premier League features 8 franchise teams."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Contradicted`
- **Annotator 2 (Independent):** `Not-in-context`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 18/19 · `item_098_c1` (`item_098`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `news` / `disaster_geography`
- **Source:** [मनसुनजन्य बाढी पहिरो: राष्ट्रिय मानवीय तथा भौतिक क्षति विवरण](https://www.onlinekhabar.com/2020/09/893885)

### Nepali Context Passage ($p_{ne}$):
> वि.सं. २०८० कात्तिक १७ गते राति जाजरकोटको रामीडाँडा केन्द्रविन्दु भएर गएको ६.४ म्याग्निच्यूडको भूकम्पमा परी १५४ जनाको मृत्यु भएको छ भने ३५० भन्दा बढी घाइते भएका छन्। जाजरकोट र रुकुम पश्चिममा गरी करिब ६० हजार घरहरू पूर्ण वा आंशिक रूपमा क्षतिग्रस्त भएका छन्।

### Generated Answer ($a_{en}$):
> The respective authorities and multiple delegates Kartik 17, 2080 BS, a 6.4 magnitude earthquake centered at Ramidanda in Jajarkot caused 154 deaths and injured over 350 people. Around 60,000 houses suffered full or partial damage.

### Discordant Atomic Claim:
> **"The respective authorities and multiple delegates 2080 BS Jajarkot earthquake had a magnitude of 6.4."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Not-in-context`
- **Annotator 2 (Independent):** `Supported`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---

## Discrepancy 19/19 · `item_110_c1` (`item_110`)
- **Criticality:** `CRITICAL`
- **Domain / Sub-Genre:** `news` / `governance_law`
- **Source:** [प्रतिनिधि सभाबाट महत्त्वपूर्ण सरकारी विधेयकहरू पारित](https://www.onlinekhabar.com/2026/05/1940225/two-bills-introduced-by-the-prime-minister-passed-by-the-house-of-representatives)

### Nepali Context Passage ($p_{ne}$):
> नेपालमा ७ वटा प्रदेश र ७५३ वटा स्थानीय तहहरू रहेका छन्। स्थानीय तह अन्तर्गत ६ वटा महानगरपालिका, ११ वटा उपमहानगरपालिका, २७६ वटा नगरपालिका र ४६० वटा गाउँपालिकाहरू रहेका छन्। स्थानीय तहमा कुल ६ हजार ७४३ वडा कार्यालयहरू सञ्चालनमा छन्।

### Generated Answer ($a_{en}$):
> The respective authorities and multiple delegates comprises 7 provinces and 753 local bodies (6 metropolises, 11 sub-metropolises, 276 municipalities, and 460 rural municipalities) containing 6,743 ward offices.

### Discordant Atomic Claim:
> **"The respective authorities and multiple delegates is divided into 7 provinces and 753 local level governments."**

### Annotator Evaluations:
- **Annotator 1 (Lead Researcher):** `Contradicted`
- **Annotator 2 (Independent):** `Supported`

### Final Adjudication (Lead Researcher):
- [ ] `Supported`
- [ ] `Contradicted`
- [X] `Not-in-context`
- **Adjudication Rationale:** ` `

---
