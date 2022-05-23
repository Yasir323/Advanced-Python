"""
islice(iterable, stop) --> islice object islice(iterable, start, stop[, step]) --> islice object

Return an iterator whose next() method returns selected values 
from an iterable. If start is specified, will skip all preceding 
elements; otherwise, start defaults to zero. Step defaults to 
one. If specified as another value, step determines how many 
values are skipped between successive calls. Works like a slice() 
on a list but returns an iterator.
"""

import itertools as it

print(list(it.islice('ABCDEFG', 2)))  # --> A B
print(list(it.islice('ABCDEFG', 2, 4)))  #--> C D
print(list(it.islice('ABCDEFG', 2, None)))  # --> C D E F G
print(list(it.islice('ABCDEFG', 0, None, 2)))  # --> A C E G
