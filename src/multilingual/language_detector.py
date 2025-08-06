from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0  # for consistent results

class LanguageDetector:
    def detect_language(self, text):
        try:
            return detect(text)
        except:
            return "unknown"

