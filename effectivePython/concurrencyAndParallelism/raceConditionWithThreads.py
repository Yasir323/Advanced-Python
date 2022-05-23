"""
I want to write a program that counts many
things in parallel, like sampling light levels from a whole network of
sensors. If I want to determine the total number of light samples over
time, I can aggregate them with a new class
"""

import random
from threading import Thread, Lock


class Counter:

    def __init__(self):
        self.count = 0

    def increment(self, offset=1):
        self.count += offset


"""
Imagine that each sensor has its own worker thread because reading
from the sensor requires blocking I/O. After each sensor measurement,
the worker thread increments the counter up to a maximum
number of desired readings
"""


def worker(sensor_id, how_many, counter):
    for _ in range(how_many):
        # time.sleep(0.0000001)
        reading = random.random()
        # print(f"Sensor: {sensor_id} -> Reading: {reading}")
        counter.increment(1)


# Now, I run one worker thread for each sensor in parallel and wait for
# them all to finish their readings

how_many = 10 ** 5
counter = Counter()

threads = []
for i in range(5):
    thread = Thread(target=worker, args=(i, how_many, counter))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count
print(f"Counter should be {expected}, got {found}.")

"""
The Python interpreter enforces fairness between all of the threads
that are executing to ensure they get roughly equal processing time.
To do this, Python suspends a thread as it’s running and resumes
another thread in turn. The problem is that you don’t know exactly
when Python will suspend your threads. A thread can even be paused
seemingly halfway through what looks like an atomic operation.
That’s what happened in this case.

By using a lock, I can have the class protect its current Counter
value against simultaneous accesses from multiple threads. Only one
thread will be able to acquire the lock at a time.
"""

class LockingCounter:

    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset=1):
        with self.lock:
            self.count += offset


counter = LockingCounter()
threads = []
for i in range(5):
    thread = Thread(target=worker, args=(i, how_many, counter))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count
print(f"With Mutex Lock:\nCounter should be {expected}, got {found}.")
