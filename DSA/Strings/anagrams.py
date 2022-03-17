"""
Check whether 2 strings are valid anagrams
"""
from collections import Counter


def are_anagrams(s1, s2):
    """
    Using Counter O(n)
    """
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s1)


def are_anagrams2(s1, s2):
    """
    Using sorting, since lexicographical order of anagrams are same O(nLog(n))
    """
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s1)


def are_anagrams3(s1, s2):
    """
    Using Hashmap/Dictionary O(n)
    """
    if len(s1) != len(s2):
        return False

    s1 = {}
    s2 = {}
    for char in s1:
        if char not in s1:
            s1[char] = 1
        else:
            s1[char] += 1
    for char in s2:
        if char not in s2:
            s2[char] = 1
        else:
            s2[char] += 1
    return s1 == s2


print(are_anagrams('nameles', 'salesman'))
print(are_anagrams2('nameles', 'salesman'))
print(are_anagrams3('nameles', 'salesman'))
print(are_anagrams('nameless', 'salesman'))
print(are_anagrams2('nameless', 'salesman'))
print(are_anagrams3('nameless', 'salesman'))
