# src/language_models/summarizer.py

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

class ExtractiveSummarizer:
    def __init__(self, num_sentences=3):
        self.num_sentences = num_sentences

    def summarize(self, text):
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, self.num_sentences)
        return " ".join(str(sentence) for sentence in summary)

