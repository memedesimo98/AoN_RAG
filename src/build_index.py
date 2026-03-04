import os
import glob
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# -------------------------------
# Config
# -------------------------------

DATA_DIRS = [
    "data/races",
    "data/feats"
]

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# -------------------------------
# Loader
# -------------------------------

def load_all_texts():
    documents = []

    for folder in DATA_DIRS:
        for path in glob.glob(os.path.join(folder, "*.txt")):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
                documents.append((path, text))

    return documents

# -------------------------------
# Chunker
# -------------------------------

def chunk_text(text, size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()
    chunks = []

    i = 0
    while i < len(words):
        chunk = words[i:i+size]
        chunks.append(" ".join(chunk))
        i += size - overlap

    return chunks

# -------------------------------
# Build index
# -------------------------------

def build_index():
    print("Loading model...")
    model = SentenceTransformer(MODEL_NAME)

    print("Loading documents...")
    docs = load_all_texts()

    all_chunks = []
    chunk_sources = []

    print("Chunking documents...")
    for path, text in docs:
        chunks = chunk_text(text)
        all_chunks.extend(chunks)
        chunk_sources.extend([path] * len(chunks))

    print(f"Total chunks: {len(all_chunks)}")

    print("Embedding chunks...")
    embeddings = model.encode(all_chunks, convert_to_numpy=True, show_progress_bar=True)

    print("Building FAISS index...")
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    print("Saving index...")
    faiss.write_index(index, "data/index.faiss")

    np.save("data/chunk_sources.npy", np.array(chunk_sources))
    np.save("data/chunks.npy", np.array(all_chunks))

    print("Index built successfully!")

if __name__ == "__main__":
    build_index()
