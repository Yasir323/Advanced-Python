"""
lru_cache() is a decorator, which wraps a function with a 
memoizing callable used for saving up to maxsize the results 
of a function call and returns the stored value if the 
function is called with the same arguments again. It can save 
time when an expensive or I/O bound function is periodically 
called with the same arguments.

Essentially it uses two data structures, a dictionary to map 
a function’s parameters to its result, and a linked list to 
keep track of the function’s call history.
"""

from functools import lru_cache
import time


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


ts = time.perf_counter()
factorial(400)
print(f"Uncached factorial of 100 took: {time.perf_counter() - ts}secs.")


@lru_cache(maxsize=None)
def cached_factorial(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    return n * factorial(n - 1)


ts = time.perf_counter()
cached_factorial(400)
print(f"Cached factorial of 100 took: {time.perf_counter() - ts}secs.")
