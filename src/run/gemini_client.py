"""NepFaith-120: Rotating Gemini Client with Deterministic Caching

Provides round-robin API key rotation, exponential backoff on 429 rate limits,
deterministic local disk caching, and structured JSON output for Arm 5 (LLM Judge).
"""

import os
import time
import json
import hashlib
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("GeminiClient")


def mask_key(key: str) -> str:
    """Masks an API key for safe logging."""
    if not key or len(key) < 8:
        return "***"
    return f"{key[:4]}...{key[-4:]}"


class GeminiRotator:
    """Manages a pool of Gemini API keys with round-robin rotation, backoff, and caching."""

    def __init__(
        self,
        api_keys: Optional[List[str]] = None,
        model_id: str = "gemini-3.6-flash",
        temperature: float = 0.0,
        cache_dir: str = "cache/llm_raw",
        timeout_seconds: int = 30,
        max_retries_per_call: int = 30,
        pace_delay: float = 1.0,
    ):
        self.model_id = model_id
        self.temperature = temperature
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries_per_call
        self.pace_delay = pace_delay
        self.current_key_idx = 0

        self.total_requests_made = 0
        self.total_cache_hits = 0
        self.requests_by_key: Dict[str, int] = {}

        self.ca_bundle = os.getenv(
            "REQUESTS_CA_BUNDLE",
            "/etc/ssl/certs/ca-certificates.crt"
            if os.path.exists("/etc/ssl/certs/ca-certificates.crt")
            else True,
        )

        # Load keys from parameter or environment
        if api_keys:
            self.keys = [k.strip() for k in api_keys if k.strip()]
        else:
            raw_env_keys = os.getenv("GEMINI_API_KEYS", "")
            if not raw_env_keys:
                single_key = os.getenv("GEMINI_API_KEY", "")
                raw_env_keys = single_key
            
            # Split by comma, semicolon, or whitespace
            delimiter = "," if "," in raw_env_keys else (";" if ";" in raw_env_keys else "\n")
            self.keys = [k.strip().strip('"').strip("'") for k in raw_env_keys.split(delimiter) if k.strip()]

        if not self.keys:
            logger.warning("No Gemini API keys detected! Set GEMINI_API_KEYS in .env")
        else:
            logger.info(f"Loaded {len(self.keys)} Gemini API keys for rotation")

        self.base_url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model_id}:generateContent"


    def get_active_key(self) -> str:
        """Returns current key in round-robin sequence."""
        if not self.keys:
            raise ValueError("No API keys configured. Please add keys to .env under GEMINI_API_KEYS")
        return self.keys[self.current_key_idx]

    def advance_key(self, reason: str = ""):
        """Advances round-robin pointer to next key."""
        old_idx = self.current_key_idx
        self.current_key_idx = (self.current_key_idx + 1) % len(self.keys)
        logger.info(
            f"Rotating key from #{old_idx + 1} ({mask_key(self.keys[old_idx])}) "
            f"to #{self.current_key_idx + 1} ({mask_key(self.keys[self.current_key_idx])}). Reason: {reason}"
        )

    def _get_cache_path(self, cache_key: str) -> Path:
        return self.cache_dir / f"{cache_key}.json"

    def _compute_cache_key(self, payload: Dict[str, Any]) -> str:
        serialized = json.dumps(payload, sort_keys=True)
        return hashlib.sha256(f"{self.model_id}:{serialized}".encode("utf-8")).hexdigest()

    def generate_content(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        json_mode: bool = True,
        use_cache: bool = True,
    ) -> Dict[str, Any]:
        """Calls Gemini with automatic key rotation, rate-limit backoff, and caching."""
        # Assemble request payload
        contents = [{"role": "user", "parts": [{"text": prompt}]}]
        
        generation_config: Dict[str, Any] = {
            "temperature": self.temperature,
            "maxOutputTokens": 2048,
        }

        if json_mode:
            generation_config["responseMimeType"] = "application/json"

        request_body: Dict[str, Any] = {
            "contents": contents,
            "generationConfig": generation_config,
        }
        if system_instruction:
            request_body["systemInstruction"] = {
                "parts": [{"text": system_instruction}]
            }

        # Check local disk cache
        cache_key = self._compute_cache_key(request_body)
        cache_file = self._get_cache_path(cache_key)

        if use_cache and cache_file.exists():
            try:
                with open(cache_file, "r", encoding="utf-8") as f:
                    cached_data = json.load(f)
                self.total_cache_hits += 1
                return {
                    "content": cached_data["content"],
                    "parsed_json": cached_data.get("parsed_json"),
                    "cached": True,
                    "model": self.model_id,
                }
            except Exception as e:
                logger.warning(f"Corrupt cache file {cache_file}, refetching. Error: {e}")

        # Attempt call across available keys
        attempts = 0
        backoff_delay = 1.0

        while attempts < self.max_retries:
            attempts += 1
            key = self.get_active_key()
            headers = {
                "Content-Type": "application/json",
                "x-goog-api-key": key,
            }

            try:
                response = requests.post(
                    self.base_url,
                    headers=headers,
                    json=request_body,
                    timeout=self.timeout_seconds,
                    verify=self.ca_bundle,
                )

                # HTTP 429: Rate limit / quota exhausted
                if response.status_code == 429:
                    logger.warning(f"HTTP 429 on key #{self.current_key_idx + 1} ({mask_key(key)})")
                    self.advance_key(reason="Rate Limit (HTTP 429)")
                    time.sleep(backoff_delay)
                    backoff_delay = min(backoff_delay * 1.5, 20.0)
                    continue


                # HTTP 503 / 500: Server transient error
                if response.status_code in (500, 502, 503, 504):
                    logger.warning(f"HTTP {response.status_code} transient error on key #{self.current_key_idx + 1}: {response.text[:200]}")
                    self.advance_key(reason=f"Server error {response.status_code}")
                    time.sleep(1.0)
                    continue

                # HTTP 404: Model not available for this key/project
                if response.status_code == 404:
                    logger.warning(f"Key #{self.current_key_idx + 1} ({mask_key(key)}) returned 404 for model {self.model_id}. Pruning key.")
                    if len(self.keys) > 1:
                        self.keys.pop(self.current_key_idx)
                        self.current_key_idx = self.current_key_idx % len(self.keys)
                        continue

                if response.status_code != 200:
                    error_msg = f"API error {response.status_code} on key #{self.current_key_idx + 1}: {response.text}"
                    logger.error(error_msg)
                    # If invalid key or bad request, rotate and try next
                    self.advance_key(reason=f"Error {response.status_code}")
                    time.sleep(0.5)
                    continue


                # Successful 200 response
                self.total_requests_made += 1
                self.requests_by_key[key] = self.requests_by_key.get(key, 0) + 1

                res_json = response.json()
                text_content = ""
                try:
                    candidates = res_json.get("candidates", [])
                    if candidates:
                        text_content = candidates[0]["content"]["parts"][0]["text"]
                except (KeyError, IndexError) as err:
                    raise ValueError(f"Malformed response structure: {res_json}") from err

                parsed_json = None
                if json_mode:
                    try:
                        parsed_json = json.loads(text_content)
                    except json.JSONDecodeError as err:
                        logger.warning(f"JSON decode failed on output: {text_content[:100]}... Error: {err}")

                result = {
                    "content": text_content,
                    "parsed_json": parsed_json,
                    "cached": False,
                    "model": self.model_id,
                    "key_used": mask_key(key),
                }

                # Save to disk cache
                with open(cache_file, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)

                # Advance key for round-robin balancing on the next call
                self.advance_key(reason="Round-robin dispatch")
                if self.pace_delay > 0:
                    time.sleep(self.pace_delay)
                return result


            except requests.RequestException as req_err:
                logger.warning(f"Network error on key #{self.current_key_idx + 1}: {req_err}")
                self.advance_key(reason="Network timeout / failure")
                time.sleep(backoff_delay)
                backoff_delay = min(backoff_delay * 1.5, 10.0)

        raise RuntimeError(f"Exceeded max retries ({self.max_retries}) across all API keys.")

    def get_stats(self) -> Dict[str, Any]:
        """Returns request counts and cache hit statistics."""
        return {
            "total_requests_made": self.total_requests_made,
            "total_cache_hits": self.total_cache_hits,
            "requests_by_key": dict(self.requests_by_key),
        }

    def verify_all_keys(self) -> List[Dict[str, Any]]:
        """Tests exactly one lightweight API call per key to verify quota and validity."""
        if not self.keys:
            return [{"error": "No keys configured in GEMINI_API_KEYS"}]

        logger.info(f"Starting key verification for {len(self.keys)} configured API keys...")
        results = []

        test_payload = {
            "contents": [{"role": "user", "parts": [{"text": "Respond with JSON: {\"ping\": \"pong\"}"}]}],
            "generationConfig": {
                "temperature": 0.0,
                "maxOutputTokens": 512,
                "responseMimeType": "application/json",
            },
        }

        for idx, key in enumerate(self.keys, start=1):
            masked = mask_key(key)
            start_t = time.time()
            headers = {
                "Content-Type": "application/json",
                "x-goog-api-key": key,
            }

            try:
                resp = requests.post(
                    self.base_url,
                    headers=headers,
                    json=test_payload,
                    timeout=15,
                    verify=self.ca_bundle,
                )
                latency = round(time.time() - start_t, 2)

                if resp.status_code == 200:
                    data = resp.json()
                    candidates = data.get("candidates", [])
                    parts = candidates[0].get("content", {}).get("parts", []) if candidates else []
                    raw_text = parts[0].get("text", "").strip() if parts else "{}"
                    logger.info(f"Key #{idx} ({masked}): SUCCESS (Latency: {latency}s)")
                    results.append({
                        "key_index": idx,
                        "key_masked": masked,
                        "status": "VALID",
                        "status_code": 200,
                        "latency_sec": latency,
                        "response": raw_text,
                    })
                else:
                    err_info = resp.json().get("error", {}).get("message", resp.text)
                    logger.error(f"Key #{idx} ({masked}): FAILED ({resp.status_code}): {err_info}")
                    results.append({
                        "key_index": idx,
                        "key_masked": masked,
                        "status": "FAILED",
                        "status_code": resp.status_code,
                        "error": err_info,
                    })

            except Exception as e:
                logger.error(f"Key #{idx} ({masked}): EXCEPTION: {e}")
                results.append({
                    "key_index": idx,
                    "key_masked": masked,
                    "status": "EXCEPTION",
                    "error": str(e),
                })

        return results

    def evaluate_claim(
        self,
        passage: str,
        claim: str,
        query: Optional[str] = None,
        context_condition: str = "C1",
        use_cache: bool = True,
    ) -> Dict[str, Any]:
        """Evaluates a single claim against a context passage with Rubric v1 instructions."""
        system_prompt = (
            "You are an expert NLP benchmark judge evaluating factual faithfulness in Retrieval-Augmented Generation (RAG).\n"
            "Evaluate whether the provided atomic claim is entailed by the reference passage.\n"
            "Rules:\n"
            "- 'Supported': The claim is directly entailed or logically inferred from the passage.\n"
            "- 'Contradicted': The claim directly contradicts or negates facts asserted in the passage.\n"
            "- 'Not-in-context': The claim introduces external facts neither confirmed nor contradicted by the passage.\n"
            "Return valid JSON strictly matching this schema:\n"
            "{\n"
            '  "label": "Supported" | "Contradicted" | "Not-in-context",\n'
            '  "explanation": "concise rationale (1-2 sentences)",\n'
            '  "confidence": float between 0.0 and 1.0\n'
            "}"
        )

        user_prompt = (
            f"Context Condition: {context_condition}\n"
            f"Reference Passage:\n\"\"\"{passage}\"\"\"\n\n"
        )
        if query:
            user_prompt += f"User Query: {query}\n\n"
        user_prompt += f"Atomic Claim to Verify:\n\"\"\"{claim}\"\"\"\n\nProvide your JSON verdict:"

        response = self.generate_content(
            prompt=user_prompt,
            system_instruction=system_prompt,
            json_mode=True,
            use_cache=use_cache,
        )


        parsed = response.get("parsed_json") or {}
        label = parsed.get("label") or parsed.get("verdict")
        if not label:
            import re
            m = re.search(r'"(?:label|verdict)"\s*:\s*"([^"]+)"', response.get("content", ""))
            label = m.group(1) if m else "Not-in-context"

        label_normalized = str(label).strip()
        for valid in ["Supported", "Contradicted", "Not-in-context"]:
            if label_normalized.lower() == valid.lower():
                label_normalized = valid
                break

        return {
            "claim": claim,
            "label": label_normalized,
            "explanation": parsed.get("explanation") or parsed.get("rationale", ""),
            "confidence": parsed.get("confidence", 0.0),
            "cached": response.get("cached", False),
            "key_used": response.get("key_used", ""),
        }



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="NepFaith-120 Gemini Client Utility")
    parser.add_argument("--verify", action="store_true", help="Perform exactly 1 lightweight verification call per key")
    args = parser.parse_args()

    client = GeminiRotator()
    if args.verify or not args.verify:
        print("\n--- Testing 1 Lightweight Call Per Key ---")
        summary = client.verify_all_keys()
        print("\n--- Summary Report ---")
        print(json.dumps(summary, indent=2))
