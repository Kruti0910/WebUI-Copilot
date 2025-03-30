from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import FAISS
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
import os

class ClinicalAgent:
    def __init__(self, data):
        # Set Hugging Face API Key
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = "your_huggingface_api_key_here"

        # Load SentenceTransformer model from Hugging Face
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

        # Generate embeddings for each piece of data
        embeddings = [self.model.encode(doc) for doc in data]

        # Convert to a compatible format (texts, embeddings)
        text_embeddings = list(zip(data, embeddings))

        # Initialize FAISS vector store with texts and embeddings
        self.vector_store = FAISS.from_embeddings(
            text_embeddings=text_embeddings,
            embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        )

    def query(self, question: str):
        # Generate the embedding for the query
        query_embedding = self.model.encode(question)

        # Perform a similarity search
        response = self.vector_store.similarity_search(query_embedding)

        return response
