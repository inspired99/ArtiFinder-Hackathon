from api.models import ArtModel


def get_arts_info_helper(query: ArtModel, cursor):
    base_query = "SELECT * FROM images"
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

    if conditions:
        query = f"{base_query} WHERE {' OR '.join(conditions)}"
    else:
        query = base_query
    cursor.execute(query, params)
    records = cursor.fetchall()

    result = [dict(r) for r in records]

    return result


def insert_image_helper(art: ArtModel, cursor):
    cursor.execute(
        "INSERT INTO images (title, path, category, description) VALUES (%s, %s, %s, %s)",
        (art.title, art.path, art.category, art.description)
    )

