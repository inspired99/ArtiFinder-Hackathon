from pydantic import BaseModel
from typing import Optional

class ArtQuery(BaseModel):
    title: Optional[str] = None
    path: Optional[str] = None
    category: Optional[str] = None


class ArtModel(BaseModel):
    title: str
    path: str
    category: str
    description: str


class FilePath(BaseModel):
    path: str