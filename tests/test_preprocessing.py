import unittest
from src.data_processing.text_preprocessor import TextPreprocessor

class TestTextPreprocessor(unittest.TestCase):
    def test_clean_text(self):
        cleaner = TextPreprocessor()
        text = "Hello!!! This is a TEST -- of www.google.com, with URLs and punctuation."
        cleaned = cleaner.clean_text(text)
        self.assertIsInstance(cleaned, str)
        self.assertNotIn("http", cleaned)
        self.assertTrue("test" in cleaned.lower())

if __name__ == '__main__':
    unittest.main()

