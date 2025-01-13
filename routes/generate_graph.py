import shutil

from fastapi import APIRouter, File, UploadFile

from functions.generate_graph import producer
from models.generate_graph_model import GenerateGraphModel

graph_router = APIRouter()

@graph_router.post("/generate")
async def generate_graph(req: GenerateGraphModel):
    data = req
    res = await producer(data)
    return { "qsize" : res }

@graph_router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    file_location = f"./uploaded_images/{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return { "message": "Upload Image" }