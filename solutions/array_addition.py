"""
For this challenge you will determine if numbers in an array can add up to a certain number in the array.
['algorithm', 'array', 'searching', 'dynamic programming', 'recursion']
"""


def ArrayAddition(l: list):
    import itertools
    target = 23
    for i in range(len(l)):
        comb = itertools.combinations(l, i + 1)
        if any(sum(c) == target for c in comb):
            return True


l1 = [4, 6, 23, 10, 1, 3]
print(ArrayAddition(l1))
