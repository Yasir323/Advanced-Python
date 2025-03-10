"""
itertools.combinations_with_replacement(iterable, r)¶

Return r length subsequences of elements from the input 
iterable allowing individual elements to be repeated more 
than once.

The combination tuples are emitted in lexicographic ordering 
according to the order of the input iterable. So, if the input 
iterable is sorted, the combination tuples will be produced in 
sorted order.

Elements are treated as unique based on their position, not on 
their value. So if the input elements are unique, the generated 
combinations will also be unique.

Roughly equivalent to:

def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

The code for combinations_with_replacement() can be also 
expressed as a subsequence of product() after filtering 
entries where the elements are not in sorted order (according 
to their position in the input pool):

def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)
"""

import itertools as it

print(list(it.combinations_with_replacement('ABC', 2)))
