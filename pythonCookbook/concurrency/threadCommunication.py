import time
import inspect
from queue import Queue
from threading import Thread

# Object that signals shutdown
SENTINEL = object()


# A thread that produces data
def producer(out_q):
    for _ in range(10):
        # Produce some data
        print(f"[{inspect.stack()[0][3]}] Producing data...")
        time.sleep(0.1)
        data = 1
        print(f"[{inspect.stack()[0][3]}] Data produced. Putting it in output queue...")
        out_q.put(data)
    # Put the sentinel on the queue to indicate completion
    print(f"[{inspect.stack()[0][3]}] Putting SENTINEL data in output queue...")
    out_q.put(SENTINEL)


# A thread that consumes data
def consumer(in_q):
    while True:
        # Get some data
        print(f"[{inspect.stack()[0][3]}] Getting data from queue...")
        data = in_q.get()
        if data is SENTINEL:
            print(f"[{inspect.stack()[0][3]}] Got SENTINEL data from queue. Exiting...")
            # A subtle feature of this example is that the consumer, upon receiving the special sentinel
            # value, immediately places it back onto the queue. This propagates the sentinel to other
            # consumers threads that might be listening on the same queue—thus shutting them all
            # down one after the other.
            in_q.put(data)
            break
        # Process the data
        print(f"[{inspect.stack()[0][3]}] Processing data...")
        data += 1
        print(data)


# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
