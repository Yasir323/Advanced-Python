"""
A critical feature of Event objects is that they wake all waiting threads. If you are writing
a program where you only want to wake up a single waiting thread, it is probably better
to use a Semaphore or Condition object instead.
"""
# Worker thread
import threading
import time


def worker(n, sema):
    # Wait to be signalled
    sema.acquire()
    # Do some work
    print("Working", n)


# Create some threads
sema = threading.Semaphore(0)
num_workers = 10
for n in range(num_workers):
    t = threading.Thread(target=worker, args=(n, sema))
    t.start()

time.sleep(2)
for _ in range(10):
    # time.sleep(0.1)
    sema.release()
