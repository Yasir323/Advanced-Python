"""
By default, the errors in a thread will be silenced and won’t be shown in
the main thread. To catch the errors in a thread, you would need to loop
through the futures returned from the executor. future is an object representing
the execution of the target function run in a thread.
"""
import time
from concurrent.futures import ThreadPoolExecutor


def thread_func(name):
    print(f"Thread {name} starting.")
    print(1/0)
    time.sleep(2)
    print(f"Thread {name} finishing.")


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_func, range(3))
