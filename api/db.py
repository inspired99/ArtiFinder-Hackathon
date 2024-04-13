from contextlib import contextmanager
from functools import partial
import psycopg2
from psycopg2.extras import RealDictCursor

import asyncio
from api.constants import DATABASE_HOST, DATABASE_NAME, DATABASE_PASS, DATABASE_USER

DATABASE_URL = f"dbname={DATABASE_NAME} user={DATABASE_USER} password={DATABASE_PASS} host={DATABASE_HOST}"

@contextmanager
def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        conn.close()

@contextmanager
def get_db_cursor(commit=False):
    with get_db_connection() as conn:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            yield cursor
            if commit:
                conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            cursor.close()
            

async def run_db_query(func, cursor, *args, **kwargs):
    loop = asyncio.get_running_loop()
    func_with_cursor = partial(func, cursor, *args, **kwargs)
    return await loop.run_in_executor(None, func_with_cursor)
