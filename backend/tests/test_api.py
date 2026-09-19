from app.main import health, process_lesson
from app.models import ProcessLessonRequest


def test_health_is_offline_first():
    assert health()["network_required"] is False


def test_process_plants_lesson():
    body = process_lesson(
        ProcessLessonRequest(
            text="पौधों को बढ़ने के लिए पानी, हवा और सूर्य के प्रकाश की आवश्यकता होती है।"
        )
    )
    assert body["lesson"]["id"] == "plants"
    assert body["translation"]["method"] == "offline-glossary-prototype"
    assert len(body["flashcards"]) == 3
