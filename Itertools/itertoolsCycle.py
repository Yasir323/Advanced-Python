import itertools as it

for count, i in enumerate(it.cycle('abcd')):
    print(i, end='')
    if count == 20:
        print()
        break

for count, i in enumerate(it.cycle(range(10))):
    print(i, end='')
    if count == 20:
        break
