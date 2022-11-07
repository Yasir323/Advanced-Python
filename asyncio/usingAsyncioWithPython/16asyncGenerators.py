import asyncio
from aioredis import create_redis

"""
Async generators are async def functions that have yield keywords inside them.
Async generators result in simpler code.

1. Coroutines and generators are completely different concepts.
2. Async generators behave much like ordinary generators.
3. For iteration, you use async for for async generators, instead of the ordinary
for used for ordinary generators.
"""


async def do_something_with(value):
    await asyncio.sleep(0)
    print(value)


async def one_at_a_time(redis, keys):
    for key in keys:
        value = await redis.get(key)
        yield value


async def main():
    redis = await create_redis(('localhost', 6379))
    keys = ['Americas', 'Africa', 'Europe', 'Asia']
    async for value in one_at_a_time(redis, keys):
        await do_something_with(value)


if __name__ == '__main__':
    asyncio.run(main())
