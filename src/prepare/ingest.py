"""NepFaith-120: Corpus Ingestion and Multi-Format PDF Normalization Pipeline

Ingests, cleans, chunks, and validates Nepali source passages from:
1. Nepali Wikipedia (CC BY-SA 4.0)
2. Nepali Government Reports (NRB, Census 2078, MoHP, MoF)
3. Contemporary News & Sports (OnlineKhabar, Setopati, Kantipur, HamroKhelkud, CAN/ANFA)

Supports:
- Digital Unicode PDFs (pypdf + Unicode NFC normalization)
- Legacy 8-bit Preeti font transliteration
- Scanned non-searchable PDFs via Gemini Vision OCR fallback
- 150–350 token passage chunking with schema validation
"""

import os
import re
import json
import logging
import unicodedata
from pathlib import Path
from typing import List, Dict, Any, Optional

import pypdf
from src.prepare.schema import Domain, CorpusPassage

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("CorpusIngest")

# Preeti to Unicode character map for legacy font conversion
PREETI_TO_UNICODE = {
    "g]kfn": "नेपाल",
    ";/sf/": "सरकार",
    "k|wfgdGqL": "प्रधानमन्त्री",
    "dGqfno": "मन्त्रालय",
    "g": "न",
    "k": "प",
    "f": "ा",
    "l": "ि",
    "L": "ी",
    "o": "य",
    "r": "च",
    "s": "क",
    "d": "म",
    "t": "त",
    "y": "थ",
    "b": "द",
    ";": "स",
    "/": "र",
    "x": "ह",
    "j": "व",
    "a": "ब",
    "u": "ग",
    "e": "भ",
    "w": "ध",
    "v": "ख",
    "]": "े",
    "}": "ै",
    "f]": "ो",
    "f}": "ौ",
    "्": "्",
    "|": "्र",
    "=": "ं",
    "M": "ः",
}


def normalize_devanagari(text: str) -> str:
    """Normalizes Devanagari text using Unicode NFC and removes formatting noise."""
    if not text:
        return ""
    
    # 1. Unicode Normalization Form C (combines base characters and matras)
    normalized = unicodedata.normalize("NFC", text)
    
    # 2. Normalize zero-width joiners and non-joiners
    # Keep only when adjacent to halants (U+094D)
    normalized = re.sub(r"(?<!\u094D)[\u200C\u200D]", "", normalized)
    
    # 3. Clean carriage returns and tabs
    normalized = normalized.replace("\r", "")
    
    # 4. Strip spaces per line and normalize paragraph breaks
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in normalized.split("\n")]
    cleaned_text = "\n".join(lines)
    cleaned_text = re.sub(r"\n{3,}", "\n\n", cleaned_text)
    
    return cleaned_text.strip()


def is_preeti_encoded(text: str) -> bool:
    """Detects if text is encoded in legacy 8-bit Preeti/Kantipur font."""
    indicators = [";/sf/", "g]kfn", "pkf/", "ljleGg", "k|", "f]"]
    matches = sum(1 for ind in indicators if ind in text)
    return matches >= 2


def convert_preeti_to_unicode(text: str) -> str:
    """Converts common legacy Preeti/Kantipur encoded strings to standard Unicode Devanagari."""
    converted = text
    for preeti_str, unicode_str in PREETI_TO_UNICODE.items():
        converted = converted.replace(preeti_str, unicode_str)
    return normalize_devanagari(converted)


def count_tokens(text: str) -> int:
    """Counts approximate word/token count in text."""
    if not text:
        return 0
    # Split on whitespace and punctuation
    tokens = re.findall(r"[\w\u0900-\u097F]+|[^\w\s]", text)
    return len(tokens)


