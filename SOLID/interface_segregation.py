"""
The I  in SOLID stands for interface segregation, and it simply means that larger interfaces should be split into
smaller ones. By doing so, we can ensure that implementing classes only need to be concerned about the methods that
are of interest to them.

For this example, we're going to try our hands as zookeepers. And more specifically, we'll be working in the bear
enclosure.

Let's start with an interface that outlines our roles as a bear keeper:
"""

import abc


class BearKeeper(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'wash_the_bear') and
                callable(subclass.wash_the_bear) and
                hasattr(subclass, 'feed_the_bear') and
                callable(subclass.feed_the_bear) and
                hasattr(subclass, 'pet_the_bear') and
                callable(subclass.pet_the_bear) or
                NotImplemented)


"""
As avid zookeepers, we're more than happy to wash and feed our beloved bears. But we're all too aware of the 
dangers of petting them. Unfortunately, our interface is rather large, and we have no choice but to implement the 
code to pet the bear. 

Let's fix this by splitting our large interface into three separate ones:
"""


class BearCleaner(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'wash_the_bear') and
                callable(subclass.wash_the_bear))


class BearFeeder(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'feed_the_bear') and
                callable(subclass.feed_the_bear))


class BearPetter(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'pet_the_bear') and
                callable(subclass.pet_the_bear))


"""
Now, thanks to interface segregation, we're free to implement only the methods that matter to us:
"""


class BearCarer:

    def wash_the_bear(self):
        print("Bear is clean now.")

    def feed_the_bear(self):
        print("Bear is full now.")


"""
And finally, we can leave the dangerous stuff to the reckless people:
"""


class CrazyPerson:

    def pet_the_bear(self):
        print("Not going well.")


print(issubclass(BearCarer, BearKeeper))
print(issubclass(CrazyPerson, BearKeeper))
print(issubclass(BearCarer, (BearFeeder, BearCleaner)))
print(issubclass(CrazyPerson, BearPetter))
