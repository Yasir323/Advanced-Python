import multiprocessing
import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    for number in numbers:
        cpu_bound(number)


def find_sums_multiprocessing(numbers):
    with multiprocessing.Pool() as pool:
        pool.map(cpu_bound, numbers)


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(20)]
    print("Synchronous Version...")
    start_time = time.perf_counter()
    find_sums(numbers)
    duration = time.perf_counter() - start_time
    print(f"Duration {duration} seconds.")
    print()
    print("Multiprocessing Version...")
    start_time = time.perf_counter()
    find_sums_multiprocessing(numbers)
    duration = time.perf_counter() - start_time
    print(f"Duration {duration} seconds.")
