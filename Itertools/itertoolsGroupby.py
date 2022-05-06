"""
itertools.groupby(iterable, key=None)

Make an iterator that returns consecutive keys and groups from 
the iterable. The key is a function computing a key value for 
each element. If not specified or is None, key defaults to an 
identity function and returns the element unchanged. Generally, 
the iterable needs to already be sorted on the same key 
function.
"""

import itertools as it

data = 'AAAABBBCCDAABBB'

for k, v in it.groupby(data):
    print(k, len(list(v)))
print()
data = list(data)
data.sort()
for k, v in it.groupby(data):
    print(k, len(list(v)))
