import time
import asyncio


async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(3)
    print(f"{time.ctime()} Goodbye!")


def blocking():
    """
    blocking() calls the traditional time.sleep() internally, which would have
    blocked the main thread and prevented your event loop from running. This
    means that you must not make this function a coroutine—indeed, you cannot
    even call this function from anywhere in the main thread, which is where the
    asyncio loop is running. We solve this problem by running this function in an
    executor.
    """
    time.sleep(2)  # Blocking call should be shorter than its nonblocking counter-part
    print(f"{time.ctime()} Hello from a thread!")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_in_executor(None, blocking)
    # This is the last of our list of essential, must-know features of asyncio. Sometimes
    # you need to run things in a separate thread or even a separate process: this
    # method is used for exactly that. Here we pass our blocking function to be run in
    # the default executor. Note that run_in_executor() does not block the main
    # thread: it only schedules the executor task to run (it returns a Future, which
    # means you can await it if the method is called within another coroutine function).
    # The executor task will begin executing only after run_until_complete() is
    # called, which allows the event loop to start processing events.
    loop.run_until_complete(task)
    pending = asyncio.all_tasks(loop=loop)
    # the set of tasks in pending does not include an
    # entry for the call to blocking() made in run_in_executor(). This will be true of
    # any call that returns a Future rather than a Task. The documentation is quite
    # good at specifying return types, so you’ll see the return type there; just
    # remember that all_tasks() really does return only Tasks, not Futures.

    for task in pending:
        task.cancel()
    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)
    loop.close()
