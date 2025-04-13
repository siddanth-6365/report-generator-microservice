import os
from fastapi import UploadFile

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

async def save_uploaded_file(upload: UploadFile, filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    content = await upload.read()
    with open(file_path, "wb") as f:
        f.write(content)
    return file_path