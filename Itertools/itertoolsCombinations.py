"""
itertools.combinations(iterable, r)

Return r length subsequences of elements from the input iterable.

The combination tuples are emitted in lexicographic ordering 
according to the order of the input iterable. So, if the input 
iterable is sorted, the combination tuples will be produced in 
sorted order.

Elements are treated as unique based on their position, not on 
their value. So if the input elements are unique, there will 
be no repeat values in each combination.

Roughly equivalent to:

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

The code for combinations() can be also expressed as a 
subsequence of permutations() after filtering entries where 
the elements are not in sorted order (according to their 
position in the input pool):

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)
"""

import itertools as it

print(list(it.combinations('ABCD', 2)))
print(list(it.combinations([1,2,3,4], 2)))
print(list(it.combinations(range(4), 3)))
