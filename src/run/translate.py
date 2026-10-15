"""NepFaith-120: IndicTrans2 Machine Translation Runner (Condition C2)

Translates Nepali context passages (p_ne) into English (p_c2) using
ai4bharat/indictrans2-indic-en-dist-200M to isolate the machine translation error gap:
Δ_MT = A(C3) - A(C2)

Features:
- Local FP16 GPU inference (RTX 3050 Ti) with automatic CPU fallback.
- Source tag: npi_Deva, Target tag: eng_Latn.
- Deterministic disk cache under cache/translations/ keyed on SHA-256.
- Invariant: Zero leakage of C3 post-edited texts or gold labels.
"""

import os
import json
import hashlib
import logging
from pathlib import Path
from typing import List, Optional, Union

import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

logger = logging.getLogger("IndicTrans2Runner")

MODEL_ID = "ai4bharat/indictrans2-indic-en-dist-200M"
SRC_LANG = "npi_Deva"
TGT_LANG = "eng_Latn"


class IndicTrans2Translator:
    """Local inference runner for IndicTrans2 Nepali -> English translation."""

    def __init__(
        self,
        model_id: str = MODEL_ID,
        device: Optional[str] = None,
        cache_dir: Path = Path("cache/translations"),
    ):
        self.model_id = model_id
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device

        self.tokenizer = None
        self.model = None
        logger.info(f"Initialized IndicTrans2Translator on device '{self.device}' with cache at '{self.cache_dir}'.")

    def _load_model(self):
        """Lazy loads the model and tokenizer upon first execution."""
        if self.model is None or self.tokenizer is None:
            logger.info(f"Loading {self.model_id} onto {self.device}...")
            # Set system CA bundle for HuggingFace downloads if behind SSL proxy
            ca_bundle = "/etc/ssl/certs/ca-certificates.crt"
            if os.path.exists(ca_bundle):
                os.environ["CURL_CA_BUNDLE"] = ca_bundle
                os.environ["REQUESTS_CA_BUNDLE"] = ca_bundle

            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_id,
                trust_remote_code=True,
            )
            dtype = torch.float16 if self.device == "cuda" else torch.float32
            self.model = AutoModelForSeq2SeqLM.from_pretrained(
                self.model_id,
                trust_remote_code=True,
                torch_dtype=dtype,
            ).to(self.device)
            self.model.eval()
            logger.info(f"Loaded {self.model_id} successfully.")

    def _get_cache_path(self, text: str) -> Path:
        """Computes deterministic cache path for a translation query."""
        payload = f"{text}|{SRC_LANG}|{TGT_LANG}|{self.model_id}".encode("utf-8")
        hash_key = hashlib.sha256(payload).hexdigest()
        return self.cache_dir / f"{hash_key}.json"

    def translate(
        self,
        text: str,
        use_cache: bool = True,
        max_length: int = 512,
    ) -> str:
        """Translates a single Nepali text string into English."""
        if not text or not text.strip():
            return ""

        text = text.strip()
        cache_file = self._get_cache_path(text)

        if use_cache and cache_file.exists():
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("translation", "")
            except Exception as e:
                logger.warning(f"Cache read error for {cache_file.name}: {e}")

        # Lazy load model
        self._load_model()

        # Batch encode with language prefix
        tagged_text = f"{text} <2{TGT_LANG}>"
        inputs = self.tokenizer(
            [tagged_text],
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=max_length,
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                num_beams=4,
                max_length=max_length,
                early_stopping=True,
            )

        translation = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0].strip()

        # Save to deterministic cache
        if use_cache:
            try:
                with open(cache_file, "w", encoding="utf-8") as f:
                    json.dump(
                        {
                            "source": text,
                            "translation": translation,
                            "src_lang": SRC_LANG,
                            "tgt_lang": TGT_LANG,
                            "model_id": self.model_id,
                        },
                        f,
                        ensure_ascii=False,
                        indent=2,
                    )
            except Exception as e:
                logger.warning(f"Failed to write cache {cache_file}: {e}")

        return translation

    def translate_batch(
        self,
        texts: List[str],
        use_cache: bool = True,
        batch_size: int = 8,
    ) -> List[str]:
        """Translates a list of Nepali texts with batch processing and caching."""
        results = []
        uncached_indices = []
        uncached_texts = []

        for idx, text in enumerate(texts):
            cache_file = self._get_cache_path(text)
            if use_cache and cache_file.exists():
                with open(cache_file, "r", encoding="utf-8") as f:
                    results.append(json.load(f).get("translation", ""))
            else:
                results.append(None)
                uncached_indices.append(idx)
                uncached_texts.append(text)

        if uncached_texts:
            self._load_model()
            for b_start in range(0, len(uncached_texts), batch_size):
                batch = uncached_texts[b_start : b_start + batch_size]
                tagged_batch = [f"{t} <2{TGT_LANG}>" for t in batch]
                inputs = self.tokenizer(
                    tagged_batch,
                    return_tensors="pt",
                    padding=True,
                    truncation=True,
                    max_length=512,
                ).to(self.device)

                with torch.no_grad():
                    outputs = self.model.generate(**inputs, num_beams=4, max_length=512)

                batch_trans = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
                for rel_idx, trans in enumerate(batch_trans):
                    global_idx = uncached_indices[b_start + rel_idx]
                    clean_trans = trans.strip()
                    results[global_idx] = clean_trans

                    # Write cache
                    if use_cache:
                        c_file = self._get_cache_path(batch[rel_idx])
                        with open(c_file, "w", encoding="utf-8") as f:
                            json.dump(
                                {
                                    "source": batch[rel_idx],
                                    "translation": clean_trans,
                                    "src_lang": SRC_LANG,
                                    "tgt_lang": TGT_LANG,
                                    "model_id": self.model_id,
                                },
                                f,
                                ensure_ascii=False,
                                indent=2,
                            )

        return results
