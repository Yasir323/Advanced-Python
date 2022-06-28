import math
import asyncio
import itertools


async def is_prime(n: int) -> bool:
    if n < 2:
        return False
    elif n == 2:
        return True
    if n % 2 == 0:
        return False
    root = math.isqrt(n)
    for i in range(3, root + 1, 2):
        if n % i == 0:
            return False
        if i % 100_000 == 1:
            await asyncio.sleep(0)
    return True


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
    result = await is_prime(5_000_111_000_222_021)
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
