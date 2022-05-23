"""
itertools.permutations(iterable, r=None)

Return successive r length permutations of elements in the iterable.

If r is not specified or is None, then r defaults to the length 
of the iterable and all possible full-length permutations are 
generated.

The permutation tuples are emitted in lexicographic ordering 
according to the order of the input iterable. So, if the input 
iterable is sorted, the combination tuples will be produced in 
sorted order.

Roughly equivalent to:

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
"""

import itertools as it

print(list(it.permutations('ABCD', 2)))
print(list(it.permutations(range(3))))
