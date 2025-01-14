import shutil

from fastapi import APIRouter, File, UploadFile, HTTPException

from functions.generate_graph import producer
from models.generate_graph_model import GenerateGraphModel
import os
graph_router = APIRouter()

@graph_router.post("/generate")
async def generate_graph(req: GenerateGraphModel):
    res = await producer(req)
    return { "message": "task sheduled successfully", "task_id": req.id }

@graph_router.post("/upload-image/{session_id}")
async def upload_image(session_id: str, file: UploadFile = File(...)):
    try:
        upload_dir = f"./uploaded_images/{session_id}"
        os.makedirs(upload_dir, exist_ok=True)

        file_location = os.path.join(upload_dir, file.filename)
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {"message": "Image uploaded successfully", "file_path": file_location}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")