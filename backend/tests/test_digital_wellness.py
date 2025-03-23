import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'app')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_digital_wellness_endpoint():
    response = client.get("/api/digital_wellness")
    assert response.status_code == 200
    assert "digital_wellness" in response.json()