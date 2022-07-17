import asyncio
import time
"""
The underlying misunderstanding is expecting async for to automatically parallelize
the iteration. It doesn't do that, it simply allows sequential iteration over an async
source. For example, you can use async for to iterate over lines coming from a TCP
stream, messages from a websocket, or database records from an async DB driver.

None of the above would work with an ordinary for, at least not without blocking the
event loop.

An async for loop then, simply awaits each next step of the iteration protocol,
where a regular for loop would block.

The asynchronous part of async for is that it lets the iterator await on behalf of
the coroutine iterating over it. It's only for use within asynchronous coroutines,
and only for use on special asynchronous iterables. Other than that, it's mostly
just like a regular for loop.
"""


async def doubler(n: int):
    """Asynchronous Generator"""
    print(f'{time.ctime()} | Inside doubler({n})')
    for i in range(n):
        wait = 4 - (i + 1)
        print(f'{time.ctime()} | Yielding next item in {wait} sec')
        await asyncio.sleep(wait)
        print(f'{time.ctime()} | Yielded {i * 2}')
        yield i, i * 2


async def main():
    result_list = [x async for x in doubler(3)]
    print(f'{time.ctime()} | {result_list}')
    result_dict = {x: y async for x, y in doubler(3)}
    print(f'{time.ctime()} | {result_dict}')
    result_set = {x async for x in doubler(3)}
    print(f'{time.ctime()} | {result_set}')


if __name__ == '__main__':
    print(f'{time.ctime()} | Start')
    asyncio.run(main())
