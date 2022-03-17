"""
Given a sorted array of integers and a target integer. Find the index of the
first and last occurence of the target in the array. If target cannot be found,
return [-1, -1]
"""


def first_and_last(arr, target):
    """O(n)"""
    initial = -1
    final = -1
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i + 1 < len(arr) and arr[i + 1] == target:
                i += 1
            return [start, i]
    return [-1, -1]


print(first_and_last([1, 2, 3, 4, 5, 5, 5, 6, 7], 5))
