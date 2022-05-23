"""
SLOTS

Slots can be used to make classes faster and use less memory.
Essentially, slots are defined using .__slots__ to list the 
variables on a class. Variables or attributes not present in 
.__slots__ may not be defined. Furthermore, a slots class may 
not have default values.
"""

from dataclasses import dataclass
import sys
from timeit import timeit


@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float


@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float


simple = SimplePosition('London', -0.1, 51.5)
slot = SlotPosition('Madrid', -3.7, 40.4)
print(sys.getsizeof(simple))
print(sys.getsizeof(slot))
print(timeit('slot.name', setup="slot=SlotPosition('Oslo', 10.8, 59.9)", globals=globals()))
print(timeit('simple.name', setup="simple=SimplePosition('Oslo', 10.8, 59.9)", globals=globals()))
