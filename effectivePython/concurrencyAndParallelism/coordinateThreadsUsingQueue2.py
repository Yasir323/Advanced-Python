"""
BAD IMPLEMENTATION, GETS STUCK AT THE LAST THREAD!!!

I want to build a system that will take a constant
stream of images from my digital camera, resize them, and then add
them to a photo gallery online. Such a program could be split into
three phases of a pipeline. New images are retrieved in the first phase.
The downloaded images are passed through the resize function in the
second phase. The resized images are consumed by the upload function
in the final phase.
"""

import time
from queue import Queue
from threading import Lock, Thread

my_queue = Queue()


def consumer():
    print("Consumer is waiting...")
    my_queue.get()
    print("Consumer done.")



thread = Thread(target=consumer)
thread.start()

print("Producer putting...")
my_queue.put(object())
print("Producer done!")
thread.join()
print('-'*50)
"""
To solve the pipeline backup issue, the Queue class lets you specify
the maximum amount of pending work to allow between two phases.

This buffer size causes calls to put to block when the queue is already
full. For example, here I define a thread that waits for a while before
consuming a queue.
"""
my_queue = Queue(1) # Buffer size of 1


def consumer():
    time.sleep(0.1) # Wait
    my_queue.get() # Runs second
    print('Consumer got 1')
    my_queue.get() # Runs fourth
    print('Consumer got 2')
    print('Consumer done')


thread = Thread(target=consumer)
thread.start()

"""
The wait should allow the producer thread to put both objects on the
queue before the consumer thread ever calls get. But the Queue size
is one. This means the producer adding items to the queue will have
to wait for the consumer thread to call get at least once before the
second call to put will stop blocking and add the second item to the
queue.
"""
my_queue.put(object()) # Runs first
print('Producer put 1')
my_queue.put(object()) # Runs third
print('Producer put 2')
print('Producer done')
thread.join()
print('-'*50)

"""
The Queue class can also track the progress of work using the
task_done method. This lets you wait for a phase’s input queue to
drain and eliminates the need to poll the last phase of a pipeline (as
with the done_queue above). For example, here I define a consumer
thread that calls task_done when it finishes working on an item
"""
in_queue = Queue()


def consumer():
    print('Consumer waiting')
    work = in_queue.get() # Runs second
    print('Consumer working')
    # Doing work
    time.sleep(0.1)
    print('Consumer done')
    in_queue.task_done() # Runs third


thread = Thread(target=consumer)
thread.start()

"""
Now, the producer code doesn’t have to join the consumer thread or
poll. The producer can just wait for the in_queue to finish by calling
join on the Queue instance. Even once it’s empty, the in_queue won’t
be joinable until after task_done is called for every item that was ever
enqueued:
"""
print('Producer putting')
in_queue.put(object()) # Runs first
print('Producer waiting')
in_queue.join() # Runs fourth
print('Producer done')
thread.join()
