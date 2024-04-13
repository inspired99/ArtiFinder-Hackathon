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


def get_db_cursor(commit=False):
    with get_db_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            try:
                yield cursor
                if commit:
                    conn.commit()
            finally:
                cursor.close()
