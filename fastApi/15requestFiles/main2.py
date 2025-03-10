"""
Optional Upload File
"""

from typing import Union
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post('/files/')
async def create_file(file: Union[bytes, None] = File(default=None)):
    if not file:
        return {'message': "No file sent."}
    else:
        return {'file_size': len(file)}


@app.post('/uploadfile/')
async def create_upload_file(file: Union[UploadFile, None] = None):
    if not file:
        return {'message': "No upload file sent."}
    else:
        return {'filename': file.filename}
