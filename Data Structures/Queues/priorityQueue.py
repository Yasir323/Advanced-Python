class MaxSizeError(Exception):
    """Raised when queue is full."""

    def __init__(self, message="Queue is full") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class EmptyQueueError(Exception):
    """Raised when queue is empty."""

    def __init__(self, message="Queue is empty") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class Node:

    def __init__(self, data, priority):
        self.data = data
        self.priority = priority


class PriorityQueue:

    def __init__(self, maxlen=None):
        self.queue = []
        self._maxlen = maxlen

    def enqueue(self, node):
        size = len(self.queue)
        # If the queue is full
        if self._maxlen:
            if size >= self._maxlen:
                raise MaxSizeError
        # If the queue is empty
        if size == 0:
            self.queue.append(node)
        else:
            for i in range(size):
                # if the priority of new node is greater
                if node.priority > self.queue[i].priority:
                    self.queue.insert(i, node)
                    return
                else:
                    if i != size - 1:
                        continue
                    else:
                        self.queue.insert(i + 1, node)
                        return

    def dequeue(self):
        if self.queue:
            return self.queue.pop()
        else:
            raise EmptyQueueError

    def __len__(self):
        return len(self.queue)

    def print_queue(self):
        for node in self.queue:
            print(f"{node.data}: {node.priority}")

    def is_empty(self):
        return True if len(self.queue) == 0 else False

    def __repr__(self) -> str:
        return f"{[(node.data, node.priority) for node in self.queue]}"

    def __str__(self) -> str:
        return f"{[(node.data, node.priority) for node in self.queue]}"


queue = PriorityQueue(maxlen=3)
print(f"Original queue: {queue}")
queue.enqueue(Node('a', 10))
print(f"After inserting data: {queue}")
queue.enqueue(Node('f', 10))
print(f"After inserting data: {queue}")
queue.enqueue(Node('g', 20))
print(f"After inserting data: {queue}")
try:
    print("Let's try to add another element.")
    queue.enqueue(Node('h', 80))
except MaxSizeError as e:
    print(f"{type(e).__name__}: {e}")
queue.dequeue()
print(f"After using dequeue: {queue}")
# queue.print_queue()
print(f"Length of queue: {len(queue)}")
print(f"Is the queue empty: {queue.is_empty()}")
queue.dequeue()
queue.dequeue()
print(f"Is the queue empty: {queue.is_empty()}")
try:
    print("Let's try to remove another element.")
    queue.dequeue()
except EmptyQueueError as e:
    print(f"{type(e).__name__}: {e}")
