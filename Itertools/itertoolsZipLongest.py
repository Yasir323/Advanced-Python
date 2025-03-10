"""
itertools.zip_longest(*iterables, fillvalue=None)

Make an iterator that aggregates elements from each of the 
iterables. If the iterables are of uneven length, missing 
values are filled-in with fillvalue. Iteration continues 
until the longest iterable is exhausted. Roughly equivalent 
to:


def zip_longest(*args, fillvalue=None):
    # zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)


If one of the iterables is potentially infinite, then the 
zip_longest() function should be wrapped with something that 
limits the number of calls (for example islice() or takewhile()). 
If not specified, fillvalue defaults to None.
"""

import itertools as it

print(list(it.zip_longest('ABCD', 'xy', fillvalue='-')))
