import random
import time
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor


class Pipeline(Queue):
    """Class to allow a single message pipeline between producer and consumer."""
    
    def __init__(self) -> None:
        super().__init__(maxsize=10)
    
    def get_message(self, name):
        """Called by consumer."""
        print(f"{name}: to get from queue.")
        value = self.get()
        print(f"{name}: got {value} from queue.")
        return value

    def set_message(self, value, name):
        """Called by consumer."""
        print(f"{name}: about to add {value} to queue.")
        self.put(value)
        print(f"{name}: added {value} to queue.")


def producer(pipeline, event):
    """Pretend we are getting a message from a network."""
    while  not event.is_set():
        message = random.randint(1, 101)
        print(f"Producer got message {message}")
        # Send the message to the consumer
        pipeline.set_message(message, 'Producer')
    print("Producer received Exit event.")


def consumer(pipeline, event):
    """Pretend we're saving a message in the database."""
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message('Consumer')
        print(f"Consumer storing message: {message} (queue size={pipeline.qsize()})")
    print(f"Consumer received EXIT event. Exiting...")


if __name__ == "__main__":
    pipeline = Pipeline()
    event = threading.Event()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        print("Main: about to set event")
        event.set()

"""
If you read through the output in my example, you can see 
some interesting things happening. Right at the top, you 
can see the producer got to create five messages and place 
four of them on the queue. It got swapped out by the 
operating system before it could place the fifth one.

The consumer then ran and pulled off the first message. 
It printed out that message as well as how deep the queue 
was at that point.

This is how you know that the fifth message hasn’t made it 
into the pipeline yet. The queue is down to size three 
after a single message was removed. You also know that the 
queue can hold ten messages, so the producer thread didn’t 
get blocked by the queue. It was swapped out by the OS.

As the program starts to wrap up, can you see the main thread 
generating the event which causes the producer to exit 
immediately. The consumer still has a bunch of work do to, 
so it keeps running until it has cleaned out the pipeline.

Try playing with different queue sizes and calls to time.sleep() 
in the producer or the consumer to simulate longer network 
or disk access times respectively. Even slight changes to 
these elements of the program will make large differences 
in your results.

This is a much better solution to the producer-consumer problem, 
but you can simplify it even more. The Pipeline really isn’t 
needed for this problem. Once you take away the logging, it 
just becomes a queue.Queue.
"""