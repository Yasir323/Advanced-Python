import math
import time


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


ts = time.perf_counter()
is_prime(5_000_111_000_222_021)
print(f"Time taken: {time.perf_counter() - ts}")
