from googletrans import Translator

class TextTranslator:
    def __init__(self):
        self.translator = Translator()

    def translate_text(self, text, dest_language='en'):
        try:
            result = self.translator.translate(text, dest=dest_language)
            return result.text
        except Exception as e:
            return f"Translation error: {str(e)}"

