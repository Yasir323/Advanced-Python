from collections import defaultdict


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

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# Dictionary of all created exchanges
_exchanges = defaultdict(Exchange)

# Return the Exchange instance associated with a given name
def get_exchange(name):
    """
    Each exchange is identified by a name, and this function simply returns the Ex
    change instance associated with a given name.
    """
    return _exchanges[name]


class Task:

    def __init__(self):
        pass

    def send(self, msg):
        print('Sending mesage: {}'.format(msg))


task_a = Task()
task_b = Task()

# Example of getting an exchange
exc = get_exchange('name')
print("Subscribing")
# Examples of subscribing tasks to it
exc.attach(task_a)
exc.attach(task_b)

print("Sending")
# Example of sending a msg
exc.send('msg1')
exc.send('msg2')

print("Unsubscribing")
# Example of unsubscribing
exc.detach(task_a)
exc.detach(task_b)


class DisplayMessages:

    def __init__(self):
        self.count = 0

    def send(self, msg):
        self.count += 1
        print('msg[{}]: {!r}'.format(self.count, msg))


exc = get_exchange('name')
d = DisplayMessages()
exc.attach(d)
