import time
import socket
from threading import Thread


class CountdownTask:

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print("T-minus", n)
            n -= 1
            time.sleep(1)


c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate()
t.join()

print('-'*50)

class IOTask:

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)
        while self._running:
            # Perform a blocking I/O operation w/ timeout
            try:
                data = sock.recv(8192)
                print(data)
                break
            except socket.timeout:
                continue
            # Continued processing
            time.sleep(0.1)
        # Teminated
        return


c = IOTask()
t = Thread(target=c.run, args=(socket.socket(),))
t.start()
c.terminate()
t.join()
