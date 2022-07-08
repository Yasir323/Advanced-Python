"""
An RLock or re-entrant lock object is a lock that can be acquired multiple times by the same thread. It is primarily
used to implement code based locking or synchronization based on a construct known
as a “monitor.” With this kind of locking, only one thread is allowed to use an entire
function or the methods of a class while the lock is held.
"""

import threading


class SharedCounter:
    """
    A counter object that can be shared among threads.
    """
    _lock = threading.RLock()
    """
    In this variant of the code, there is just a single class-level lock shared by all instances
    of the class. Instead of the lock being tied to the per-instance mutable state, the lock is
    meant to synchronize the methods of the class. Specifically, this lock ensures that only
    one thread is allowed to be using the methods of the class at once. However, unlike a
    standard lock, it is OK for methods that already have the lock to call other methods that
    also use the lock.
    """

    def __init__(self, initial_value=0):
        self._value = initial_value

    def increment(self, delta=1):
        """
        Increment the counter with locking.
        """
        with SharedCounter._lock:
            self._value += delta

    def decrement(self, delta=-1):
        """
        Increment the counter with locking.
        """
        if delta > 0:
            self.increment(-delta)
        self.increment(delta)
