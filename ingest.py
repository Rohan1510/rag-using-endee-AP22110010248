import os
import uuid
import json
import requests
from sentence_transformers import SentenceTransformer

ENDEE_URL = "http://localhost:8080"
INDEX_NAME = "rag_index"
DIMENSION = 384
LOCAL_CACHE = "local_vectors.json"

model = SentenceTransformer("all-MiniLM-L6-v2")


def reset_index():
    requests.post(
        f"{ENDEE_URL}/api/v1/index/delete",
        json={"name": INDEX_NAME}
    )
    requests.post(
        f"{ENDEE_URL}/api/v1/index/create",
        json={"name": INDEX_NAME, "dimension": DIMENSION}
    )


def chunk_text(text, size=300):
    words = text.split()
    return [" ".join(words[i:i + size]) for i in range(0, len(words), size)]


def ingest_documents():
    docs_dir = "data/documents"
    local_store = []

    for file in os.listdir(docs_dir):
        if not file.endswith(".txt"):
            continue

        with open(os.path.join(docs_dir, file), "r", encoding="utf-8") as f:
            text = f.read()

        chunks = chunk_text(text)
        embeddings = model.encode(chunks).tolist()

        vectors = []
        for chunk, emb in zip(chunks, embeddings):
            vectors.append({
                "id": str(uuid.uuid4()),
                "values": emb,
                "metadata": {
                    "text": chunk,
                    "source": file
                }
            })

            # Local cache for retrieval
            local_store.append({
                "text": chunk,
                "embedding": emb
            })

        requests.post(
            f"{ENDEE_URL}/api/v1/vector/upsert",
            json={"index": INDEX_NAME, "vectors": vectors}
        )

        print(f" Ingested: {file}")

    with open(LOCAL_CACHE, "w") as f:
        json.dump(local_store, f)

    print(" Ingestion complete (Endee + local cache)")


if __name__ == "__main__":
    print(" Resetting index")
    reset_index()
    ingest_documents()
