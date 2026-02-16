from fastapi import APIRouter

router = APIRouter(prefix="/ner", tags=["NER"])

@router.post("/")
def ner():
    return {"entities": []}




