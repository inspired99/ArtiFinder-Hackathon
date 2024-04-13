from fastapi import File, UploadFile
import os
import uuid

from api.constants import IMAGES_PATH, UPLOADS_PATH


async def upload_image_helper(
    file: UploadFile = File(...),
):
    file_location = f"{UPLOADS_PATH}/{file.filename}"
    unique_id = uuid.uuid4()
    filename = f"{unique_id}_{file.filename}"
    file_location = f"{IMAGES_PATH}/{filename}"

    os.makedirs(os.path.dirname(file_location), exist_ok=True)

    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())

    return {"info": "File saved successfully.", "path": file_location}

