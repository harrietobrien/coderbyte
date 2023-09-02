"""
15    For this challenge you will determine if numbers within an array follow an arithmetic or geometric sequence.

Take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic
pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern
return -1. An arithmetic sequence is one where the difference between each of the numbers is consistent,
whereas in a geometric sequence, each term after the first is multiplied by some constant or common ratio.
Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as
parameters, 0 will not be entered, and no array will contain all the same elements.
"""


def isArithmetic(numList):
    return all((i - j) == (j - k) for i, j, k in
               zip(numList[:-2], numList[1:-1], numList[2:]))


def isGeometric(numList: list):
    if len(numList) <= 1:
        return True
    ratio = numList[1] / float(numList[0])
    for i in range(1, len(numList)):
        if numList[i] / float(numList[i - 1]) != ratio:
            return False
    return True


def ArithGeo(numList: list):
    if isArithmetic(numList):
        return "Arithmetic"
    elif isGeometric(numList):
        return "Geometric"
    else:
        return -1


a = [2, 4, 6, 8, 10, 12, 14]
g = [2, 6, 18, 54]
print(ArithGeo(a))
print(ArithGeo(g))
