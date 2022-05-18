import time
import inspect
from queue import Queue
from threading import Thread

_sentinel = object()


def producer(out_queue):
    for _ in range(10):
        # Produce some data
        print(f"[{inspect.stack()[0][3]}] Producing data...")
        time.sleep(0.1)
        data = 1
        print(f"[{inspect.stack()[0][3]}] Data produced. Putting it in output queue...")
        out_queue.put(data)
    print(f"[{inspect.stack()[0][3]}] Putting sentinel data in queue...")
    out_queue.put(_sentinel)


def consumer(in_queue):
    while True:
        # Get some data
        print(f"[{inspect.stack()[0][3]}] Getting data from queue...")
        data = in_queue.get()
        print(f"[{inspect.stack()[0][3]}] Got the data from queue.")

        if data is _sentinel:
            print(f"[{inspect.stack()[0][3]}] Sentinel data received. Putting it in input queue and quiting...")
            in_queue.put(_sentinel)
            break
        # Process the data
        print(f"[{inspect.stack()[0][3]}] Processing data...")
        data += 1
        # Indicate completion
        print(f"[{inspect.stack()[0][3]}] Done.")
        in_queue.task_done()


queue = Queue()
threads = [
    Thread(target=consumer, args=(queue,)),
    Thread(target=producer, args=(queue,))
]
for thread in threads:
    thread.start()
queue.join()
