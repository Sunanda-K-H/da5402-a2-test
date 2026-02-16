from fastapi import APIRouter

router = APIRouter(prefix="/speech", tags=["Speech"])

@router.post("/")
def speech():
    return {"audio_url": "mock-url"}




