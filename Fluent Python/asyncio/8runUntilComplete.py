import asyncio


async def f():
    await asyncio.sleep(0)
    return 111


loop = asyncio.get_event_loop()
coro = f()
loop.run_until_complete(coro)
"""
Run the coroutine to completion. Internally, this is doing all those .send(None)
method calls for us, and it detects completion of our coroutine with the
StopIteration exception, which also contains our return value.
"""
