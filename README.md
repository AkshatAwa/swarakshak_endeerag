SwaRakshak 2.0 – AI-Powered Legal Intelligence System
Endee-Based Retrieval-Augmented Generation (RAG) Architecture

SwaRakshak 2.0 is a modular Legal AI backend built on a Retrieval-Augmented Generation (RAG) architecture.

The system integrates the Endee Vector Database as its semantic retrieval engine and uses a local embedding model via Ollama to enable fully self-contained, scalable AI workflows without reliance on external embedding APIs.

Overview

Legal information is extensive, context-sensitive, and structurally complex. Traditional keyword-based search systems fail to capture semantic meaning, interpret nuance, and connect relevant statutory provisions or judicial precedents.

SwaRakshak 2.0 addresses these limitations through:

Semantic similarity search over structured legal corpora

Context-aware query rewriting

Evidence-backed AI response generation

Modular, scalable vector-based infrastructure

System Architecture

User Query
↓
Query Rewriter (Legal Normalization)
↓
Local Embedding Model (Ollama – mxbai-embed-large)
↓
Endee Vector Database (Semantic Retrieval)
↓
Top-K Relevant Legal Context
↓
RAG Context Injection
↓
Structured Legal Response

Core Components
1. Embedding Layer

Local embedding generation using the mxbai-embed-large model via Ollama

No external API dependency

Fully offline semantic vectorization

2. Endee Vector Database

High-performance vector similarity search

Efficient high-dimensional embedding storage

Metadata-backed citation filtering

Scalable semantic retrieval infrastructure

3. Retrieval Engine

Domain classification logic

Statute validation and section verification

Semantic relevance scoring

Declaratory provision filtering

4. Generator Module

Context-aware legal explanation

Structured and evidence-backed output

Modular integration with RAG pipeline

5. API Layer

FastAPI-based backend

Modular endpoint exposure

Clean separation of concerns

Legal Corpus Coverage

The system supports structured ingestion and retrieval across:

Constitutional Articles

Landmark Judgments

Statutory Provisions (Section-wise)

JSON-based structured legal corpus

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
└── UI Layer

Technology Stack

Python

FastAPI

Endee Vector Database

Ollama (Local Embeddings)

Modular RAG Architecture

Docker (Vector Database Deployment)

JSON-based Legal Corpus

Environment Setup
1. Start Ollama

ollama serve
ollama pull mxbai-embed-large

2. Start Endee

docker run -p 8080:8080 -v endee-data:/data --name endee-server endeeio/endee-server:latest

3. Ingest Legal Data

python legalchat/services/endee_ingest.py

4. Run Backend

uvicorn legalchat.api.main:app --reload

Example Query Workflow

Query:
"Is Right to Privacy a fundamental right in India?"

System Flow:

Query rewritten into structured legal terminology

Embedding generated locally

Semantic similarity search performed using Endee

Relevant constitutional provisions and judgments retrieved

Context injected into generation layer

Structured legal explanation returned

Why Use a Vector Database?

Traditional relational databases are insufficient for semantic reasoning tasks.

Endee enables:

High-dimensional vector storage

Efficient similarity-based retrieval

Context-aware legal reasoning

AI-native backend infrastructure

This architecture ensures precision, contextual relevance, and scalability in legal AI workflows.

Security and Design Principles

No mandatory external embedding API dependency

Local embedding execution via Ollama

Environment-based configuration management

Modular and extensible service architecture

Clear separation between ingestion, retrieval, and generation layers

Future Enhancements

Hybrid Search (Keyword + Semantic)

Confidence scoring mechanism

Agentic legal workflow integration

Fine-tuned legal embeddings

Multi-document PDF ingestion support

Disclaimer

This system is developed for educational and research purposes only and does not constitute legal advice.

Author

Akshat Awasthi
AI/ML Engineer
Legal AI Systems and Vector-Based Architectures
