import abc


class FlyBehaviour(metaclass=abc.ABCMeta):
    """Interface"""
    @abc.abstractmethod
    def fly(self):
        raise NotImplementedError(f"Must implement {self.fly.__name__}")


class QuackBehaviour(metaclass=abc.ABCMeta):
    """Interface"""
    @abc.abstractmethod
    def quack(self):
        raise NotImplementedError(f"Must implement {self.quack.__name__}")


class FlyWithWings(abc.ABC, FlyBehaviour):
    """Implements Interface FlyBehaviour"""

    def fly(self):
        print("I can fly.")


class FlyNoWay(abc.ABC, FlyBehaviour):
    """Implements Interface FlyBehaviour"""

    def fly(self):
        print("I cannot fly.")


class Quack(abc.ABC, QuackBehaviour):
    """Implements Interface QuackBehaviour."""

    def quack(self):
        print("Quack!")


class Squeak(abc.ABC, QuackBehaviour):
    """Implements Interface QuackBehaviour."""

    def quack(self):
        print("Squeak!")


class Duck(abc.ABC, FlyBehaviour, QuackBehaviour):
    """"Abstract class"""

    @abc.abstractmethod
    def display(self):
        raise NotImplementedError(f"Must implement {self.display.__name__}")

    @staticmethod
    def swim():
        print("Swimming")

    def perform_fly(self):
        self.fly()

    def perform_quack(self):
        self.quack()


class MallardDuck(Duck, FlyWithWings, Quack):
    """Concrete Implementation"""

    def display(self):
        print("I'm a Mallard Duck.")


if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.perform_fly()
    mallard.perform_quack()
