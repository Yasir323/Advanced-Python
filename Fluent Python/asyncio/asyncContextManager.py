import asyncio
from contextlib import asynccontextmanager


def download_webpage(url):
    return ''


def update_stats(url):
    pass


def process(data):
    pass


@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_running_loop()
    # Suppose download_webpage is a blocking function using the
    # requests library; we run it in a separate thread to avoid blocking the
    # event loop.
    data = await loop.run_in_executor(
        None, download_webpage, url
    )
    yield data
    await loop.run_in_executor(None, update_stats, url)


async with web_page('google.com') as data:
    process(data)

"""
Native coroutines are awaitable: they can be driven by await
expressions or passed to one of the many asyncio functions that
take awaitable arguments, such as create_task. Asynchronous
generators are not awaitable. They are asynchronous iterables,
driven by async for or by asynchronous comprehensions.

To summarize: an asynchronous generator expression can be defined
anywhere in your program, but it can only be used inside a native coroutine
or asynchronous generator function.
"""