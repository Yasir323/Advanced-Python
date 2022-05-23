"""
itertools.pairwise(iterable)

itertools.pairwise was introduced in Python v3.10

Return successive overlapping pairs taken from the input iterable.

The number of 2-tuples in the output iterator will be one fewer 
than the number of inputs. It will be empty if the input iterable 
has fewer than two values.

Roughly equivalent to:

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
"""

import itertools as it

print(list(it.pairwise('ABCDEF')))  # AB BC CD DE EF
