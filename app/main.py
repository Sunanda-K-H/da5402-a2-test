from fastapi import FastAPI
from app.routers import translation, image_gen, ner, speech

app = FastAPI(title="Collaborative AI Microservice (TEST REPO)")

app.include_router(translation.router)
app.include_router(image_gen.router)
app.include_router(ner.router)
app.include_router(speech.router)

@app.get("/health")
def health():
    return {"status":"ok"}
