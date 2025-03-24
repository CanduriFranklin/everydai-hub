import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

os.environ["TESTING"] = "1"

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.session import Base
from app.models.meals import Meals

# Use an in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

def test_meals_endpoint():
    response = client.get("/api/meals")
    assert response.status_code == 200
    assert response.json() == {"message": "Meals API"}

def test_meals(db):
    pass