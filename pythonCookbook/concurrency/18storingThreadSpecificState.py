"""
Sometimes in multi-threaded programs, you need to store data that is only specific to
the currently executing thread. To do this, create a thread-local storage object using
.local(). Attributes stored and read on this object are only visible to the
threading executing thread and no others.
"""

import threading
from functools import partial
from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:

    def __init__(self, address, family=AF_INET, type_=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type_ = type_
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already Connected.')
        self.local.sock = socket(self.family, self.type_)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock


def check(conn):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))

    print('Got {} bytes'.format(len(resp)))


if __name__ == '__main__':
    conn = LazyConnection(('www.python.org', 80))
    thread1 = threading.Thread(target=check, args=(conn,))
    thread2 = threading.Thread(target=check, args=(conn,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

"""
Creating and manipulating thread-specific state is not a problem that often arises in
most programs. However, when it does, it commonly involves situations where an object
being used by multiple threads needs to manipulate some kind of dedicated system
resource, such as a socket or file. You can’t just have a single socket object shared by
everyone because chaos would ensue if multiple threads ever started reading and writing
on it at the same time. Thread-local storage fixes this by making such resources only
visible in the thread where they’re being used.

In this recipe, the use of makes the class support threading.local() LazyConnection
one connection per thread, as opposed to one connection for the entire process. It’s a
subtle but interesting distinction.

Under the covers, an instance of maintains a separate instance threading.local() dictionary for each thread. All of the
usual instance operations of getting, setting, and deleting values just manipulate the per-thread dictionary. The fact
that each thread uses a separate dictionary is what provides the isolation of data.
"""
