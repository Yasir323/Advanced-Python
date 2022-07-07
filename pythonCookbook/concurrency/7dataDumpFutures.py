import time
import redis
from concurrent.futures import ThreadPoolExecutor

data = []
ts = time.perf_counter()


def worker(multiple):
    for i in range(1, 40):
        data.append((i * multiple))
        redis.StrictRedis()  # System call
        time.sleep(0.1)


with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(worker, (i + 1 for i in range(3)))

print(data)
print(time.perf_counter() - ts)
