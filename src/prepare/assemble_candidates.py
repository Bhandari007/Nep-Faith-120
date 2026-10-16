"""NepFaith-120: Stratified Candidate Evaluation Set Assembler (120 Items)

Assembles the 120 candidate evaluation items adhering strictly to:
- docs/PREREGISTRATION.md Section 4
- docs/adr/0003-topical-taxonomy-and-subgenre-stratification.md
- docs/RUBRIC_V1.md

Stratification:
- Macro-Strata: 40 Wikipedia, 40 Government Reports, 40 News.
- 10 Approved Topical Sub-genres:
  * Health (10)
  * Agriculture (10)
  * Education (10)
  * Economy & Finance (10)
  * Disaster & Geography (10)
  * Governance & Law (10)
  * Sports (12)
  * Culture & Heritage (15)
  * Biodiversity & Parks (15)
  * Infrastructure & Tourism (18)
- Provenance: Exactly 60 Natural / 60 Perturbed (balanced across 7 typed edits).
- Invariant: Zero writes to data/raw/labels/. Output strictly to data/interim/preannotations/.
"""

import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

from src.prepare.schema import (
    Domain,
    Provenance,
    PerturbationType,
    RetrievalCondition,
    AtomicClaim,
    EvaluationItem,
)
from src.prepare.perturb import apply_perturbation

logger = logging.getLogger("CandidateAssembler")

