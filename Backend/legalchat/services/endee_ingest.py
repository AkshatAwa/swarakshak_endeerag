import json
import requests
from pathlib import Path
from uuid import uuid4

BASE_DIR = Path("legalchat/data")
ARTICLES_DIR = BASE_DIR / "constitution_articles"
CASES_DIR = BASE_DIR / "cases"
STATUTES_DIR = BASE_DIR / "statutes"

ENDEE_BASE_URL = "http://localhost:8080"
INDEX_NAME = "legal_index"
EMBED_MODEL = "mxbai-embed-large"


def get_embedding(text):
    res = requests.post(
        "http://localhost:11434/api/embeddings",
        json={
            "model": EMBED_MODEL,
            "prompt": text
        }
    )
    return res.json()["embedding"]


def create_index(dimension):
    requests.post(
        f"{ENDEE_BASE_URL}/api/v1/index/create",
        json={
            "index_name": INDEX_NAME,
            "dimension": dimension
        }
    )


def load_documents():
    documents = []

    for file in ARTICLES_DIR.glob("article_*.json"):
        data = json.loads(file.read_text(encoding="utf-8"))
        documents.append((data["text"], {
            "type": "constitution",
            "identifier": f"Article {data['article']}",
            "title": data["title"],
            "source": data["source"]
        }))

    for file in CASES_DIR.glob("*.json"):
        data = json.loads(file.read_text(encoding="utf-8"))
        documents.append((data["text"], {
            "type": "judgment",
            "identifier": data["case_name"],
            "court": data["court"],
            "source": data["source"]
        }))

    for file in STATUTES_DIR.glob("*.json"):
        data = json.loads(file.read_text(encoding="utf-8"))
        statute_name = data["name"]
        for section_no, section_text in data["sections"].items():
            documents.append((section_text, {
                "type": "statute",
                "identifier": f"Section {section_no}",
                "statute": statute_name,
                "source": data["source"]
            }))

    return documents


def ingest():
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")

    # Get dimension dynamically
    test_embedding = get_embedding("test")
    dimension = len(test_embedding)

    create_index(dimension)

    vectors = []

    for i, (text, meta) in enumerate(docs):
        embedding = get_embedding(text)

        vectors.append({
            "id": str(uuid4()),
            "values": embedding,
            "metadata": {
                **meta,
                "doc_index": i
            }
        })

    requests.post(
        f"{ENDEE_BASE_URL}/api/v1/vector/add",
        json={
            "index_name": INDEX_NAME,
            "vectors": vectors
        }
    )

    print("Endee ingestion complete")


if __name__ == "__main__":
    ingest()
