import threading


class SharedCounter:
    """
    A counter object that can be shared among threads.
    """

    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def increment(self, delta=1):
        """
        Increment the counter with locking.
        """
        with self._value_lock:
            self._value += delta

    def decrement(self, delta=-1):
        """
        Increment the counter with locking.
        """
        self.increment(delta)


