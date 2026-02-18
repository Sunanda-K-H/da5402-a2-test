from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import socket
import os

import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

router = APIRouter(prefix="/translate", tags=["Translation"])

class TranslateRequest(BaseModel):
    text: str
    target_lang: str   # "fr", "de", "es", "hi", "ta"
    source_lang: str | None = None  # optional, ignored (we assume EN->target)

def container_id():
    return socket.gethostname()

MODEL_MAP = {
    "fr": "Helsinki-NLP/opus-mt-en-fr",
    "de": "Helsinki-NLP/opus-mt-en-de",
    "es": "Helsinki-NLP/opus-mt-en-es",
    "hi": "Helsinki-NLP/opus-mt-en-hi",
    "ta": "Helsinki-NLP/opus-mt-en-ta",
}

# Cache loaded models/tokenizers
_CACHE: dict[str, tuple[AutoTokenizer, AutoModelForSeq2SeqLM]] = {}

def get_model(target_lang: str):
    if target_lang not in MODEL_MAP:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported target_lang='{target_lang}'. Supported: {sorted(MODEL_MAP.keys())}"
        )

    if target_lang not in _CACHE:
        env_key = f"HF_TRANSLATION_MODEL_{target_lang.upper()}"
        model_name = os.getenv(env_key, MODEL_MAP[target_lang])

        tok = AutoTokenizer.from_pretrained(model_name)
        mdl = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        mdl.eval()
        _CACHE[target_lang] = (tok, mdl)

    return _CACHE[target_lang]

@router.post("/")
def translate(req: TranslateRequest):
    text = (req.text or "").strip()
    if not text:
        raise HTTPException(status_code=400, detail="text cannot be empty")

    tok, mdl = get_model(req.target_lang)

    try:
        inputs = tok(text, return_tensors="pt", truncation=True)
        with torch.no_grad():
            out_ids = mdl.generate(**inputs, max_length=256)

        translated = tok.decode(out_ids[0], skip_special_tokens=True)

        return {
            "container_id": container_id(),
            "provider": "hf-local-mariano",
            "original_text": req.text,
            "target_lang": req.target_lang,
            "translated_text": translated,
        }

    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Translation failed: {e}")



