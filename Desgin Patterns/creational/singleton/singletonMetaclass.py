"""
In the case of the singleton implementation using __new__(),
if a class inherits from a second base class that also overrides
__new__(), there is a possibility of conflicts or unintended behavior.
The second base class might provide its own implementation of
__new__(), which could override or interfere with the singleton
implementation.

To avoid such conflicts, it's generally recommended to use a
metaclass-based approach for implementing a singleton rather than
relying solely on __new__(). Metaclasses provide more control over
the creation and behavior of classes. By defining a metaclass, you
can enforce the singleton pattern at the class level, ensuring that
only one instance is created regardless of multiple inheritance.
"""


class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class Logger(metaclass=Singleton):
    pass
