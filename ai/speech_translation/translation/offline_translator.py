from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "prototype_glossary_hi_sat.json"


@dataclass(frozen=True)
class TranslationResult:
    source_language: str
    target_language: str
    source_text: str
    translated_text: str
    confidence: float
    method: str
    warning: str | None = None


def _load_glossary() -> dict[str, str]:
    with DATA_PATH.open("r", encoding="utf-8") as file:
        raw = json.load(file)
    return {item["hi"]: item["sat"] for item in raw["entries"]}


def _tokenize_hindi(text: str) -> list[str]:
    return re.findall(r"[\u0900-\u0963\u0970-\u097f]+|[A-Za-z]+|\d+|[^\s]", text)


def _join_tokens(tokens: list[str]) -> str:
    text = " ".join(tokens)
    text = re.sub(r"\s+([।,.!?])", r"\1", text)
    return text.strip()


def translate_text(
    text: str,
    source_language: str = "hi",
    target_language: str = "sat",
) -> TranslationResult:
    """Translate Hindi text to prototype Santali using an offline glossary.

    This is not a full machine translation system. It is a deterministic MVP
    bridge that proves the offline pipeline shape while the team evaluates real
    Santali datasets, speakers, and model options.
    """

    if source_language != "hi" or target_language != "sat":
        return TranslationResult(
            source_language=source_language,
            target_language=target_language,
            source_text=text,
            translated_text=text,
            confidence=0.0,
            method="unsupported-language-pair",
            warning="Only the Hindi to Santali prototype path is implemented.",
        )

    glossary = _load_glossary()
    tokens = _tokenize_hindi(text)
    translated_tokens: list[str] = []
    translated_count = 0

    for token in tokens:
        replacement = glossary.get(token)
        if replacement:
            translated_tokens.append(replacement)
            translated_count += 1
        else:
            translated_tokens.append(token)

    translated_text = _join_tokens(translated_tokens)
    lexical_coverage = translated_count / max(len([t for t in tokens if re.search(r"[\u0900-\u097f]", t)]), 1)
    confidence = min(0.70, 0.20 + lexical_coverage * 0.50)

    return TranslationResult(
        source_language=source_language,
        target_language=target_language,
        source_text=text,
        translated_text=translated_text,
        confidence=round(confidence, 2),
        method="offline-glossary-prototype",
        warning="Prototype word-level translation. Validate with Santali speakers before demo claims.",
    )
