import unittest
from src.analysis.classifier import NewsClassifier

class TestNewsClassifier(unittest.TestCase):
    def test_train_predict(self):
        X = ["AI is great", "Sports are fun", "Government news today"]
        y = ["tech", "sports", "politics"]
        model = NewsClassifier(model_type='svm')
        model.train(X, y)
        preds = model.predict(["AI breakthrough"])
        self.assertEqual(len(preds), 1)

if __name__ == '__main__':
    unittest.main()

