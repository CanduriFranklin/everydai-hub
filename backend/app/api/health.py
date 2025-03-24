from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_health():
    return {"message": "Health API"}
