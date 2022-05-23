from collections import deque

stack = deque([1, 2, 3], maxlen=5)
print(f"Original stack: {stack}")
stack.append(4)
print(f"After pushing 4: {stack}")
stack.pop()
print(f"After popping: {stack}")
print(f"Length of stack: {len(stack)}")
print(f"Top of the stack: {stack[-1]}")
print(f"Is the stack empty: {len(stack) == 0}")