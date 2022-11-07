import time
import asyncio

"""
You can also use await inside comprehensions, as outlined in PEP 530. This shouldn’t
be a surprise; await coro is a normal expression and can be used in most places you
would expect.

It’s the async for that makes a comprehension an async comprehension, not the presence
of await. All that’s needed for await to be legal (inside a comprehension) is for it
to be used inside the body of a coroutine function—i.e., a function declared with
async def. 
"""


async def f(x):
    await asyncio.sleep(1)
    return x + 100


async def factory(n):
    """Asynchronous Generator"""
    for x in range(n):
        await asyncio.sleep(1)
        yield f, x


async def main():
    results = [await func(x) async for func, x in factory(3)]
    """
    First, the factory(3) call returns an async generator, which must be driven by
    iteration. Because it’s an async generator, you can’t just use for; you must use
    async for.
    The values produced by the async generator are a tuple of a coroutine function f
    and an int. Calling the coroutine function f() produces a coroutine, which must
    be evaluated with await.
    Note that inside the comprehension, the use of await has nothing at all to do
    with the use of async for: they are doing completely different things and acting
    on different objects entirely.
    """
    print(f"{time.ctime()} | Results = {results}")


if __name__ == '__main__':
    asyncio.run(main())
