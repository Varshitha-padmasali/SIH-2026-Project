import unittest

from translation import translate_text


class TranslationTests(unittest.TestCase):
    def test_hindi_to_santali_glossary_translation_marks_known_words(self) -> None:
        result = translate_text("पौधों को पानी और सूर्य के प्रकाश की आवश्यकता होती है।")

        self.assertEqual(result.source_language, "hi")
        self.assertEqual(result.target_language, "sat")
        self.assertIn("dak", result.translated_text)
        self.assertIn("singi", result.translated_text)
        self.assertIn("kana", result.translated_text)
        self.assertEqual(result.method, "offline-glossary-prototype")
        self.assertTrue(result.warning)

    def test_unsupported_pair_returns_warning(self) -> None:
        result = translate_text("Plants need water.", source_language="en", target_language="sat")

        self.assertEqual(result.translated_text, "Plants need water.")
        self.assertEqual(result.confidence, 0.0)
        self.assertTrue(result.warning)


if __name__ == "__main__":
    unittest.main()
