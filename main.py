import uvicorn

from fastapi import FastAPI
from api.arts_api import get_arts_info_helper
from api.models import ArtQuery
from ml_framework.ml_framework import MLFramework
from embeddings_database.embeddings_database import EmbeddingsDatabase
from exhibits_database.exhibits_database import ExhibitsDatabase
from concurrent.futures import ProcessPoolExecutor


app = FastAPI()

# POST: add new exhibit
@app.post("/add_exhibit/")
async def add_exhibit(query):
    return

@app.post("/get_arts_info/", response_model=list)
async def get_arts_info(query: ArtQuery):
    
    result = get_arts_info_helper(query)

    return result


with ProcessPoolExecutor(max_workers=1) as ml_executor:
    with ProcessPoolExecutor(max_workers=1) as faiss_executor:  # is thread safe?
        ml_framework = MLFramework(ml_executor)
        embeddings_database = EmbeddingsDatabase(faiss_executor, ml_framework.get_emb_size())
        exhibits_database = ExhibitsDatabase()

        uvicorn.run(app, host="0.0.0.0", port=8000)