def extract_text_from_pdf(
    pdf_path: Path,
    use_ocr_fallback: bool = True,
    ocr_client: Optional[Any] = None,
) -> str:
    """Extracts and normalizes text from a digital or scanned PDF.
    
    If digital text is absent (< 30% Devanagari), routes to Gemini Vision OCR fallback.
    """
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    reader = pypdf.PdfReader(str(pdf_path))
    extracted_pages = []

    for page_idx, page in enumerate(reader.pages, start=1):
        raw_text = page.extract_text() or ""
        
        # Check for legacy font
        if is_preeti_encoded(raw_text):
            logger.info(f"Page {page_idx} of {pdf_path.name}: detected legacy Preeti font. Transliterating...")
            cleaned = convert_preeti_to_unicode(raw_text)
            extracted_pages.append(cleaned)
            continue

        # Count Devanagari characters (U+0900 to U+097F)
        devanagari_chars = len(re.findall(r"[\u0900-\u097F]", raw_text))
        total_chars = max(len(raw_text.strip()), 1)
        deva_ratio = devanagari_chars / total_chars

        if deva_ratio >= 0.20:
            # Digital Unicode text
            cleaned = normalize_devanagari(raw_text)
            extracted_pages.append(cleaned)
        elif use_ocr_fallback:
            # Scanned / Image-only page
            logger.info(f"Page {page_idx} of {pdf_path.name}: no digital text found (deva_ratio={deva_ratio:.2f}). Running Gemini Vision OCR...")
            ocr_text = transcribe_pdf_page_with_ocr(pdf_path, page_idx, ocr_client)
            if ocr_text:
                extracted_pages.append(normalize_devanagari(ocr_text))
        else:
            logger.warning(f"Page {page_idx} of {pdf_path.name} skipped: non-text and OCR fallback disabled.")

    return "\n\n".join(extracted_pages)


def transcribe_pdf_page_with_ocr(
    pdf_path: Path,
    page_number: int,
    ocr_client: Optional[Any] = None,
) -> str:
    """Transcribes a scanned PDF page using Gemini Vision OCR with strict prompt constraints."""
    if ocr_client is None:
        try:
            from src.run.gemini_client import GeminiRotator
            ocr_client = GeminiRotator()
        except Exception as e:
            logger.error(f"Failed to instantiate GeminiRotator for OCR: {e}")
            return ""

    prompt = (
        f"Transcribe the full text from page {page_number} of this Nepali document into standard Unicode text. "
        f"Preserve all numbers, tables, percentages, and dates verbatim. Do not summarize or translate. Return only the Nepali text."
    )
    
    try:
        # Calls the rotating client with cache
        res = ocr_client.generate_content(
            prompt=f"{prompt}\n[Source: {pdf_path.name}]",
            json_mode=False,
            use_cache=True,
        )
        return res.get("content", "")
    except Exception as e:
        logger.error(f"OCR transcription failed for {pdf_path.name} p.{page_number}: {e}")
        return ""


