"""
update_wrapper()

It updates the metadata of a wrapper function to look like the 
wrapped function. For example, in the case of partial functions, 
update_wrapper(partial, parent) will update the 
documentation(__doc__) and name(__name__) of the partial 
function to match that of the parent function.
"""

from functools import update_wrapper, partial


#parent function
def power(a, b): 
    ''' a to the power b'''
    return a**b 


# partial function 
square = partial(power, b=2) 
square.__doc__='''a to the power 2'''
square.__name__ = 'square'

# Before wrapper update
print('Documentation of square :', square.__doc__) 
print('Name of square :', square.__name__, end='\n\n')

update_wrapper(square, power)

# After wrapper update 
print('Documentation of square :', square.__doc__) 
print('Name of square :', square.__name__)