# Curated seed bank across the 10 approved domains
# Each entry contains authentic Nepali passages, queries, answers, and decomposed atomic claims
PASSAGE_SEEDS: List[Dict[str, Any]] = [
    # 1. Health & Public Medicine (10 items: 5 natural, 5 perturbed)
    {
        "sub_genre": "health",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "नेपाल स्वास्थ्य अनुसन्धान परिषद्का अनुसार नेपालमा नसर्ने रोगहरूको प्रकोप तीव्र रूपमा बढ्दै गएको छ। कुल मृत्युमध्ये करिब ७१ प्रतिशत नसर्ने रोगहरू (मुटुरोग, क्यान्सर, मधुमेह र श्वासप्रश्वास सम्बन्धी रोग) का कारण हुने गरेको छ। यसैगरी उच्च रक्तचापका बिरामीहरूको सङ्ख्या कुल वयस्क जनसङ्ख्याको ३० प्रतिशतभन्दा बढी पुगेको स्वास्थ्य मन्त्रालयको पछिल्लो सर्वेक्षणले देखाएको छ।",
        "query_en": "What percentage of total deaths in Nepal are caused by non-communicable diseases, and what is the prevalence of hypertension among adults?",
        "base_answer": "According to the Nepal Health Research Council, non-communicable diseases account for approximately 71 percent of all deaths in Nepal. Furthermore, recent Ministry of Health surveys show that over 30 percent of the adult population suffers from hypertension.",
        "claims": [
            {"text": "Non-communicable diseases account for approximately 71 percent of all deaths in Nepal.", "critical": True},
            {"text": "Over 30 percent of the adult population in Nepal suffers from hypertension.", "critical": True},
            {"text": "The findings are reported by the Nepal Health Research Council and Ministry of Health.", "critical": False},
        ],
    },
    {
        "sub_genre": "health",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "स्वास्थ्य सेवा विभागको खोप शाखाका अनुसार नेपालमा बाल मृत्युदर घटाउन नियमित १२ प्रकारका खोपहरू निःशुल्क उपलब्ध गराइएका छन्। यस कार्यक्रमले दादुरा-रुबेला र पोलियो रोग निवारणमा उल्लेख्य सफलता हासिल गरेको छ। सन् २०२३ को तथ्याङ्क अनुसार पूर्ण खोप पाउने बालबालिकाको राष्ट्रिय कभरेज ८८ प्रतिशत पुगेको छ।",
        "query_en": "How many free routine vaccines are provided in Nepal for children, and what was the national full vaccination coverage in 2023?",
        "base_answer": "The Department of Health Services provides 12 types of routine childhood vaccines free of charge. In 2023, the national coverage of fully vaccinated children reached 88 percent.",
        "claims": [
            {"text": "Nepal provides 12 routine childhood vaccines free of charge.", "critical": True},
            {"text": "National coverage of fully vaccinated children reached 88 percent in 2023.", "critical": True},
            {"text": "The routine immunization program has contributed to reducing child mortality.", "critical": False},
        ],
    },
    {
        "sub_genre": "health",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "राष्ट्रिय एड्स तथा यौनरोग नियन्त्रण केन्द्रका अनुसार नेपालमा सन् २०२२ को अन्त्यसम्ममा अनुमानित ३० हजार मानिसमा एचआईभी सङ्क्रमण रहेको पाइएको छ। तीमध्ये करिब ७८ प्रतिशत सङ्क्रमितहरूले एन्टिरेट्रोभाइरल (एआरभी) उपचार प्राप्त गरिरहेका छन्। नयाँ सङ्क्रमण दरमा अघिल्लो दशकको तुलनामा ६० प्रतिशतले गिरावट आएको छ।",
        "query_en": "What was the estimated number of people living with HIV in Nepal by end of 2022, and what percentage received antiretroviral treatment?",
        "base_answer": "By the end of 2022, an estimated 30,000 people were living with HIV in Nepal. Among them, approximately 78 percent were receiving antiretroviral therapy, and new infections declined by 60 percent compared to the previous decade.",
        "claims": [
            {"text": "An estimated 30,000 people were living with HIV in Nepal by late 2022.", "critical": True},
            {"text": "Approximately 78 percent of HIV-infected individuals were receiving antiretroviral treatment.", "critical": True},
            {"text": "New HIV infections in Nepal declined by 60 percent compared to the previous decade.", "critical": False},
        ],
    },
    {
        "sub_genre": "health",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "नेपाल जनसाङ्ख्यिक तथा स्वास्थ्य सर्वेक्षण (एनडीएचएस २०२२) अनुसार पाँच वर्ष मुनिका बालबालिकामा पुड्कोपनको दर २५ प्रतिशतमा झरेको छ। सन् २००१ मा यो दर ५७ प्रतिशत रहेको थियो। त्यस्तै कम तौल भएका बालबालिकाको सङ्ख्या १९ प्रतिशत र ख्याउटेपनको दर ८ प्रतिशत रहेको प्रतिवेदनमा उल्लेख छ।",
        "query_en": "According to NDHS 2022, what is the prevalence of stunting in children under five in Nepal?",
        "base_answer": "According to the Nepal Demographic and Health Survey 2022, stunting among children under five dropped to 25 percent from 57 percent in 2001. Additionally, 19 percent are underweight and 8 percent suffer from wasting.",
        "claims": [
            {"text": "Stunting among children under five dropped to 25 percent according to NDHS 2022.", "critical": True},
            {"text": "The stunting rate in children under five was 57 percent in 2001.", "critical": False},
            {"text": "The NDHS 2022 recorded an underweight rate of 19 percent and wasting rate of 8 percent.", "critical": True},
        ],
    },
    {
        "sub_genre": "health",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "काठमाडौँ उपत्यकामा पछिल्लो वर्ष डेंगु सङ्क्रमणका कारण १५ जनाको मृत्यु भएको छ भने २० हजारभन्दा बढी व्यक्तिहरू प्रभावित भएका छन्। इपिडिमियोलोजी तथा रोग नियन्त्रण महाशाखा (ईडीसीडी) ले लामखुट्टेको लार्भा नष्ट गर्ने 'खोज र नष्ट गर' अभियान ७७ वटै जिल्लामा सञ्चालन गरिएको जानकारी दिएको छ।",
        "query_en": "How many dengue deaths occurred in Kathmandu Valley in the recent outbreak and what campaign was launched?",
        "base_answer": "In the recent outbreak in Kathmandu Valley, 15 people died and over 20,000 were infected with dengue. In response, EDCD conducted a search-and-destroy campaign to eliminate mosquito larvae across all 77 districts.",
        "claims": [
            {"text": "15 people died of dengue in Kathmandu Valley during the recent outbreak.", "critical": True},
            {"text": "Over 20,000 people in Kathmandu Valley were infected with dengue.", "critical": True},
            {"text": "EDCD conducted a search-and-destroy campaign across all 77 districts.", "critical": False},
        ],
    },

    # 2. Agriculture, Forestry & Livestock (10 items: 5 natural, 5 perturbed)
    {
        "sub_genre": "agriculture",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "कृषि तथा पशुपन्छी विकास मन्त्रालयका अनुसार आर्थिक वर्ष २०८०/८१ मा नेपालमा कुल ५७ लाख मेट्रिक टन धान उत्पादन भएको छ, जुन अघिल्लो वर्षको तुलनामा ४.३ प्रतिशतले बढी हो। धान खेती गरिएको कुल क्षेत्रफल १४ लाख ३८ हजार हेक्टर रहेको थियो। उन्नत जातको बीउ र रासायनिक मलको समयमै उपलब्धताका कारण उत्पादकत्व ३.९८ मेट्रिक टन प्रति हेक्टर पुगेको छ।",
        "query_en": "What was the total paddy production in Nepal in FY 2080/81 and what productivity was achieved?",
        "base_answer": "In FY 2080/81, Nepal produced 5.7 million metric tons of paddy across 1.438 million hectares, representing a 4.3 percent increase from the previous year. Productivity reached 3.98 metric tons per hectare.",
        "claims": [
            {"text": "Nepal produced 5.7 million metric tons of paddy in FY 2080/81.", "critical": True},
            {"text": "Paddy was cultivated across 1.438 million hectares in FY 2080/81.", "critical": False},
            {"text": "Paddy productivity reached 3.98 metric tons per hectare.", "critical": True},
        ],
    },
    {
        "sub_genre": "agriculture",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "राष्ट्रिय कृषि गणना २०७८ अनुसार नेपालमा कृषक परिवारको सङ्ख्या ४१ लाख ३० हजार पुगेको छ। कुल खेतीयोग्य जमिनमध्ये ५४.५ प्रतिशत जमिनमा मात्र सिँचाइ सुविधा पुगेको छ। त्यसमध्ये बाह्रै महिना सिँचाइ सुविधा उपलब्ध भएको जमिन कुल सिञ्चित जमिनको ३९ प्रतिशत मात्र रहेको छ।",
        "query_en": "According to the National Agricultural Census 2078, what is the number of farming households and irrigation coverage in Nepal?",
        "base_answer": "The National Agricultural Census 2078 indicates there are 4.13 million farming households in Nepal. Irrigation facilities reach only 54.5 percent of cultivable land, with year-round irrigation available on just 39 percent of irrigated land.",
        "claims": [
            {"text": "There are 4.13 million farming households in Nepal according to Census 2078.", "critical": True},
            {"text": "Irrigation facilities cover 54.5 percent of cultivable land.", "critical": True},
            {"text": "Year-round irrigation is accessible on 39 percent of irrigated agricultural land.", "critical": False},
        ],
    },
    {
        "sub_genre": "agriculture",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "नेपालबाट भारततर्फ अलैँची र अदुवा निर्यातमा उल्लेख्य वृद्धि भएको छ। व्यापार तथा निकासी प्रवर्द्धन केन्द्रका अनुसार गत वर्ष करिब ८ अर्ब रुपैयाँ बराबरको ठूलो अलैँची निर्यात भएको थियो। ताप्लेजुङ, पाँचथर र इलाम जिल्ला नेपालको प्रमुख अलैँची उत्पादन क्षेत्र हुन्।",
        "query_en": "What was the export value of large cardamom from Nepal and which districts are the primary production zones?",
        "base_answer": "Nepal exported approximately 8 billion rupees worth of large cardamom last year. The primary production areas are Taplejung, Panchthar, and Ilam districts.",
        "claims": [
            {"text": "Nepal exported approximately 8 billion rupees worth of large cardamom last year.", "critical": True},
            {"text": "Taplejung, Panchthar, and Ilam are the primary cardamom-producing districts in Nepal.", "critical": True},
        ],
    },
    {
        "sub_genre": "agriculture",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "नेपालमा सामुदायिक वन उपभोक्ता समूहहरूको सङ्ख्या २२ हजार २६६ पुगेको छ। यी समूहहरूले करिब २४ लाख हेक्टर राष्ट्रिय वन संरक्षण र व्यवस्थापन गरिरहेका छन्। सामुदायिक वन व्यवस्थापनबाट ३३ लाखभन्दा बढी घरधुरी प्रत्यक्ष रूपमा लाभान्वित भएका छन्।",
        "query_en": "How many community forest user groups exist in Nepal and how much forest land do they manage?",
        "base_answer": "Nepal has 22,266 community forest user groups managing approximately 2.4 million hectares of national forest, benefiting over 3.3 million households directly.",
        "claims": [
            {"text": "Nepal has 22,266 community forest user groups.", "critical": True},
            {"text": "Community forest user groups manage approximately 2.4 million hectares of forest land.", "critical": True},
            {"text": "Over 3.3 million households benefit directly from community forestry management.", "critical": False},
        ],
    },
    {
        "sub_genre": "agriculture",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "मकै नेपालको दोस्रो प्रमुख खाद्यान्न बाली हो। आर्थिक वर्ष २०७९/८० मा नेपालमा मकैको कुल उत्पादन ३० लाख मेट्रिक टन भएको थियो। पहाडी जिल्लाहरूमा मकै खेती कुल मकै उत्पादन क्षेत्रको ७० प्रतिशतभन्दा बढी ओगटेको छ।",
        "query_en": "What is the ranking and production volume of maize in Nepal?",
        "base_answer": "Maize is Nepal's second major food crop, with total production reaching 3.0 million metric tons in FY 2079/80, where hilly districts account for over 70 percent of maize cultivation.",
        "claims": [
            {"text": "Maize is the second major food crop in Nepal.", "critical": True},
            {"text": "Total maize production reached 3.0 million metric tons in FY 2079/80.", "critical": True},
            {"text": "Hilly districts account for over 70 percent of Nepal's maize cultivation area.", "critical": False},
        ],
    },

    # 3. Education & Demographics (10 items: 5 natural, 5 perturbed)
    {
        "sub_genre": "education",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "राष्ट्रिय जनगणना २०७८ अनुसार नेपालको समग्र साक्षरता दर ७६.३ प्रतिशत पुगेको छ। पुरुष साक्षरता दर ८३.६ प्रतिशत र महिला साक्षरता दर ६९.४ प्रतिशत रहेको छ। प्रदेशगत रूपमा बागमती प्रदेशमा सबैभन्दा बढी (८२.१ प्रतिशत) र मधेश प्रदेशमा सबैभन्दा कम (६३.५ प्रतिशत) साक्षरता दर पाइएको छ।",
        "query_en": "What is the national literacy rate in Nepal according to the 2078 Census, and which province has the lowest rate?",
        "base_answer": "According to the 2078 National Census, Nepal's overall literacy rate is 76.3 percent, with male literacy at 83.6 percent and female literacy at 69.4 percent. Madhesh Province has the lowest literacy rate at 63.5 percent.",
        "claims": [
            {"text": "Nepal's overall literacy rate reached 76.3 percent in the 2078 Census.", "critical": True},
            {"text": "Male literacy is 83.6 percent and female literacy is 69.4 percent.", "critical": False},
            {"text": "Madhesh Province recorded the lowest literacy rate at 63.5 percent.", "critical": True},
        ],
    },
    {
        "sub_genre": "education",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "राष्ट्रिय परीक्षा बोर्डले सार्वजनिक गरेको वि.सं. २०८० को माध्यमिक शिक्षा परीक्षा (एसईई) को नतिजा अनुसार नियमित तर्फ सम्मिलित ४ लाख ६४ हजार ७८५ विद्यार्थीमध्ये ४७.८६ प्रतिशत मात्र उत्तीर्ण भएका छन्। नयाँ लेटर ग्रेडिङ निर्देशिका अनुसार सैद्धान्तिकतर्फ कम्तीमा ३५ प्रतिशत अंक नल्याउने विद्यार्थीलाई नन-ग्रेडेड (एनजी) मा राखिएको छ।",
        "query_en": "What was the pass rate in the 2080 SEE examination and what criterion triggers a non-graded evaluation?",
        "base_answer": "In the 2080 SEE examination, only 47.86 percent of 464,785 regular students passed. Under the new grading directive, students scoring below 35 percent in theoretical exams are classified as Non-Graded (NG).",
        "claims": [
            {"text": "Only 47.86 percent of students passed the 2080 regular SEE examination.", "critical": True},
            {"text": "A total of 464,785 regular students appeared in the 2080 SEE exam.", "critical": False},
            {"text": "Students scoring below 35 percent in theoretical exams receive a Non-Graded (NG) mark.", "critical": True},
        ],
    },
    {
        "sub_genre": "education",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "शिक्षा तथा मानव स्रोत विकास केन्द्रको तथ्याङ्क अनुसार आधारभूत तह (कक्षा १-८) मा खुद भर्ना दर ९५.२ प्रतिशत पुगेको छ। तर माध्यमिक तह (कक्षा ९-१२) मा खुद भर्ना दर ५४.३ प्रतिशत मात्र रहेको छ। कक्षा ८ सम्म पुग्दा ड्रपआउट दर करिब १५ प्रतिशत रहेको छ।",
        "query_en": "What are the net enrollment rates at basic and secondary levels in Nepal?",
        "base_answer": "At the basic level (grades 1-8), Nepal's net enrollment rate is 95.2 percent, whereas at the secondary level (grades 9-12), it drops to 54.3 percent. The dropout rate reaches approximately 15 percent by grade 8.",
        "claims": [
            {"text": "Net enrollment rate at the basic level is 95.2 percent.", "critical": True},
            {"text": "Net enrollment rate at the secondary level is 54.3 percent.", "critical": True},
            {"text": "Student dropout rate reaches roughly 15 percent by grade 8.", "critical": False},
        ],
    },
    {
        "sub_genre": "education",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "त्रिभुवन विश्वविद्यालय नेपालको सबैभन्दा पुरानो र ठूलो विश्वविद्यालय हो, जसको स्थापना वि.सं. २०१६ मा भएको थियो। त्रिवि अन्तर्गत हाल ६२ वटा आंगिक क्याम्पस र १ हजारभन्दा बढी सम्बन्धन प्राप्त क्याम्पसहरू सञ्चालनमा छन्। नेपालमा उच्च शिक्षा अध्ययन गर्ने कुल विद्यार्थीमध्ये करिब ७५ प्रतिशत त्रिविमै अध्ययनरत छन्।",
        "query_en": "When was Tribhuvan University established and what share of higher education students in Nepal does it enroll?",
        "base_answer": "Tribhuvan University was established in 2016 BS (1959 AD) and operates 62 constituent campuses along with over 1,000 affiliated colleges, enrolling around 75 percent of all higher education students in Nepal.",
        "claims": [
            {"text": "Tribhuvan University was established in 2016 BS.", "critical": True},
            {"text": "TU enrolls approximately 75 percent of all higher education students in Nepal.", "critical": True},
            {"text": "TU has 62 constituent campuses and over 1,000 affiliated colleges.", "critical": False},
        ],
    },
    {
        "sub_genre": "education",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "नेपाल सरकारले प्राविधिक तथा व्यावसायिक शिक्षा एवं तालिम परिषद् (सीटीईभीटी) मार्फत देशभरका ७५३ वटै स्थानीय तहमा प्राविधिक शिक्षा विस्तार गर्ने नीति लिएको छ। हालसम्म ६५० भन्दा बढी स्थानीय तहमा प्राविधिक धारका विद्यालयहरू स्थापना भइसकेका छन्।",
        "query_en": "How many local levels in Nepal have technical education schools established under CTEVT?",
        "base_answer": "The government aims to expand technical education across all 753 local levels through CTEVT, with technical schools already established in more than 650 local bodies.",
        "claims": [
            {"text": "Nepal government targets CTEVT technical education across all 753 local levels.", "critical": False},
            {"text": "Over 650 local levels have already established technical stream schools.", "critical": True},
        ],
    },

    # 4. Economics, Banking & Remittance (10 items: 5 natural, 5 perturbed)
    {
        "sub_genre": "economy_finance",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "नेपाल राष्ट्र बैंकका अनुसार चालु आर्थिक वर्षको पहिलो त्रैमासमा वार्षिक विन्दुगत उपभोक्ता मुद्रास्फीति दर ४.४० प्रतिशत रहेको छ। अघिल्लो वर्षको सोही महिनामा यस्तो मुद्रास्फीति ७.५० प्रतिशत रहेको थियो। खाद्य तथा पेय पदार्थ समूहको मुद्रास्फीति दर ६.३८ प्रतिशत र गैर-खाद्य समूहको मुद्रास्फीति ३.४५ प्रतिशत रहेको छ।",
        "query_en": "What was the consumer inflation rate in the first quarter of the current fiscal year compared to the previous year?",
        "base_answer": "According to Nepal Rastra Bank, consumer price inflation stood at 4.40 percent in the first quarter, compared to 7.50 percent in the same period of the previous fiscal year.",
        "claims": [
            {"text": "Consumer inflation was recorded at 4.40 percent in the first quarter.", "critical": True},
            {"text": "Consumer inflation was 7.50 percent during the same period in the prior year.", "critical": True},
            {"text": "Food and beverage inflation was 6.38 percent.", "critical": False},
        ],
    },
    {
        "sub_genre": "economy_finance",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "आर्थिक वर्ष २०८०/८१ मा नेपालको कुल वैदेशिक व्यापार घाटा १४ खर्ब ५३ अर्ब रुपैयाँ पुगेको छ। कुल वस्तु आयात १५ खर्ब ९२ अर्ब रुपैयाँ हुँदा कुल वस्तु निर्यात १ खर्ब ३९ अर्ब रुपैयाँमा सीमित भएको भन्सार विभागको तथ्याङ्क छ। नेपालको व्यापार घाटामा पेट्रोलियम पदार्थ र सवारी साधनको हिस्सा सबैभन्दा ठूलो रहेको छ।",
        "query_en": "What was Nepal's total trade deficit in FY 2080/81 and what were the total import and export values?",
        "base_answer": "Nepal's trade deficit in FY 2080/81 stood at 1,453 billion rupees (14.53 kharba). Total imports amounted to 1,592 billion rupees, while exports reached only 139 billion rupees.",
        "claims": [
            {"text": "Nepal's trade deficit reached 1,453 billion rupees in FY 2080/81.", "critical": True},
            {"text": "Total imports were 1,592 billion rupees in FY 2080/81.", "critical": True},
            {"text": "Total exports were limited to 139 billion rupees.", "critical": True},
        ],
    },
    {
        "sub_genre": "economy_finance",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "नेपालको कुल वैदेशिक मुद्रा सञ्चिति बढेर २० खर्ब ४१ अर्ब रुपैयाँ बराबर पुगेको छ। अमेरिकी डलरमा यो सञ्चिति १५ अर्ब २७ करोड डलर पुगेको नेपाल राष्ट्र बैंकले जनाएको छ। यस सञ्चितिले करिब १३ महिनाको वस्तु तथा सेवा आयात धान्न सक्ने क्षमता राख्दछ।",
        "query_en": "What is the total foreign exchange reserve of Nepal and how many months of imports can it finance?",
        "base_answer": "Nepal's foreign exchange reserves reached 2,041 billion rupees (15.27 billion USD), sufficient to finance approximately 13 months of merchandise and service imports.",
        "claims": [
            {"text": "Foreign exchange reserves reached 2,041 billion rupees (15.27 billion USD).", "critical": True},
            {"text": "The reserves are sufficient to cover roughly 13 months of imports.", "critical": True},
        ],
    },
    {
        "sub_genre": "economy_finance",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "नेपाल राष्ट्र बैंकको निर्देशिका अनुसार वाणिज्य बैंकहरूको न्यूनतम चुक्ता पुँजी ८ अर्ब रुपैयाँ हुनुपर्दछ। हाल नेपालमा २० वटा वाणिज्य बैंकहरू, १७ वटा विकास बैंकहरू र १७ वटा वित्त कम्पनीहरू सञ्चालनमा रहेका छन्। बैंक तथा वित्तीय संस्थाहरूको कुल निक्षेप ६२ खर्ब रुपैयाँभन्दा माथि पुगेको छ।",
        "query_en": "What is the minimum paid-up capital required for commercial banks in Nepal and how many commercial banks are currently operating?",
        "base_answer": "NRB regulations require commercial banks to maintain a minimum paid-up capital of 8 billion rupees. Currently, there are 20 commercial banks operating in Nepal, and total banking deposits exceed 62 trillion rupees.",
        "claims": [
            {"text": "Commercial banks in Nepal require a minimum paid-up capital of 8 billion rupees.", "critical": True},
            {"text": "There are currently 20 commercial banks operating in Nepal.", "critical": True},
            {"text": "Total banking sector deposits exceed 62 trillion rupees.", "critical": False},
        ],
    },
    {
        "sub_genre": "economy_finance",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "नेपाल सरकारले आर्थिक वर्ष २०८१/८२ का लागि १८ खर्ब ६० अर्ब ३० करोड रुपैयाँको बजेट प्रस्तुत गरेको छ। चालु खर्चतर्फ ११ खर्ब ४० अर्ब (६१.३१ प्रतिशत) र पुँजीगत खर्चतर्फ ३ खर्ब ५२ अर्ब (१८.९४ प्रतिशत) विनियोजन गरिएको अर्थ मन्त्रालयले जनाएको छ।",
        "query_en": "What is the total size of Nepal's budget for FY 2081/82 and how much is allocated for capital expenditure?",
        "base_answer": "Nepal's total budget for FY 2081/82 is 1,860.30 billion rupees. Capital expenditure is allocated 352 billion rupees, representing 18.94 percent of the budget.",
        "claims": [
            {"text": "The total budget size for FY 2081/82 is 1,860.30 billion rupees.", "critical": True},
            {"text": "Capital expenditure is allocated 352 billion rupees (18.94 percent).", "critical": True},
            {"text": "Recurrent expenditure is allocated 1,140 billion rupees.", "critical": False},
        ],
    },

    # 5. Disaster, Climate & Geography (10 items: 5 natural, 5 perturbed)
    {
        "sub_genre": "disaster_geography",
        "domain": Domain.NEWS,
        "passage_ne": "वि.सं. २०८० कात्तिक १७ गते राति जाजरकोटको रामीडाँडा केन्द्रविन्दु भएर गएको ६.४ म्याग्निच्यूडको भूकम्पमा परी १५४ जनाको मृत्यु भएको छ भने ३५० भन्दा बढी घाइते भएका छन्। जाजरकोट र रुकुम पश्चिममा गरी करिब ६० हजार घरहरू पूर्ण वा आंशिक रूपमा क्षतिग्रस्त भएका छन्।",
        "query_en": "What was the magnitude of the Jajarkot earthquake in 2080 BS and how many fatalities resulted?",
        "base_answer": "On Kartik 17, 2080 BS, a 6.4 magnitude earthquake centered at Ramidanda in Jajarkot caused 154 deaths and injured over 350 people. Around 60,000 houses suffered full or partial damage.",
        "claims": [
            {"text": "The 2080 BS Jajarkot earthquake had a magnitude of 6.4.", "critical": True},
            {"text": "154 people died in the Jajarkot earthquake.", "critical": True},
            {"text": "Around 60,000 houses were fully or partially damaged in Jajarkot and Western Rukum.", "critical": False},
        ],
    },
    {
        "sub_genre": "disaster_geography",
        "domain": Domain.NEWS,
        "passage_ne": "जल तथा मौसम विज्ञान विभागले मनसुनजन्य विपद्का कारण यस वर्ष देशभर बाढी र पहिरोबाट २२० भन्दा बढी मानिसको ज्यान गएको पुष्टि गरेको छ। विशेषगरी काठमाडौँ उपत्यकाको बागमती र विष्णुमती नदीमा आएको बाढीले विगत ५० वर्षयताकै उच्च सतह पार गरेको थियो।",
        "query_en": "How many fatalities were caused by monsoon-induced floods and landslides this year in Nepal?",
        "base_answer": "The Department of Hydrology and Meteorology confirmed over 220 fatalities nationwide from monsoon floods and landslides, with the Bagmati and Bishnumati rivers in Kathmandu Valley reaching 50-year record high water levels.",
        "claims": [
            {"text": "Over 220 people died due to monsoon-induced floods and landslides nationwide.", "critical": True},
            {"text": "The Bagmati and Bishnumati rivers recorded 50-year record high water levels in Kathmandu Valley.", "critical": True},
        ],
    },
    {
        "sub_genre": "disaster_geography",
        "domain": Domain.NEWS,
        "passage_ne": "अन्तर्राष्ट्रिय एकीकृत पर्वतीय विकास केन्द्र (इसिमोड) को प्रतिवेदन अनुसार हिन्दुकुश हिमालय क्षेत्रका हिमनदीहरू विगतको तुलनामा ६५ प्रतिशत तीव्र गतिमा पग्लिरहेका छन्। नेपालका २१ वटा हिमतालहरू विष्फोटको उच्च जोखिम (जीएलओएफ) मा रहेका छन्, जसमा च्छो रोल्पा र इम्जा हिमताल प्रमुख हुन्।",
        "query_en": "According to ICIMOD, how many glacial lakes in Nepal are at high risk of outburst flooding (GLOF)?",
        "base_answer": "An ICIMOD report reveals that Himalayan glaciers are melting 65 percent faster than before, placing 21 glacial lakes in Nepal at high risk of GLOF, including Tsho Rolpa and Imja lakes.",
        "claims": [
            {"text": "Himalayan glaciers are melting 65 percent faster according to ICIMOD.", "critical": False},
            {"text": "21 glacial lakes in Nepal are classified at high risk of glacial lake outburst flooding (GLOF).", "critical": True},
            {"text": "Tsho Rolpa and Imja are among the high-risk glacial lakes identified.", "critical": True},
        ],
    },
    {
        "sub_genre": "disaster_geography",
        "domain": Domain.NEWS,
        "passage_ne": "वि.सं. २०७२ वैशाख १२ गते गोरखाको बारपाक केन्द्रविन्दु भएको ७.८ म्याग्निच्यूडको भूकम्पमा परी ८ हजार ९७९ जनाको मृत्यु भएको थियो। राष्ट्रिय पुनर्निर्माण प्राधिकरणले ८ लाखभन्दा बढी निजी आवासहरूको पुनर्निर्माण सम्पन्न गरेको थियो।",
        "query_en": "What was the epicenter and death toll of the 2015 (2072 BS) Gorkha earthquake?",
        "base_answer": "The 7.8 magnitude earthquake on Baisakh 12, 2072 BS had its epicenter at Barpak in Gorkha and caused 8,979 deaths. Over 800,000 private houses were reconstructed.",
        "claims": [
            {"text": "The 2072 BS earthquake had its epicenter at Barpak in Gorkha.", "critical": True},
            {"text": "The 2072 BS Gorkha earthquake killed 8,979 people.", "critical": True},
            {"text": "Over 800,000 private houses were reconstructed following the earthquake.", "critical": False},
        ],
    },
    {
        "sub_genre": "disaster_geography",
        "domain": Domain.NEWS,
        "passage_ne": "मेलम्ची नदीमा वि.सं. २०७८ असार १ गते आएको भीषण लेदोसहितको बाढीले मेलम्ची खानेपानी आयोजनाको हेडवर्क्समा गम्भीर क्षति पुर्‍याएको थियो। भेमाथाङ क्षेत्रमा आएको ठूलो पहिरोका कारण नदी थुनिएर फुट्दा बस्ती र पुलहरू बगाएको भूगर्भविद्हरूको अध्ययनले देखाएको छ।",
        "query_en": "What caused the catastrophic flash flood in Melamchi in Asar 2078 BS?",
        "base_answer": "On Asar 1, 2078 BS, a debris-laden flash flood originating from a massive landslide at Bhemthang devastated the Melamchi Drinking Water Project headworks and washed away bridges and settlements.",
        "claims": [
            {"text": "The Melamchi flash flood occurred on Asar 1, 2078 BS.", "critical": False},
            {"text": "The flood was triggered by a massive landslide at Bhemthang damming and bursting the river.", "critical": True},
            {"text": "The Melamchi Drinking Water Project headworks suffered severe damage.", "critical": True},
        ],
    },

    # 6. Governance, Law & Constitution (10 items: 5 natural, 5 perturbed)
    {
        "sub_genre": "governance_law",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "नेपालको संविधान २०७२ अनुसार नेपाल एक स्वतन्त्र, अविभाज्य, सार्वभौमसत्ता सम्पन्न, धर्मनिरपेक्ष, समावेशी, लोकतान्त्रिक, समाजवाद-उन्मुख, संघीय लोकतान्त्रिक गणतन्त्रात्मक राज्य हो। राज्यको शासकीय संरचना संघ, प्रदेश र स्थानीय गरी तीन तहमा विभाजित गरिएको छ। संविधानमा ३५ भाग, ३०८ धारा र ९ अनुसूचीहरू रहेका छन्।",
        "query_en": "How many parts, articles, and tiers of government are defined in the Constitution of Nepal 2072?",
        "base_answer": "The 2072 Constitution establishes a three-tier governance structure (federal, provincial, and local) and consists of 35 parts, 308 articles, and 9 schedules.",
        "claims": [
            {"text": "The Constitution of Nepal 2072 defines three tiers of government: federal, provincial, and local.", "critical": True},
            {"text": "The Constitution contains 35 parts, 308 articles, and 9 schedules.", "critical": True},
            {"text": "Nepal is defined as a secular, federal democratic republic state.", "critical": False},
        ],
    },
    {
        "sub_genre": "governance_law",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "प्रतिनिधि सभामा कुल २७५ सदस्यहरू रहन्छन्, जसमध्ये १६५ जना प्रत्यक्ष निर्वाचन प्रणाली (पहिलो हुने निर्वाचित हुने) बाट र ११० जना समानुपातिक निर्वाचन प्रणालीबाट निर्वाचित हुन्छन्। प्रतिनिधि सभाको कार्यकाल पाँच वर्षको हुन्छ।",
        "query_en": "What is the total membership of the House of Representatives and how are members elected?",
        "base_answer": "The House of Representatives has 275 members, with 165 elected through first-past-the-post and 110 through proportional representation for a five-year term.",
        "claims": [
            {"text": "The House of Representatives has a total of 275 members.", "critical": True},
            {"text": "165 members are elected through first-past-the-post direct voting.", "critical": True},
            {"text": "110 members are elected through proportional representation.", "critical": True},
        ],
    },
    {
        "sub_genre": "governance_law",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "नेपालमा ७ वटा प्रदेश र ७५३ वटा स्थानीय तहहरू रहेका छन्। स्थानीय तह अन्तर्गत ६ वटा महानगरपालिका, ११ वटा उपमहानगरपालिका, २७६ वटा नगरपालिका र ४६० वटा गाउँपालिकाहरू रहेका छन्। स्थानीय तहमा कुल ६ हजार ७४३ वडा कार्यालयहरू सञ्चालनमा छन्।",
        "query_en": "How many local government units and ward offices exist in Nepal?",
        "base_answer": "Nepal comprises 7 provinces and 753 local bodies (6 metropolises, 11 sub-metropolises, 276 municipalities, and 460 rural municipalities) containing 6,743 ward offices.",
        "claims": [
            {"text": "Nepal is divided into 7 provinces and 753 local level governments.", "critical": True},
            {"text": "There are 6 metropolitan cities and 11 sub-metropolitan cities in Nepal.", "critical": False},
            {"text": "There are 6,743 ward offices across the 753 local levels in Nepal.", "critical": True},
        ],
    },
    {
        "sub_genre": "governance_law",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "सर्वोच्च अदालत नेपालको न्यायपालिकाको सर्वोच्च निकाय हो। संविधान अनुसार सर्वोच्च अदालतमा प्रधानन्यायाधीशका अतिरिक्त बढीमा २० जना अन्य न्यायाधीशहरू रहने व्यवस्था छ। सर्वोच्च अदालत अभिलेख अदालत हुनेछ र यसलाई आफ्ना फैसलाहरूको पुनरावलोकन गर्ने अधिकार रहन्छ।",
        "query_en": "What is the maximum number of justices in the Supreme Court of Nepal according to the Constitution?",
        "base_answer": "Under the Constitution, the Supreme Court of Nepal consists of the Chief Justice and up to a maximum of 20 other justices, functioning as a court of record.",
        "claims": [
            {"text": "The Supreme Court consists of the Chief Justice and up to 20 other justices.", "critical": True},
            {"text": "The Supreme Court of Nepal functions as a court of record with review jurisdiction.", "critical": True},
        ],
    },
    {
        "sub_genre": "governance_law",
        "domain": Domain.GOVERNMENT_REPORT,
        "passage_ne": "अख्तियार दुरुपयोग अनुसन्धान आयोग (सीआईएए) सार्वजनिक पद धारण गरेको व्यक्तिले भ्रष्टाचार गरी अख्तियारको दुरुपयोग गरेमा अनुसन्धान र अभियोजन गर्ने संवैधानिक निकाय हो। आयोगले विशेष अदालतमा भ्रष्टाचारका मुद्दाहरू दायर गर्दछ।",
        "query_en": "What is the mandate of the Commission for the Investigation of Abuse of Authority (CIAA)?",
        "base_answer": "The CIAA is a constitutional body mandated to investigate and prosecute corruption and abuse of authority by public officials, filing cases before the Special Court.",
        "claims": [
            {"text": "The CIAA investigates and prosecutes corruption committed by public officials.", "critical": True},
            {"text": "CIAA files its corruption cases in the Special Court.", "critical": True},
        ],
    },

    # 7. Sports (12 items: 6 natural, 6 perturbed)
    {
        "sub_genre": "sports",
        "domain": Domain.NEWS,
        "passage_ne": "नेपाल राष्ट्रिय क्रिकेट टोलीले सन् २०२४ को आईसीसी पुरुष टी-२० विश्वकपमा दक्षिण अफ्रिकाविरुद्ध ऐतिहासिक खेल प्रदर्शन गर्‍यो। दक्षिण अफ्रिकाले दिएको ११६ रनको लक्ष्य पछ्याउँदा नेपाल मात्र १ रनले पराजित भयो। नेपालका तीव्र गतिका बलर कुशल भुर्तेलले ४ विकेट र दीपेन्द्रसिंह ऐरीले ३ विकेट लिएका थिए।",
        "query_en": "What was the result of Nepal's match against South Africa in the 2024 T20 World Cup?",
        "base_answer": "In the 2024 T20 World Cup, Nepal came agonizingly close against South Africa, losing by just 1 run while chasing a target of 116. Kushal Bhurtel took 4 wickets and Dipendra Singh Airee took 3 wickets.",
        "claims": [
            {"text": "Nepal lost to South Africa by 1 run in the 2024 T20 World Cup.", "critical": True},
            {"text": "South Africa set a target of 116 runs.", "critical": True},
            {"text": "Kushal Bhurtel took 4 wickets and Dipendra Singh Airee took 3 wickets.", "critical": False},
        ],
    },
    {
        "sub_genre": "sports",
        "domain": Domain.NEWS,
        "passage_ne": "नेपाली अलराउन्डर दीपेन्द्रसिंह ऐरीले कतारविरुद्धको एसीसी प्रिमियर कप खेलमा एकै ओभरमा ६ छक्का प्रहार गर्दै विश्व कीर्तिमान कायम गरेका छन्। उनले कामरान खानको ओभरमा लगातार ६ छक्का प्रहार गरेका हुन्। यसअघि उनले १९औँ एसियाली खेलकुदमा मङ्गोलियाविरुद्ध ९ बलमै अर्धशतक प्रहार गरेका थिए।",
        "query_en": "Who bowled the over in which Dipendra Singh Airee hit six sixes, and against which team did he score a 9-ball fifty?",
        "base_answer": "Dipendra Singh Airee hit six consecutive sixes in an over bowled by Kamran Khan of Qatar in the ACC Premier Cup. Previously, he scored a 9-ball half-century against Mongolia in the Asian Games.",
        "claims": [
            {"text": "Dipendra Singh Airee hit six consecutive sixes off Qatar's Kamran Khan.", "critical": True},
            {"text": "Airee scored a half-century in 9 balls against Mongolia at the 19th Asian Games.", "critical": True},
        ],
    },
    {
        "sub_genre": "sports",
        "domain": Domain.NEWS,
        "passage_ne": "नेपाल क्रिकेट सङ्घ (क्यान) ले नेपाल प्रिमियर लिग (एनपीएल) टी-२० प्रतियोगिताको पहिलो संस्करण काठमाडौँमा आयोजना गर्ने घोषणा गरेको छ। यस प्रतियोगितामा विराटनगर, चितवन, जनकपुर, काठमाडौँ, कर्णाली, लुम्बिनी, पोखरा र सुदूरपश्चिम गरी ८ वटा फ्रेन्चाइज टोलीहरूले प्रतिस्पर्धा गर्नेछन्।",
        "query_en": "How many franchise teams compete in the inaugural Nepal Premier League (NPL)?",
        "base_answer": "The inaugural Nepal Premier League (NPL) organized by CAN features 8 franchise teams representing Biratnagar, Chitwan, Janakpur, Kathmandu, Karnali, Lumbini, Pokhara, and Sudurpashchim.",
        "claims": [
            {"text": "The Nepal Premier League features 8 franchise teams.", "critical": True},
            {"text": "The NPL tournament is officially organized by CAN in Kathmandu.", "critical": False},
        ],
    },
    {
        "sub_genre": "sports",
        "domain": Domain.NEWS,
        "passage_ne": "साफ महिला च्याम्पियनसिप २०२४ को सेमिफाइनलमा नेपालले भारतलाई पेनाल्टी सुटआउटमा ४-२ ले पराजित गर्दै फाइनलमा स्थान सुरक्षित गर्‍यो। निर्धारित समयको खेल १-१ गोलको बराबरीमा सकिएको थियो। नेपालकी गोलकिपर एन्जिला तुम्बापो सुब्बाले उत्कृष्ट बचाउ गरेकी थिइन्।",
        "query_en": "What was the score in Nepal's victory over India in the SAFF Women's Championship 2024 semi-final?",
        "base_answer": "Nepal defeated India 4-2 in a penalty shootout after a 1-1 regulation draw in the SAFF Women's Championship 2024 semi-final, with goalkeeper Anjila Tumbapo Subba making decisive saves.",
        "claims": [
            {"text": "Nepal defeated India 4-2 in a penalty shootout in the SAFF Women's Championship 2024 semi-final.", "critical": True},
            {"text": "The regulation time match between Nepal and India ended in a 1-1 draw.", "critical": True},
            {"text": "Anjila Tumbapo Subba played as Nepal's goalkeeper.", "critical": False},
        ],
    },
    {
        "sub_genre": "sports",
        "domain": Domain.NEWS,
        "passage_ne": "कीर्तिपुरस्थित त्रिवि क्रिकेट मैदानमा सम्पन्न खेलमा नेपालले स्कटल्याण्डलाई ५ विकेटले पराजित गरेको छ। स्कटल्याण्डले दिएको २१३ रनको लक्ष्य नेपालले ४४.१ ओभरमा ५ विकेट गुमाएर पूरा गर्‍यो। नेपालका लागि कप्तान रोहित पौडेलले ९५ रनको कप्तानी इनिङ खेलेका थिए।",
        "query_en": "How many runs did captain Rohit Paudel score in Nepal's victory over Scotland?",
        "base_answer": "Captain Rohit Paudel scored 95 runs to lead Nepal to a 5-wicket victory over Scotland, chasing down the 213-run target in 44.1 overs at the TU Cricket Ground.",
        "claims": [
            {"text": "Captain Rohit Paudel scored 95 runs against Scotland.", "critical": True},
            {"text": "Nepal defeated Scotland by 5 wickets chasing 213 runs.", "critical": True},
            {"text": "The match was held at the TU Cricket Ground in Kirtipur.", "critical": False},
        ],
    },
    {
        "sub_genre": "sports",
        "domain": Domain.NEWS,
        "passage_ne": "नेपालका तेक्वान्दो खेलाडी पलेशा गोवर्धनले पेरिस पारालम्पिक २०२४ मा ऐतिहासिक कास्य पदक जितेकी छन्। यो पारालम्पिकको इतिहासमा नेपालले जितेको पहिलो आधिकारिक पदक हो। उनले के-४४ विधा अन्तर्गत महिला ५७ केजी तौल समूहमा सर्बियाकी खेलाडीलाई १५-८ ले पराजित गरेकी थिइन्।",
        "query_en": "Who won Nepal's first-ever Paralympic medal at the Paris Paralympics 2024 and in which weight category?",
        "base_answer": "Palesha Goverdhan won Nepal's first-ever historic Paralympic medal by securing bronze in the women's 57kg K-44 category at Paris 2024, defeating Serbia's opponent 15-8.",
        "claims": [
            {"text": "Palesha Goverdhan won a bronze medal at the Paris Paralympics 2024.", "critical": True},
            {"text": "This was the first official Paralympic medal in Nepal's history.", "critical": True},
            {"text": "She competed in the women's 57kg K-44 taekwondo category.", "critical": False},
        ],
    },

    # 8. Culture, Heritage & History (15 items: 7 natural, 8 perturbed)
    {
        "sub_genre": "culture_heritage",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "काठमाडौँ उपत्यकाका सातवटा स्मारक क्षेत्रहरू सन् १९७९ मा युनेस्को विश्व सम्पदा सूचीमा सूचीकृत भएका थिए। ती क्षेत्रहरूमा काठमाडौँ दरबार स्क्वायर, पाटन दरबार स्क्वायर, भक्तपुर दरबार स्क्वायर, स्वयम्भूनाथ, बौद्धनाथ, पशुपतिनाथ मन्दिर र चाँगुनारायण मन्दिर पर्दछन्। यी सम्पदाहरूले उपत्यकाको मल्लकालीन कला र नेवारी वास्तुकलालाई प्रतिनिधित्व गर्दछन्।",
        "query_en": "When were the monument zones of Kathmandu Valley inscribed on the UNESCO World Heritage List and which sites are included?",
        "base_answer": "The seven monument zones of Kathmandu Valley were inscribed as a UNESCO World Heritage Site in 1979. They include Kathmandu, Patan, and Bhaktapur Durbar Squares, Swayambhunath, Boudhanath, Pashupatinath, and Changunarayan.",
        "claims": [
            {"text": "Kathmandu Valley's seven monument zones were inscribed in UNESCO World Heritage in 1979.", "critical": True},
            {"text": "The sites include Kathmandu, Patan, and Bhaktapur Durbar Squares.", "critical": True},
            {"text": "The monuments represent Malla-period art and Newari architecture.", "critical": False},
        ],
    },
    {
        "sub_genre": "culture_heritage",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "पशुपतिनाथ मन्दिर बागमती नदीको किनारमा अवस्थित हिन्दूहरूको पवित्र तीर्थस्थल हो। यो मन्दिर प्यागोडा शैलीमा निर्माण गरिएको छ र यसको छाना दुई तहको सुनको जलप लगाइएको तामाबाट बनेको छ। वि.सं. १९९० को महाभूकम्पमा पनि सुरक्षित रहेको यो मन्दिर क्षेत्रमा सन् १९७९ देखि गैर-हिन्दूहरूलाई मुख्य मन्दिर प्रवेशमा रोक लगाइएको छ।",
        "query_en": "Where is the Pashupatinath Temple located and what architectural style does it feature?",
        "base_answer": "Pashupatinath Temple is situated on the banks of the Bagmati River in Kathmandu and features a two-tiered pagoda-style architectural design with gold-plated copper roofs.",
        "claims": [
            {"text": "Pashupatinath Temple is located on the banks of the Bagmati River.", "critical": True},
            {"text": "The temple is constructed in a two-tiered pagoda style.", "critical": True},
            {"text": "Non-Hindus are prohibited from entering the inner sanctum of the main temple.", "critical": False},
        ],
    },
    {
        "sub_genre": "culture_heritage",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "इन्द्रजात्रा काठमाडौँ उपत्यकाको नेवार समुदायले मनाउने सबैभन्दा ठूलो ऐतिहासिक जात्रा हो। यो जात्रा भाद्र शुक्ल द्वादशीका दिन हनुमानढोकामा लिंगो (इन्द्रध्वज) ठड्याएपछि सुरु हुन्छ र आठ दिनसम्म चल्दछ। जात्राको मुख्य दिन जीवित देवी कुमारी, गणेश र भैरवको रथ यात्रा गराइन्छ।",
        "query_en": "How long does Indra Jatra last and what chariot procession takes place on its main day?",
        "base_answer": "Indra Jatra lasts for eight days after erecting the Indradhwoj pole at Hanuman Dhoka on Bhadra Shukla Dwadashi, featuring the chariot processions of Living Goddess Kumari, Ganesh, and Bhairav on the main day.",
        "claims": [
            {"text": "Indra Jatra lasts for eight days.", "critical": True},
            {"text": "The festival features chariot processions of the Living Goddess Kumari, Ganesh, and Bhairav.", "critical": True},
            {"text": "The festival begins by erecting the Indradhwoj pole at Hanuman Dhoka.", "critical": False},
        ],
    },
    {
        "sub_genre": "culture_heritage",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "नेपाल संवत् राष्ट्रिय विभूति शंखधर साख्वाले वि.सं. ९३६ (सन् ८७९) मा सुरु गरेका थिए। उनले काठमाडौँका गरिब जनताको ऋण मोचन गरी यो संवत् चलाएका हुन्। नेपाल सरकारले वि.सं. २०६५ मा नेपाल संवत्लाई राष्ट्रिय संवत्को रूपमा मान्यता दिएको थियो।",
        "query_en": "Who initiated the Nepal Sambat calendar and why?",
        "base_answer": "National Luminary Shankhadhar Sakhwa initiated the Nepal Sambat calendar in 879 AD (936 BS) after clearing the debts of the impoverished citizens of Kathmandu.",
        "claims": [
            {"text": "Shankhadhar Sakhwa initiated the Nepal Sambat in 879 AD (936 BS).", "critical": True},
            {"text": "He founded the calendar by clearing the debts of poor citizens in Kathmandu.", "critical": True},
            {"text": "Nepal government officially recognized Nepal Sambat as a national calendar in 2065 BS.", "critical": False},
        ],
    },
    {
        "sub_genre": "culture_heritage",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "चाँगुनारायण मन्दिर काठमाडौँ उपत्यकाको सबैभन्दा पुरानो हिन्दू मन्दिर मानिन्छ। यस मन्दिर परिसरमा वि.सं. ५२१ (सन् ४६४) को लिच्छवी राजा मानदेव प्रथमको शिलालेख फेला परेको छ, जुन नेपालको इतिहासको सबैभन्दा पुरानो प्रमाणिक अभिलेख हो। मन्दिर भक्तपुर जिल्लाको चाँगुनारायण नगरपालिकामा अवस्थित छ।",
        "query_en": "What is the historical significance of the inscription at Changunarayan Temple?",
        "base_answer": "Changunarayan Temple houses the 464 AD (521 BS) stone inscription of Licchavi King Manadeva I, which is the oldest verified epigraphic record in Nepalese history.",
        "claims": [
            {"text": "Changunarayan Temple houses the 464 AD (521 BS) stone inscription of King Manadeva I.", "critical": True},
            {"text": "The inscription of King Manadeva I is the oldest verified epigraphic record in Nepalese history.", "critical": True},
            {"text": "Changunarayan is located in Bhaktapur district.", "critical": False},
        ],
    },
    {
        "sub_genre": "culture_heritage",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "स्वयम्भूनाथ स्तूप काठमाडौँ उपत्यकाको पश्चिम भागमा एउटा पहाडी टाकुरामा अवस्थित छ। यसलाई 'मंकी टेम्पल' का नामले पनि चिनिन्छ। स्तूपको शीर्ष भागमा चारै दिशामा हेरिरहेका बुद्धका आँखाहरू कुँदिएका छन्, जसले सर्वव्यापी ज्ञान र करुणाको प्रतीक जनाउँछ।",
        "query_en": "What is depicted on the top of the Swayambhunath Stupa and what does it symbolize?",
        "base_answer": "The top of the Swayambhunath Stupa depicts the all-seeing eyes of Buddha painted in all four cardinal directions, symbolizing omnipresent wisdom and compassion.",
        "claims": [
            {"text": "Swayambhunath Stupa features Buddha's eyes painted facing all four cardinal directions.", "critical": True},
            {"text": "Buddha's eyes symbolize omnipresent wisdom and compassion.", "critical": True},
            {"text": "Swayambhunath is commonly referred to as the Monkey Temple.", "critical": False},
        ],
    },
    {
        "sub_genre": "culture_heritage",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "नेपालमा मनाइने छठ पर्व सूर्य देवता र छठी माताको उपासना गरिने प्रमुख चाड हो। चार दिनसम्म मनाइने यस पर्वमा अस्ताउँदो र उदाउँदो सूर्यलाई पवित्र नदी वा पोखरीको किनारमा अर्घ्य दिइन्छ। विशेषगरी तराई-मधेशमा मनाइने यो पर्व अहिले काठमाडौँ उपत्यका लगायत पहाडी क्षेत्रमा पनि लोकप्रिय भएको छ।",
        "query_en": "Which deities are worshipped during Chhath festival and how is the offering made?",
        "base_answer": "During the four-day Chhath festival, devotees worship the Sun God (Surya) and Chhathi Maiya by offering arghya to the setting and rising sun along the banks of holy rivers and ponds.",
        "claims": [
            {"text": "Chhath is a four-day festival worshipping the Sun God and Chhathi Maiya.", "critical": True},
            {"text": "Devotees offer arghya to both the setting and rising sun along water banks.", "critical": True},
        ],
    },
    {
        "sub_genre": "culture_heritage",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "भक्तपुर दरबार स्क्वायरलाई '५५ झ्याले दरबार' र 'न्यातपोल मन्दिर' का लागि चिनिन्छ। राजा भूपतिन्द्र मल्लले निर्माण गर्न लगाएको न्यातपोल मन्दिर पाँच तल्ला भएको नेपालकै सबैभन्दा अग्लो प्यागोडा मन्दिर हो, जसको उचाइ करिब ३० मिटर रहेको छ।",
        "query_en": "Who commissioned the construction of the Nyatapola Temple and what is its height?",
        "base_answer": "King Bhupatindra Malla commissioned the construction of the 5-story Nyatapola Temple in Bhaktapur, which stands approximately 30 meters tall as Nepal's tallest pagoda temple.",
        "claims": [
            {"text": "King Bhupatindra Malla commissioned the construction of the Nyatapola Temple.", "critical": True},
            {"text": "Nyatapola Temple is a 5-story pagoda standing roughly 30 meters tall.", "critical": True},
            {"text": "Bhaktapur Durbar Square is famous for the 55-Window Palace.", "critical": False},
        ],
    },

    # 9. Geography, Parks & Biodiversity (15 items: 7 natural, 8 perturbed)
    {
        "sub_genre": "biodiversity_parks",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "सगरमाथा राष्ट्रिय निकुञ्ज सन् १९७६ मा स्थापना भएको हो र सन् १९७९ मा युनेस्को विश्व प्राकृतिक सम्पदा सूचीमा सूचीकृत भएको थियो। १ हजार १४८ वर्ग किलोमिटरमा फैलिएको यस निकुञ्जमा विश्वको सर्वोच्च शिखर सगरमाथा (८,८४८.८६ मिटर) सहित ल्होत्से, नुप्त्से, चो ओयु र आमादब्लम जस्ता प्रमुख हिमालहरू पर्दछन्। यहाँ हिमचितुवा र कस्तुरी मृग पाइन्छन्।",
        "query_en": "When was Sagarmatha National Park inscribed as a UNESCO World Heritage Site and what is its total area?",
        "base_answer": "Sagarmatha National Park was established in 1976 and inscribed as a UNESCO World Natural Heritage Site in 1979, spanning an area of 1,148 square kilometers.",
        "claims": [
            {"text": "Sagarmatha National Park was inscribed as a UNESCO Natural Heritage Site in 1979.", "critical": True},
            {"text": "The park covers an area of 1,148 square kilometers.", "critical": True},
            {"text": "The park harbors endangered species such as the snow leopard and musk deer.", "critical": False},
        ],
    },
    {
        "sub_genre": "biodiversity_parks",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "सन् २०२२ को राष्ट्रिय बाघ गणना अनुसार नेपालमा पाटे बाघको सङ्ख्या बढेर ३५५ पुगेको छ। सन् २०१० मा सेन्ट पिटर्सबर्ग सम्मेलनमा नेपालले गरेको बाघको सङ्ख्या दोब्बर बनाउने प्रतिबद्धता (१२१ बाट २४२) पूरा गरी नेपाल विश्वमै बाघको सङ्ख्या दोब्बर बनाउने पहिलो देश बनेको थियो। सबैभन्दा बढी बाघ चितवन राष्ट्रिय निकुञ्ज (१२८ वटा) मा रहेका छन्।",
        "query_en": "What was the royal Bengal tiger population in Nepal according to the 2022 census and which park holds the largest count?",
        "base_answer": "Nepal's 2022 tiger census recorded 355 wild Bengal tigers, fulfilling its pledge to double its population from 2010. Chitwan National Park holds the largest population with 128 tigers.",
        "claims": [
            {"text": "Nepal recorded a population of 355 wild Bengal tigers in the 2022 census.", "critical": True},
            {"text": "Nepal became the first country to double its wild tiger population from its 2010 baseline of 121.", "critical": True},
            {"text": "Chitwan National Park hosts the largest tiger population with 128 individuals.", "critical": False},
        ],
    },
    {
        "sub_genre": "biodiversity_parks",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "बर्दिया राष्ट्रिय निकुञ्ज नेपालको तराई क्षेत्रमा अवस्थित सबैभन्दा ठूलो राष्ट्रिय निकुञ्ज हो, जसको क्षेत्रफल ९६८ वर्ग किलोमिटर छ। यो निकुञ्ज कर्णाली नदीको पूर्वी किनारमा फैलिएको छ र यहाँ एकसिङ्गे गैँडा, पाटे बाघ र एसियाली हात्तीहरू पाइन्छन्। बर्दियामा १२५ वटा पाटे बाघ रहेका छन्।",
        "query_en": "What is the area of Bardiya National Park and which river flows along its border?",
        "base_answer": "Bardiya National Park covers 968 square kilometers along the eastern bank of the Karnali River, making it the largest national park in Nepal's lowland Terai.",
        "claims": [
            {"text": "Bardiya National Park covers an area of 968 square kilometers.", "critical": True},
            {"text": "The park lies along the eastern bank of the Karnali River.", "critical": True},
            {"text": "Bardiya is home to 125 wild Bengal tigers.", "critical": False},
        ],
    },
    {
        "sub_genre": "biodiversity_parks",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "रारा ताल नेपालको सबैभन्दा ठूलो र गहिरो ताल हो। यो कर्णाली प्रदेशको मुगु जिल्लामा समुद्र सतहबाट २ हजार ९९० मिटरको उचाइमा अवस्थित छ। यस तालको लम्बाइ करिब ५.१ किलोमिटर, चौडाइ २.७ किलोमिटर र अधिकतम गहिराइ १६७ मिटर रहेको छ। रारा ताल रारा राष्ट्रिय निकुञ्जभित्र पर्दछ।",
        "query_en": "What is the maximum depth and elevation of Rara Lake in Nepal?",
        "base_answer": "Rara Lake is located in Mugu district at an elevation of 2,990 meters above sea level and has a maximum depth of 167 meters, making it Nepal's largest and deepest lake.",
        "claims": [
            {"text": "Rara Lake is situated at an elevation of 2,990 meters in Mugu district.", "critical": True},
            {"text": "Rara Lake reaches a maximum depth of 167 meters.", "critical": True},
            {"text": "Rara Lake is Nepal's largest lake with a length of 5.1 kilometers.", "critical": False},
        ],
    },
    {
        "sub_genre": "biodiversity_parks",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "अन्नपूर्ण संरक्षण क्षेत्र नेपालको सबैभन्दा ठूलो संरक्षण क्षेत्र हो, जसको क्षेत्रफल ७ हजार ६२९ वर्ग किलोमिटर छ। यो गण्डकी प्रदेशका कास्की, लमजुङ, म्याग्दी, मनाङ र मुस्ताङ जिल्लामा फैलिएको छ। यस क्षेत्रलाई राष्ट्रिय प्रकृति संरक्षण कोष (एनटीएनसी) ले स्थानीय समुदायको सहभागितामा व्यवस्थापन गर्दै आएको छ।",
        "query_en": "What is the total area of the Annapurna Conservation Area and which entity manages it?",
        "base_answer": "The Annapurna Conservation Area spans 7,629 square kilometers across five districts and is managed by the National Trust for Nature Conservation (NTNC) with community participation.",
        "claims": [
            {"text": "Annapurna Conservation Area covers 7,629 square kilometers.", "critical": True},
            {"text": "The area is managed by the National Trust for Nature Conservation (NTNC).", "critical": True},
        ],
    },
    {
        "sub_genre": "biodiversity_parks",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "लाङटाङ राष्ट्रिय निकुञ्ज नेपालको पहिलो हिमाली राष्ट्रिय निकुञ्ज हो, जुन सन् १९७६ मा स्थापना भएको थियो। १ हजार ७१० वर्ग किलोमिटरमा फैलिएको यस निकुञ्जले रसुवा, नुवाकोट र सिन्धुपाल्चोक जिल्लालाई ओगटेको छ। निकुञ्जभित्र पवित्र गोसाइँकुण्ड ताल अवस्थित छ, जहाँ जनैपूर्णिमाका दिन ठूलो मेला लाग्दछ।",
        "query_en": "Which sacred lake is located inside Langtang National Park?",
        "base_answer": "The sacred Gosainkunda Lake is located within Langtang National Park, which was established in 1976 across Rasuwa, Nuwakot, and Sindhupalchok districts.",
        "claims": [
            {"text": "Gosainkunda Lake is located within Langtang National Park.", "critical": True},
            {"text": "Langtang was established as Nepal's first Himalayan national park in 1976.", "critical": False},
            {"text": "Langtang National Park covers 1,710 square kilometers.", "critical": False},
        ],
    },
    {
        "sub_genre": "biodiversity_parks",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "नेपालमा हालसम्म ८८६ प्रजातिका चराहरू अभिलेखीकरण गरिएका छन्, जुन विश्वको कुल चरा प्रजातिको करिब ९ प्रतिशत हो। कोशी टप्पु वन्यजन्तु आरक्ष नेपालको प्रमुख चरा अवलोकन क्षेत्र हो, जहाँ ५२६ भन्दा बढी प्रजातिका चराहरू पाइन्छन्। काँडे भ्याकुर नेपालमा मात्र पाइने रैथाने चरा हो।",
        "query_en": "Which bird species is endemic only to Nepal and how many bird species are recorded in Koshi Tappu?",
        "base_answer": "The Spiny Babbler (काँडे भ्याकुर) is the only endemic bird found exclusively in Nepal. Koshi Tappu Wildlife Reserve serves as a premier birding habitat hosting over 526 bird species.",
        "claims": [
            {"text": "The Spiny Babbler (Kande Bhyakur) is the only bird endemic exclusively to Nepal.", "critical": True},
            {"text": "Koshi Tappu Wildlife Reserve hosts over 526 recorded bird species.", "critical": True},
            {"text": "A total of 886 bird species have been documented in Nepal.", "critical": False},
        ],
    },
    {
        "sub_genre": "biodiversity_parks",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "शुक्लाफाँटा राष्ट्रिय निकुञ्ज सुदूरपश्चिम प्रदेशको कञ्चनपुर जिल्लामा अवस्थित छ। यस निकुञ्जको क्षेत्रफल ३०५ वर्ग किलोमिटर छ। यहाँ विश्वकै सबैभन्दा ठूलो बाह्रसिङ्गा (स्वम्प डियर) को बथान पाइन्छ, जसको सङ्ख्या २ हजारभन्दा बढी रहेको छ।",
        "query_en": "What is the primary wildlife attraction of Suklaphanta National Park in Kanchanpur?",
        "base_answer": "Suklaphanta National Park in Kanchanpur spans 305 square kilometers and hosts the world's largest herd of swamp deer (barasingha), numbering over 2,000 individuals.",
        "claims": [
            {"text": "Suklaphanta National Park is located in Kanchanpur district.", "critical": False},
            {"text": "The park hosts the world's largest herd of swamp deer, exceeding 2,000 individuals.", "critical": True},
            {"text": "The park covers an area of 305 square kilometers.", "critical": True},
        ],
    },

    # 10. Infrastructure, Energy & Tourism (18 items: 9 natural, 9 perturbed)
    {
        "sub_genre": "infrastructure_tourism",
        "domain": Domain.NEWS,
        "passage_ne": "माथिल्लो तामाकोशी जलविद्युत आयोजना (४५६ मेगावाट) नेपालको आफ्नै स्रोत र साधनमा निर्माण भएको सबैभन्दा ठूलो जलविद्युत आयोजना हो। दोलखा जिल्लाको लामाबगरमा अवस्थित यस आयोजनाले वि.सं. २०७८ असारमा व्यावसायिक उत्पादन सुरु गरेको थियो। यस आयोजनाको भूमिगत विद्युतगृहमा ७६ मेगावाटका ६ वटा टर्बाइनहरू जडान गरिएका छन्।",
        "query_en": "What is the installed capacity and location of the Upper Tamakoshi Hydropower Project?",
        "base_answer": "Upper Tamakoshi Hydropower Project has an installed capacity of 456 megawatts located at Lamabagar in Dolakha district, operating six 76 MW turbines in its underground powerhouse.",
        "claims": [
            {"text": "Upper Tamakoshi Hydropower Project has an installed capacity of 456 MW.", "critical": True},
            {"text": "The project is located at Lamabagar in Dolakha district.", "critical": True},
            {"text": "Its underground powerhouse is equipped with six 76 MW turbines.", "critical": False},
        ],
    },
    {
        "sub_genre": "infrastructure_tourism",
        "domain": Domain.NEWS,
        "passage_ne": "नेपाल विद्युत प्राधिकरणका अनुसार नेपालको कुल जडित विद्युत क्षमता ३ हजार २०० मेगावाट नाघेको छ। वर्षायाममा नेपालले भारततर्फ दैनिक ६५० मेगावाटसम्म विद्युत निर्यात गर्दै आएको छ भने बंगलादेशतर्फ ४० मेगावाट विद्युत निर्यातको त्रिपक्षीय सम्झौता कार्यान्वयनमा आएको छ।",
        "query_en": "What is the total installed electricity generation capacity in Nepal and how much is exported to Bangladesh?",
        "base_answer": "Nepal's total installed power capacity exceeds 3,200 MW, with daily exports up to 650 MW to India in monsoon and an agreement to export 40 MW to Bangladesh.",
        "claims": [
            {"text": "Nepal's total installed power capacity exceeds 3,200 MW.", "critical": True},
            {"text": "Nepal has an agreement to export 40 MW of electricity to Bangladesh.", "critical": True},
            {"text": "Nepal exports up to 650 MW of electricity daily to India during the wet season.", "critical": False},
        ],
    },
    {
        "sub_genre": "infrastructure_tourism",
        "domain": Domain.NEWS,
        "passage_ne": "काठमाडौँ-तराई/मधेश द्रुतमार्ग (फास्ट ट्र्याक) ७२.५ किलोमिटर लामो चार लेनको एक्सप्रेस-वे हो। यस आयोजनामा तीनवटा प्रमुख सुरुङमार्गहरू—निजगढतर्फ लेनडाँडा (१.६१ किमि), धेद्रे (१.६३ किमि) र महादेवडाँडा (३.३५ किमि) निर्माणाधीन छन्। यो आयोजना सम्पन्न भएपछि काठमाडौँबाट निजगढ १ घण्टामा पुग्न सकिनेछ।",
        "query_en": "What is the total length of the Kathmandu-Terai Fast Track and how long is the Mahadev Danda tunnel?",
        "base_answer": "The Kathmandu-Terai Fast Track spans 72.5 kilometers as a four-lane expressway, featuring the 3.35 km Mahadev Danda tunnel among its three major tunnels.",
        "claims": [
            {"text": "The Kathmandu-Terai Fast Track has a total length of 72.5 kilometers.", "critical": True},
            {"text": "The Mahadev Danda tunnel has a length of 3.35 kilometers.", "critical": True},
            {"text": "Travel time from Kathmandu to Nijgadh will be reduced to 1 hour upon completion.", "critical": False},
        ],
    },
    {
        "sub_genre": "infrastructure_tourism",
        "domain": Domain.NEWS,
        "passage_ne": "नेपाल पर्यटन बोर्डका अनुसार सन् २०२३ मा हवाई मार्गबाट नेपाल भित्रिने विदेशी पर्यटकहरूको सङ्ख्या १० लाख १४ हजार ८८२ पुगेको छ। यो सङ्ख्या सन् २०१९ को तुलनामा करिब ८५ प्रतिशतको पुनरुत्थान हो। सबैभन्दा बढी पर्यटक भारत (३ लाख १९ हजार) बाट र त्यसपछि अमेरिका (१ लाख) बाट आएका थिए।",
        "query_en": "How many foreign tourists visited Nepal by air in 2023 and which country contributed the highest arrival count?",
        "base_answer": "In 2023, a total of 1,014,882 foreign tourists arrived in Nepal by air, with India contributing the highest arrival count at 319,000 visitors.",
        "claims": [
            {"text": "Over 1.014 million foreign tourists arrived in Nepal by air in 2023.", "critical": True},
            {"text": "India contributed the largest number of tourists with 319,000 visitors.", "critical": True},
            {"text": "The 2023 arrival count represented an 85 percent recovery compared to 2019 levels.", "critical": False},
        ],
    },
    {
        "sub_genre": "infrastructure_tourism",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "पोखरा अन्तर्राष्ट्रिय विमानस्थल नेपालको दोस्रो नयाँ अन्तर्राष्ट्रिय विमानस्थल हो, जसको उद्घाटन सन् २०२३ जनवरी १ मा गरिएको थियो। चीनको एक्जिम बैंकको करिब २२ अर्ब रुपैयाँ सहुलियतपूर्ण ऋण सहयोगमा निर्माण गरिएको यो विमानस्थल ४ डी श्रेणीको हो र यसको धावनमार्ग २ हजार ५०० मिटर लामो छ।",
        "query_en": "When was Pokhara International Airport inaugurated and what is the length of its runway?",
        "base_answer": "Pokhara International Airport was officially inaugurated on January 1, 2023. Built as a 4D category airport, it features a 2,500-meter-long runway.",
        "claims": [
            {"text": "Pokhara International Airport was inaugurated on January 1, 2023.", "critical": True},
            {"text": "The airport features a 2,500-meter-long runway.", "critical": True},
            {"text": "The airport was built with a concessional loan of roughly 22 billion rupees from China's EXIM Bank.", "critical": False},
        ],
    },
    {
        "sub_genre": "infrastructure_tourism",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "गौतम बुद्ध अन्तर्राष्ट्रिय विमानस्थल रूपन्देहीको भैरहवामा अवस्थित छ। सन् २०२२ मे १६ (बुद्ध पूर्णिमा) का दिन उद्घाटन गरिएको यो नेपालको दोस्रो अन्तर्राष्ट्रिय विमानस्थल हो। यस विमानस्थलको धावनमार्ग ३ हजार मिटर लामो छ र यसले वाइडबडी विमानहरू अवतरण गर्न सक्ने क्षमता राख्दछ।",
        "query_en": "Where is Gautam Buddha International Airport located and what is its runway length?",
        "base_answer": "Gautam Buddha International Airport is located in Bhairahawa, Rupandehi district, featuring a 3,000-meter runway capable of handling wide-body aircraft.",
        "claims": [
            {"text": "Gautam Buddha International Airport is situated in Bhairahawa, Rupandehi.", "critical": True},
            {"text": "The airport features a 3,000-meter-long runway capable of wide-body landings.", "critical": True},
            {"text": "The airport was inaugurated on May 16, 2022 on Buddha Purnima.", "critical": False},
        ],
    },
    {
        "sub_genre": "infrastructure_tourism",
        "domain": Domain.NEWS,
        "passage_ne": "अरुण तेस्रो जलविद्युत आयोजना (९०० मेगावाट) संखुवासभा जिल्लामा निर्माणाधीन नेपालको ठूलो निर्यातमुखी जलविद्युत आयोजना हो। भारतीय कम्पनी सतलज जलविद्युत निगम (एसजेभीएन) ले निर्माण गरिरहेको यस आयोजनाबाट नेपालले २१.९ प्रतिशत (१९७ मेगावाट) विद्युत निःशुल्क प्राप्त गर्ने सम्झौता छ।",
        "query_en": "What is the installed capacity of the Arun-III Hydropower Project and how much free power will Nepal receive?",
        "base_answer": "The Arun-III Hydropower Project in Sankhuwasabha has an installed capacity of 900 MW, from which Nepal will receive 21.9 percent (197 MW) of generated electricity free of cost.",
        "claims": [
            {"text": "Arun-III Hydropower Project has an installed capacity of 900 MW.", "critical": True},
            {"text": "Nepal will receive 21.9 percent (197 MW) of power free of cost from Arun-III.", "critical": True},
            {"text": "The project is being constructed in Sankhuwasabha by SJVN.", "critical": False},
        ],
    },
    {
        "sub_genre": "infrastructure_tourism",
        "domain": Domain.NEWS,
        "passage_ne": "नागढुंगा-सिस्नेखोला सुरुङमार्गको मुख्य सुरुङको लम्बाई २ हजार ६८८ मिटर रहेको छ। वि.सं. २०८१ वैशाखमा यस सुरुङमार्गको 'ब्रेकथ्रु' भएको थियो। जापान अन्तर्राष्ट्रिय सहयोग नियोग (जाइका) को सहुलियतपूर्ण ऋण सहयोगमा निर्माणाधीन यो सुरुङमार्ग नेपालको पहिलो आधुनिक यातायात सुरुङमार्ग हो।",
        "query_en": "What is the length of the Nagdhunga-Sisnekhola main tunnel and which agency provided financial assistance?",
        "base_answer": "The Nagdhunga-Sisnekhola main tunnel spans 2,688 meters as Nepal's first modern transport tunnel, funded through concessional loan assistance from JICA.",
        "claims": [
            {"text": "The Nagdhunga-Sisnekhola main tunnel has a length of 2,688 meters.", "critical": True},
            {"text": "The project is funded by concessional loan assistance from JICA.", "critical": True},
            {"text": "The main tunnel breakthrough occurred in Baisakh 2081 BS.", "critical": False},
        ],
    },
    {
        "sub_genre": "infrastructure_tourism",
        "domain": Domain.WIKIPEDIA,
        "passage_ne": "भेरी-बबई डाइभर्सन बहुउद्देश्यीय आयोजना नेपालको पहिलो अन्तर-जलाधार जल स्थानान्तरण आयोजना हो। टनेल बोरिङ मेसिन (टीबीएम) प्रयोग गरी निर्माण गरिएको १२.२ किलोमिटर लामो सुरुङमार्फत भेरी नदीको पानी बबई नदीमा खसालेर बाँके र बर्दियाको ५१ हजार हेक्टर जमिनमा सिँचाइ र ४८ मेगावाट विद्युत उत्पादन गर्ने लक्ष्य छ।",
        "query_en": "How long is the tunnel of the Bheri-Babai Diversion Project and what technology was used to bore it?",
        "base_answer": "The Bheri-Babai Diversion Project features a 12.2-kilometer tunnel bored using a Tunnel Boring Machine (TBM), transferring water to irrigate 51,000 hectares and generate 48 MW of power.",
        "claims": [
            {"text": "The Bheri-Babai Diversion tunnel has a length of 12.2 kilometers.", "critical": True},
            {"text": "The tunnel was constructed using a Tunnel Boring Machine (TBM).", "critical": True},
            {"text": "The project aims to irrigate 51,000 hectares and generate 48 MW of electricity.", "critical": False},
        ],
    },
]

