from queue import Queue

queue = Queue(maxsize=3)
print(f"Original stack: {queue}")
queue.put(1, block=True, timeout=2)
queue.put(2, block=True, timeout=2)
queue.put(4, block=True, timeout=2)
print(f"After pushing 4: {queue}")
queue.get(block=True, timeout=2)
print(f"After popping: {queue}")
queue.put(5, block=True, timeout=2)
print(f"Length of queue: {queue.qsize()}")
print(f"Is the queue empty: {queue.empty()}")
print(f"Is the queue full: {queue.full()}")
try:
    queue.put(90, block=True, timeout=2)
except Exception as e:
    print(type(e).__name__)
