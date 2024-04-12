import uvicorn

from fastapi import FastAPI
from api.arts_api import get_arts_info_helper
from api.models import ArtQuery

app = FastAPI()

# POST: add new exhibit
@app.post("/add_exhibit/")
async def add_exhibit(query):
    return

@app.post("/get_arts_info/", response_model=list)
async def get_arts_info(query: ArtQuery):
    
    result = get_arts_info_helper(query)

    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
