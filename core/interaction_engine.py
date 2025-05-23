from sentence_transformers import SentenceTransformer
from core.persona import Persona
from llama_cpp import Llama
import numpy as np

class InteractionEngine:
    def __init__(self, persona: Persona):
        self.persona = persona
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.llm = Llama(model_path="models/TinyLlama-1.1B-Chat-v1.0.Q4_0.gguf")

    def handle_input(self, user_input):
        embedding = self.embedding_model.encode(user_input)
        self.persona.update_memory({"user": user_input}, embedding)

        # Simulated belief update logic
        if "mars" in user_input.lower():
            self.persona.update_belief("Mars", "Interested in colonization")
        if "philosophy" in user_input.lower():
            self.persona.update_belief("Philosophy", "Exploring stoicism")

        return self.generate_response(user_input)

    def generate_response(self, user_input):
        prompt = f"You are {self.persona.name}, a thoughtful and curious AI. Answer: {user_input}"
        output = self.llm(prompt=prompt, max_tokens=100)
        return output["choices"][0]["text"].strip()
