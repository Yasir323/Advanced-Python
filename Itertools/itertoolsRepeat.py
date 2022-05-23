import itertools as it

for i in it.repeat(10, 3):
    print(i)

for count, i in enumerate(it.repeat(100)):
    print(i)
    if count == 20:
        break

