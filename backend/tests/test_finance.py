from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_finance_endpoint():
    response = client.get("/api/finance")
    assert response.status_code == 200
    assert "finance" in response.json()