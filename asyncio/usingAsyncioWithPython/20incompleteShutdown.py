import asyncio
"""
This program will produce an error:

`Task was destroyed but it is pending!`

This error is telling you that some tasks had not yet been completed when the loop
was closed. We want to avoid this, and that is why the idiomatic shutdown procedure
is to collect all unfinished tasks, cancel them, and then let them all finish before clos‐
ing the loop. asyncio.run() does all of these steps for you.
"""


async def f(delay):
    await asyncio.sleep(delay)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    t1 = loop.create_task(f(1))
    t2 = loop.create_task(f(2))
    loop.run_until_complete(t1)
    loop.close()
