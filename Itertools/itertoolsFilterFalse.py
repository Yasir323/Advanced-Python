"""
itertools.filterfalse(predicate, iterable)

Make an iterator that filters elements from iterable returning
only those for which the predicate is False. If predicate is 
None, return the items that are false. Roughly equivalent to:

def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x
"""

import itertools as it

print(list(it.filterfalse(lambda x: x % 2, range(1, 10))))
