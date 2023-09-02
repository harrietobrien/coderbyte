"""
45    For this challenge you will determine the length of a power set.

Have the function PowerSetCount(arr) take the array of integers stored in arr, and return the length
of the power set (the number of all possible sets) that can be generated. For example: if arr is [1, 2, 3],
then the following sets form the power set: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


def PowerSetCount(arr):
    # cascading
    res = [[]]
    for n in arr:
        res += [cur + [n] for cur in res]
    return res


print(PowerSetCount([1, 2, 3]))
