from usingLists import Stack

stack = Stack()


def reverse_string(string_: str) -> str:
    for char in string_:
        stack.push(char)
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string


print(reverse_string('Yasir'))
