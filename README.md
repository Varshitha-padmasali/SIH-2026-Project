# Siksha Saathi — Smart Education (SIH26042)

An offline-first MVP that helps a teacher turn a short Hindi EVS explanation into child-friendly learning cards. The first complete flow targets **Class 2 · EVS · Plants** and uses a deliberately limited Hindi → Santali prototype path.

## What works now

- A responsive tablet-style teacher and child learning experience.
- Local Class 2 Plants lesson pack and visual flashcards.
- Teacher text → language hint → offline glossary translation → child-friendly explanation → matched learning cards.
- Existing local Whisper integration remains available for audio transcription when its model is preloaded.
- Clear in-product warnings for the unverified Santali glossary and device speech fallback.

## Run the MVP

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
PYTHONPATH=backend uvicorn app.main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). The browser UI is served by the backend, so the demo needs no separate frontend build step.

## Test

```bash
PYTHONPATH=backend python3 -m pytest backend/tests
cd ai/speech_translation && PYTHONPATH=. python3 -m unittest discover -s tests
```

## Offline boundary

The lesson pack, educational mapping, simplifier, and prototype glossary are local. The current Hindi → Santali output is a **small draft word-level glossary**, not validated machine translation. Browser voice recognition and browser speech playback are convenience fallbacks for this desktop demo; a deployment tablet must use verified local ASR and Santali TTS or recorded audio.

See [architecture.md](docs/architecture.md) for the component boundaries and [API documentation](docs/api-documentation.md) for endpoint details.
