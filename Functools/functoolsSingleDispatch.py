"""
SingleDispatch

It is a function decorator. It transforms a function into a 
generic function so that it can have different behaviors 
depending upon the type of its first argument. It is used for 
function overloading, the overloaded implementations are 
registered using the register() attribute.
"""

from functools import singledispatch


@singledispatch
def divide(a:int, b:int) -> float:
    return a / b


@divide.register(str)
def _(a:str, b:str) -> str:
    return f"{a}/{b}"


print(divide(8, 2))
print(divide('10', '3'))
