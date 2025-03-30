from transformers import pipeline
import os
from dotenv import load_dotenv

load_dotenv()

class GeneralAgent:
    def __init__(self):
        # Use HuggingFace pipeline for text generation (using HuggingFace API key)
        self.model = pipeline(
            "text-generation",
            model="gpt2",
            use_auth_token=os.getenv("HUGGINGFACE_API_KEY")
        )
    
    def query(self, question: str):
        response = self.model(question, max_length=150, num_return_sequences=1)
        return response[0]["generated_text"]
