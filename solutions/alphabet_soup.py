"""
9    For this challenge you will be sorting characters in a string.

Take the str string parameter being passed and return the string with the letters in alphabetical order
(i.e. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.
"""

import string


def AlphabetSoupEfficient(s: str):
    rm_punc = s.translate(s.maketrans('', '', string.punctuation))
    return ''.join(sorted(rm_punc))


def AlphabetSoupNaive(s: str):
    rm_punc = s.translate(s.maketrans('', '', string.punctuation))
    res = list()
    n = len(rm_punc)
    for i in range(n):
        res.append(rm_punc[i])
    for i in range(n):
        for j in range(n):
            if res[i] < res[j]:
                res[i], res[j] = res[j], res[i]
    j = ""
    for i in range(len(rm_punc)):
        j = j + res[i]
    return j


print(AlphabetSoupEfficient("hel,lo"))
print(AlphabetSoupNaive("hel{lo"))
