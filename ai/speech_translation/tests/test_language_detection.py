import unittest

from language_detection import detect_language


class LanguageDetectionTests(unittest.TestCase):
    def test_detects_hindi_from_devanagari(self) -> None:
        result = detect_language("पौधों को पानी की आवश्यकता होती है।")

        self.assertEqual(result.language_code, "hi")
        self.assertGreater(result.confidence, 0.5)

    def test_detects_unknown_for_empty_text(self) -> None:
        result = detect_language("  ")

        self.assertEqual(result.language_code, "unknown")
        self.assertEqual(result.confidence, 0.0)


if __name__ == "__main__":
    unittest.main()
