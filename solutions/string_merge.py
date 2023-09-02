"""
67    For this challenge you will be merging two different strings together.

Have the function StringMerge(str) read the str parameter being passed which will contain a
large string of alphanumeric characters with a single asterisk character splitting the string
evenly into two separate strings. Your goal is to return a new string by pairing up the characters
in the corresponding locations in both strings. For example: if str is "abc1*kyoo" then your
program should return the string akbyco1o because a pairs with k, b pairs with y, etc. The string
will always split evenly with the asterisk in the center.
"""


def StringMerge(s: str):
    s1, s2 = s.split("*")
    n = len(s1)
    return "".join([s1[i] + s2[i] for i in range(n)])


print(StringMerge("abc1*kyoo"))
