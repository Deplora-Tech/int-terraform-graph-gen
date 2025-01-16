import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from functions.generate_graph import Threads, number_queue
from routes import generate_graph
import time
from contextlib import asynccontextmanager

UPLOAD_DIR = "./uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    consumer = Threads()
    consumer.start()
    time.sleep(10)
    yield
    number_queue.join()

app = FastAPI(lifespan=lifespan)
app.include_router(generate_graph.graph_router, prefix="/graph")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return { "Hello": "World" }