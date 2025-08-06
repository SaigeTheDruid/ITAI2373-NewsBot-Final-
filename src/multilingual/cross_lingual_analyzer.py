from langdetect import detect
from src.multilingual.translator import TextTranslator
from src.analysis.sentiment_analyzer import SentimentAnalyzer
from src.analysis.topic_modeler import TopicModeler

class CrossLingualAnalyzer:
    def __init__(self, target_language='en'):
        self.translator = TextTranslator()
        self.sentiment = SentimentAnalyzer()
        self.topic_modeler = TopicModeler(method='lda', num_topics=3)
        self.target_language = target_language

    def analyze_texts(self, texts):
        translated = []
        for text in texts:
            if detect(text) != self.target_language:
                translated.append(self.translator.translate_text(text, dest_language=self.target_language))
            else:
                translated.append(text)

        sentiments = [self.sentiment.analyze_sentiment(t) for t in translated]
        self.topic_modeler.fit(translated)
        topics = self.topic_modeler.display_topics()

        return {
            "sentiments": sentiments,
            "topics": topics
        }

