async def c():
    return 123


def g():
    yield 123


coro = c()
gen = g()
print(f"c() is a: {type(c)}")
print(f"g() is also a: {type(g)}")
print(f"Calling c() returns a: {type(coro)}")
print(f"Just like calling g() returns a: {type(gen)}")

"""
A coroutine
is an object that encapsulates the ability to resume an underlying function that has
been suspended before completion. If that sounds familiar, it’s because coroutines are
very similar to generators.

When a coroutine returns, what really happens is that a StopIteration exception is
raised.
"""

try:
    coro.send(None)  # Just like initiating a generator
    """
    A coroutine is initiated by “sending” it a None. Internally, this is what the event
    loop is going to be doing to your precious coroutines; you will never have to do
    this manually. All the coroutines you make will be executed either with
    loop.create_task(coro) or await coro. It’s the loop that does the .send(None)
    behind the scenes.
    """
except StopIteration as err:
    print(f"The answer is {err.value}")

"""
When the coroutine returns, a special kind of exception is raised, called StopIteration.
Note that we can access the return value of the coroutine via the value
attribute of the exception itself. Again, you don’t need to know that it works like
this: from your point of view, async def functions will simply return a value with
the return statement, just like normal functions.
These two points, the send() and the StopIteration, define the start and end of the
executing coroutine, respectively.
"""
