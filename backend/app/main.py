from fastapi import FastAPI
from .api import calendar, digital_wellness, entertainment, finance, health, meals, productivity

app = FastAPI()

# Include API routers
app.include_router(calendar.router, prefix="/api/calendar", tags=["calendar"])
app.include_router(digital_wellness.router, prefix="/api/digital_wellness", tags=["digital_wellness"])
app.include_router(entertainment.router, prefix="/api/entertainment", tags=["entertainment"])
app.include_router(finance.router, prefix="/api/finance", tags=["finance"])
app.include_router(health.router, prefix="/api/health", tags=["health"])
app.include_router(meals.router, prefix="/api/meals", tags=["meals"])
app.include_router(productivity.router, prefix="/api/productivity", tags=["productivity"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Everydai-Hub"}
