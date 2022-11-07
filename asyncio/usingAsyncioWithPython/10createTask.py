import asyncio


async def f(n):
    for i in range(n):
        asyncio.create_task(await asyncio.sleep(1))
    return 123


async def main():
    await f(5)


asyncio.run(main())

"""
In this example, the intention is to launch completely new tasks inside the coroutine.
By not awaiting them, we ensure they will run independently of the execution context
inside coroutine function f(). In fact, f() will exit before the tasks that it launched
have completed.
"""
