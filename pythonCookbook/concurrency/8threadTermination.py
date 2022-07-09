import time
import redis
from threading import Thread, Event

data = []
threads = []
kill_signal = Event()
ts = time.perf_counter()


def worker(multiple, signal: Event):
    for i in range(1, 40):
        if signal.is_set():
            return
        data.append((i * multiple))
        redis.StrictRedis()  # System call
        time.sleep(0.1)


for i in range(3):
    thread = Thread(target=worker, args=(i + 1, kill_signal), daemon=True)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish, stop if KeyboardInterrupt
while any(map(lambda x: x.is_alive(), threads)):
    try:
        pass
    except KeyboardInterrupt:
        kill_signal.set()

print(data)
print(time.perf_counter() - ts)
