from usingLists import Stack, EmptyStackError


def check(expr: str) -> bool:
    stack = Stack()
    for char in expr:
        if char in '({[':
            stack.push(char)
        elif char == ')':
            try:
                if stack.pop() != '(':
                    return False
            except EmptyStackError:
                return False
        elif char == '}':
            try:
                if stack.pop() != '{':
                    return False
            except EmptyStackError:
                return False
        elif char == ']':
            try:
                if stack.pop() != '[':
                    return False
            except EmptyStackError:
                return False
        else:
            continue
    if not stack.is_empty():
        return False
    return True


print(check("{()}[]"))
