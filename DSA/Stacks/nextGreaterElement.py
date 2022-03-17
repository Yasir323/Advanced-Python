from usingLists import Stack


def next_greater_elements(array):
    stack = Stack()
    stack.push(array.pop(0))
    for element in array:
        while (not stack.is_empty()) and (element > stack.peek()):
            print(f"{stack.pop()} -> {element}")
        stack.push(element)
    while not stack.is_empty():
        print(f"{stack.pop()} -> -1")


next_greater_elements([13, 7, 6, 12])
next_greater_elements([11, 13, 21, 3])
