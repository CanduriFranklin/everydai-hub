from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_entertainment_endpoint():
    response = client.get("/api/entertainment")
    assert response.status_code == 200
    assert "entertainment" in response.json()