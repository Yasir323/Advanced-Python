import asyncio

"""
Interacting with event loop. There are two ways:

Recommended
asyncio.get_running_loop(), callable from inside the context of a coroutine

Discouraged
asyncio.get_event_loop(), callable from anywhere
"""

loop = asyncio.get_event_loop()
loop2 = asyncio.get_event_loop()
print(loop is loop2)

"""
This means that if you’re inside a coroutine function and you need access to the loop
instance, it’s fine to call get_event_loop() or get_running_loop() to obtain it. 

The get_event_loop() method works only within the same thread. In fact,
get_event_loop() will fail if called inside a new thread unless you specifically create
a new loop with new_event_loop(), and set that new instance to be the loop for that
thread by calling set_event_loop(). Most of us will only ever need (and want!) a single
loop instance running in a single thread.

In contrast, get_running_loop() (the recommended method) will always do what
you expect: because it can be called only within the context of a coroutine, a task, or a
function called from one of those, it always provides the current running event loop,
which is almost always what you want.
"""
