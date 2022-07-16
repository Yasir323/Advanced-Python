import asyncio
import time
from contextlib import asynccontextmanager

import requests

"""
I said it was necessary to modify some functions to return coroutines; these were
download_webpage() and update_stats(). This is usually not that easy to do, since
async support needs to be added down at the socket level.

The focus of the preceding examples was simply to show off the new
@asynccontextmanager decorator, not to show how to convert blocking functions
into nonblocking ones. The more common situation is when you want to use a block‐
ing function in your program, but it’s not possible to modify the code in that
function.

This situation will usually happen with third-party libraries, and a great example is
the requests library, which uses blocking calls throughout.8

If you can’t change the code being called, there is another way. This is a convenient
place to show you how an executor can be used to do exactly that.
"""


def download_webpage(url):
    resp = requests.get(url)
    return resp


def update_stats(data):
    time.sleep(1)
    print(len(data))


@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, download_webpage, url)
    yield response
    await loop.run_in_executor(None, update_stats, response.text)


def process(resp):
    print(resp.status_code)


async def main():
    async with web_page('https://www.google.com') as data:
        process(data)


if __name__ == '__main__':
    asyncio.run(main())
