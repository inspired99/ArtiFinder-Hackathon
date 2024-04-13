from api.models import ArtQuery


def get_arts_info_helper(query: ArtQuery, cursor):
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
