import json
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

LOCAL_CACHE = "local_vectors.json"

# Thresholds
MIN_SEMANTIC_FLOOR = 0.30
SIMILARITY_THRESHOLD = 0.55

model = SentenceTransformer("all-MiniLM-L6-v2")


def load_vectors():
    with open(LOCAL_CACHE, "r") as f:
        return json.load(f)


def detect_intent(question):
    q = question.lower().strip()
    if q.startswith("who"):
        return "PERSON"
    if q.startswith("where"):
        return "LOCATION"
    if q.startswith("how"):
        return "PROCESS"
    if q.startswith("what"):
        return "DEFINITION"
    return "GENERAL"


def intent_compatible(intent, text):
    text = text.lower()

    if intent == "PERSON":
        return False  # no people in docs

    if intent == "LOCATION":
        return any(word in text for word in ["region", "location", "place", "network", "edge"])

    if intent == "PROCESS":
        return any(word in text for word in ["steps", "process", "how", "works", "method"])

    if intent == "DEFINITION":
        return any(word in text for word in ["is", "refers", "defined", "model", "service"])

    return True


def retrieve_context(question, top_k=3):
    data = load_vectors()

    texts = [item["text"] for item in data]
    vectors = np.array([item["embedding"] for item in data])

    query_vec = model.encode(question).reshape(1, -1)
    scores = cosine_similarity(query_vec, vectors)[0]

    best_score = float(scores.max())
    best_indices = scores.argsort()[-top_k:][::-1]

    if best_score < MIN_SEMANTIC_FLOOR:
        return [], best_score

    intent = detect_intent(question)
    contexts = []

    for i in best_indices:
        if scores[i] >= SIMILARITY_THRESHOLD and intent_compatible(intent, texts[i]):
            contexts.append(texts[i])

    return contexts, best_score


def generate_answer(contexts, question):
    text = contexts[0]

    q = question.lower()

    # Normalize text
    lines = text.replace("\n", " ").split(".")

    definition = []
    working = []

    for line in lines:
        l = line.lower()

        # Definition patterns
        if "is" in l and "cloud" in l and len(definition) < 2:
            definition.append(line.strip())

        # How it works patterns
        if "how does" in l or "front end" in l or "back end" in l or "servers" in l:
            working.append(line.strip())

    answer = ""

    if q.startswith("what"):
        answer += "Definition:\n"
        answer += "- " + ". ".join(definition[:2]) + "\n\n"

        if working:
            answer += "How it works:\n"
            for i, step in enumerate(working[:4], 1):
                answer += f"{i}. {step}\n"

    elif q.startswith("how"):
        answer += "How it works:\n"
        for i, step in enumerate(working[:5], 1):
            answer += f"{i}. {step}\n"

    else:
        answer = text[:600]

    return answer



if __name__ == "__main__":
    question = input("Ask a question: ")

    contexts, score = retrieve_context(question)

    print(f"\n Best similarity score: {score:.3f}")

    if not contexts:
        print("\n Retrieved Context:")
        print("No relevant context found.")

        print("\n Answer:")
        print(
            "No relevant information was found in the indexed documents. "
            "Please ask a question related to the uploaded content."
        )
    else:
        print("\n Retrieved Context:")
        for c in contexts:
            print("-", c[:200], "...")

        print("\n Answer:")
        print(generate_answer(contexts, question))
        