import asyncio
from contextlib import contextmanager, asynccontextmanager


async def get_conn(host, port):
    pass


class Connection:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()


async with Connection('http://www.google.com', 80) as conn:
    pass


# CONTEXTLIB: THE BLOCKING WAY
def update_stats(url):
    """
    Imagine that we update some statistics every time we process data from a URL,
    such as the number of times the URL has been downloaded. From a concurrency
    perspective, we would need to know whether this function involves I/O internally,
    such as writing to a database over a network. If so, update_stats() is also a
    blocking call.
    """
    pass


def download_webpage(url):
    """
    This function call (which I made up for this example) looks suspiciously like the
    sort of thing that will want to use a network interface, which is many orders of
    magnitude slower than “normal” CPU-bound code. This context manager must
    be used in a dedicated thread; otherwise, the whole program will be paused while
    waiting for data.
    """
    return url


def process(data):
    """This function call, process(), might also be blocking."""
    pass


@contextmanager
def web_page(url):
    data = download_webpage(url)
    yield data
    update_stats(url)


with web_page('google.com') as data:
    process(data)


# CONTEXTLIB: THE NON-BLOCKING WAY
@asynccontextmanager
async def web_page2(url):
    data = await download_webpage(url)
    # This change presupposes that we were also able to modify the download_webpage()
    # function itself, and convert it into a coroutine that is compatible with the
    # await keyword.
    yield data
    await update_stats(url)
    # Here, assume that we’ve also converted the code inside the update_stats() func‐
    # tion to allow it to produce coroutines. We can then use the await keyword,
    # which allows a context switch to the event loop while we wait for the I/O-bound
    # work to complete.


async with web_page2('google.com') as data:
    process(data)
