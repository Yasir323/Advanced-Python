import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)


# Create a thread, non-daemonic by default
thread = Thread(target=countdown, args=(10,), daemon=True)
"""
Daemonic threads can’t be joined. However, they are
destroyed automatically when the main thread terminates.
"""
# Start thread
thread.start()

# Once started, threads run independently until the
# target function returns.

# Check status
if thread.is_alive():
    print('Busy...')
else:
    print('Done.')

"""
There are no operations to terminate a thread, signal a
thread, adjust its scheduling, or perform any other
high-level operations. If you want these features, you
need to build them yourself.
"""
