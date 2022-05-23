import time
from queue import Queue
from threading import Thread


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


class MyQueue(Queue):
    """
    When using queues, it can be somewhat tricky to coordinate the
    shutdown of the producer and consumer.

    A common solution to this problem is to rely on a special sentinel
    value, which when placed in the queue, causes consumers to
    terminate as shown in the code below
    """
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        """
        I define an iterator for the queue that looks for this special
        object and stops iteration when it’s found. This __iter__ method also
        calls task_done at appropriate times, letting me track the progress of
        work on the queue.
        """
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return  # Cause the thread to exit
                yield item
            finally:
                self.task_done()


class Worker(Thread):

    def __init__(self, func, input_queue, output_queue):
        super().__init__()
        self.func = func
        self.input_queue = input_queue
        self.output_queue = output_queue

    def run(self):
        for item in self.input_queue:
            result = self.func(item)
            self.output_queue.put(result)


download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()
threads = [
    Worker(download, download_queue, resize_queue),
    Worker(resize, resize_queue, upload_queue),
    Worker(upload, upload_queue, done_queue),
]

for thread in threads:
    thread.start()

for _ in range(20):
    download_queue.put(object())

"""
Finally, I wait for the work to finish by joining the queues that connect
the phases. Each time one phase is done, I signal the next phase
to stop by closing its input queue. At the end, the done_queue contains
all of the output objects, as expected
"""

download_queue.close()
download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()
print(done_queue.qsize(), 'items finished')

for thread in threads:
    thread.join()
