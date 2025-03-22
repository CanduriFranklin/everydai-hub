from fastapi import APIRouter

router = APIRouter()

@router.get("/meals")
def get_meals():
    return {"message": "Meal planner"}
