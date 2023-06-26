"""
In some cases, you may have a set of predefined objects
that you want to clone and use throughout your application.
You can use a prototype registry to store and manage these
prototypes.
"""
import copy


class PrototypeRegistry:
    def __init__(self):
        self._prototypes = {}

    def register(self, name, prototype):
        self._prototypes[name] = prototype

    def clone(self, name, **kwargs):
        prototype = self._prototypes.get(name)
        if prototype:
            cloned_obj = copy.deepcopy(prototype)
            cloned_obj.__dict__.update(kwargs)
            return cloned_obj
        raise ValueError(f"No prototype found with name '{name}'")


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


# Usage
registry = PrototypeRegistry()

# Register prototypes
obj1 = Prototype()
registry.register('Object1', obj1)

obj2 = Prototype()
registry.register('Object2', obj2)

# Clone prototypes
cloned_obj1 = registry.clone('Object1', param1='value1')
cloned_obj2 = registry.clone('Object2', param2='value2')
