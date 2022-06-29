"""
Semaphore
A Semaphore is a counter with a few special properties. 
The first one is that the counting is atomic. This means 
that there is a guarantee that the operating system will 
not swap out the thread in the middle of incrementing or 
decrementing the counter.

The internal counter is incremented when you call .release() 
and decremented when you call .acquire().

The next special property is that if a thread calls .acquire() 
when the counter is zero, that thread will block until a 
different thread calls .release() and increments the counter 
to one.

Semaphores are frequently used to protect a resource that has 
a limited capacity. An example would be if you have a pool of 
connections and want to limit the size of that pool to a 
specific number.
"""
