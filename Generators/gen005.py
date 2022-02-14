# Implementing for loop using a while loop

letters = ['a', 'b', 'f', 'e']
it = iter(letters)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)