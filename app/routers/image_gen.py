from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/generate-image", tags=["Image Generation"])

class ImageRequest(BaseModel):
    prompt: str

@router.post("/")
def generate_image(req: ImageRequest):
    return {"image_url": f"https://example.com/mock?prompt={req.prompt}"}

