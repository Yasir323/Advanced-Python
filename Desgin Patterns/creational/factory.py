class Dog:

    """A simple dog class"""

    def __init__(self, name):
        self._name = name

    @staticmethod
    def speak():
        return "Woof!"


class Cat:

    """A simple cat class"""

    def __init__(self, name):
        self._name = name

    @staticmethod
    def speak():
        return "Meow!"


def get_pet(pet="dog"):
    """The Factory Method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Kiki"))
    return pets[pet]


if __name__ == '__main__':
    d = get_pet("dog")
    print(d.speak())
    c = get_pet("cat")
    print(c.speak())
