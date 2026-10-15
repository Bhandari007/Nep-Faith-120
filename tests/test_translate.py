"""Tests for IndicTrans2 Translation Runner."""

import json
from pathlib import Path
import pytest

from src.run.translate import IndicTrans2Translator, MODEL_ID, SRC_LANG, TGT_LANG


def test_translator_init_and_cache_path(tmp_path):
    translator = IndicTrans2Translator(cache_dir=tmp_path)
    assert translator.device in ("cuda", "cpu")
    
    sample_ne = "सगरमाथा नेपालको सर्वोच्च शिखर हो।"
    c_path = translator._get_cache_path(sample_ne)
    assert c_path.parent == tmp_path
    assert c_path.suffix == ".json"


def test_translator_cache_hit(tmp_path):
    translator = IndicTrans2Translator(cache_dir=tmp_path)
    sample_ne = "चितवन राष्ट्रिय निकुञ्ज नेपालमा पर्दछ।"
    expected_en = "Chitwan National Park is located in Nepal."

    # Seed the cache
    c_path = translator._get_cache_path(sample_ne)
    with open(c_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "source": sample_ne,
                "translation": expected_en,
                "src_lang": SRC_LANG,
                "tgt_lang": TGT_LANG,
                "model_id": MODEL_ID,
            },
            f,
        )

    # Calling translate should return immediately from cache without instantiating model
    res = translator.translate(sample_ne, use_cache=True)
    assert res == expected_en
    assert translator.model is None  # Model was never loaded into memory!


def test_translator_batch_cache_hit(tmp_path):
    translator = IndicTrans2Translator(cache_dir=tmp_path)
    texts = [
        "काठमाडौँ नेपालको राजधानी हो।",
        "पोखरा पर्यटकीय सहर हो।",
    ]
    translations = [
        "Kathmandu is the capital of Nepal.",
        "Pokhara is a tourist city.",
    ]

    for t, trans in zip(texts, translations):
        c_path = translator._get_cache_path(t)
        with open(c_path, "w", encoding="utf-8") as f:
            json.dump({"source": t, "translation": trans}, f)

    batch_res = translator.translate_batch(texts, use_cache=True)
    assert batch_res == translations
    assert translator.model is None
