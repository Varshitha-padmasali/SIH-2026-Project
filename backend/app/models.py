from __future__ import annotations

from pydantic import BaseModel, Field


class ProcessLessonRequest(BaseModel):
    text: str = Field(min_length=1, max_length=1_000, description="Teacher explanation in Hindi")
    grade: int = Field(default=2, ge=1, le=5)
    lesson_id: str = "plants"


class LessonSummary(BaseModel):
    id: str
    title: str
    subject: str
    grade: int
    description: str
    icon: str
