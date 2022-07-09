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


class UpperCaseActor(Actor):
    """Sample actor task."""
    def run(self):
        while True:
            msg = self.recv()
            try:
                res = str(msg).upper()
            except TypeError:
                res = msg
            print("Got: ", res)


if __name__ == '__main__':
    p = UpperCaseActor()
    p.start()
    p.send('Hello')
    p.send('World')
    p.send(4)
    p.close()
    p.join()
