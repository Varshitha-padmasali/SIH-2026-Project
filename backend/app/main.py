from __future__ import annotations

import sys
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parents[2]
AI_MODULE = ROOT / "ai" / "speech_translation"
if str(AI_MODULE) not in sys.path:
    sys.path.insert(0, str(AI_MODULE))

from pipeline import run_pipeline  # noqa: E402
from app.models import ProcessLessonRequest
from app.services.education_service import lesson_representation
from app.services.lesson_service import get_lesson, load_lessons

app = FastAPI(title="Smart Education Offline MVP", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict:
    return {"status": "ready", "mode": "offline-first", "network_required": False}


@app.get("/api/lessons")
def lessons() -> list[dict]:
    return [
        {key: lesson[key] for key in ("id", "title", "subject", "grade", "description", "icon")}
        for lesson in load_lessons()
    ]


@app.get("/api/lessons/{lesson_id}")
def lesson(lesson_id: str) -> dict:
    item = get_lesson(lesson_id)
    if item["id"] != lesson_id:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return item


@app.post("/api/process-lesson")
def process_lesson(request: ProcessLessonRequest) -> dict:
    result = run_pipeline(text=request.text, target_language="sat", make_audio=False)
    representation = lesson_representation(request.lesson_id, result.input_text)
    return {
        "input_text": result.input_text,
        "language": result.detected_language,
        "translation": result.translation,
        **representation,
        "offline_note": "The lesson pack and rule-based simplification run locally. Translation is a small, unverified Hindi–Santali glossary prototype.",
    }


FRONTEND = ROOT / "frontend"
if FRONTEND.exists():
    app.mount("/", StaticFiles(directory=FRONTEND, html=True), name="frontend")
