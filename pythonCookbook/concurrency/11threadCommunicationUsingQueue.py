import time
import random
from queue import Queue
from threading import Thread

# Object that signals shutdown
SENTINEL = ...


def produce_data():
    time.sleep(0.2)
    num = random.randint(0, 10_000)
    if num % 10 == 0:
        return SENTINEL
    return num


def consume_data(data):
    time.sleep(0.5)
    print('Consumed data: ', data)


def producer(out_q: Queue):
    """
    A thread that produces data.
    """
    running = True
    while running:
        # Produce some data
        produced_data = produce_data()
        if produced_data == SENTINEL:
            running = False
        out_q.put(produced_data)


def consumer(in_q: Queue):
    """
    A thread that consumes data.
    """
    while True:
        # Get some data
        data = in_q.get()
        if data is SENTINEL:
            in_q.put(SENTINEL)  # For other listening threads
            break
        # Process data
        consume_data(data)
        # Signal completion
        in_q.task_done()


q = Queue()
thread1 = Thread(target=consumer, args=(q,))
thread2 = Thread(target=producer, args=(q,))
thread1.start()
thread2.start()

# Wait for all produced items to be consumed
q.join()
