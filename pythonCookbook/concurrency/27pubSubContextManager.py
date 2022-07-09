import time
from threading import Lock
from contextlib import contextmanager
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

lock = Lock()


class Exchange:

    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)
        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    def publish(self, msg):
        with ThreadPoolExecutor(max_workers=len(self._subscribers)) as executor:
            for subscriber in self._subscribers:
                executor.submit(subscriber.send, msg)


class Task:
    def __init__(self, name):
        self.name = name

    def send(self, msg):
        time.sleep(1)
        with lock:
            print(f"[{self.name}] {msg} loaded.")


task_a = Task('Process1')
task_b = Task('Process2')
task_c = Task('Process3')


# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)


def get_exchange(name):
    """Return the Exchange instance associated with a given name"""
    return _exchanges[name]


# Example of using the subscribe() method
exc = get_exchange('File Removed')
with exc.subscribe(task_a, task_b, task_c):
    exc.publish('File1')
    exc.publish('File2')
