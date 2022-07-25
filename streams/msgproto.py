"""
Message protocol: read and write
"""

import asyncio

SIZE_PREFIX = 4


async def read_msg(stream: asyncio.StreamReader) -> bytes:
    size_bytes = await stream.readexactly(SIZE_PREFIX)  # 1
    size = int.from_bytes(size_bytes, byteorder='big')  # 2
    data = await stream.readexactly(size)  # 3
    return data


async def send_msg(stream: asyncio.StreamWriter, data: bytes) -> None:
    size_bytes = len(data).to_bytes(SIZE_PREFIX, byteorder='big')
    stream.writelines([size_bytes, data])  # 4
    await stream.drain()  # Flush the write buffer.


"""
1. Get the first 4 bytes. This is the size prefix.
2. Those 4 bytes must be converted into an integer.
3. Now we know the payload size, so we read that off the stream.
4. Write is the inverse of read: first we send the length of the data,
encoded as 4 bytes, and thereafter the data.
"""