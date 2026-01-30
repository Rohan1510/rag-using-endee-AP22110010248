Here is the corrected, **single-file Markdown code**.

I fixed the broken code blocks in the *Setup & Usage* section so each command is isolated and copy-paste ready. You can copy this entire block and paste it directly into your `README.md`.

```markdown
#  RAG using Endee Vector Database

##  Project Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system using **Endee** as the vector database. It allows users to ask natural language questions and receive **accurate, grounded answers** strictly based on the indexed documents.

The system is designed to:
- Retrieve only **relevant information**
- Reject **out-of-scope queries**
- Avoid **hallucinated responses**
- Present answers in a **clear and ordered format**

---

##  Problem Statement
Traditional question-answering systems may generate responses without verifying whether the information exists in the knowledge base. This project addresses that issue by combining **semantic vector retrieval** with **intent-aware filtering**, ensuring answers are returned **only when supported by the ingested data**.

---

##  Use Case
* **Question Answering** over custom documents
* **Semantic Search** using vector similarity
* **RAG Architecture Demonstration**
* Accurate handling of **what / how / who / where** queries

---

##  System Architecture
1. **Document Ingestion** – Text documents are loaded and chunked.
2. **Embedding Generation** – Sentence embeddings generated using Sentence Transformers.
3. **Vector Storage** – Embeddings stored using Endee.
4. **Semantic Retrieval** – Cosine similarity-based matching.
5. **Intent-Aware Filtering** – Ensures compatibility between query type and content.
6. **Answer Structuring** – Outputs ordered, readable responses (definition → explanation).

---

##  Tech Stack
* **Python 3.9+**
* **Endee Vector Database**
* **Sentence Transformers**
* **NumPy**
* **Scikit-learn**
* **Docker**

---

## ⚙️ Setup & Usage

### 1. Prerequisites
Ensure the following are installed:
* Python 3.9+
* Docker & Docker Compose

### 2. Run Endee Database
Start the Endee vector database container:

```bash
docker compose up -d

```

### 3. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt

```

### 4. Ingest Documents

Process documents and store embeddings:

```bash
python ingest.py

```

### 5. Query the System

Run the query interface:

```bash
python rag_query.py

```

---

##  Example Queries

Try these inputs to test the system:

* `what is cloud computing`
* `how does cloud computing work`
* `what is infrastructure as a service`

###  Out-of-Scope Example

If a question is not supported by the indexed documents, the system rejects it:

> **Input:** `who is rohan`
> **Response:** *[System indicates information is not available]*

---

##  Design Decisions

* **Semantic Confidence Floor:** Prevents unrelated queries from returning results.
* **Hybrid Matching:** Keyword overlap is applied only when semantic similarity is reasonable.
* **Intent Awareness:** Query intent (what/how/who/where) is checked before retrieval.
* **Structured Answers:** Improves readability without generating new information.
* **No Generative LLM:** Retrieval-only approach avoids hallucination entirely.

---

##  Limitations

* **Strict Dependency:** Answers depend strictly on the content of the ingested documents.
* **API Constraints:** The open-source Endee build does not expose full vector search APIs, so retrieval logic is implemented at the application layer.

---

##  Author

**Rohan Krishna Surapaneni**

* SRM University – AP
* B.Tech (Computer Science & Engineering)

---

##  License

This project is intended for academic and evaluation purposes.


```