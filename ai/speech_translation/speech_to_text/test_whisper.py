"""Manual Whisper smoke test.

Run from ai/speech_translation after installing requirements:

    PYTHONPATH=. python3 speech_to_text/test_whisper.py
"""


def main() -> None:
    import whisper

    model = whisper.load_model("base")

    result = model.transcribe(
        "speech_to_text/audio/sample.m4a",
        language="hi"
    )

    print("Transcription:")
    print(result["text"])


if __name__ == "__main__":
    main()
