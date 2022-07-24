import asyncio
from typing import List

from flags import BASE_URL, save_flag, main  # <2>

from httpx import AsyncClient  # <1>


async def download_one(client: AsyncClient, cc: str):  # <3>
    image = await get_flag(client, cc)
    # save_flag(image, f'{cc}.gif')
    # For better performance, the save_flag call inside get_flag should be
    # asynchronous, but asyncio does not provide an asynchronous filesystem API at this
    # time—as Node.js does. If profiling reveals that is a bottleneck in your application, you
    # can use the loop.run_in_executor function to run save_flag in a thread pool
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, save_flag, image, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    return cc


async def get_flag(client: AsyncClient, cc: str) -> bytes:  # <4>
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = await client.get(url, timeout=6.1,
                            allow_redirects=True)  # <5>
    return resp.read()  # <6>


def download_many(cc_list: List[str]) -> int:  # <1>
    return asyncio.run(supervisor(cc_list))  # BLOCKING


async def supervisor(cc_list: List[str]) -> int:
    # HTTP client operations in aiohttp are methods of
    # AsyncClient, which is also an asynchronous context manager: a
    # context manager with asynchronous set-up and tear-down methods
    async with AsyncClient() as client:  # <3>
        to_do = [download_one(client, cc)
                 for cc in sorted(cc_list)]  # <4>
        # Wait for the asyncio.gather coroutine, which accepts one or
        # more awaitable arguments and waits for all of them to complete,
        # returning a list of results for the given awaitables in the order
        # they were submitted.
        res = await asyncio.gather(*to_do)  # <5>

    return len(res)  # <6>


if __name__ == '__main__':
    main(download_many)
