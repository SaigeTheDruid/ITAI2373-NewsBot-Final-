# src/language_models/embeddings.py

from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def get_embedding(self, text):
        return self.model.encode(text)

    def get_batch_embeddings(self, texts):
        return self.model.encode(texts, convert_to_tensor=True)

