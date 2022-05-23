# Synchronisation using Locks
# Race Condition
import time
from concurrent.futures import ThreadPoolExecutor
import threading


class FakeDatabase:
    def __init__(self):
        """Initialize value to zero
        """
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        """Simulating reading a value from a database, doing some 
        computation on it, and then writing a new value back to 
        the database.

        Args:
            name (int): Name of the thread updating the shared data.
        """
        print(f"Thread {name} starting update.")
        print(f"Thread {name} waiting to acquire the lock.")
        with self._lock:
            print(f"Thread {name} has the lock.")
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            print(f"Thread {name} is releasing the lock.")
        print(f"Thread {name} has released the lock.")
        print(f"Thread {name} finishing update.")


if __name__ == '__main__':
    database = FakeDatabase()
    print(f"Testing update. Starting value is {database.value}")
    with ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    print(f"Testing update. Ending value is {database.value}")
