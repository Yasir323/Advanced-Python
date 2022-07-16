"""
Let's see what asyncio.run() kinda does in the background.
"""

import time
import asyncio


async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # You need a loop instance before you can run any coroutines, and this is how you
    # get one. In fact, anywhere you call it, get_event_loop() will give you the same
    # loop instance each time, as long as you’re using only a single thread.
    #  If you’re  inside an async def function, you should call
    #  asyncio.get_running_loop() instead, which always gives you what you expect.
    task = loop.create_task(main())
    # Your coroutine function will not be executed until you do this. We say that
    # create_task() schedules your coroutine to be run on the loop. The returned
    # task object can be used to monitor the status of the task (for example, whether
    # it is still running or has completed), and can also be used to obtain a result
    # value from your completed coroutine. You can cancel the task with task.cancel().
    loop.run_until_complete(task)
    # This call will block the current thread, which will usually be the main thread.
    # Note that run_until_complete() will keep the loop running only until the given
    # coro completes—but all other tasks scheduled on the loop will also run while the
    # loop is running. Internally, asyncio.run() calls run_until_complete() for you
    # and therefore blocks the main thread in the same way.
    pending = asyncio.all_tasks(loop=loop)
    # Return a set of all tasks for the loop.
    for task in pending:
        task.cancel()
    group = asyncio.gather(*pending, return_exceptions=True)
    # When the “main” part of the program unblocks, either due to a process signal
    # being received or the loop being stopped by some code calling loop.stop(), the
    # code after run_until_complete() will run. The standard idiom as shown here is
    # to gather the still-pending tasks, cancel them, and then use loop.run_until_com
    # plete() again until those tasks are done. gather() is the method for doing the
    # gathering. Note that asyncio.run() will do all the cancelling, gathering, and
    # waiting for pending tasks to finish up.

    loop.run_until_complete(group)
    loop.close()
    # loop.close() is usually the final action: it must be called on a stopped loop, and
    # it will clear all queues and shut down the executor. A stopped loop can be restarted,
    # but a closed loop is gone for good. Internally, asyncio.run() will close the
    # loop before returning. This is fine because run() creates a new event loop every
    # time you call it.
