import time
import itertools
from multiprocessing import Process, Event
from multiprocessing import synchronize


def spin(msg: str, is_done: synchronize.Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        # See if the processing is done.
        if is_done.wait(.1):
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')


def slow() -> int:
    time.sleep(3)
    return 42


def supervisor() -> int:
    is_done = Event()
    spinner = Process(target=spin, args=('thinking!', is_done))
    print(f'Spinner Object: {spinner}')
    # Start Spinner child process
    spinner.start()  # it starts spinning
    # Do something
    result = slow()  # Blocks the main thread
    # Main thread is released now, send a signal to stop the spinner
    is_done.set()  # Spinner stops
    # Wait for the spinner process to finish
    spinner.join()
    return result


def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')


if __name__ == '__main__':
    ts = time.perf_counter()
    main()
    print(f"Total time taken: {time.perf_counter() - ts}")
