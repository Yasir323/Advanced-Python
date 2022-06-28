import math
import time
import itertools
from threading import Event, Thread


def is_prime(n: int) -> bool:
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
    return True


def spin(msg: str, is_done: Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        # See if the processing is done.
        if is_done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def supervisor() -> int:
    is_done = Event()
    spinner = Thread(target=spin, args=('thinking!', is_done))
    print(f'Spinner Object: {spinner}')
    # Start Spinner thread
    spinner.start()  # it starts spinning
    # Do something
    result = is_prime(5_000_111_000_222_021)  # Blocks the main thread
    # Main thread is released now, send a signal to stop the spinner
    is_done.set()  # Spinner stops
    # Wait for the spinner thread to finish
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    ts = time.perf_counter()
    main()
    print(f"Total time taken: {time.perf_counter() - ts}")