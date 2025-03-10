"""
You can define files to be uploaded by the client using File.

"""

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post('/files/')
async def create_file(file: bytes = File()) -> dict:
    return {'file_size': len(file)}


@app.post('/uploadfile/')
async def create_upload_file(file: UploadFile) -> dict:
    return {'filename': file.filename}


"""
Using UploadFile has several advantages over bytes:

* You don't have to use File() in the default value of the parameter.
* It uses a "spooled" file:
    A file stored in memory up to a maximum size limit, and after
    passing this limit it will be stored in disk.
* This means that it will work well for large files like images, videos, large binaries, etc. without consuming all the memory.
* You can get metadata from the uploaded file.
* It has a file-like async interface.
* It exposes an actual Python SpooledTemporaryFile object that you
can pass directly to other libraries that expect a file-like object.

UploadFile has the following attributes:

* filename: A str with the original file name that was uploaded
(e.g. myimage.jpg).
* content_type: A str with the content type (MIME type / media
type) (e.g. image/jpeg).
* file: A SpooledTemporaryFile (a file-like object). This is the
actual Python file that you can pass directly to other functions
or libraries that expect a "file-like" object.

UploadFile has the following async methods. They all call the
corresponding file methods underneath (using the internal
SpooledTemporaryFile).

* write(data): Writes data (str or bytes) to the file.
* read(size): Reads size (int) bytes/characters of the file.
* seek(offset): Goes to the byte position offset (int) in the file.
    E.g., await myfile.seek(0) would go to the start of the file.
    This is especially useful if you run await myfile.read() once
    and then need to read the contents again.
* close(): Closes the file.

As all these methods are async methods, you need to "await" them.

For example, inside of an async path operation function you can
get the contents with:

contents = await myfile.read()

If you are inside of a normal def path operation function, you can
access the UploadFile.file directly, for example:

contents = myfile.file.read()


When you use the async methods, FastAPI runs the file methods in
a threadpool and awaits for them.
"""
