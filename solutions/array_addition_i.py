"""
16    For this challenge you will determine if numbers in an array can add up to a certain number in the array.

Take the array of numbers stored in arr and return the string true if any combination of numbers in the
array can be added up to equal the largest number in the array, otherwise return the string false. For
example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23.
The array will not be empty, will not contain all the same elements, and may contain negative numbers.
"""


def ArrayAddition(nums: list):
    import itertools
    target = 23
    for i in range(len(nums)):
        comb = itertools.combinations(nums, i + 1)
        if any(sum(c) == target for c in comb):
            return True


l1 = [4, 6, 23, 10, 1, 3]
print(ArrayAddition(l1))