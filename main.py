import os
import uvicorn

from fastapi import Request, FastAPI, APIRouter, File, HTTPException, Query, UploadFile
from api.arts_api import get_arts_info_helper, insert_image_helper
from api.db import get_db_cursor, run_db_query
from api.models import ArtModel, ArtQuery, FilePath
from api.upload import upload_image_helper
from ml_framework.ml_framework import MLFramework
from embeddings_database.embeddings_database import EmbeddingsDatabase

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


router = APIRouter()
ml_framework = MLFramework()
embeddings_database = EmbeddingsDatabase(ml_framework.get_emb_size())

@router.get("/get_arts_info")
async def get_arts_info():
    return {"message": "Everything is ok"}


@router.post("/get_arts_info", response_model=list)
async def get_arts_info(query: ArtQuery, limit: int = Query(default=10, ge=1), offset: int = Query(default=0, ge=0)):
    logger.info(f"Fetching arts info with query: {query.dict()}, limit: {limit}, offset: {offset}")
    try:
        if not query.path:
            with get_db_cursor() as cursor:
                result = await run_db_query(get_arts_info_helper, query, cursor, limit, offset)
                logger.info(f"....Sent {len(result)} objects....")
            return result

        img_path = query.path
        emb = ml_framework.get_img_embedding(img_path)
        img_ids = embeddings_database.find_similar(emb, k=30)
        logger.info(f"Got ids: {len(img_ids)}")
        with get_db_cursor() as cursor:
            result = await run_db_query(get_arts_info_helper, query, cursor, limit, offset, img_ids)
            logger.info(f"....Sent {len(result)} objects....")
        return result

    except Exception as e:
        logger.error(f"Error in get_arts_info: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/add_image", response_model=ArtModel)
async def add_image(art: ArtModel):
    logger.info(f"Adding new image with details: {art.dict()}")
    try:
        with get_db_cursor(commit=True) as cursor:
            art_id, result = await run_db_query(insert_image_helper, art, cursor)

        path = result.path
        emb = ml_framework.get_img_embedding(path)
        logger.info(f"{path}, {emb.shape}, {art_id}")
        embeddings_database.add_embedding(emb, art_id)

        return result
    except Exception as e:
        logger.error(f"Error in add_image: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/gen_description")
async def gen_description(file_path: FilePath):
    if not os.path.exists(file_path.path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        description = ml_framework.get_img_description(file_path.path)
        return {"description": description}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        result = await upload_image_helper(file)
        path = result["path"]
        if path:
            result["category"] = ml_framework.get_img_class(path)
            return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status code: {response.status_code}")
    return response

app.include_router(router, prefix="/api")


def fill_embeddings_db_from_postgresql_db():
    from tqdm import tqdm

    with get_db_cursor() as cursor:
        cursor.execute("SELECT id, path FROM images")
        results = cursor.fetchall()

    for result in tqdm(results):
        emb = ml_framework.get_img_embedding(result['path'])
        embeddings_database.add_embedding(emb, result['id'])

    embeddings_database.save_database()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
