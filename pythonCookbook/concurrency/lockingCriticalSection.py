"""
Locking Critical Sections

To avoid the potential for deadlock, programs that use locks should be written in a way
such that each thread is only allowed to acquire one lock at a time. If this is not possible,
you may need to introduce more advanced deadlock avoidance into your program.

In the threading library, you’ll find other synchronization primitives, such as RLock
and Semaphore objects. As a general rule of thumb, these are more special purpose and
should not be used for simple locking of mutable state. An RLock or re-entrant lock
object is a lock that can be acquired multiple times by the same thread. It is primarily
used to implement code based locking or synchronization based on a construct known
as a “monitor.” With this kind of locking, only one thread is allowed to use an entire
function or the methods of a class while the lock is held. For example, you could implement
the SharedCounter class like this
"""

import threading


class SharedCounter:
    """
    A counter that can be used by multiple threads.
    """

    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def increment(self, delta=1):
        """
        Increment the counter
        """
        # self._value_lock.acquire()
        # self._value += delta
        # self._value_lock.release()
        with self._value_lock:
            self._value += delta

    def decrement(self, delta=1):
        """
        Decrement the counter
        """
        # self._value_lock.acquire()
        # self._value -= delta
        # self._value_lock.release()
        with self._value_lock:
            self._value += delta
