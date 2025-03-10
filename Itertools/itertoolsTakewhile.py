"""
itertools.takewhile(predicate, iterable)
Make an iterator that returns elements from the iterable as 
long as the predicate is true. Roughly equivalent to:

def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break
"""

import itertools as it

print(list(it.takewhile(lambda x: x<5, [1,4,6,4,1])))
