"""
Trying threads for a CPU bound process.
"""

import time
from threading import Thread


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield 1


numbers = [2139079, 1214759, 1516637, 1852285]
start = time.time()
for number in numbers:
    list(factorize(number))

end = time.time()
delta = end - start
print(f'Without threading factorization took {delta:.3f} seconds.')

"""
Using multiple threads to do this computation would make sense in
other languages because I could take advantage of all the CPU cores
of my computer. Let me try that in Python. Here, I define a Python
thread for doing the same computation as before:
"""


class FactorizeThread(Thread):

    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self) -> None:
        self.factors = list(factorize(self.number))


start = time.time()
# Start the threads
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)
# Wait for the threads to finish
for thread in threads:
    thread.join()
end = time.time()
delta = end - start
print(f"With threading factorization took {delta:.3f} seconds.")
