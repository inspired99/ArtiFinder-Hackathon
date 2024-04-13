import uvicorn

from fastapi import Depends, FastAPI, APIRouter, HTTPException, File, UploadFile, Form
from api.arts_api import get_arts_info_helper
from api.constants import IMAGES_PATH
from api.db import get_db_cursor
from api.models import ArtQuery
from api.upload import upload_image_helper


router = APIRouter()


@router.get("/get_arts_info")
async def get_arts_info():
    return {"message": "Everything is ok"}

@router.post("/get_arts_info", response_model=list)
async def get_arts_info(query: ArtQuery, cursor=Depends(get_db_cursor)):
    try:
        result = await get_arts_info_helper(query, cursor)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/upload")
async def upload_image(
    file: UploadFile = File(...),
    description: str = Form(...),
    category: str = Form(...),
    title: str = Form(...),
    author: str = Form(None),
    date: str = Form(None)
):
    result = await upload_image_helper(file, description, category, title, author, date)
    return result


app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

app.include_router(router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
