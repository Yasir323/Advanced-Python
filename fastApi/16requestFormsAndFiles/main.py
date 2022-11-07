from fastapi import FastAPI, File, Form, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form()
):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }


"""
You can declare multiple File and Form parameters in a path operation,
but you can't also declare Body fields that you expect to receive as
JSON, as the request will have the body encoded using
multipart/form-data instead of application/json.

This is not a limitation of FastAPI, it's part of the HTTP protocol.
"""
