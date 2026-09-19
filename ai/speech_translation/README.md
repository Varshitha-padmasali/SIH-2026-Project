# Speech + Translation Module

Member 2 owns the pipeline from teacher audio to translated child-facing audio:

```text
Audio
↓
Speech-to-Text
↓
Language Identification
↓
Translation
↓
Text-to-Speech
```

This module is intentionally offline-first. It includes a working local pipeline shape, but it does **not** claim full Santali machine translation yet.

## Current Prototype

- Speech-to-text: local Whisper through `openai-whisper`.
- Language detection: lightweight script heuristics for Hindi, Santali/Ol Chiki, English, and unknown.
- Translation: offline Hindi to Santali glossary prototype for MVP wiring.
- Text-to-speech: optional local macOS `say` output for demo wiring only.

Important: the glossary contains draft transliteration placeholders and must be validated by Santali speakers before SIH presentation claims.

## Setup

```bash
cd ai/speech_translation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Whisper downloads model weights the first time a model is used. After the weights are cached locally, inference can run offline.

## Run Text Pipeline

```bash
cd ai/speech_translation
PYTHONPATH=. python demo_pipeline.py \
  --text "बच्चों, पौधों को बढ़ने के लिए पानी, हवा और सूर्य के प्रकाश की आवश्यकता होती है।"
```

## Run Audio Pipeline

```bash
cd ai/speech_translation
PYTHONPATH=. python demo_pipeline.py --audio speech_to_text/audio/sample.m4a
```

## Optional Demo Audio Output

```bash
cd ai/speech_translation
PYTHONPATH=. python demo_pipeline.py \
  --text "पौधों को पानी और सूर्य के प्रकाश की आवश्यकता होती है।" \
  --make-audio
```

This uses the local macOS voice if available. It should be replaced with verified recorded Santali audio or a tested offline TTS model for the real tablet demo.

## Tests

```bash
cd ai/speech_translation
PYTHONPATH=. python3 -m unittest discover -s tests
```

## Next Member 2 Tasks

1. Validate the selected tribal language and script with SIH requirements and available speakers.
2. Replace the prototype glossary with verified vocabulary and common classroom phrases.
3. Evaluate Bhashini for prototype mode, clearly labeling it as online if it needs internet.
4. Investigate offline ASR/TTS options for the target tablet hardware.
5. Add translation quality checks using human review and small parallel sentence sets.
