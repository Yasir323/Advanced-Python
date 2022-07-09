"""
To implement publish/subscribe messaging, you typically introduce a separate “exchange”
or “gateway” object that acts as an intermediary for all messages. That is, instead
of directly sending a message from one task to another, a message is sent to the exchange,
and it delivers it to one or more attached tasks.

Although there are many variations on this theme, the overall idea is the same.
Messages will be delivered to an exchange and the exchange will deliver them to attached
subscribers.
"""

import time
from collections import defaultdict
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

lock = Lock()


class Exchange:
    """
    An exchange is really nothing more than an object that keeps a set of active
    subscribers and provides methods for attaching, detaching, and sending messages.
    """

    def __init__(self):
        self._subscribers = set()

    def subscribe(self, task):
        self._subscribers.add(task)

    def unsubscribe(self, task):
        self._subscribers.remove(task)

    def publish(self, msg):
        with ThreadPoolExecutor(max_workers=len(self._subscribers)) as executor:
            for subscriber in self._subscribers:
                executor.submit(subscriber.send, msg)

    def publish_sequential(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


_exchanges = defaultdict(Exchange)


def get_exchange(name):
    """
    Each exchange is identified by a name, and the get_exchange() function simply
    returns the Exchange instance associated with a given name.
    """
    return _exchanges[name]


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

# Getting an exchange
exc = get_exchange('File Removed')

exc.subscribe(task_a)
exc.subscribe(task_b)
exc.subscribe(task_c)

exc.publish('File1')
print()
exc.publish_sequential('File2')
print()

exc.unsubscribe(task_c)

exc.publish('File3')
exc.unsubscribe(task_a)
exc.unsubscribe(task_b)
