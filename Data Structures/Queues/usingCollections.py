from collections import deque

queue = deque([1, 2, 3], maxlen=5)
print(f"Original stack: {queue}")
queue.append(4)
print(f"After using enqueue with a value of 4: {queue}")
queue.popleft()
print(f"After using dequeue: {queue}")
print(f"Length of queue: {len(queue)}")
print(f"Is the queue empty: {len(queue) == 0}")
