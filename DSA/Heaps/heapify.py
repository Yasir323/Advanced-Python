import math

ls = [1, 3, 5, 2, 4, 6]
ls2 = [5, 3, 2]
ls3 = [100, 99, 98, 5, 3, 60]


def heapify(array, n, i=0):
    while i < math.ceil(math.log2(n)):
        left_index = (2 * i) + 1
        right_index = (2 * i) + 2
        if left_index >= n:
            break
        elif right_index >= n:
            ind = (2 * i) + 1
        else:
            if array[right_index] < array[left_index]:
                ind = right_index
            else:
                ind = left_index

        if array[i] > array[ind]:
            array[ind], array[i] = array[i], array[ind]
        i += 1

    return array


print(heapify(ls, len(ls)))
print(heapify(ls2, len(ls2)))
print(heapify(ls3, len(ls3)))
