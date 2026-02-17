from fastapi import FastAPI
from app.ner import router as ner_router
from app.tts import router as tts_router

app = FastAPI(
    title="Multi-Modal AI API",
    description="Translation, Image Generation, NER, Speech Synthesis",
    version="1.0"
)

app.include_router(ner_router)
app.include_router(tts_router)

@app.get("/")
def home():
    return {"message": "Multi-Modal AI Service Running"}
