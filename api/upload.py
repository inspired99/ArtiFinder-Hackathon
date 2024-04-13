
from fastapi import File, UploadFile, Form

from api.constants import IMAGES_PATH
from api.db import get_db_cursor

async def upload_image_helper(
    file: UploadFile = File(...),
    description: str = Form(...),
    category: str = Form(...),
    title: str = Form(...),
    author: str = Form(None),
    date: str = Form(None)
):
    file_location = f"{IMAGES_PATH}/{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())


    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            """
            INSERT INTO images (path, description, category, title, author, date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (file_location, description, category, title, author, date)
        )

    return {"info": "File saved successfully.", "path": file_location}
