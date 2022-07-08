import threading
import time
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired
_local = threading.local()
stop_event = threading.Event()


@contextmanager
def acquire(*locks):
    # Sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # Acquire all of the locks
    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


def philosopher(left, right):
    running = True
    while running:
        if stop_event.is_set():
            running = False
        with acquire(left, right):
            print(threading.currentThread(), 'eating')


# The chopsticks (represented by locks()
N_STICKS = 5
chopsticks = [threading.Lock() for n in range(N_STICKS)]

# Create all of the philosophers
for n in range(N_STICKS):
    thread = threading.Thread(target=philosopher, args=(chopsticks[n], chopsticks[(n + 1) % N_STICKS]))
    thread.start()

time.sleep(10)
stop_event.set()
