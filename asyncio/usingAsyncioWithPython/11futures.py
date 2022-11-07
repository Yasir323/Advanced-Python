import asyncio

"""
The Future class is actually a superclass of Task, and it provides all of the
functionality for interaction with the loop.

A simple way to think of it is like this: a Future represents a future completion state
of some activity and is managed by the loop. A Task is exactly the same, but the specific
“activity” is a coroutine— probably one of yours that you created with an async
def function plus create_task().

The Future class represents a state of something that is interacting with a loop. That
description is too fuzzy to be useful, so you can instead think of a Future instance as
a toggle for completion status. When a Future instance is created, the toggle is set to
“not yet completed,” but at some later time it will be “completed.” In fact, a Future
instance has a method called done() that allows you to check the status.
"""
f = asyncio.Future()
print(f.done())

"""
A Future instance may also do the following:
1. Have a “result” value set (use .set_result(value) to set it and .result() to
obtain it)
2. Be cancelled with .cancel() (and check for cancellation with .cancelled())
3. Have additional callback functions added that will be run when the future
completes

Even though Tasks are more common, you can’t avoid Futures entirely: for instance,
running a function on an executor will return a Future instance, not a Task.
"""


async def main(fut: asyncio.Future):
    await asyncio.sleep(1)
    fut.set_result("I have finished.")


loop = asyncio.get_event_loop()
future = asyncio.Future()
"""
Manually create a Future instance. Note that this instance is (by default) tied to
our loop, but it is not and will not be attached to any coroutine (that’s what Tasks
are for).
"""
print(future.done())
loop.create_task(main(future))
"""
Schedule the main() coroutine, passing the future. Remember, all the main()
coroutine does is sleep and then toggle the Future instance. (Note that the
main() coroutine will not start running yet: coroutines run only when the loop is
running.)
"""
loop.run_until_complete(future)
"""
Here we use run_until_complete() on a Future instance, rather than a Task
instance. This is different from what you’ve seen before. Now that the loop is
running, the main() coroutine will begin executing.
"""
print(future.done())
print(future.result())
"""
Eventually, the future completes when its result is set. After completion, the
result can be accessed.

Of course, it is unlikely that you will work with Future directly in the way shown
here; the code sample is for education purposes only. Most of your contact with 
asyncio will be through Task instances.

You might wonder what happens if you call set_result() on a Task instance. It was
possible to do this before Python 3.8, but it is no longer allowed. Task instances are
wrappers for coroutine objects, and their result values can be set only internally as the
result of the underlying coroutine function
"""
