"""
Our next plan is to wrap the future (produced by the
executor) inside a new task object.
"""

import time
import asyncio


async def make_coro(future):
    """
    We take the future returned from the run_in_executor() call and pass it into a
    new utility function, make_coro(). The important point here is that we’re using
    create_task(), which means that this task will appear in the list of all_tasks()
    within the shutdown handling of asyncio.run(), and will receive a cancellation
    during the shutdown process.

    This utility function make_coro() simply waits for the future to complete—but
    crucially, it continues to wait for the future even inside the exception handler for
    CancelledError.
    """
    try:
        return await future
    except asyncio.CancelledError:
        return await future


async def main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)
    asyncio.create_task(make_coro(future))
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')


def blocking():
    time.sleep(2.0)
    print(f"{time.ctime()} Hello from a thread!")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye!')
