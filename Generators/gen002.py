# Generating infinite sequence
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_sequence()
for _ in range(10):
    print(next(gen))
