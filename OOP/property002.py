"""
Instead of using property(), you can use the Python decorator @property to
assign the getter, setter, and deleter.
"""


class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """Getter."""
        print('Getting name')
        return self._name

    @name.setter
    def name(self, value):
        """Setter."""
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        """Deleter."""
        print('Deleting name')
        del self._name


p = Person('Adam')
print('The name is:', p.name)
p.name = 'John'
del p.name
