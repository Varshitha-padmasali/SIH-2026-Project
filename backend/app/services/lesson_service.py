from __future__ import annotations

import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parents[3] / "data" / "lessons" / "class_2_evs.json"


def load_lessons() -> list[dict]:
    with DATA_FILE.open(encoding="utf-8") as file:
        return json.load(file)["lessons"]


def get_lesson(lesson_id: str) -> dict:
    return next((lesson for lesson in load_lessons() if lesson["id"] == lesson_id), load_lessons()[0])
