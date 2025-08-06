import unittest

from src.data_processing.text_preprocessor import TextPreprocessor
from src.analysis.classifier import NewsClassifier
from src.analysis.topic_modeler import TopicModeler
from src.analysis.sentiment_analyzer import SentimentAnalyzer
from src.analysis.ner_extractor import NERExtractor


class TestNewsBotIntegration(unittest.TestCase):
    def setUp(self):
        self.sample_texts = [
            "The president held a press conference today in Washington.",
            "Tesla stocks have skyrocketed due to innovation in AI.",
            "Manchester United won their last match against Liverpool."
        ]
        self.labels = ["politics", "technology", "sports"]  # Mock labels for training

        self.cleaner = TextPreprocessor()
        self.classifier = NewsClassifier(model_type='svm')
        self.topic_modeler = TopicModeler(method='lda', num_topics=2)
        self.sentiment_analyzer = SentimentAnalyzer()
        self.ner_extractor = NERExtractor()

    def test_end_to_end_pipeline(self):
        # Preprocessing
        cleaned = [self.cleaner.clean_text(text) for text in self.sample_texts]
        self.assertEqual(len(cleaned), len(self.sample_texts))

        # Classification
        self.classifier.train(cleaned, self.labels)
        preds = self.classifier.predict(["AI is transforming the car industry"])
        self.assertEqual(len(preds), 1)

        # Topic Modeling
        self.topic_modeler.fit(cleaned)
        topics = self.topic_modeler.display_topics()
        self.assertGreater(len(topics), 0)

        # Sentiment
        result = self.sentiment_analyzer.analyze_sentiment(self.sample_texts[0])
        self.assertIn(result['sentiment'], ['positive', 'neutral', 'negative'])

        # Named Entity Recognition
        entities = self.ner_extractor.extract_entities(self.sample_texts[0])
        self.assertIsInstance(entities, list)

if __name__ == '__main__':
    unittest.main()

