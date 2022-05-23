import itertools as it

print(list(it.chain('ABC', 'DEF')))
print(list(it.chain.from_iterable(['ABC', 'DEF'])))
