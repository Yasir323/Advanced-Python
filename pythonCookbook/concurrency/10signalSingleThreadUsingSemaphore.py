import time
from threading import Thread, Semaphore


def worker(n, sema: Semaphore):
    print(int(time.time()), 'Started', n)
    # Wait to be signalled
    sema.acquire()
    print(int(time.time()), 'Acquired', n)
    # Do some work
    time.sleep(3)
    print(int(time.time()), 'Working', n)


# Create some threads
semaphore = Semaphore(0)
nworkers = 5
for i in range(nworkers):
    thread = Thread(target=worker, args=(i, semaphore))
    thread.start()

for i in range(nworkers):
    time.sleep(1)
    semaphore.release()
