import requests

BASE_URL = "http://localhost:8080"

def create_index():
    response = requests.post(
        f"{BASE_URL}/api/v1/index/create",
        json={
            "index_name": "legal_index",
            "dimension": 1536
        }
    )
    print(response.json())

create_index()
