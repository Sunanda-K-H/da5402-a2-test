from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import Response
from pydantic import BaseModel
import os, socket, base64
from io import BytesIO

from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from PIL import Image

router = APIRouter(prefix="/generate-image", tags=["Image Generation"])

class ImageRequest(BaseModel):
    prompt: str

def container_id():
    return socket.gethostname()

@router.post("/")
def generate_image(req: ImageRequest):
    # Support either env var name (nice for your setup)
    key = os.getenv("STABILITY_KEY") or os.getenv("STABILITY_API_KEY")
    if not key:
        raise HTTPException(status_code=500, detail="Missing STABILITY_KEY (or STABILITY_API_KEY) in environment")

    try:
        stability_api = client.StabilityInference(
            key=key,
            verbose=False,
            engine="stable-diffusion-xl-1024-v1-0",
        )

        answers = stability_api.generate(
            prompt=req.prompt,
            steps=30,
            cfg_scale=7.0,
            width=1024,
            height=1024,
            samples=1,
        )

        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(BytesIO(artifact.binary))
                    buf = BytesIO()
                    img.save(buf, format="PNG")
                    b64 = base64.b64encode(buf.getvalue()).decode("utf-8")

                    return {
                        "container_id": container_id(),
                        "provider": "stability-sdk-grpc",
                        "image_base64": b64,
                    }

        raise HTTPException(status_code=502, detail="No image artifact returned by Stability")

    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Image generation failed: {e}")

@router.get("/view")
def view_image(prompt: str = Query(..., description="Text prompt for image")):
    """
    Returns image directly as image/png so it can be opened in browser.
    """

    # Call your existing image generation logic
    result = generate_image(ImageRequest(prompt=prompt))

    if "image_base64" not in result:
        raise HTTPException(status_code=500, detail="Image generation failed")

    image_bytes = base64.b64decode(result["image_base64"])

    return Response(content=image_bytes, media_type="image/png")






