import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'app')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_finance_endpoint():
    response = client.get("/api/finance")
    assert response.status_code == 200
    assert "finance" in response.json()