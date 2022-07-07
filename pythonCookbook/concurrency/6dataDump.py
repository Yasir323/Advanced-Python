import time
from threading import Thread

data = []
threads = []


def worker(multiple, thread_num):
    for i in range(1, 40):
        data.append((i * multiple, thread_num))
        time.sleep(0.005)


for i in range(3):
    thread = Thread(target=worker, args=(i + 1, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(data)
