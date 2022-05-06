import itertools as it

print(list(it.compress('ABCDEF', [1, 0, 1, 0, 1, 1])))