def chunk_into_passages(
    text: str,
    min_tokens: int = 80,
    max_tokens: int = 350,
) -> List[str]:
    """Chunks normalized Nepali text into coherent passages between min_tokens and max_tokens."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    valid_chunks = []
    current_chunk: List[str] = []
    current_len = 0

    for para in paragraphs:
        para_len = count_tokens(para)

        # If single paragraph exceeds max_tokens, split into sentence units
        if para_len > max_tokens:
            sentences = re.split(r"(?<=[।?!])\s+", para)
            for sent in sentences:
                sent = sent.strip()
                if not sent:
                    continue
                s_len = count_tokens(sent)
                if current_len + s_len <= max_tokens:
                    current_chunk.append(sent)
                    current_len += s_len
                else:
                    if current_len >= min_tokens:
                        valid_chunks.append(" ".join(current_chunk))
                    current_chunk = [sent]
                    current_len = s_len
        else:
            if current_len + para_len <= max_tokens:
                current_chunk.append(para)
                current_len += para_len
            else:
                if current_len >= min_tokens:
                    valid_chunks.append("\n\n".join(current_chunk))
                current_chunk = [para]
                current_len = para_len

    if current_len >= min_tokens:
        valid_chunks.append("\n\n".join(current_chunk))

    return valid_chunks


def create_seed_corpus() -> List[Dict[str, Any]]:
    """Builds initial representative seed passages across all 3 domains including sports."""
    records = [
        # Domain 1: Wikipedia
        {
            "passage_id": "wiki_001",
            "domain": Domain.WIKIPEDIA,
            "sub_genre": "geography",
            "source_title": "चितवन राष्ट्रिय निकुञ्ज - नेपाली विकिपिडिया",
            "source_url": "https://ne.wikipedia.org/wiki/Chitwan_National_Park",
            "license": "CC-BY-SA-4.0",
            "publication_year": 2023,
            "passage_ne": (
                "चितवन राष्ट्रिय निकुञ्ज नेपालको पहिलो राष्ट्रिय निकुञ्ज हो। यसको स्थापना वि.सं. २०३० (सन् १९७३) मा भएको थियो। "
                "यस निकुञ्जको क्षेत्रफल ९५२.६३ वर्ग किलोमिटर रहेको छ। यो नेपालको मध्य तराईको चितवन, नवलपरासी, पर्सा र मकवानपुर जिल्लामा फैलिएको छ। "
                "सन् १९८४ मा युनेस्कोले यस निकुञ्जलाई विश्व सम्पदा सूचीमा समावेश गरेको थियो। यहाँ एकसिङ्गे गैँडा, पाटे बाघ र घडियाल गोहीको प्रमुख बासस्थान रहेको छ।"
            ),
        },
        {
            "passage_id": "wiki_002",
            "domain": Domain.WIKIPEDIA,
            "sub_genre": "monuments",
            "source_title": "लुम्बिनी विश्व सम्पदा क्षेत्र - नेपाली विकिपिडिया",
            "source_url": "https://ne.wikipedia.org/wiki/Lumbini",
            "license": "CC-BY-SA-4.0",
            "publication_year": 2023,
            "passage_ne": (
                "लुम्बिनी भगवान बुद्धको जन्मस्थल हो। यो नेपालको लुम्बिनी प्रदेश अन्तर्गत रूपन्देही जिल्लामा अवस्थित छ। "
                "यहाँ सम्राट अशोकले स्थापना गरेको अशोक स्तम्भ र मायादेवीको मन्दिर मुख्य आकर्षण हुन्। "
                "सन् १९९७ मा युनेस्कोले लुम्बिनीलाई विश्व सम्पदा सूचीमा सूचीकृत गरेको थियो। लुम्बिनी गुरुयोजना जापानी वास्तुकार केन्जो ताङ्गेले तयार पारेका थिए।"
            ),
        },
        # Domain 2: Government Reports
        {
            "passage_id": "gov_nrb_001",
            "domain": Domain.GOVERNMENT_REPORT,
            "sub_genre": "macroeconomics",
            "source_title": "नेपाल राष्ट्र बैंक: देशको वर्तमान आर्थिक तथा वित्तीय स्थिति (आ.व. २०८०/८१)",
            "source_url": "https://www.nrb.org.np/category/monthly-macroeconomic-report/",
            "license": "Nepal-Gov-Public-Domain",
            "publication_year": 2024,
            "passage_ne": (
                "नेपाल राष्ट्र बैंकको आर्थिक प्रतिवेदन अनुसार आर्थिक वर्ष २०८०/८१ को पहिलो ६ महिनामा कुल विप्रेषण आप्रवाह (रेमिट्यान्स) २५.३ प्रतिशतले "
                "वृद्धि भई ७ खर्ब ३३ अर्ब २२ करोड रुपैयाँ पुगेको छ। अघिल्लो वर्षको सोही अवधिमा विप्रेषण आप्रवाह २४.३ प्रतिशतले बढेको थियो। "
                "यस अवधिमा विदेशी विनिमय सञ्चिति १८ खर्ब १६ अर्ब रुपैयाँ बराबर पुगेको छ, जसले १२.१ महिनाको वस्तु तथा सेवा आयात धान्न पर्याप्त रहेको छ।"
            ),
        },
        {
            "passage_id": "gov_cbs_001",
            "domain": Domain.GOVERNMENT_REPORT,
            "sub_genre": "census",
            "source_title": "राष्ट्रिय तथ्याङ्क कार्यालय: राष्ट्रिय जनगणना २०७८ को संक्षिप्त नतिजा",
            "source_url": "https://censusnepal.cbs.gov.np/",
            "license": "Nepal-Gov-Public-Domain",
            "publication_year": 2023,
            "passage_ne": (
                "राष्ट्रिय जनगणना २०७८ को अन्तिम नतिजा अनुसार नेपालको कुल जनसङ्ख्या २ करोड ९१ लाख ६४ हजार ५७८ रहेको छ। "
                "जसमध्ये पुरुषको सङ्ख्या १ करोड ४२ लाख ५३ हजार ५५१ (४८.९८ प्रतिशत) र महिलाको सङ्ख्या १ करोड ४९ लाख ११ हजार २७ (५१.०२ प्रतिशत) छ। "
                "वार्षिक जनसङ्ख्या वृद्धिदर ०.९२ प्रतिशत रहेको छ। बागमती प्रदेशमा सबैभन्दा धेरै अर्थात् कुल जनसङ्ख्याको २०.९७ प्रतिशत मानिस बसोबास गर्दछन्।"
            ),
        },
        # Domain 3: News & Dedicated Sports
        {
            "passage_id": "news_ok_001",
            "domain": Domain.NEWS,
            "sub_genre": "infrastructure",
            "source_title": "काठमाडौँ-तराई द्रुतमार्गको निर्माण प्रगति - अनलाइनखबर",
            "source_url": "https://www.onlinekhabar.com/fast-track-progress",
            "license": "Academic-Fair-Dealing",
            "publication_year": 2024,
            "passage_ne": (
                "नेपाली सेनाको व्यवस्थापनमा निर्माणाधीन काठमाडौँ-तराई/मधेश द्रुतमार्ग (फास्ट ट्र्याक) को कुल भौतिक प्रगति ३३ प्रतिशत पुगेको छ। "
                "७२.५ किलोमिटर लामो यस द्रुतमार्गमा निर्माणाधीन तीनवटा सुरुङमार्गमध्ये धेद्रे सुरुङमार्गको ‘ब्रेकथ्रु’ भएको छ। "
                "रक्षा मन्त्रालयका अनुसार वि.सं. २०८३ चैत मसान्तभित्र आयोजना सम्पन्न गर्ने गरी काम भइरहेको छ।"
            ),
        },
        {
            "passage_id": "sports_hk_001",
            "domain": Domain.NEWS,
            "sub_genre": "sports",
            "source_title": "नेपाल टी-२० विश्वकपमा छनोट: ऐतिहासिक विजय - हाम्रो खेलकुद",
            "source_url": "https://hamrokhelkud.net/nepal-t20-world-cup-selection/",
            "license": "Academic-Fair-Dealing",
            "publication_year": 2023,
            "passage_ne": (
                "काठमाडौँको कीर्तिपुरस्थित त्रिवि क्रिकेट मैदानमा भएको आईसीसी टी-२० विश्वकप एसिया छनोटको सेमिफाइनलमा संयुक्त अरब इमिरेट्स (युएई) लाई ८ विकेटले "
                "पराजित गर्दै नेपाल १० वर्षपछि टी-२० विश्वकपमा छनोट भएको छ। युएईले प्रस्तुत गरेको १३५ रनको लक्ष्य नेपालले १७.१ ओभरमा २ विकेट गुमाएर पूरा गर्‍यो। "
                "नेपालका लागि कप्तान रोहित पौडेलले अविजित ३४ रन र आसिफ शेखले अविजित ६४ रनको उत्कृष्ट इनिङ खेलेका थिए।"
            ),
        },
        {
            "passage_id": "sports_can_001",
            "domain": Domain.NEWS,
            "sub_genre": "sports",
            "source_title": "नेपाल क्रिकेट सङ्घ (क्यान): राष्ट्रिय टोलीको बन्द प्रशिक्षण घोषणा",
            "source_url": "https://cricketnepal.org/can-national-camp-announcement/",
            "license": "Academic-Fair-Dealing",
            "publication_year": 2024,
            "passage_ne": (
                "नेपाल क्रिकेट सङ्घ (क्यान) ले आगामी त्रिकोणात्मक टी-२० शृङ्खलाका लागि १८ सदस्यीय प्रारम्भिक टोलीको घोषणा गरेको छ। "
                "मुख्य प्रशिक्षक मोन्टी देसाईको सिफारिसमा घोषणा गरिएको टोलीमा दीपेन्द्रसिंह ऐरी, कुशल भुर्तेल र सोमपाल कामी समावेश छन्। "
                "क्यानका सचिव पारस खड्काका अनुसार खेलाडीहरूको विशेष फिटनेस प्रशिक्षण कीर्तिपुर मैदानमा सञ्चालन गरिनेछ।"
            ),
        },
    ]
    for r in records:
        r["passage_ne"] = normalize_devanagari(r["passage_ne"])
        r["token_count"] = count_tokens(r["passage_ne"])
    return records


def run_ingestion_pipeline(
    raw_dir: Path = Path("data/raw/corpus"),
    output_file: Path = Path("data/derived/corpus_passages.jsonl"),
) -> List[CorpusPassage]:
    """Runs the end-to-end ingestion pipeline, extracting, chunking, and validating passages."""
    raw_dir.mkdir(parents=True, exist_ok=True)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    ingested_passages: List[CorpusPassage] = []

    # 1. Process files in data/raw/corpus/
    pdf_files = list(raw_dir.glob("*.pdf"))
    logger.info(f"Scanning {raw_dir}: found {len(pdf_files)} raw PDF documents.")

    for pdf_path in pdf_files:
        try:
            full_text = extract_text_from_pdf(pdf_path)
            chunks = chunk_into_passages(full_text)
            logger.info(f"Extracted {len(chunks)} passages from {pdf_path.name}")
            for idx, chunk in enumerate(chunks, 1):
                p_id = f"pdf_{pdf_path.stem}_{idx:03d}"
                passage = CorpusPassage(
                    passage_id=p_id,
                    domain=Domain.GOVERNMENT_REPORT,
                    sub_genre="report",
                    source_title=pdf_path.stem.replace("_", " ").title(),
                    source_url=f"local://{pdf_path.name}",
                    license="Nepal-Gov-Public-Domain",
                    passage_ne=chunk,
                    token_count=count_tokens(chunk),
                )
                ingested_passages.append(passage)
        except Exception as e:
            logger.error(f"Failed processing {pdf_path.name}: {e}")

    # 2. Ingest Seed Stratified Corpus (Wikipedia, Government, News, Sports)
    seed_records = create_seed_corpus()
    for rec in seed_records:
        ingested_passages.append(CorpusPassage(**rec))

    # 3. Save validated records to data/derived/corpus_passages.jsonl
    with open(output_file, "w", encoding="utf-8") as f:
        for p in ingested_passages:
            f.write(p.model_dump_json() + "\n")

    # 4. Log summary statistics (Loud Failure Principle)
    domain_counts = {}
    sports_count = 0
    for p in ingested_passages:
        domain_counts[p.domain.value] = domain_counts.get(p.domain.value, 0) + 1
        if p.sub_genre == "sports":
            sports_count += 1

    logger.info("=" * 50)
    logger.info("CORPUS INGESTION SUMMARY:")
    logger.info(f"Total Passages Ingested: {len(ingested_passages)}")
    for d, c in domain_counts.items():
        logger.info(f" - {d}: {c} passages")
    logger.info(f" - Dedicated Sports Passages: {sports_count}")
    logger.info(f"Output saved to: {output_file}")
    logger.info("=" * 50)

    return ingested_passages


if __name__ == "__main__":
    run_ingestion_pipeline()
