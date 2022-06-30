import time
from threading import Thread


class CountdownTask:

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(1)


c = CountdownTask()
# Initialize thread
thread = Thread(target=c.run, args=(10,))
# Start Thread
thread.start()
time.sleep(3)
# Signal termination
c.terminate()
# Wait for actual termination
thread.join()

"""
Polling for thread termination can be tricky to coordinate
if threads perform blocking operations such as I/O. For
example, a thread blocked indefinitely on an I/O operation
may never return to check if it’s been killed.
"""
