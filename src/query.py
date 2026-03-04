import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import requests
import json

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 5

index = faiss.read_index("data/index.faiss")
chunks = np.load("data/chunks.npy", allow_pickle=True)
sources = np.load("data/chunk_sources.npy", allow_pickle=True)
embedder = SentenceTransformer(MODEL_NAME)

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" + API_KEY

def retrieve(query, k=TOP_K):
    q_emb = embedder.encode([query], convert_to_numpy=True)
    distances, indices = index.search(q_emb, k)
    return [chunks[i] for i in indices[0]]

def answer_question(query):
    context = "\n\n".join(retrieve(query))

    prompt = f"""
Use ONLY the following context from Archives of Nethys to answer the question.
If the answer is not in the context, say you don't know.

CONTEXT:
{context}

QUESTION:
{query}

ANSWER:
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(GEMINI_URL, json=payload)
    data = response.json()

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return f"Error: {json.dumps(data, indent=2)}"

if __name__ == "__main__":
    print("Gemini RAG (REST API) ready.")
    while True:
        q = input("\nAsk a question (or 'exit'): ")
        if q == "exit":
            break
        print(answer_question(q))
