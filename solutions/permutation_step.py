"""
For this challenge you will determine the next greatest number.

Have the function PermutationStep(num) take the num parameter being passed and return the next
number greater than num using the same digits. For example: if num is 123 return 132, if it's
12453 return 12534. If a number has no greater permutations, return -1 (ie. 999).
"""


def getDigits(num):
    digits = list()
    while num > 0:
        digit = num % 10
        digits.append(digit)
        num //= 10
    return digits


def toDecimal(numList):
    new = 0
    newList = numList[::-1]
    n = len(newList)
    for i in range(n):
        new += newList[i] * 10 ** (n - i - 1)
    return new


def PermutationStep(num):
    import itertools
    digits = getDigits(num)
    perms = itertools.permutations(digits, len(digits))
    nums = list()
    for p in perms:
        decimal = toDecimal(p)
        if toDecimal(p) > num:
            nums.append(decimal)
    return sorted(nums)[0]


print(getDigits(12453))
print(PermutationStep(12453))
