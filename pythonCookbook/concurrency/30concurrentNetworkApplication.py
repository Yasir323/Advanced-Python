from collections import deque
from select import select


class YieldEvent:
    """This class represents a generic yield event in the scheduler."""

    def handle_yield(self, scheduler, task):
        pass

    def handle_resume(self, scheduler, task):
        pass


class Scheduler:
    """Task scheduler"""
    def __init__(self):
        self._num_tasks = 0
        self._ready = deque()
        self._read_waiting = {}
        self._write_waiting = {}

    def _iopoll(self):
        rset, wset, eset = select(self._read_waiting, self._write_waiting, [])
        for r in rset:
            evt, task = self._read_waiting.pop(r)
            evt.handle_resume(self, task)

        for w in wset:
            evt, task = self._write_waiting.pop(w)
            evt.handle_resume(self, task)

    def new(self, task):
        """Add a newly started task to the scheduler."""
        self._ready.append((task, None))
        self._num_tasks += 1

    def add_ready(self, task, msg=None):
        """Append an already started task to the ready queue.
        msg is what to send into the task when it resumes."""
        self._ready.append((task, msg))

    def read_wait(self, file_no, evt, task):
        """Add a task to the reading set."""
        self._read_waiting[file_no] = (evt, task)

    def write_wait(self, file_no, evt, task):
        """Add a task to the writing set."""
        self._write_waiting[file_no] = (evt, task)

    def run(self):
        """Run the task scheduler until there are no tasks."""
        while self._num_tasks:
            if not self._ready:
                self._iopoll()
            task, msg = self._ready.popleft()
            try:
                # Run the coroutine to the next yield
                r = task.send(msg)
                if isinstance(r, YieldEvent):
                    r.handle_yield(self, task)
                else:
                    raise RuntimeError('unrecogized yield event')
            except StopIteration:
                self._num_tasks -= 1


class ReadSocket(YieldEvent):
    def __init__(self, sock, n_bytes):
        self.sock = sock
        self.n_bytes = n_bytes

    def handle_yield(self, sched, task):
        sched.read_wait(self.sock.fileno(), self, task)

    def handle_resume(self, sched, task):
        data = self.sock.recv(self.n_bytes)
        sched.add_ready(task, data)


class WriteSocket(YieldEvent):

    def __init__(self, sock, data):
        self.sock = sock
        self.data = data

    def handle_yield(self, sched, task):
        sched.write_wait(self.sock.fileno(), self, task)

    def handle_resume(self, sched, task):
        n_sent = self.sock.send(self.data)
        sched.add_ready(task, n_sent)


class AcceptSocket(YieldEvent):

    def __init__(self, sock):
        self.sock = sock

    def handle_yield(self, sched, task):
        sched.read_wait(self.sock.fileno(), self, task)

    def handle_resume(self, sched, task):
        r = self.sock.accept()
        sched.add_ready(task, r)


class Socket(object):
    """Wrapper around a socket object for use with yield"""

    def __init__(self, sock):
        self._sock = sock

    def recv(self, maxbytes):
        return ReadSocket(self._sock, maxbytes)

    def send(self, data):
        return WriteSocket(self._sock, data)

    def accept(self):
        return AcceptSocket(self._sock)

    def __getattr__(self, name):
        return getattr(self._sock, name)


if __name__ == '__main__':
    from socket import socket, AF_INET, SOCK_STREAM

    # Example of a function involving generators. This should
    # be called using line = yield from readline(sock)
    def readline(sock):
        chars = []
        while True:
            c = yield sock.recv(1)
            if not c:
                break
            chars.append(c)
            if c == b'\n':
                break
        return b''.join(chars)


    class EchoServer:
        """Echo server using generators"""

        def __init__(self, addr, sched):
            self.sched = sched
            sched.new(self.server_loop(addr))

        def server_loop(self, addr):
            s = Socket(socket(AF_INET, SOCK_STREAM))
            s.bind(addr)
            s.listen(5)
            while True:
                c, a = yield s.accept()
                print('Got connection from ', a)
                self.sched.new(self.client_handler(Socket(c)))

        @staticmethod
        def client_handler(client):
            while True:
                line = yield from readline(client)
                if not line:
                    break
                line = b'GOT:' + line
                while line:
                    n_sent = yield client.send(line)
                    line = line[n_sent:]
            client.close()
            print('Client closed')


    sched = Scheduler()
    EchoServer(('', 16000), sched)
    sched.run()
