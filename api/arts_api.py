import psycopg2
import json

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
from api.models import ArtQuery

def get_arts_info_helper(query: ArtQuery):
    conn = psycopg2.connect(
        dbname="artifinder_db", 
        user="your_username", 
        password="your_password", 
        host="localhost"
    )
    cur = conn.cursor()

    # Build the SQL query dynamically based on provided query parameters
    query_parts = []
    if query.title:
        query_parts.append(f"title = '{query.title}'")
    if query.path:
        query_parts.append(f"path = '{query.path}'")
    if query.category:
        query_parts.append(f"category = '{query.category}'")

    where_clause = " AND ".join(query_parts) if query_parts else "1=1"

    # Execute the SQL query
    sql = f"SELECT id, path, description, category, title, author, date FROM images WHERE {where_clause}"
    cur.execute(sql)
    records = cur.fetchall()
    cur.close()
    conn.close()

    # Transform the records into a list of dictionaries
    columns = ["id", "path", "description", "category", "title", "author", "date"]
    result = [dict(zip(columns, record)) for record in records]

    return result