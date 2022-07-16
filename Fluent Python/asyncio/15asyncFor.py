import asyncio
from aioredis import create_redis


class OneAtATime:

    def __init__(self, redis, keys):
        self.redis = redis
        self.keys = keys

    def __aiter__(self):
        self.ikeys = iter(self.keys)
        return self

    async def __anext__(self):
        try:
            k = next(self.ikeys)
        except StopIteration:
            raise StopAsyncIteration

        value = await self.redis.get(k)
        return value


async def do_something_with(val):
    await asyncio.sleep(0)
    print(val)


async def main():
    redis = await create_redis(('localhost', 6379))
    keys = ['blah', 'blahh', 'blahhh']
    async for value in OneAtATime(redis, keys):
        """
        We’re using async for: the point is that iteration is able to suspend itself while
        waiting for the next datum to arrive.
        """
        await do_something_with(value)


asyncio.run(main())
