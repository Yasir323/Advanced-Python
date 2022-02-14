import sys

sq_lc = [i ** 2 for i in range(1_000)]
sq_gc = (i ** 2 for i in range(1_000))

size_lc = sys.getsizeof(sq_lc)
size_gc = sys.getsizeof(sq_gc)

print(f"Size of List: {size_lc}")
print(f"Size of Generator: {size_gc}")
