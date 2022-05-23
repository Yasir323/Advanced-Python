"""
The Italians figured out their pizza taxonomy centuries ago, 
and so these delicious types of pizzas all have their own 
names. We’d do well to take advantage of that and give the 
users of our Pizza class a better interface for creating the 
pizza objects they crave.

A nice and clean way to do that is by using class methods as 
factory functions for the different kinds of pizzas we can 
create:
"""


class Pizza:
    def __init__(self, radius, ingredients):
        self.ingredients = ingredients
        self.radius = radius

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    @classmethod
    def margherita(cls, radius):
        return cls(radius, ['mozzarella', 'tomatoes'])
    
    @classmethod
    def prosciutto(cls, radius):
        return cls(radius, ['mozzarella', 'tomatoes', 'ham'])

    def area(self):
        return self.circle_area(self.radius)
    
    @staticmethod
    def circle_area(radius):
        return radius ** 2 * 3.14


print(Pizza.margherita(4))
print(Pizza.prosciutto(4))

p = Pizza(4, ['mozzerrella', 'tomatoes'])
print(p)
print(p.area())
print(Pizza.circle_area(4))
