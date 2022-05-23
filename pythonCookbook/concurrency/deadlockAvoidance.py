import threading
from contextlib import contextmanager

_local = threading.local()


@contextmanager
def acquire(*locks):
    # Sort the locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError("Lock Order Violation.")

    # Acquire all the locks
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


x_lock = threading.Lock()
y_lock = threading.Lock()


def thread1():
    while True:
        with acquire(x_lock, y_lock):
            print("Thread-1")


def thread2():
    while True:
        with acquire(y_lock, x_lock):
            print("Thread-2")


t1 = threading.Thread(target=thread1, daemon=True)
t1.start()
t2 = threading.Thread(target=thread2, daemon=True)
t2.start()

import time
while True:
    time.sleep(1)
