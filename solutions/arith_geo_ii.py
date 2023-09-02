"""
For this challenge you will determine if numbers within an array follow a sequence.

Have the function ArithGeoII(arr) take the array of numbers stored in arr and return the string
"Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a
geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence
is one where the difference between each of the numbers is consistent, whereas in a geometric sequence,
each term after the first is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8]
and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be
entered, and no array will contain all the same elements.
"""


def is_arithmetic(l):
    return all((i - j) == (j - k) for i, j, k in zip(l[:-2], l[1:-1], l[2:]))


def is_geometric(li):
    if len(li) <= 1:
        return True
    # Calculate ratio
    ratio = li[1] / float(li[0])
    # Check the ratio of the remaining
    for i in range(1, len(li)):
        if li[i] / float(li[i - 1]) != ratio:
            return False
    return True


def ArithGeoII(arr: list):
    if is_arithmetic(arr):
        return "Arithmetic"
    elif is_geometric(arr):
        return "Geometric"
    else:
        return -1

print(ArithGeoII([2, 6, 18, 54]))