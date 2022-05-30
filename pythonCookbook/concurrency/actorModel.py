"""
The “actor model” is one of the oldest and most simple approaches to concurrency and
distributed computing. In fact, its underlying simplicity is part of its appeal. In a nutshell,
an actor is a concurrently executing task that simply acts upon messages sent to it. In
response to these messages, it may decide to send further messages to other actors.
Communication with actors is one way and asynchronous. Thus, the sender of a message
does not know when a message actually gets delivered, nor does it receive a response
or acknowledgment that the message has been processed.
"""

from queue import Queue
from threading import Thread, Event


class ActorExit(Exception):
    """Sentinel used for shutdown.
    """
    pass


class Actor:

    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        """Send a msg to the actor.
        """
        self._mailbox.put(msg)

    def recv(self):
        """Receive an incoming msg.
        """
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        """Close the actor, thus shutting it down.
        """
        self.send(ActorExit)

    def start(self):
        """Start concurrent execution.
        """
        self._terminated = Event()
        t = Thread(target=self._bootstrap, daemon=True)
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        """Run method to be implemented by the user.
        """
        while True:
            msg = self.recv()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print("Got:", msg)


# Sample use
p = PrintActor()
p.start()
p.send('Hello')
p.send('World')
p.close()
p.join()
