import asyncio
import time

"""
asyncio.gather properly allows multiple async tasks to run asynchronously while
the list comprehension awaits one after the other, leading to effectively serial
code.
"""


async def slowtask():
    await asyncio.sleep(1)


async def gather():
    await asyncio.gather(*[slowtask() for _ in range(10)])


async def listcomp():
    [await slowtask() for _ in range(10)]


start = time.time()
asyncio.run(gather())
print("gather", time.time() - start)

start = time.time()
asyncio.run(listcomp())
print("listcomp", time.time() - start)
