# Offline-first architecture

```text
Teacher Hindi text / locally transcribed voice
             │
             ▼
  speech_translation pipeline (local module)
  ├─ language script heuristic
  └─ Hindi → Santali draft glossary
             │
             ▼
 education service (local, deterministic)
 ├─ age-appropriate simplification
 └─ flashcard keyword mapping
             │
             ▼
 FastAPI local API → static tablet UI → child learning cards
```

`data/lessons/class_2_evs.json` is the offline lesson pack. It is intentionally structured so future lessons, images, verified vocabulary, and pre-recorded audio can be added without changing the API.

The pipeline distinguishes implementation from aspiration:

- Implemented locally: lesson data, concept mapping, simplification rules, script-based language hint, small glossary translation, and FastAPI UI/API wiring.
- Optional local component: Whisper transcription after a model is downloaded and cached.
- Not yet verified for deployment: Santali translation quality and Santali TTS. These require language-speaker review and target-tablet evaluation.

When connectivity is available, it should only update versioned lesson packs or model resources; the core lesson flow must remain available from the device cache.
