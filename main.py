import uvicorn

from fastapi import Depends, FastAPI, APIRouter, HTTPException
from api.arts_api import get_arts_info_helper
from api.db import get_db_cursor
from api.models import ArtQuery


router = APIRouter()


@router.get("/get_arts_info")
async def get_arts_info():
    return {"message": "Everything is ok"}

@router.post("/get_arts_info", response_model=list)
async def get_arts_info(query: ArtQuery, cursor=Depends(get_db_cursor)):
    
    result = await get_arts_info_helper(query, cursor)
    try:
        result = await get_arts_info_helper(query)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



app = FastAPI(
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

app.include_router(router, prefix="/api")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
