"""
itertools.product(*iterables, repeat=1)

Cartesian product of input iterables.
Roughly equivalent to nested for-loops in a generator expression. 
For example, product(A, B) returns the same as 
((x,y) for x in A for y in B).

To compute the product of an iterable with itself, specify 
the number of repetitions with the optional repeat keyword 
argument. For example, product(A, repeat=4) means the same as product(A, A, A, A).

This function is roughly equivalent to the following code, except 
that the actual implementation does not build up intermediate 
results in memory:

def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
"""

import itertools as it

print(list(it.product('ABCD', 'xy')))
print(list(it.product(range(2), repeat=3)))
