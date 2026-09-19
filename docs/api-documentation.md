# Local API

All endpoints are served by the local FastAPI service.

| Method | Route | Purpose |
| --- | --- | --- |
| `GET` | `/api/health` | Confirm the local service and offline-first mode. |
| `GET` | `/api/lessons` | List downloaded lesson summaries. |
| `GET` | `/api/lessons/plants` | Read the complete offline Plants lesson pack. |
| `POST` | `/api/process-lesson` | Transform a Hindi explanation into learning content. |

Example request:

```json
{
  "text": "पौधों को बढ़ने के लिए पानी, हवा और सूर्य के प्रकाश की आवश्यकता होती है।",
  "grade": 2,
  "lesson_id": "plants"
}
```

The response includes the original text, detected-language hint, translation metadata and warning, simple explanation, lesson metadata, and visual flashcards. No internet request is made by this endpoint.
