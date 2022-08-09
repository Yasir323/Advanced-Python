import math


def meta_binary_search(arr, size, target):
    # Find the number of bits required
    num_bits = math.ceil(math.log2(size))
    # Initial Bit
    bits = ['0'] * num_bits
    counter = 0
    while counter < len(bits):
        index = int(''.join(bits), 2)
        if index >= size:
            bits[counter] = '0'
            counter += 1
            bits[counter] = '1'
            continue
        if arr[index] == target:
            return index
        elif arr[index] > target:
            bits[counter] = '0'
            counter += 1
            bits[counter] = '1'
        else:
            if bits[counter] == '1':
                counter += 1
                bits[counter] = '1'
            else:
                bits[counter] = '1'
    return -1


if __name__ == '__main__':
    array = [1, 3, 4, 5, 7, 89, 91]
    print(meta_binary_search(array, len(array), 89))
