"""
BAD IMPLEMENTATION, GETS STUCK AT THE LAST THREAD!!!

I want to build a system that will take a constant
stream of images from my digital camera, resize them, and then add
them to a photo gallery online. Such a program could be split into
three phases of a pipeline. New images are retrieved in the first phase.
The downloaded images are passed through the resize function in the
second phase. The resized images are consumed by the upload function
in the final phase.
"""

import time
from collections import deque
from threading import Lock, Thread


def download(item):
    time.sleep(0.1)
    return item


def resize(item):
    # Do something here
    time.sleep(0.1)
    return item


def upload(item):
    time.sleep(0.1)
    return item


"""
The first thing I need is a way to hand off work between the pipeline
phases. This can be modeled as a thread-safe producer–consumer
queue
"""

class MyQueue:

    def __init__(self):
        self.items = deque()
        self.lock = Lock()


    def put(self, item):
        """
        The producer, my digital camera, adds new images to the end of the
        deque of pending items:
        """
        with self.lock:
            self.items.append(item)

    def get(self):
        """
        The consumer, the first phase of the processing pipeline, removes
        images from the front of the deque of pending items:
        """
        with self.lock:
            return self.items.popleft()


"""
Here, I represent each phase of the pipeline as a Python thread that
takes work from one queue like this, runs a function on it, and puts
the result on another queue. I also track how many times the worker
has checked for new input and how much work it’s completed.

The trickiest part is that the worker thread must properly handle
the case where the input queue is empty because the previous
phase hasn’t completed its work yet. This happens where I catch the
IndexError exception below. You can think of this as a holdup in the
assembly line.
"""


class Worker(Thread):

    def __init__(self, func, in_queue, out_queue):
        super().__init__()
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.polled_count = 0
        self.work_done = 0

    def run(self) -> None:
        while True:
            self.polled_count += 1
            try:
                item = self.in_queue.get()
            except IndexError:
                print(f"[{self.func.__name__}] Queue is empty, nothing to do")
                time.sleep(0.01)
            else:
                result = self.func(item)
                self.out_queue.put(result)
                self.work_done += 1


"""
Now, I can connect the three phases together by creating the queues
for their coordination points and the corresponding worker threads
"""
download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()

threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue),
]

"""
I can start the threads and then inject a bunch of work into the first
phase of the pipeline. Here, I use a plain object instance as a proxy
for the real data required by the download function
"""
for thread in threads:
    thread.start()

for _ in range(20):
    download_queue.put(object())

"""
Now, I wait for all of the items to be processed by the pipeline and end
up in the done_queue
"""
prev_done = len(done_queue.items)
while len(done_queue.items) < 20:
    # Do something useful while waiting
    if prev_done < len(done_queue.items):
        print(len(done_queue.items))
        prev_done = len(done_queue.items)

"""
This runs properly, but there’s an interesting side effect caused by
the threads polling their input queues for new work. The tricky part,
where I catch IndexError exceptions in the run method, executes a
large number of times
"""

processed = len(done_queue.items)
polled = sum(t.polled_count for t in threads)
print(f"Processed {processed} items after polling {polled} items.")