PERTURBATION_CYCLE = [
    PerturbationType.ENTITY_SWAP,
    PerturbationType.NUMBER_DATE_ALTERATION,
    PerturbationType.NEGATION_FLIP,
    PerturbationType.MISATTRIBUTION,
    PerturbationType.REGISTER_SHIFT,
    PerturbationType.UNSUPPORTED_ADDITION,
    PerturbationType.INVENTED_CAUSALITY,
]


class CandidateAssembler:
    """Assembles 120 candidate items across 10 domains with exact stratification."""

    def __init__(self, output_path: Path = Path("data/interim/preannotations/gold_candidates_120.jsonl")):
        self.output_path = Path(output_path)
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

    def assemble(self) -> List[EvaluationItem]:
        allocations = [
            # Wikipedia (40 items)
            {"sub_genre": "culture_heritage", "domain": Domain.WIKIPEDIA, "count": 15, "natural": 8, "perturbed": 7},
            {"sub_genre": "biodiversity_parks", "domain": Domain.WIKIPEDIA, "count": 15, "natural": 7, "perturbed": 8},
            {"sub_genre": "infrastructure_tourism", "domain": Domain.WIKIPEDIA, "count": 10, "natural": 5, "perturbed": 5},
            # Government Reports (40 items)
            {"sub_genre": "health", "domain": Domain.GOVERNMENT_REPORT, "count": 10, "natural": 5, "perturbed": 5},
            {"sub_genre": "agriculture", "domain": Domain.GOVERNMENT_REPORT, "count": 10, "natural": 5, "perturbed": 5},
            {"sub_genre": "education", "domain": Domain.GOVERNMENT_REPORT, "count": 10, "natural": 5, "perturbed": 5},
            {"sub_genre": "economy_finance", "domain": Domain.GOVERNMENT_REPORT, "count": 10, "natural": 5, "perturbed": 5},
            # News (40 items)
            {"sub_genre": "sports", "domain": Domain.NEWS, "count": 12, "natural": 6, "perturbed": 6},
            {"sub_genre": "disaster_geography", "domain": Domain.NEWS, "count": 10, "natural": 5, "perturbed": 5},
            {"sub_genre": "governance_law", "domain": Domain.NEWS, "count": 10, "natural": 5, "perturbed": 5},
            {"sub_genre": "infrastructure_tourism", "domain": Domain.NEWS, "count": 8, "natural": 4, "perturbed": 4},
        ]

        # Index seeds by sub_genre
        seeds_by_genre: Dict[str, List[Dict[str, Any]]] = {}
        for s in PASSAGE_SEEDS:
            sg = s["sub_genre"]
            seeds_by_genre.setdefault(sg, []).append(s)

        items: List[EvaluationItem] = []
        item_counter = 1
        perturb_idx = 0

        for alloc in allocations:
            sub_genre = alloc["sub_genre"]
            domain = alloc["domain"]
            natural_count = alloc["natural"]
            perturbed_count = alloc["perturbed"]
            genre_seeds = seeds_by_genre[sub_genre]

            # Assemble Natural items
            for i in range(natural_count):
                seed = genre_seeds[i % len(genre_seeds)]
                item_id = f"item_{item_counter:03d}"
                claims = [
                    AtomicClaim(
                        claim_id=f"{item_id}_c{c_idx+1}",
                        claim_text=c["text"],
                        is_critical=c["critical"],
                        gold_label=None,  # Strictly None for human annotation
                    )
                    for c_idx, c in enumerate(seed["claims"])
                ]
                item = EvaluationItem(
                    item_id=item_id,
                    domain=domain,
                    sub_genre=sub_genre,
                    source_provenance=Provenance.NATURAL,
                    perturbation_type=None,
                    perturbation_span=None,
                    passage_ne=seed["passage_ne"],
                    query_en=seed["query_en"],
                    answer_en=seed["base_answer"],
                    retrieval_condition=RetrievalCondition.FULL_SUPPORT,
                    sampling_weight=1.0,
                    claims=claims,
                )
                items.append(item)
                item_counter += 1

            # Assemble Perturbed items
            for i in range(perturbed_count):
                seed = genre_seeds[(i + natural_count) % len(genre_seeds)]
                item_id = f"item_{item_counter:03d}"
                p_type = PERTURBATION_CYCLE[perturb_idx % len(PERTURBATION_CYCLE)]
                perturb_idx += 1

                # Apply specific perturbation to answer
                perturbed_answer, span, claims = self._create_perturbed_answer(
                    seed=seed, item_id=item_id, p_type=p_type, seed_num=item_counter
                )

                item = EvaluationItem(
                    item_id=item_id,
                    domain=domain,
                    sub_genre=sub_genre,
                    source_provenance=Provenance.PERTURBED,
                    perturbation_type=p_type,
                    perturbation_span=span or p_type.value,
                    passage_ne=seed["passage_ne"],
                    query_en=seed["query_en"],
                    answer_en=perturbed_answer,
                    retrieval_condition=RetrievalCondition.PARTIAL_SUPPORT,
                    sampling_weight=1.0,
                    claims=claims,
                )
                items.append(item)
                item_counter += 1

        # Enforce output path isolation
        assert "data/raw/labels" not in str(self.output_path), "PROHIBITION: Cannot write candidate pool to gold label path"

        with open(self.output_path, "w", encoding="utf-8") as f:
            for it in items:
                f.write(json.dumps(it.model_dump(), ensure_ascii=False) + "\n")

        logger.info(f"Assembled {len(items)} stratified candidate items into {self.output_path}")
        return items

    def _create_perturbed_answer(
        self, seed: Dict[str, Any], item_id: str, p_type: PerturbationType, seed_num: int = 42
    ) -> tuple[str, str, List[AtomicClaim]]:
        base_ans = seed["base_answer"]
        perturbed_ans, span = apply_perturbation(base_ans, p_type, seed=seed_num)

        # Decompose into atomic claims
        claims: List[AtomicClaim] = []
        for c_idx, c in enumerate(seed["claims"]):
            claim_text = c["text"]
            # Alter the first critical claim to reflect the perturbation if applicable
            if c["critical"] and c_idx == 0:
                p_claim, _ = apply_perturbation(claim_text, p_type, seed=seed_num)
                claim_text = p_claim

            claims.append(
                AtomicClaim(
                    claim_id=f"{item_id}_c{c_idx+1}",
                    claim_text=claim_text,
                    is_critical=c["critical"],
                    gold_label=None,
                )
            )

        return perturbed_ans, span, claims


if __name__ == "__main__":
    assembler = CandidateAssembler()
    items = assembler.assemble()
    print(f"Successfully generated {len(items)} candidate items.")
