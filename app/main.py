from fastapi import FastAPI
from app.routers import translation, image_gen, ner, speech

app = FastAPI(
    title="Collaborative AI Microservice (TEST REPO)",
    description="Translation, Image Generation, NER, Speech Synthesis",
    version="1.0",
)

app.include_router(translation.router)
app.include_router(image_gen.router)
app.include_router(ner.router)
app.include_router(speech.router)

@app.get("/")
def home():
    return {"message": "Multi-Modal AI Service Running"}

@app.get("/health")
def health():
    return {"status": "ok"}
