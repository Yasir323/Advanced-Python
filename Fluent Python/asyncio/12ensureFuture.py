import asyncio

"""
Here is a (hopefully) clearer description of ensure_future():
1. If you pass in a coroutine, it will produce a Task instance (and your coroutine
will be scheduled to run on the event loop). This is identical to calling
asyncio.create_task() (or loop.create_task()) and returning the new Task
instance.
2. If you pass in a Future instance (or a Task instance, because Task is a subclass of
Future), you get that very same thing returned, unchanged. Yes, really!
"""


async def f():
    pass


coro = f()
loop = asyncio.get_event_loop()
task = loop.create_task(coro)
assert isinstance(task, asyncio.Task)

new_task = asyncio.ensure_future(coro)
assert isinstance(new_task, asyncio.Task)

mystery_meat = asyncio.ensure_future(task)
assert mystery_meat is task

"""
Conclusion:
If you know that you have a coroutine and you want it to be scheduled, the correct API
to use is create_task(). The only time when you should be calling ensure_future()
is when you are providing an API (like most of asyncio’s own APIs) that accepts either
a coroutine or a Future and you need to do something to it that requires you to have a
Future. In sum, asyncio.ensure_future() is a helper function intended for framework
designers.

For example, the asyncio.gather() function has the following signature:

asyncio.gather(*aws, loop=None, ...)

The aws parameter means “awaitable objects,” which includes coroutines, tasks, and
futures. Internally, gather() is using ensure_future() for type coercion: tasks and
futures are left untouched, while tasks are created for coroutines.
"""
