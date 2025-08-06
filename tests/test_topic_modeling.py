import unittest
from src.analysis.topic_modeler import TopicModeler

class TestTopicModeler(unittest.TestCase):
    def test_topic_extraction(self):
        texts = [
            "The economy is growing fast with new policies.",
            "The stock market fluctuated after economic reforms.",
            "New tax laws affect businesses and investments."
        ]
        tm = TopicModeler(method='lda', num_topics=2)
        tm.fit(texts)
        topics = tm.display_topics()
        self.assertTrue(len(topics) > 0)

if __name__ == '__main__':
    unittest.main()

