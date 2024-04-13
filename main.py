import uvicorn

from fastapi import Depends, FastAPI, APIRouter, File, HTTPException, UploadFile
from api.arts_api import get_arts_info_helper, insert_image_helper
from api.db import get_db_cursor, run_db_query
from api.models import ArtModel
from api.upload import upload_image_helper


router = APIRouter()


@router.get("/get_arts_info")
async def get_arts_info():
    return {"message": "Everything is ok"}


@router.post("/get_arts_info", response_model=list)
async def get_arts_info(query: ArtModel, cursor=Depends(get_db_cursor)):
    try:
        result = await run_db_query(get_arts_info_helper, query, cursor)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/add_image", response_model=ArtModel)
async def add_image(art: ArtModel, cursor=Depends(get_db_cursor)):
    try:
        await run_db_query(insert_image_helper, art, cursor)
        return art
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


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
