from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_productivity():
    return {"message": "Productivity API"}
