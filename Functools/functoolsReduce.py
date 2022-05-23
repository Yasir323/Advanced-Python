"""
reduce(function, sequence) function receives two arguments, a 
function and an iterable. It applies the argument function 
cumulatively to all elements of the iterable from the left to 
the right and then returns a single value.

To put it simply, it first applies the argument function to the 
first two elements of the iterable and the value returned by this 
first call becomes the function’s first argument and the third 
element of the iterable becomes the second argument. This 
process is repeated until the iterable is exhausted.
"""
from functools import reduce
import operator

ls = [1, 2, 3, 4]
print(reduce(operator.add, ls))  # 1 + 2 + 3 + 4 = 10
print(reduce(operator.mul, ls))  # 1 * 2 * 3 * 4 = 24
