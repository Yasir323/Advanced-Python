import queue
import threading
import requests

hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com",
"http://ibm.com", "http://apple.com"]


def func(q: queue.Queue, r: queue.Queue):
    while not q.empty():
        url = q.get()
        q.task_done()
        response = requests.get(url, timeout=3)
        r.put(response.content[:20])
        # r.task_done()
        print(response.status_code)
        # print(f'Thread #{thread_no} is doing task #{task} in the queue.')


source = queue.Queue()
sink = queue.Queue()
for host in hosts:
    source.put(host)

for i in range(5):
    worker = threading.Thread(target=func, args=(source, sink))
    worker.start()
# func(source, sink)

source.join()

for i in range(len(hosts)):
    print(sink.get())
