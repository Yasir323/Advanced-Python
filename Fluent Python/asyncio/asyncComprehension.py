import asyncio
import random
from domainlib import *


async def gen():
    for i in range(10):
        await asyncio.sleep(0.1)
        yield random.randint(0, 10)


async def main():
    result = [i async for i in gen()]  # BLOCKING
    # Using await in a list comprehension does the same job as asyncio.gather
    print(result)
    names = 'python.org rust-lang.org golang.org n05uch1an9.org'.split()
    names = sorted(names)
    result2 = [await probe(name) for name in names]
    print(result2)


if __name__ == '__main__':
    asyncio.run(main())
