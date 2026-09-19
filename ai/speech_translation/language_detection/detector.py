from __future__ import annotations

from dataclasses import dataclass


DEVANAGARI_START = "\u0900"
DEVANAGARI_END = "\u097f"
OL_CHIKI_START = "\u1c50"
OL_CHIKI_END = "\u1c7f"


@dataclass(frozen=True)
class LanguageDetectionResult:
    language_code: str
    language_name: str
    confidence: float
    method: str


LANGUAGE_NAMES = {
    "hi": "Hindi",
    "sat": "Santali",
    "en": "English",
    "unknown": "Unknown",
}


def _count_chars_in_range(text: str, start: str, end: str) -> int:
    return sum(start <= char <= end for char in text)


def detect_language(text: str) -> LanguageDetectionResult:
    """Detect a small set of languages required by the MVP.

    This intentionally avoids claiming broad language ID coverage. The MVP only
    needs a reliable enough hint for Hindi input and possible Santali text.
    """

    normalized = text.strip()
    if not normalized:
        return LanguageDetectionResult("unknown", "Unknown", 0.0, "empty-input")

    devanagari = _count_chars_in_range(normalized, DEVANAGARI_START, DEVANAGARI_END)
    ol_chiki = _count_chars_in_range(normalized, OL_CHIKI_START, OL_CHIKI_END)
    letters = sum(char.isalpha() for char in normalized)

    if ol_chiki:
        confidence = min(0.99, 0.55 + (ol_chiki / max(letters, 1)))
        return LanguageDetectionResult("sat", LANGUAGE_NAMES["sat"], confidence, "unicode-script")

    if devanagari:
        confidence = min(0.98, 0.50 + (devanagari / max(letters, 1)))
        return LanguageDetectionResult("hi", LANGUAGE_NAMES["hi"], confidence, "unicode-script")

    ascii_letters = sum(("a" <= char.lower() <= "z") for char in normalized)
    if ascii_letters:
        confidence = min(0.75, 0.30 + (ascii_letters / max(letters, 1)) * 0.45)
        return LanguageDetectionResult("en", LANGUAGE_NAMES["en"], confidence, "latin-script-heuristic")

    return LanguageDetectionResult("unknown", "Unknown", 0.1, "fallback")

