from queue import Queue
from threading import Thread, Event


class ActorExit(Exception):
    """Sentinel used for shutdown."""
    pass


class Actor:

    def __init__(self):
        self._terminated = Event()
        self._mailbox = Queue()

    def send(self, msg):
        """Send a message to any actor."""
        self._mailbox.put(msg)

    def recv(self):
        """Receive an incoming message."""
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        """Close the actor, thus shutting it down."""
        self.send(ActorExit)

    def start(self):
        """Start a concurrent execution."""
        thread = Thread(target=self._bootstrap, daemon=True)
        thread.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        """Wait for the actor to finish."""
        self._terminated.wait()

    def run(self):
        """Run method implemented by the user."""
        while True:
            msg = self.recv()  # Blocking


# As another example, here is a variation of an actor that allows arbitrary functions to be
# executed in a worker and results to be communicated back using a special Result object:
class Result:

    def __init__(self):
        self._evt = Event()
        self._result = None

    def set_result(self, value):
        self._result = value
        self._evt.set()

    def result(self):
        self._evt.wait()
        return self._result


class Worker(Actor):

    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))


if __name__ == '__main__':
    # Example use
    worker = Worker()
    worker.start()
    r = worker.submit(pow, 2, 3)
    print(r.result())
