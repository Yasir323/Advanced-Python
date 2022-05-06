"""
It is a convenience function for invoking update_wrapper() to 
the decorated function. It is equivalent to running 
partial(update_wrapper, wrapped=wrapped, assigned=assigned, 
updated=updated).
"""

from functools import wraps


def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Calling the decorated function.")
        return f(*args, **kwargs)
    return wrapper


@my_decorator
def example():
    """Temp"""
    print("Inside the decorated funtion.")


example()
print(example.__name__)
print(example.__doc__)
