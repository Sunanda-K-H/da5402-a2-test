from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/translate", tags=["Translation"])

class TranslateRequest(BaseModel):
    text: str
    target_lang: str

@router.post("/")
def translate(req: TranslateRequest):
    # Mock implementation (replace with API call later)
    return {
        "original_text": req.text,
        "target_lang": req.target_lang,
        "translated_text": f"[translated to {req.target_lang}] {req.text}"
    }




