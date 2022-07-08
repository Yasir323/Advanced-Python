"""
A object is a synchronization primitive based on a shared counter. If the
Semaphore counter is nonzero, the statement decrements the count and a thread is allowed to
with proceed. The counter is incremented upon the conclusion of the
block. If the with counter is zero, progress is blocked until the counter is incremented by another thread.
Although a semaphore can be used in the same manner as a standard Lock, the added
complexity in implementation negatively impacts performance. Instead of simple lock
in objects are more useful for applications involving signaling between Semaphore
threads or throttling. For example, if you want to limit the amount of concurrency in a
part of code, you might use a semaphore.
"""

import requests
from threading import Semaphore
from concurrent.futures import ThreadPoolExecutor, as_completed

# At most 5 threads allowed to run at once.
_fetch_url_sema = Semaphore(5)


def fetch_url(url):
    with _fetch_url_sema:
        return requests.get(url)


url = ['https://www.google.com'] * 20
with ThreadPoolExecutor(max_workers=10) as executor:
    for future in executor.map(fetch_url, url):
        print(future.text[:5])
