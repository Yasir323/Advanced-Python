from collections import defaultdict
from contextlib import contextmanager


class Exchange:
    """
    An exchange is really nothing more than an object that keeps a set of active subscribers
    and provides methods for attaching, detaching, and sending messages.
    """

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

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


class Task:

    def __init__(self):
        pass

    def send(self, msg):
        print('Sending mesage: {}'.format(msg))


task_a = Task()
task_b = Task()

# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)


# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]


# Example of using the subscribe() method
exc = get_exchange('name')
with exc.subscribe(task_a, task_b):
    exc.send('msg1')
    exc.send('msg2')
