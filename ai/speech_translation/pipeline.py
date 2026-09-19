from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

from language_detection import detect_language
from speech_to_text import transcribe_audio
from text_to_speech import synthesize_speech
from translation import translate_text


@dataclass(frozen=True)
class SpeechTranslationPipelineResult:
    input_text: str
    detected_language: dict
    translation: dict
    tts: dict | None


def run_pipeline(
    text: str | None = None,
    audio_path: str | Path | None = None,
    target_language: str = "sat",
    make_audio: bool = False,
    output_audio_path: str | Path = "outputs/translated_audio.aiff",
) -> SpeechTranslationPipelineResult:
    if not text and not audio_path:
        raise ValueError("Provide either text or audio_path.")

    if text:
        input_text = text.strip()
    else:
        transcription = transcribe_audio(audio_path=audio_path)
        input_text = transcription.text

    detected = detect_language(input_text)
    translation = translate_text(
        input_text,
        source_language=detected.language_code if detected.language_code != "unknown" else "hi",
        target_language=target_language,
    )

    tts_result = None
    if make_audio:
        tts_result = synthesize_speech(
            translation.translated_text,
            output_path=output_audio_path,
            language=target_language,
        )

    return SpeechTranslationPipelineResult(
        input_text=input_text,
        detected_language=asdict(detected),
        translation=asdict(translation),
        tts=asdict(tts_result) if tts_result else None,
    )

