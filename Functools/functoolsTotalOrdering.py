"""
total_ordering()

Given a class defining one or more rich comparison ordering 
methods i.e., __lt__(), __le__(), __gt__(), __ge__() or 
__eq__() (corresponding to <, <=, >, >=, and ==). You can 
define a few of the comparison methods, and @total_ordering 
will automatically supply the rest as per the given definitions. 
It is important that the class should supply an __eq__() method.

For example, if you want to create a class that compares 
different numbers. You would probably need to implement all of 
the rich comparison methods. However, this might be quite 
tedious and redundant, to solve this you can only implement 
the __eq__ and the __gt__ method and use @total_ordering to 
automatically fill up the rest.
"""

from functools import total_ordering


@total_ordering
class CompareNums: 
    def __init__(self, value): 
        self.value = value 
    def __eq__(self, new_val): 
        return self.value == new_val.value 
  
    def __gt__(self, new_val): 
        return self.value > new_val.value


print('5 > 3 :', CompareNums(5)>CompareNums(3)) 
print('1 < 6:', CompareNums(1)<CompareNums(6))

print('2 <= 7 :', CompareNums(2)<= CompareNums(7)) 
print('9 >= 10 :', CompareNums(9)>= CompareNums(10)) 

print('5 == 5 :', CompareNums(5)== CompareNums(5)) 
