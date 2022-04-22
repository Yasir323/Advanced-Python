# Using ThreadpoolExecutor
from concurrent.futures import ThreadPoolExecutor
import time


def thread_func(name):
    print(f"Thread {name} starting.")
    time.sleep(2)
    print(f"Thread {name} finishing.")


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_func, range(3))
