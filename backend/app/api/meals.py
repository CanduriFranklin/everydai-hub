from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_meals():
    return {"message": "Meals API"}
