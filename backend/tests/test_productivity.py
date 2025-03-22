from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_productivity_endpoint():
    response = client.get("/api/productivity")
    assert response.status_code == 200
    assert "productivity" in response.json()