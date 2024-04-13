from pydantic import BaseModel
from typing import Optional

class ArtModel(BaseModel):
    title: Optional[str] = None
    path: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
