from api.db import get_db_cursor
from api.models import ArtModel, ArtQuery


def get_arts_info_helper(query: ArtQuery, cursor, limit=10, offset=0):
    base_query = "SELECT * FROM images"
    conditions = []
    params = []

    if query.title:
        conditions.append("title LIKE %s")
        params.append(f"%{query.title}%")
    if query.path:
        conditions.append("path = %s")
        params.append(query.path)
    if query.category:
        conditions.append("category = %s")
        params.append(query.category)

    where_clause = ' AND '.join(conditions) if conditions else '1=1'

    query_with_pagination = f"{base_query} WHERE {where_clause} LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    cursor.execute(query_with_pagination, params)
    records = cursor.fetchall()

    result = [dict(r) for r in records]

    return result


def insert_image_helper(art: ArtModel, cursor) -> ArtModel:
    cursor.execute(
        "INSERT INTO images (title, path, category, description) VALUES (%s, %s, %s, %s)",
        (art.title, art.path, art.category, art.description)
    )
    return art
