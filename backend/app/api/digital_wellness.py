from fastapi import APIRouter

router = APIRouter()

@router.get("/digital_wellness")
def get_digital_wellness():
    return {"message": "Digital wellness"}
