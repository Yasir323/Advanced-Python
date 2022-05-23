"""
itertools.accumulate(iterable[, func, *, initial=None])

Make an iterator that returns accumulated sums, or accumulated
results of other binary functions (specified via the optional 
func argument).

If func is supplied, it should be a function of two arguments.
"""

import operator
import itertools as it

# Cumsum
print(list(it.accumulate(range(10))))
print(list(it.accumulate(range(10), func=operator.add)))  # Same as above

# Running product
data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
print(list(it.accumulate(data, func=operator.mul)))

# running maximum
print(list(it.accumulate(data, func=max)))

cashflows = [1000, -90, -90, -90, -90]
print(list(it.accumulate(cashflows, lambda acc, curr: acc*1.05 + curr)))
