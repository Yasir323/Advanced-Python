"""
Partial functions are derived functions that have some pre-assigned 
input parameters. For example, if a function takes in two 
parameters say “a” and “b”, a partial function can be created 
from it that has “a” as a prefilled argument and it can then 
be called with “b” as the only parameter. Functool’s partial() 
is used to create partial functions/objects and this is a 
useful feature as it allows for the:
    
    Replication of existing functions with some arguments already passed in.
    
    Creation of newer version of the existing function in a well-documented manner.

Partials are incredibly useful. For example, in a pipe-lined 
sequence of function calls in which the returned value from 
one function is the argument passed to the next.
"""

from functools import partial


def power(a, b):
    return a ** b


power_of_two = partial(power, a=2)
power_of_ten = partial(power, a=10)

print(power_of_two(b=10))
print(power_of_ten(b=3))
