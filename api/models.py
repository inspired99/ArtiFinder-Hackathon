from pydantic import BaseModel
from typing import Optional

class ArtQuery(BaseModel):
    title: Optional[str] = None
    path: Optional[str] = None
    category: Optional[str] = None
