import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)


# Create a thread, non-daemonic by default
thread = Thread(target=countdown, args=(10,))
"""
Since it is not a daemon thread, the main thread will wait
at the end for this thread to finish.
"""
# Start thread
thread.start()

# Once started, threads run independently until the
# target function returns.

# Wait here for the hread for finish
thread.join()

# Check status
if thread.is_alive():
    print('Busy...')
else:
    print('Done.')
