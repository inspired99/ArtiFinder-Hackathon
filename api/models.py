from pydantic import BaseModel, Field
from typing import Optional

class ArtQuery(BaseModel):
    title: Optional[str] = None
    path: Optional[str] = None
    category: Optional[str] = None
