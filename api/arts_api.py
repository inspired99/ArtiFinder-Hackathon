import psycopg2
import json

from fastapi import Depends, FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from api.constants import DATABASE_PASS, DATABASE_USER
from api.db import get_db_cursor
from api.models import ArtQuery


async def get_arts_info_helper(query: ArtQuery, cursor=Depends(get_db_cursor)):
    conditions = []
    params = []
    if query.title:
        conditions.append("title = %s")
        params.append(query.title)
    if query.path:
        conditions.append("path = %s")
        params.append(query.path)
    if query.category:
        conditions.append("category = %s")
        params.append(query.category)

    where_clause = ' OR '.join(conditions) if conditions else 'TRUE'
    cursor.execute(f"SELECT * FROM images WHERE {where_clause}", tuple(params))
    records = cursor.fetchall()

    columns = ["id", "path", "description", "category", "title", "author", "date"]
    result = [dict(zip(columns, record)) for record in records]

    return result