"""
Creating and manipulating thread-specific state is not a problem that often arises in
most programs. However, when it does, it commonly involves situations where an object
being used by multiple threads needs to manipulate some kind of dedicated system
resource, such as a socket or file. You can’t just have a single socket object shared by
everyone because chaos would ensue if multiple threads ever started reading and writing
on it at the same time. Thread-local storage fixes this by making such resources only
visible in the thread where they’re being used.
In this recipe, the use of threading.local() makes the LazyConnection class support
one connection per thread, as opposed to one connection for the entire process. It’s a
subtle but interesting distinction.
Under the covers, an instance of threading.local() maintains a separate instance
dictionary for each thread. All of the usual instance operations of getting, setting, and
deleting values just manipulate the per-thread dictionary. The fact that each thread uses
a separate dictionary is what provides the isolation of data.
"""

import threading
from functools import partial
from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:

    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.local= threading.local()

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError("Already Connected.")
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock


def test(conn):
    with conn as c:
        c.send(b"GET /index.html HTTP/1.0\r\n")
        c.send(b"Host: www.python.org\r\n")
        c.send(b"\r\n")
        response = b"".join(iter(partial(c.recv, 8192), b""))

    print("Got {} bytes".format(len(response)))


if __name__ == '__main__':
    conn = LazyConnection(("www.python.org", 80))
    t1 = threading.Thread(target=test, args=(conn,))
    t2 = threading.Thread(target=test, args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
