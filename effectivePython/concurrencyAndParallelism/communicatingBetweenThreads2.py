import time
import inspect
from threading import Event, Thread
from queue import Queue

SENTINEL = object()
EXIT_APP = False


def producer(out_queue):
    for _ in range(10):
        # Produce some data
        print(f"[{inspect.stack()[0][3]}] Producing data...")
        time.sleep(0.1)
        event = Event()
        data = 1
        print(f"[{inspect.stack()[0][3]}] Data produced. Putting it in output queue...")
        out_queue.put((data, event))
        # Wait for consumer to process the item
        event.wait()
    print(f"[{inspect.stack()[0][3]}] Putting sentinel data in queue...")
    out_queue.put((SENTINEL, -1))


def consumer(in_queue):
    while not EXIT_APP:
        # Get some data
        print(f"[{inspect.stack()[0][3]}] Getting data from queue...")
        data, event = in_queue.get(timeout=3)
        print(f"[{inspect.stack()[0][3]}] Got the data from queue.")
        if data is SENTINEL:
            print(f"[{inspect.stack()[0][3]}] Sentinel data received. Putting it in input queue and quiting...")
            in_queue.put(SENTINEL)
            break
        # Process the data
        print(f"[{inspect.stack()[0][3]}] Processing data...")
        data += 1
        # Indicate completion
        print(f"[{inspect.stack()[0][3]}] Done.")
        event.set()


def main():
    queue = Queue()
    threads = [
        Thread(target=consumer, args=(queue,)),
        Thread(target=producer, args=(queue,))
    ]
    for thread in threads:
        thread.start()
    queue.join()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        EXIT_APP = True
        raise
