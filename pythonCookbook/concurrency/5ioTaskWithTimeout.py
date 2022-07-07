import socket
from threading import Thread


class IOTask:

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(3)
        while self._running:
            # Perform a blocking operation with a
            # Timeout specified.
            try:
                data = sock.recv(8192).decode()
                data.append(all_data)
                break
            except socket.timeout:
                continue
        return


all_data = []
c = IOTask()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
# print(s.recv(1024).decode())
t = Thread(target=c.run, args=(s,))
t.start()
c.terminate()
t.join()
print(all_data)
