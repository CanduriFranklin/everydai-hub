from fastapi import APIRouter

router = APIRouter()

@router.get("/entertainment")
def get_entertainment():
    return {"message": "Entertainment recommendations"}
