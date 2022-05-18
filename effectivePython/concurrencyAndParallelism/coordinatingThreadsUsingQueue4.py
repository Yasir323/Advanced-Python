import time
from threading import Thread
from queue import Queue


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


def start_threads(count, *args):
    threads = [Worker(*args) for _ in range(count)]
    for thread in threads:
        thread.start()
    return threads


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


def stop_threads(queue, threads):
    for _ in threads:
        queue.close()  # Send the sentinel value
    queue.join()
    for thread in threads:
        thread.join()


download_queue = MyQueue()
resize_queue = MyQueue()
upload_queue = MyQueue()
done_queue = MyQueue()
download_threads = start_threads(
    3, download, download_queue, resize_queue)
resize_threads = start_threads(
    4, resize, resize_queue, upload_queue)
upload_threads = start_threads(
    5, upload, upload_queue, done_queue)
for _ in range(1000):
    download_queue.put(object())

stop_threads(download_queue, download_threads)
stop_threads(resize_queue, resize_threads)
stop_threads(upload_queue, upload_threads)
print(done_queue.qsize(), 'items finished')
