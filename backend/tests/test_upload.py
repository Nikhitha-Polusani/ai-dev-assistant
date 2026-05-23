from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload():
    with open("test.txt", "w") as f:
        f.write("Java is a programming language.")

    with open("test.txt", "rb") as f:
        response = client.post("/upload", files={"file": f})

    assert response.status_code == 200

def test_upload_empty_file():
    with open("empty.txt", "w") as f:
        f.write("")

    with open("empty.txt", "rb") as f:
        response = client.post("/upload", files={"file": f})

    assert response.status_code == 200


def test_upload_multiple_lines():
    with open("multi.txt", "w") as f:
        f.write("Java\nPython\nFastAPI")

    with open("multi.txt", "rb") as f:
        response = client.post("/upload", files={"file": f})

    assert response.status_code == 200
 
