import asyncio

"""
gather(*, return_exceptions=True): that setting makes the “group” future treat
exceptions from the subtasks as returned values, so that they don’t bubble out and
interfere with run_until_complete().

An undesirable consequence of capturing exceptions in this
way is that some errors may escape your attention because they’re now (effectively)
being handled inside the group task. If this is a concern, you can obtain the output
list from run_until_complete() and scan it for any subclasses of Exception, and
then write log messages appropriate for your situation.
"""


async def f(delay):
    await asyncio.sleep(1 / delay)
    return delay


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    for i in range(10):
        loop.create_task(f(i))
    pending = asyncio.all_tasks(loop)
    group = asyncio.gather(*pending, return_exceptions=True)
    results = loop.run_until_complete(group)
    print(f'Results: {results}')
    loop.close()

    """
    Without return_exceptions=True, the ZeroDivisionError would be raised from
    run_until_complete(), stopping the loop and thus preventing the other tasks from
    finishing.
    """
