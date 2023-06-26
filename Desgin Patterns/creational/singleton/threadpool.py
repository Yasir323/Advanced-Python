import threading
from queue import Queue


class ThreadPool:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.queue = Queue()
            cls._instance.workers = []
        return cls._instance

    def add_task(self, task):
        self.queue.put(task)

    def start(self, num_workers):
        for _ in range(num_workers):
            worker = threading.Thread(target=self._worker_loop)
            worker.start()
            self.workers.append(worker)

    def _worker_loop(self):
        while True:
            task = self.queue.get()
            if task is None:
                break
            # Perform task execution
            task()
            self.queue.task_done()

    def stop(self):
        for _ in range(len(self.workers)):
            self.queue.put(None)
        for worker in self.workers:
            worker.join()


# Usage
def do_work():
    # Perform the actual work
    print("Work executed by thread:", threading.current_thread().name)


# Create and start the thread pool
thread_pool = ThreadPool()
thread_pool.start(num_workers=4)

# Add tasks to the thread pool
for _ in range(10):
    thread_pool.add_task(do_work)

# Wait for all tasks to complete
thread_pool.queue.join()

# Stop the thread pool
thread_pool.stop()
