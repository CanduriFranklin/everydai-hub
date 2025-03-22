from fastapi import APIRouter

router = APIRouter()

@router.get("/finance")
def get_finance():
    return {"message": "Financial management"}
