"""
What is a class method?

A class method is a method that is bound to a class rather than its object.
It doesn't require creation of a class instance, much like staticmethod.

The difference between a static method and a class method is:

    Static method knows nothing about the class and just deals with the parameters
    Class method works with the class since its parameter is always the class itself.

The class method can be called both by the class and its object.

When do you use the class method?
1. Factory methods

Factory methods are those methods that return a class object (like
constructor) for different use cases.

It is similar to function overloading in C++. Since, Python doesn't
have anything as such, class methods and static methods are used.

2. Correct instance creation in inheritance

Whenever you derive a class from implementing a factory method as a
class method, it ensures correct instance creation of the derived class.

You can create a static method for the above example but the object it
creates, will always be hard coded as Base class.

But, when you use a class method, it creates the correct instance of the
derived class.
"""

from datetime import date


# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person = Person('Adam', 19)
person.display()

person1 = Person.from_birth_year('John',  1985)
person1.display()
