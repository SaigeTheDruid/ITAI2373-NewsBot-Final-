# src/language_models/generator.py

from transformers import pipeline, set_seed

class TextGenerator:
    def __init__(self, model_name="gpt2", max_length=100):
        self.generator = pipeline("text-generation", model=model_name)
        self.max_length = max_length

    def generate_text(self, prompt, seed=42):
        set_seed(seed)
        results = self.generator(prompt, max_length=self.max_length, num_return_sequences=1)
        return results[0]['generated_text']

