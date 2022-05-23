from queue import LifoQueue

stack = LifoQueue(maxsize=3)
print(f"Original stack: {stack}")
stack.put(1, block=True, timeout=2)
stack.put(2, block=True, timeout=2)
stack.put(4, block=True, timeout=2)
print(f"After pushing 4: {stack}")
stack.get(block=True, timeout=2)
print(f"After popping: {stack}")
stack.put(5, block=True, timeout=2)
print(f"Length of stack: {stack.qsize()}")
# print(f"Top of the stack: {stack}")
print(f"Is the stack empty: {stack.empty()}")
print(f"Is the stack full: {stack.full()}")
