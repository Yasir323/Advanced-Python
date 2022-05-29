"""
The property() construct returns the property attribute.

The syntax of property() is:

property(fget=None, fset=None, fdel=None, doc=None)

property() Parameters

The property() takes four optional parameters:

    fget (optional) - Function for getting the attribute value. Defaults to None.
    fset (optional) - Function for setting the attribute value. Defaults to None.
    fdel (optional) - Function for deleting the attribute value. Defaults to None.
    doc (optional) - A string that contains the documentation (docstring)
                    for the attribute. Defaults to None.

Return value from property()

property() returns the property attribute from the given getter, setter, and deleter.

    If no arguments are given, property() returns a base property attribute
        that doesn't contain any getter, setter or deleter.
    If doc isn't provided, property() takes the docstring of the getter
        function.
"""


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('Getting name')
        return self._name

    def set_name(self, value):
        print('Setting name to ' + value)
        self._name = value

    def del_name(self):
        print('Deleting name')
        del self._name

    # Set property to use get_name, set_name
    # and del_name methods
    name = property(get_name, set_name, del_name, 'Name property')


p = Person('Adam')
print(p.name)
p.name = 'John'
del p.name
