"""
cached_property()

As the name suggests the cached_property() is a decorator that 
transforms a class method into a property whose value is 
calculated only once and then cached as a normal attribute for 
the life of the instance. It is similar to @property except 
the for its caching functionality. It is useful for computationally 
expensive properties of instances that are otherwise 
effectively permanent.
"""

from functools import cached_property
import statistics


class DataSet:
    def __init__(self, sequence_of_numbers):
        self._data = sequence_of_numbers

    @cached_property
    def stdev(self):
        return statistics.stdev(self._data)

    @cached_property
    def variance(self):
        return statistics.variance(self._data)


obs = DataSet([50,60,70,80,90,100])
print(obs.stdev)
print(obs.variance)
