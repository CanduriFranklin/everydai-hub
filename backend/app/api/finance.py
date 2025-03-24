from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_finance():
    return {"message": "Finance API"}
