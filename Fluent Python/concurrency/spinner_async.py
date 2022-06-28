import asyncio
import itertools


async def slow() -> int:
    # If we use time.sleep() it'll block the thread from which
    # it is called. In this case, the only thread i.e. the main
    # thread. So the control will not be transferred to the other
    # Coroutine, i.e. spin. And right after slow returns, the
    # spin coroutine is cancelled in supervisor, and hence we'll
    # not see the spinner at all.
    await asyncio.sleep(3)
    return 42


async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            # Use await asyncio.sleep(.1) instead of time.sleep(.1),
            # to pause without blocking other coroutines.
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


async def supervisor() -> int:
    # Schedule the eventual execution of spin.
    # This call does not suspend the current coroutine.
    spinner = asyncio.create_task(spin('thinking!'))
    print(f"Spinner Object: {spinner}")
    # The await keyword calls slow, blocking supervisor until
    # slow returns. The return value of slow will be assigned to
    # result.
    result = await slow()
    # The Task.cancel method raises a CancelledError exception
    # inside the spin coroutine
    spinner.cancel()
    return result


def main() -> None:
    # Start the event loop to drive the coroutine that will
    # eventually set the other coroutines in motion.
    # The main function will stay blocked till supervisor returns.
    # The return value of the supervisor will become the result.
    result = asyncio.run(supervisor())
    print(f"Answer: {result}")


if __name__ == '__main__':
    main()
