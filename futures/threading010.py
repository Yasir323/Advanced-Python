import random
import time
import threading
from concurrent.futures import ThreadPoolExecutor

SENTINEL = object()


class Pipeline:
    """Class to allow a single message pipeline between producer and consumer."""
    
    def __init__(self) -> None:
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()
    
    def get_message(self, name):
        """Called by consumer."""
        print(f"{name} to acquire the getlock.")
        self.consumer_lock.acquire()
        #  This is the call that will make the consumer 
        # wait until a message is ready.
        print(f"{name} has acquired getlock.")
        message = self.message
        print(f"{name} about to release setlock.")
        self.producer_lock.release()
        # Releasing this lock is what allows the producer 
        # to insert the next message into the pipeline.
        print(f"{name} setlock released.")
        return message

    def set_message(self, message, name):
        """Called by consumer."""
        print(f"{name} about to acquire setlock.")
        self.producer_lock.acquire()
        print(f"{name} has setlock.")
        self.message = message
        print(f"{name} about to release getlock.")
        self.consumer_lock.release()
        print(f"{name} getlock released.")


def producer(pipeline):
    """Pretend we are getting a message from a network."""
    for index in range(10):
        message = random.randint(1, 101)
        print(f"Producer got message {message}")
        # Send the message to the consumer
        pipeline.set_message(message, 'Producer')

    # Send a sentinel signal to tell consumer to stop after sending a burst of 10 messages.
    pipeline.set_message(SENTINEL, 'Producer')


def consumer(pipeline):
    """Pretend we're saving a message in the database."""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message('Consumer')
        if message is not SENTINEL:
            # Writing message to the fake database (stdout)
            time.sleep(0.1)
            print(f"Consumer storing message: {message}")


if __name__ == "__main__":
    pipeline = Pipeline()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
