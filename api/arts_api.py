from api.db import get_db_cursor
from api.models import ArtModel, ArtQuery


def get_arts_info_helper(query: ArtQuery, cursor, limit=10, offset=0, ids=None):
    base_query = "SELECT * FROM images"
    conditions = []
    params = []

    if ids:
        conditions.append("id IN %s")
        params.append(tuple(ids))
    if query.title:
        conditions.append("title ILIKE %s")
        params.append(f"%{query.title}%")
    if query.category:
        conditions.append("category = %s")
        params.append(query.category)

    where_clause = ' AND '.join(conditions) if conditions else '1=1'

    query_with_pagination = f"{base_query} WHERE {where_clause} LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    cursor.execute(query_with_pagination, params)
    records = cursor.fetchall()

    result = [dict(r) for r in records]

    if ids:
        index_map = {id: index for index, id in enumerate(ids)}
        result.sort(key=lambda x: index_map[x['id']])
    
    return result


def insert_image_helper(art: ArtModel, cursor):
    cursor.execute(
        "INSERT INTO images (title, path, category, description) VALUES (%s, %s, %s, %s)",
        (art.title, art.path, art.category, art.description)
    )

    cursor.execute(
        f"SELECT id FROM images WHERE path = '{art.path}'"
    )
    art_id = cursor.fetchone()['id']

    return art_id, art
