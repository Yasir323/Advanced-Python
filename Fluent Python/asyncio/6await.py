"""
This keyword await always takes a parameter and will accept only a thing called
an awaitable, which is defined as one of these (exclusively!):

1. A coroutine (i.e., the result of a called async def function).
2. Any object implementing the __await__() special method. That special method
must return an iterator.
"""

import asyncio


async def f():
    await asyncio.sleep(1)  # It is an awaitable function
    return 123


async def main():
    result = await f()  # f() returns a coroutine, so we can await it as well
    return result
