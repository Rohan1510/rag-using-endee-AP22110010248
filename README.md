# RAG using Endee Vector Database

## Project Overview
This project implements a **Retrieval-Augmented Generation (RAG)** system using **Endee** as the vector database.  
It allows users to ask natural language questions and receive **accurate, grounded answers** strictly based on the indexed documents.

The system is designed to:
- Retrieve only **relevant information**
- Reject **out-of-scope queries**
- Avoid hallucinated responses
- Present answers in a **clear and ordered format**

---

## Problem Statement
Traditional question-answering systems often generate responses without verifying whether the information exists in the knowledge base.  
This project addresses that issue by combining **semantic vector retrieval** with **intent-aware filtering**, ensuring answers are returned **only when supported by data**.

---

## Use Case
- Question answering over custom documents  
- Semantic search  
- Demonstration of RAG architecture  
- Accurate handling of *what / how / who / where* queries  

---

## System Architecture
1. Document ingestion and chunking  
2. Embedding generation using Sentence Transformers  
3. Vector storage using Endee  
4. Semantic similarity-based retrieval  
5. Intent-aware filtering (who / what / how / where)  
6. Structured answer generation (definition → explanation)

---

## Why Endee
Endee is used as the **vector database** for storing and managing document embeddings.

Due to limited public REST exposure for vector search in the open-source build, a **hybrid retrieval approach** is used:
- Endee serves as the system of record for vectors  
- Retrieval logic is handled at the application layer  

This mirrors real-world production systems where **storage and retrieval are decoupled**.

---

## Key Features
- Real vector embeddings (no mock or simulation)  
- Confidence-based semantic retrieval  
- Intent-aware query handling  
- Clean and ordered answers  
- Out-of-scope query rejection  
- No hallucinated responses  

---

## Tech Stack
- Python  
- Endee Vector Database  
- Sentence Transformers  
- NumPy  
- Scikit-learn  
- Docker  

---

## Setup Instructions

### Prerequisites
- Python 3.9+  
- Docker & Docker Compose  

---

### Run Endee
```bash
docker compose up -d
