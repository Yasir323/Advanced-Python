"""
(class) dropwhile(__predicate: (int) -> object, __iterable: Iterable[int], /)

Drop items from the iterable while predicate(item) is true.
Afterwards, return every element until the iterable is 
exhausted.
"""

import itertools as it

print(list(it.dropwhile(lambda x: x < 5, [1,4,6,4,1])))
