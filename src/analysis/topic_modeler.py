from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

class TopicModeler:
    def __init__(self, method='lda', num_topics=5, max_features=1000):
        self.method = method
        self.num_topics = num_topics
        self.max_features = max_features
        self.model = None
        self.feature_names = None

    def fit(self, texts):
        if self.method == 'lda':
            vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=self.max_features, stop_words='english')
            data_vectorized = vectorizer.fit_transform(texts)
            model = LatentDirichletAllocation(n_components=self.num_topics, random_state=42)
        else:
            vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=self.max_features, stop_words='english')
            data_vectorized = vectorizer.fit_transform(texts)
            model = NMF(n_components=self.num_topics, random_state=42)

        self.model = model.fit(data_vectorized)
        self.feature_names = vectorizer.get_feature_names_out()
        return self.model

    def display_topics(self, num_top_words=10):
        topics = []
        for topic_idx, topic in enumerate(self.model.components_):
            top_features = [self.feature_names[i] for i in topic.argsort()[:-num_top_words - 1:-1]]
            topics.append((f"Topic {topic_idx}", top_features))
        return topics

