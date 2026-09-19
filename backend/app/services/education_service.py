from __future__ import annotations

import re

from app.services.lesson_service import get_lesson


def simplify_for_child(text: str, lesson: dict) -> str:
    """Use deterministic, local simplification for the small MVP lesson set."""
    normalized = re.sub(r"\s+", " ", text).strip()
    if lesson["id"] == "plants" and any(word in normalized for word in ("पौध", "सूर्य", "पानी")):
        return "पौधों को बढ़ने के लिए पानी, हवा, धूप और मिट्टी चाहिए।"
    sentences = re.split(r"[।.!?]+", normalized)
    first_sentence = next((sentence.strip() for sentence in sentences if sentence.strip()), normalized)
    return first_sentence[:180] + ("।" if not first_sentence.endswith("।") else "")


def matching_cards(text: str, lesson: dict) -> list[dict]:
    lowered = text.lower()
    cards = [
        card for card in lesson["flashcards"]
        if any(keyword.lower() in lowered for keyword in card["keywords"])
    ]
    return cards or lesson["flashcards"]


def lesson_representation(lesson_id: str, text: str) -> dict:
    lesson = get_lesson(lesson_id)
    return {
        "lesson": {key: lesson[key] for key in ("id", "title", "subject", "grade", "description", "hero")},
        "simple_explanation": simplify_for_child(text, lesson),
        "flashcards": matching_cards(text, lesson),
    }
