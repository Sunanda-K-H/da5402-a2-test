import spacy
from fastapi import APIRouter
from .schemas import TextRequest

nlp = spacy.load("en_core_web_sm")

router = APIRouter()

@router.post("/ner")
def extract_entities(request: TextRequest):
    doc = nlp(request.text)

    entities = [
        {
            "text": ent.text,
            "label": ent.label_
        }
        for ent in doc.ents
    ]

    return {
        "task": "Named Entity Recognition",
        "input": request.text,
        "entities": entities
    }
