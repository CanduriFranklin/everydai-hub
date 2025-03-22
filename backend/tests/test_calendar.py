from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Everydai-Hub"}

def test_calendar_endpoint():
    response = client.get("/api/calendar")
    assert response.status_code == 200
    assert "calendar" in response.json()