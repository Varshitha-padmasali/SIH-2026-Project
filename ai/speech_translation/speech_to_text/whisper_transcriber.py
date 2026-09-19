from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TranscriptionResult:
    text: str
    language: str
    model_name: str
    method: str


def transcribe_audio(
    audio_path: str | Path,
    language: str = "hi",
    model_name: str = "base",
) -> TranscriptionResult:
    """Transcribe teacher audio with a local Whisper model.

    The openai-whisper package downloads model weights the first time a model is
    used. After weights are available locally, inference can run offline.
    """

    try:
        import whisper
    except ImportError as exc:
        raise RuntimeError(
            "openai-whisper is not installed. Install ai/speech_translation/requirements.txt "
            "or pass text directly to the pipeline for offline glossary testing."
        ) from exc

    path = Path(audio_path)
    if not path.exists():
        raise FileNotFoundError(f"Audio file not found: {path}")

    model = whisper.load_model(model_name)
    result = model.transcribe(str(path), language=language)

    return TranscriptionResult(
        text=result.get("text", "").strip(),
        language=result.get("language", language),
        model_name=model_name,
        method="local-whisper",
    )

