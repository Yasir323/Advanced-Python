"""
I want to send a signal to a remote-controlled
helicopter through a serial port. I’ll use a slow system call (select) as
a proxy for this activity. This function asks the operating system to
block for 0.1 seconds and then return control to my program, which is
similar to what would happen when using a synchronous serial port:
"""

import time
import select
import socket
from threading import Thread



def compute_helicopter_location(index):
    # Just do some calculations here
    for i in range(index * 10_000):
        _ = i * i


def slow_systemcall():
    select.select([socket.socket()], [], [], 0.5)


# Running this system call in serial requires a linearly increasing
# amount of time
start = time.perf_counter()
for i in range(5):
    slow_systemcall()
    compute_helicopter_location(i)

end = time.perf_counter()
delta = end - start

print(f"Without threading the program took {delta:.4f} seconds.")

"""
The problem is that while the slow_systemcall function is running, my
program can’t make any other progress. My program’s main thread of
execution is blocked on the select system call. This situation is awful
in practice. You need to be able to compute your helicopter’s next move
while you’re sending it a signal; otherwise, it’ll crash. When you find
yourself needing to do blocking I/O and computation simultaneously,
it’s time to consider moving your system calls to threads.
"""

start = time.perf_counter()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)

for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()

end = time.perf_counter()
delta = end - start

print(f"With threading the program took {delta:.4f} seconds.")
