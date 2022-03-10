"""
Infix to postfix conversion

Scan through an expression, getting one token at a time.

1 Fix a priority level for each operator. For example, from high to low:

    3.    - (unary negation)
    2.    * /
    1.    + - (subtraction)

Thus, high priority corresponds to high number in the table.

2 If the token is an operand, do not stack it. Pass it to the output.

3 If token is an operator or parenthesis, do the following:

   -- Pop the stack until you find a symbol of lower priority number than the current one. An incoming left parenthesis
   will be considered to have higher priority than any other symbol. A left parenthesis on the stack will not be removed
   unless an incoming right parenthesis is found.
The popped stack elements will be written to output.

   --Stack the current symbol.

   -- If a right parenthesis is the current symbol, pop the stack down to (and including) the first left parenthesis.
   Write all the symbols except the left parenthesis to the output (i.e. write the operators to the output).

   -- After the last token is read, pop the remainder of the stack and write any symbol (except left parenthesis) to
   output.
"""
from usingLists import Stack

stack = Stack()
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 10}


def convert(expr, stack):
    output = ''
    for char in expr:
        # Operand
        if char.isalpha():
            output += char

        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.peek() != '(':
                output += stack.pop()
            stack.pop()  # Remove '('
        else:
            if not stack.is_empty():
                while priority[stack.peek()] >= priority[char] and stack.peek() != '(':
                    # char_priority = priority[char]
                    # stacked_priority = priority[stack.peek()]
                    output += stack.pop()
                    if stack.is_empty():
                        break
            stack.push(char)

    while not stack.is_empty():
        operator = stack.pop()
        if operator != '(':
            output += operator
    return output


print(convert("A*(B+C)*D", stack))
print(convert("a+b*(c^d-e)^(f+g*h)-i", stack))
