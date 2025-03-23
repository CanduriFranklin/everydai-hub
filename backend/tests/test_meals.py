import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_meals_endpoint():
    response = client.get("/api/meals")
    assert response.status_code == 200
    assert "meals" in response.json()