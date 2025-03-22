from fastapi import APIRouter

router = APIRouter()

@router.get("/calendar")
def get_calendar():
    return {"message": "Smart calendar"}
