from __future__ import annotations

import platform
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TTSResult:
    audio_path: str | None
    method: str
    warning: str | None = None


def synthesize_speech(text: str, output_path: str | Path, language: str = "hi") -> TTSResult:
    """Create offline speech audio when a local OS voice is available.

    macOS `say` is useful for demo wiring but voice availability for Santali is
    not guaranteed. For SIH claims, replace this with a verified local TTS model
    or recorded speaker audio.
    """

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if platform.system() != "Darwin":
        return TTSResult(
            audio_path=None,
            method="not-available",
            warning="Offline TTS currently uses macOS say. Add a verified local TTS engine for deployment tablets.",
        )

    command = ["say", "-o", str(path), text]
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        return TTSResult(
            audio_path=None,
            method="macos-say-failed",
            warning=completed.stderr.strip() or "macOS say failed.",
        )

    return TTSResult(
        audio_path=str(path),
        method="macos-say-offline",
        warning=(
            "Generated with local macOS voice. This does not prove Santali TTS support; "
            "use verified recorded audio or a tested local TTS model for final demo."
        ),
    )

