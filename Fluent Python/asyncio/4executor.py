import asyncio
import time


async def sleep_test():
    loop = asyncio.get_event_loop()
    print('going to sleep')
    await loop.run_in_executor(None, time.sleep, 5)
    # time.sleep(5)
    print('waking up')


async def parallel():
    # run two sleep_tests in parallel and wait until both finish
    await asyncio.gather(sleep_test(), sleep_test())


asyncio.run(parallel())
"""
Running this code shows that both instances of the coroutine sleep in parallel. If
we used time.sleep() directly, they would sleep in series because the sleep would
block the event loop.

Realistic use cases for run_in_executor include:

1. integrating CPU-bound code, such as numpy or pandas calculations, into an asyncio
program
2. invoking legacy code that hasn't yet been ported to asyncio
3. blocking calls where non-blocking APIs are simply unavailable - e.g. proprietary
database drivers, or blocking OS-level calls such as those for file system access
"""
