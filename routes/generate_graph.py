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
