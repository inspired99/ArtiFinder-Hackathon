import os
import uvicorn

from fastapi import Depends, FastAPI, APIRouter, File, HTTPException, UploadFile
from api.arts_api import get_arts_info_helper, insert_image_helper
from api.db import get_db_cursor, run_db_query
from api.models import ArtModel, ArtQuery, FilePath
from api.upload import upload_image_helper


router = APIRouter()


@router.get("/get_arts_info")
async def get_arts_info():
    return {"message": "Everything is ok"}


@router.post("/get_arts_info", response_model=list)
async def get_arts_info(art: ArtQuery):
    try:
        with get_db_cursor() as cursor:
            result = await run_db_query(get_arts_info_helper, art, cursor)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/add_image", response_model=ArtModel)
async def add_image(art: ArtModel):
    try:
        with get_db_cursor() as cursor:
            result = await run_db_query(insert_image_helper, art, cursor)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/gen_description")
async def gen_description(file_path: FilePath):
    if not os.path.exists(file_path.path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        # call ML function, can be await
        description = "some text here"
        return {"description": description}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    return await upload_image_helper(file)


app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

app.include_router(router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
