"""
EVALUATE POSTFIX EXPRESSION

Following is an algorithm for evaluation postfix expressions.
1) Create a stack to store operands (or values).
2) Scan the given expression and do the following for every scanned element.
    a) If the element is a number, push it into the stack
    b) If the element is an operator, pop operands for the operator from the stack.
    Evaluate the operator and push the result back to the stack
3) When the expression is ended, the number in the stack is the final answer
"""
from usingLists import Stack


def evaluate(expr: str):
    stack = Stack()
    for char in expr:
        if char.isdigit():
            stack.push(char)
        else:
            second_operand = str(stack.pop())
            operator = char
            first_operand = str(stack.pop())
            expression = first_operand + operator + second_operand
            result = eval(expression)
            stack.push(result)
    return stack.pop()


print(evaluate("231*+9-"))

"""
There are the following limitations of the above implementation. 
1) It supports only 4 binary operators ‘+’, ‘*’, ‘-‘ and ‘/’. It can be
extended for more operators by adding more switch cases. 
2) The allowed operands are only single-digit operands. The program can 
be extended for multiple digits by adding a separator-like space between 
all elements (operators and operands) of the given expression.
"""


def evaluate_better(expr: str):
    expr = expr.split(' ')
    stack = Stack()
    for char in expr:
        if char.isdigit():
            stack.push(char)
        else:
            second_operand = str(stack.pop())
            operator = char
            first_operand = str(stack.pop())
            expression = first_operand + operator + second_operand
            result = eval(expression)
            stack.push(result)
    return stack.pop()


print(evaluate_better("100 200 + 2 / 5 * 7 +"))
