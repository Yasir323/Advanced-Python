def double_inputs():
    while True:
        x = yield
        yield x * 2


gen = double_inputs()
print(next(gen))       # run up to the first yield: output = None
print(gen.send(10))    # goes into 'x' variable

print(next(gen))       # run up to the next yield: output = None
print(gen.send(6))     # goes into 'x' again

print(next(gen))       # run up to the next yield: output = None
print(gen.send(94.3))  # goes into 'x' again
