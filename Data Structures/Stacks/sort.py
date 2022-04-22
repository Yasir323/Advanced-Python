from usingLists import Stack


def sort(stack, inplace=False):
    temp_stack = Stack()
    while not stack.is_empty():
        if not stack.is_empty():
            temp = stack.pop()
        if not temp_stack.is_empty():
            if temp <= temp_stack.peek():
                temp_stack.push(temp)
            else:
                #loop
                count = 0
                while True:
                    if temp_stack.is_empty():
                        temp_stack.push(temp)
                        break
                    elif temp <= temp_stack.peek():
                        temp_stack.push(temp)
                        break
                    elif temp > temp_stack.peek():
                        stack.push(temp_stack.pop())
                        count += 1
                for i in range(count):
                    temp_stack.push(stack.pop())
                
        else:
            temp_stack.push(temp)
    if inplace:
        stack = temp_stack
        return stack
    return temp_stack


stack = Stack()
stack.push(9)
stack.push(7)
stack.push(16)
stack.push(10)
print("Original Stack ")
print(stack)
stack = sort(stack)
 
print("Sorted Stack ")
print(stack)
