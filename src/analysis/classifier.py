from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

class NewsClassifier:
    def __init__(self, model_type='svm'):
        self.model_type = model_type
        self.pipeline = self._build_pipeline()

    def _build_pipeline(self):
        model = LinearSVC() if self.model_type == 'svm' else MultinomialNB()
        pipeline = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', model)
        ])
        return pipeline

    def train(self, X_train, y_train):
        self.pipeline.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        preds = self.pipeline.predict(X_test)
        acc = accuracy_score(y_test, preds)
        report = classification_report(y_test, preds, output_dict=True)
        conf_matrix = confusion_matrix(y_test, preds)
        return {
            'accuracy': acc,
            'classification_report': report,
            'confusion_matrix': conf_matrix
        }

    def predict(self, texts):
        return self.pipeline.predict(texts)

