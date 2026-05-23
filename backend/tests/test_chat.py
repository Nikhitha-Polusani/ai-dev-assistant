from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat():
    response = client.post("/chat", json={"message": "What is Java?"})

    assert response.status_code == 200
    assert "response" in response.json()

def test_empty_message():
    response = client.post("/chat", json={"message": ""})
    assert response.status_code == 200

def test_random_question():
    response = client.post("/chat", json={"message": "unknown question"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_root():
    response = client.get("/")
    assert response.status_code == 200
