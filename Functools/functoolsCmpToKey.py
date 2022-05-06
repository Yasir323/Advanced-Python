"""
cmp_to_key()

It transforms an old-style comparison function to a key 
function. A comparison function is any callable that accepts 
two arguments, compares them, and returns a negative number 
for less-than, zero for equality, or a positive number for 
greater-than. Whereas a key function is a callable that 
accepts one argument and returns another value to be used as 
the sort key, an example is the operator.itemgetter() key 
function. Key functions are used in tools such as sorted(), 
min(), max() and itertools.groupby().

cmp_to_key() is majorly used as a transition tool for programs 
written in Python 2 that support comparison functions.
"""

from functools import cmp_to_key


#first we define a comparison function
def comparison(a,b):
    if a[0] < b[0]:
        return -1
    elif a[0] == b[0]:
        return 0
    else:
        return 1


name = ['Towards', 'Data', 'Science']
sorted_names = sorted(name, key=cmp_to_key(comparison))
print(f'Sorted Names = {sorted_names}')
