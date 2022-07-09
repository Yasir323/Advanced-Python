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


# You could pass tagged messages in the form of tuples and have actors take different
# courses of action like this:
class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self, 'do_' + tag)(*payload)

    @staticmethod
    def do_a(x):
        print("Running a: ", x)

    @staticmethod
    def do_b(*args):
        print("Running b: ", *args)


if __name__ == '__main__':
    t = TaggedActor()
    t.start()
    t.send(('a', 1))
    t.send(('b', 11, 2))
    t.close()
    t.join()
