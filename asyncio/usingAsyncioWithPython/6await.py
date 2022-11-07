"""
This keyword await always takes a parameter and will accept only a thing called
an awaitable, which is defined as one of these (exclusively!):

1. A coroutine (i.e., the result of a called async def function).
2. Any object implementing the __await__() special method. That special method
must return an iterator.
"""

import time

import asyncio


async def f(t):
    await asyncio.sleep(t)  # It is an awaitable function. BLOCKING!!!
    print(f'{time.ctime()} | f({t})')
    return 123


async def main():
    print(f"{time.ctime()} | First call.")
    await f(2)  # BLOCKING!!!
    print(f"{time.ctime()} | Second call.")
    await f(2)  # BLOCKING!!!
    print(f"{time.ctime()} | Third call.")
    result = await f(2)  # f() returns a coroutine, so we can await it as well
    return result


if __name__ == '__main__':
    asyncio.run(main())

"""
await suspends the execution of the current function until the future has returned.
In f(), that makes the function wait for 2 seconds until asyncio.sleep has returned,
before printing. In main, it makes the function wait until f() has returned (which
it does after print which it does after sleep has returned), before continuing on
the next line with the next await f().

If you want to execute all test at the same time and have them each print at once
after two seconds, you can use asyncio.gather:

async def main():
    await asyncio.gather(test(2), test(2), test(2))

This schedules three test coroutines on the event loop at the same time and awaits
all their combined results, which will arrive in ~2 seconds.

You could also fire and forget the coroutines without awaiting their completion:

def main():
    asyncio.ensure_future(test(2))
    asyncio.ensure_future(test(2))
    asyncio.ensure_future(test(2))
"""