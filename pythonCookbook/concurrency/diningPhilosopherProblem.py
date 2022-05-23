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


def philosopher(left, right):
    while True:
        with acquire(left, right):
            print(threading.currentThread(), 'eating')


NSTICKS = 5
chopsticks = [threading.Lock() for _ in range(NSTICKS)]
for n in range(NSTICKS):
    t = threading.Thread(target=philosopher,
                         args=(chopsticks[n], chopsticks[(n+1) % NSTICKS]))
    t.start()
