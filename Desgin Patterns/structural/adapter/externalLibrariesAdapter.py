"""
Suppose you are working with an external library that has a different interface
from what your code expects. You can create an adapter to bridge the gap between
the two interfaces.
"""


# Existing interface
class TargetInterface:
    def request(self):
        pass


# External library with incompatible interface
class Adaptee:
    def specific_request(self):
        pass


# Adapter
class Adapter(TargetInterface):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()


# Usage
adaptee = Adaptee()
adapter = Adapter(adaptee)
adapter.request()
