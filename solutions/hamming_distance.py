"""
33    For this challenge you will determine the difference between two strings.

Have the function HammingDistance(strArr) take the array of strings stored in strArr,
which will only contain two strings of equal length and return the Hamming distance
between them. The Hamming distance is the number of positions where the corresponding
characters are different. For example: if strArr is ["coder", "codec"] then your
program should return 1. The string will always be of equal length and will only
contain lowercase characters from the alphabet and numbers.
"""


def HammingDistance(strArr):
    s1, s2 = strArr[0], strArr[1]
    assert len(s1) == len(s2)
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count


print(HammingDistance(["coder", "codec"]))
