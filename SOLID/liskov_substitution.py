"""if class A is a subtype of class B, we should be able to replace B with A without disrupting the behavior of our
program.

Let's jump straight to the code to help us understand this concept:
"""

import abc


class Car(metaclass=abc.ABCMeta):
    """Interface"""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'turn_on_engine') and
                callable(subclass.turn_on_engine) and
                hasattr(subclass, 'accelerate') and
                callable(subclass.accelerate) or
                NotImplemented)


"""
Above, we define a simple Car interface with a couple of methods that all cars should be able to fulfill: turning 
on the engine and accelerating forward. 

Let's implement our interface and provide some code for the methods:
"""


class MotorCar:

    __engine: str = 'Off'
    speed: int = 0

    def turn_on_engine(self):
        self.__engine = 'On'

    def accelerate(self):
        self.speed += 5


"""
As our code describes, we have an engine that we can turn on, and we can increase the power.
But wait — we are now living in the era of electric cars:
"""


class ElectricCar:

    speed: int = 0

    def turn_on_engine(self):
        raise AssertionError("I don't have an engine.")

    def accelerate(self):
        self.speed += 10


"""
By throwing a car without an engine into the mix, we are inherently changing the behavior of our program. This is 
a blatant violation of Liskov substitution and is a bit harder to fix than our previous two principles. 

One possible solution would be to rework our model into interfaces that take into account the engine-less state of 
our Car.
"""