import time
import asyncio


async def main():
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, blocking)
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.ctime()} Goodbye!')


def blocking():
    time.sleep(1.5)
    print(f"{time.ctime()} Hello from a thread!")


if __name__ == '__main__':
    asyncio.run(main())

"""
What’s happening here is that behind the scenes, run_in_executor() does not create
a Task instance: it returns a Future. That means it isn’t included in the set of “active
tasks” that get cancelled inside asyncio.run(), and therefore run_until_complete()
(called inside asyncio.run()) does not wait for the executor task to finish. The
RuntimeError is being raised from the internal loop.close() call made inside asyn
cio.run().
At the time of writing, loop.close() in Python 3.8 does not wait for all executor jobs
to finish, and this is why the Future returned from run_in_executor() complains:
by the time it resolves, the loop has already been closed.
"""