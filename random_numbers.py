from random import randint as r, seed
import random
from statistics import mean

ls = []
iterations = [60, 100, 200, 300, 500] 
missed = {}
for _ in range(100):
    seed(r(1, 10000))
    for i in iterations:
        for _ in range(i):
            ls.append(r(1, 10000) % 60)
        ls = list(set(ls))
        if i in missed:
            missed[i].append(60 - len(ls))
        else:
            missed[i] = [60 - len(ls)]
        ls.clear()
for i in missed:
    print(f'Mean for {i} iterations is : {mean(missed[i])}')
# print(missed)

# print(f'Values missed: {60 - len(ls)}')
