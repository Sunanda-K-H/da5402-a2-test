from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/translate", tags=["Translation"])

class TranslateRequest(BaseModel):
    text: str
    target_lang: str

@router.post("/")
def translate(req: TranslateRequest):
    return {"translated_text": f"[mock:{req.target_lang}] {req.text}"}

