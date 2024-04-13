from fastapi import Depends, FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

from api.constants import DATABASE_HOST, DATABASE_NAME, DATABASE_PASS, DATABASE_USER

DATABASE_URL = f"dbname={DATABASE_NAME} user={DATABASE_USER} password={DATABASE_PASS} host={DATABASE_HOST}"

@contextmanager
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()

# Dependency that can be used in path operations
def get_db_cursor():
    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            yield cursor