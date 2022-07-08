"""
If a thread needs to know immediately when a consumer thread has processed a particular
item of data, you should pair the sent data with an Event object that allows the
producer to monitor its progress.

One caution with thread queues is that putting an item in a queue doesn’t make a copy
of the item. Thus, communication actually involves passing an object reference between
threads. If you are concerned about shared state, it may make sense to only pass im
mutable
data structures (e.g., integers, strings, or tuples) or to make deep copies of the
queued items.
"""

import copy
import time
import random
from queue import Queue
from threading import Thread, Event

# Object that signals shutdown
SENTINEL = ...


def produce_data():
    time.sleep(0.2)
    return random.randint(0, 10_000)


def consume_data(data):
    time.sleep(0.5)
    print('Consumed data: ', data)


def producer(out_q: Queue):
    """
    A thread that produces data.
    """
    items_left = 10
    while items_left > 0:
        # Produce some data
        produced_data = produce_data()
        if produced_data == SENTINEL:
            break
        # Put it in the queue
        evt = Event()
        out_q.put((copy.deepcopy(produced_data), evt))
        items_left -= 1
        # Wait for the consumer to process the item
        evt.wait()
    out_q.put((SENTINEL, None))


def consumer(in_q: Queue):
    """
    A thread that consumes data.
    """
    while True:
        # Get some data
        data, evt = in_q.get()
        if data is SENTINEL:
            in_q.put(SENTINEL)  # For other listening threads
            break
        # Process data
        consume_data(data)
        # Signal completion
        in_q.task_done()
        evt.set()


q = Queue()
thread1 = Thread(target=consumer, args=(q,))
thread2 = Thread(target=producer, args=(q,))
thread1.start()
thread2.start()

# Wait for all produced items to be consumed
q.join()
