from fastapi import FastAPI
import asyncio
import uvicorn

from ml_framework.ml_framework import MLFramework
from embeddings_database.embeddings_database import EmbeddingsDatabase
from exhibits_database.exhibits_database import ExhibitsDatabase
from concurrent.futures import ProcessPoolExecutor


app = FastAPI()


# POST: add new exhibit
@app.post("/add_exhibit/")
async def add_exhibit(query):
    return


# GET: get exhibits based on filters
@app.get("/get_exhibits/")
async def get(query):
    # If there is an image: ask for emb with ml_framework, then ask for similar images with embeddings_database

    # Filter exhibits (all or found above)

    return


with ProcessPoolExecutor(max_workers=1) as ml_executor:
    with ProcessPoolExecutor(max_workers=1) as faiss_executor:  # is thread safe?
        ml_framework = MLFramework(ml_executor)
        embeddings_database = EmbeddingsDatabase(faiss_executor, ml_framework.get_emb_size())
        exhibits_database = ExhibitsDatabase()

        uvicorn.run(app, host="0.0.0.0", port=8000)
