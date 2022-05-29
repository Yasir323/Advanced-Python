"""
Static methods, much like class methods, are methods that are bound to a
class rather than its object.

They do not require a class instance creation. So, they are not dependent
on the state of the object.

The difference between a static method and a class method is:

    Static method knows nothing about the class and just deals with the parameters.
    Class method works with the class since its parameter is always the class itself.

They can be called both by the class and its object.

When do you use static methods?

1. Grouping utility function to a class
Static methods have a limited use case because, like class methods or any
other methods within a class, they cannot access the properties of the
class itself.

However, when you need a utility function that doesn't access any properties
of a class but makes sense that it belongs to the class, we use static
functions.

2. Having a single implementation

Static methods are used when we don't want subclasses of a class change/override
a specific implementation of a method.
"""


class Dates:
    def __init__(self, date_):
        self.date = date_

    def get_date(self):
        return self.date

    @staticmethod
    def to_dashed_date(date_):
        return date_.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.to_dashed_date(dateFromDB)

if date.get_date() == dateWithDash:
    print("Equal")
else:
    print("Unequal")
