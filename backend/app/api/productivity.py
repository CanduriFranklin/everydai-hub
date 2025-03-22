from fastapi import APIRouter

router = APIRouter()

@router.get("/productivity")
def get_productivity():
    return {"message": "Productivity assistant"}
