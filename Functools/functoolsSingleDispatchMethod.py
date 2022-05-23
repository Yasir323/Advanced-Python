from functools import singledispatchmethod
from typing import List, Set
import math


class Product:

    def __init__(self) -> None:
        self.type_ = None
    
    @singledispatchmethod
    def prod(self, arg):
        self.type_ = type(arg)
        raise NotImplementedError(f"Cannot multiply {arg}")
    
    @prod.register
    def _(self, arg:list)->int:
        return math.prod(arg)
    
    @prod.register
    def _(self, arg:set)->int:
        return math.prod(arg)


product = Product()
print(product.prod([1,2,3,4]))
print(product.prod({7,8,9,10}))
try:
    print(product.prod('12345'))
except NotImplementedError:
    print(f'Not implemented for {product.type_}.')
