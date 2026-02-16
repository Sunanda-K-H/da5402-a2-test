from fastapi import APIRouter
from fastapi.responses import FileResponse
from gtts import gTTS
import uuid
import os
from .schemas import TextRequest

router = APIRouter()

@router.post("/tts")
def text_to_speech(request: TextRequest):

    filename = f"audio_{uuid.uuid4().hex}.mp3"

    tts = gTTS(text=request.text, lang='en')
    tts.save(filename)

    return FileResponse(
        path=filename,
        media_type="audio/mpeg",
        filename="speech.mp3"
    )
