"""
38    For this challenge you will add elements from two arrays in a particular order.

Have the function ArrayMatching(strArr) read the array of strings stored in strArr which will contain only
two elements, both of which will represent an array of positive integers. For example: if strArr is
["[1, 2, 5, 6]", "[5, 2, 8, 11]"], then both elements in the input represent two integer arrays, and your
goal for this challenge is to add the elements in corresponding locations from both arrays. For the example
input, your program should do the following additions: [(1 + 5), (2 + 2), (5 + 8), (6 + 11)] which then equals
[6, 4, 13, 17]. Your program should finally return this resulting array in a string format with each element
separated by a hyphen: 6-4-13-17. If the two arrays do not have the same amount of elements, then simply
append the remaining elements onto the new array(example shown below).Both arrays will be in the format :
[e1, e2, e3, ...] where at least one element will exist in each array.
"""


def ArrayMatching(strArr: list[str]):
    import re
    rm_brackets = list(map(lambda s: re.sub(r"[([{})\]]", "", s), strArr))
    split_by_comma = list(map(lambda s: s.split(","), rm_brackets))
    l1, l2 = len(split_by_comma[0]), len(split_by_comma[1])
    mx = max(l1, l2)
    split_by_comma = [i + [0] * (mx - len(i)) for i in split_by_comma]
    result = list()
    for i in range(mx):
        result.append(int(split_by_comma[0][i]) + int(split_by_comma[1][i]))
    return result


sa = ["[1, 2, 5, 6]", "[5, 2, 8, 11, 12]"]
print(ArrayMatching(sa))
