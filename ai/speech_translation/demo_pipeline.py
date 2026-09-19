from __future__ import annotations

import argparse
import json

from pipeline import run_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the SIH26042 speech and translation MVP pipeline.")
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--text", help="Hindi teacher text to process directly.")
    input_group.add_argument("--audio", help="Path to teacher audio for local Whisper transcription.")
    parser.add_argument("--target-language", default="sat", help="Target language code. Default: sat.")
    parser.add_argument("--make-audio", action="store_true", help="Generate local demo TTS audio when available.")
    parser.add_argument("--output-audio", default="outputs/translated_audio.aiff")
    args = parser.parse_args()

    result = run_pipeline(
        text=args.text,
        audio_path=args.audio,
        target_language=args.target_language,
        make_audio=args.make_audio,
        output_audio_path=args.output_audio,
    )
    print(json.dumps(result.__dict__, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

