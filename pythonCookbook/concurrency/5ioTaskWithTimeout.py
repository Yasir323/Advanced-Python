import requests
from requests.exceptions import ConnectTimeout
from threading import Thread


class IOTask:

    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, timeout):
        while self._running:
            # Perform a blocking operation with a
            # Timeout specified.
            try:
                data = requests.get("https://www.python.org", timeout=timeout)
                all_data.append(data.text)
                break
            except ConnectTimeout:
                self.terminate()
        return


all_data = []
c = IOTask()
t = Thread(target=c.run, args=(0.3,))
t.start()
c.terminate()
t.join()
print(all_data)
