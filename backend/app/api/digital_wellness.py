from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class DigitalWellnessRequest(BaseModel):
    social_time: int
    productivity_time: int
    notification_frequency: str
    wellbeing_goals: List[str]

@router.get("/")
def read_digital_wellness():
    return {"message": "Digital Wellness API"}

@router.post("/api/digital_wellness")
def generate_recommendations(request: DigitalWellnessRequest):
    # Logic to generate recommendations based on digital wellness data
    recommendations = [
        "Limit social media usage to 2 hours per day.",
        "Increase productivity app usage to 4 hours per day.",
        "Reduce notification frequency to minimize distractions."
    ]
    return {"recommendations": recommendations}
