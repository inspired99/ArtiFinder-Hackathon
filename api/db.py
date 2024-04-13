from fastapi import Depends, FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

from api.constants import DATABASE_PASS, DATABASE_USER

@contextmanager
def get_db_connection():
    conn = psycopg2.connect(
        dbname="artifinder_db", 
        user=DATABASE_USER, 
        password=DATABASE_PASS, 
        host="localhost"
    )
    try:
        yield conn
    finally:
        conn.close()

def get_db_cursor(conn=Depends(get_db_connection)):
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        yield cursor