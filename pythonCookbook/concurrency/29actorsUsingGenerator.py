from collections import deque


class ActorScheduler:

    def __init__(self):
        self._actors = {}
        self._mailbox = deque()

    def new_actor(self, name, actor):
        """Admit a newly started actor to the scheduler and give it a name."""
        self._mailbox.append((actor, None))
        self._actors[name] = actor

    def send(self, name, msg):
        """Send a message to a names actor"""
        actor = self._actors.get(name)
        if actor:
            self._mailbox.append((actor, msg))

    def run(self):
        """Run as long as there are pending messages."""
        while self._mailbox:
            actor, msg = self._mailbox.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass


if __name__ == '__main__':
    def printer():
        """Printer actor"""
        while True:
            msg = yield
            print('Got: ', msg)


    def counter(sched):
        """counter actor"""
        while True:
            # Receive the current count
            n = yield
            if n == 0:
                break

            # Send to the printer task
            sched.send('printer', n)
            # Send the next count to the counter task
            sched.send('counter', n - 1)


    sched = ActorScheduler()
    # Create the initial actors
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))
    # Send an initial message to the counter to initiate
    sched.send('counter', 10000)
    sched.run()
