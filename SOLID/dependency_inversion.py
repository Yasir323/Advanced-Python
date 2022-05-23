"""
The principle of dependency inversion refers to the decoupling of software modules. This way, instead of
high-level modules depending on low-level modules, both will depend on abstractions.

To demonstrate this, let's go old-school and bring to life a Windows 98 computer with code:
"""

import abc


class GamingMonitor:

    width: int = 1920
    height: int = 1080
    resolution: str = f'{width} x {height}'
    technology: str = 'LED'
    panel_type: str = 'IPS'

    @staticmethod
    def display():
        print("Displaying output...")


class GamingKeyboard:

    mechanical: bool = True
    backlit: bool = True
    rbg: bool = True

    @staticmethod
    def type_():
        print("Typing...")


class Windows7Machine:

    keyboard: GamingKeyboard
    monitor: GamingMonitor

    def __init__(self):
        keyboard = GamingKeyboard()
        monitor = GamingMonitor()


"""
This code will work, and we'll be able to use the StandardKeyboard and Monitor freely within our Windows98Computer 
class. 

Problem solved? Not quite. By declaring the StandardKeyboard and Monitor with the new keyword, we've tightly coupled 
these three classes together.

Not only does this make our Windows98Computer hard to test, but we've also lost the ability to switch out our 
StandardKeyboard class with a different one should the need arise. And we're stuck with our Monitor class too. 

Let's decouple our machine from the StandardKeyboard by adding a more general Keyboard interface and using this in 
our class:
"""


class Keyboard(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'mechanical') and
                hasattr(subclass, 'rgb') and
                hasattr(subclass, 'backlit') and
                hasattr(subclass, 'type_') and
                callable(subclass.type_) or
                NotImplemented)


class Monitor(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'width') and
                hasattr(subclass, 'height') and
                hasattr(subclass, 'technology') and
                hasattr(subclass, 'panel_type') and
                hasattr(subclass, 'display') and
                callable(subclass.display) or
                NotImplemented)


class Windows8Machine:

    keyboard: Keyboard
    monitor: Monitor

    def __init__(self, keyboard, monitor):
        self.keyboard = keyboard
        self.monitor = monitor


"""
Here, we're using the dependency injection pattern to facilitate adding the Keyboard dependency into the 
Windows98Machine class. Now our classes are decoupled and communicate through the Keyboard abstraction. If we want, 
we can easily switch out the type of keyboard in our machine with a different implementation of the interface. We can 
follow the same principle for the Monitor class.
"""
