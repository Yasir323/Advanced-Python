import asyncio


async def f():
    try:
        while True:
            await asyncio.sleep(0)
    except asyncio.CancelledError:
        print("I was cancelled!")
    else:
        return 123


"""
When you call task.cancel(), the event loop will internally use coro.throw() to
raise asyncio.CancelledError inside your coroutine.
The throw() method is used (internally in asyncio) for task cancellation, which we
can also demonstrate quite easily. 
"""

coro = f()
coro.send(None)
coro.send(None)
coro.throw(asyncio.CancelledError)
