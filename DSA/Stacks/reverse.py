from usingLists import Stack


def insert_(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        temp = stack.pop()
        insert_(stack, item)
        stack.push(temp)


def reverse(stack):
    if not stack.is_empty():
        temp = stack.pop()
        reverse(stack)
        insert_(stack, temp)


stack = Stack()
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
print("Original Stack ")
print(stack)
reverse(stack)
 
print("Reversed Stack ")
print(stack)
