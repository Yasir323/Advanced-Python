from concurrent.futures import ThreadPoolExecutor
import urllib.request


def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data


pool = ThreadPoolExecutor(10)

# Submit work to the pool
a = pool.submit(fetch_url, 'http://www.python.org')
b = pool.submit(fetch_url, 'http://www.pypy.org')

# Get the results back
x = a.result()
y = b.result()
print(x)
print(y)

"""
The operation a.result() blocks until the corresponding function 
has been executed by the pool and returned a value.

You might be concerned with the effect of creating a large number of threads. However,
modern systems should have no trouble creating pools of a few thousand threads.
Moreover, having a thousand threads just sitting around waiting for work isn’t going to
have much, if any, impact on the performance of other code (a sleeping thread does just
that—nothing at all). Of course, if all of those threads wake up at the same time and
start hammering on the CPU, that’s a different story—especially in light of the Global
Interpreter Lock (GIL). Generally, you only want to use thread pools for I/O-bound
processing.
One possible concern with creating large thread pools might be memory use. For example,
if you create 2,000 threads on OS X, the system shows the Python process using
up more than 9 GB of virtual memory. However, this is actually somewhat misleading.
When creating a thread, the operating system reserves a region of virtual memory to
hold the thread’s execution stack (often as large as 8 MB). Only a small fragment of this
memory is actually mapped to real memory, though. Thus, if you look a bit closer, you
might find the Python process is using far less real memory (e.g., for 2,000 threads, only
70 MB of real memory is used, not 9 GB). If the size of the virtual memory is a concern,
you can dial it down using the threading.stack_size() function. For example:

import threading
threading.stack_size(65536)

If you add this call and repeat the experiment of creating 2,000 threads, you’ll find that
the Python process is now only using about 210 MB of virtual memory, although the
amount of real memory in use remains about the same. Note that the thread stack size
must be at least 32,768 bytes, and is usually restricted to be a multiple of the system
memory page size (4096, 8192, etc.).
"""
