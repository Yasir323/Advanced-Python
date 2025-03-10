"""
itertools.starmap(function, iterable)
Make an iterator that computes the function using arguments 
obtained from the iterable. Used instead of map() when argument 
parameters are already grouped in tuples from a single 
iterable (the data has been “pre-zipped”). The difference 
between map() and starmap() parallels the distinction between 
function(a,b) and function(*c). Roughly equivalent to:

def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)
"""

import itertools as it

print(list(it.starmap(pow, [(2,5), (3,2), (10,3)])))
print(list(it.starmap(sum, [[range(5)], [range(5, 10)], [range(10, 15)]])))
