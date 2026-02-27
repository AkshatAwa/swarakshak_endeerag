# SwaRakshak 2.0 – AI-Powered Legal Intelligence System  
### Retrieval-Augmented Generation (RAG) with Endee Vector Database

SwaRakshak 2.0 is an AI-driven Legal Intelligence backend that leverages a Retrieval-Augmented Generation (RAG) architecture to provide contextual, semantically accurate legal responses.

The system integrates the **Endee Vector Database** as the core semantic retrieval engine, enabling scalable vector similarity search over constitutional articles, landmark cases, and statutory provisions.

---

## Problem Statement

Legal information is vast, complex, and context-sensitive. Traditional keyword-based search fails to capture semantic meaning and nuanced interpretation of legal queries.

This project addresses:

- Context-aware legal query understanding
- Semantic similarity search across structured statutes
- Evidence-backed AI-generated responses
- Modular and scalable vector-based architecture

---

System Architecture


User Query
↓
Query Rewriter
↓
Embedding Model
↓
Endee Vector Database (Semantic Retrieval)
↓
Top-K Relevant Legal Context
↓
RAG Pipeline (Context Injection)
↓
Structured Legal Response


### Core Components

- **Embedding Layer** – Converts queries and legal documents into dense vectors.
- **Endee Vector Store** – Stores and retrieves embeddings using similarity search.
- **Retriever Module** – Fetches top-k semantically relevant chunks.
- **Generator Module** – Produces contextual, structured legal output.
- **Modular API Layer** – Exposes endpoints for analysis, research, and drafting.

---

Key Features

- Semantic Search over legal corpus
- Constitutional Article & Case Law Retrieval
- Context-aware AI Legal Explanation
- Modular RAG Pipeline
- Secure API key-based backend architecture
- Clean separation of frontend and backend services

---

Project Structure


Backend/
├── legalchat/
│ ├── api/
│ ├── services/
│ ├── data/
│ ├── memory/
│
├── LegalAPI/
├── Contract_Maker/
├── requirements.txt
└── .env.example

Frontend/
└── (UI Layer)


---

Example Workflow

### Query:
> "Is Right to Privacy a fundamental right in India?"

### System Flow:
1. Query rewritten into legal terminology
2. Embedding generated
3. Semantic similarity search performed in Endee
4. Relevant articles and judgments retrieved
5. Context injected into generator
6. Structured legal explanation returned

---

Tech Stack

- Python
- FastAPI
- Endee Vector Database
- Embedding Models (OpenAI / HF)
- Modular RAG Architecture
- JSON-based legal corpus
- PDF legal ingestion pipeline

---

 Environment Setup

Create a `.env` file in the Backend directory:


OPENAI_API_KEY=
ENDEE_API_KEY=


Install dependencies:


pip install -r requirements.txt


Run the server:


uvicorn app.main:app --reload


---

Why Vector Database?

Traditional databases are insufficient for semantic reasoning tasks.

Endee enables:

- High-dimensional vector storage
- Efficient similarity search
- Context-aware retrieval
- Scalable AI-native backend systems

This architecture ensures precision, relevance, and scalability in legal AI workflows.

---

Future Improvements

- Multi-document ingestion
- Hybrid search (keyword + semantic)
- Confidence scoring mechanism
- Fine-tuned legal embeddings
- Agentic AI workflow integration

---

Disclaimer

This project is for educational and research purposes and does not constitute legal advice.

---

👨‍💻 Author

Akshat Awasthi  
AI/ML Engineer | Legal AI Systems | Vector-Based Architectures
