from fastapi import FastAPI
from app.api.calendar import router as calendar_router
from app.api.digital_wellness import router as digital_wellness_router
from app.api.entertainment import router as entertainment_router
from app.api.finance import router as finance_router
from app.api.health import router as health_router
from app.api.meals import router as meals_router
from app.api.productivity import router as productivity_router
from .database.session import engine, Base
from sqlalchemy import create_engine
from .models import calendar, digital_wellness, entertainment, finance, health, meals, productivity, user
import os

app = FastAPI()

# Use in-memory SQLite database for testing
if os.getenv("TESTING"):
    DATABASE_URL = "sqlite:///:memory:"
    engine = create_engine(DATABASE_URL)

# Create all tables
Base.metadata.create_all(bind=engine)

# Include API routers
app.include_router(calendar_router, prefix="/api/calendar", tags=["calendar"])
app.include_router(digital_wellness_router, prefix="/api/digital_wellness", tags=["digital_wellness"])
app.include_router(entertainment_router, prefix="/api/entertainment", tags=["entertainment"])
app.include_router(finance_router, prefix="/api/finance", tags=["finance"])
app.include_router(health_router, prefix="/api/health", tags=["health"])
app.include_router(meals_router, prefix="/api/meals", tags=["meals"])
app.include_router(productivity_router, prefix="/api/productivity", tags=["productivity"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Everydai-Hub"}
