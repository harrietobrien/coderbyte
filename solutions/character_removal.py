"""
For this challenge you will attempt to modify a word and then find it within a dictionary.

have the function CharacterRemoval(strArr) read the array of strings stored in strArr,
which will contain 2 elements: the first element will be a sequence of characters representing
a word, and the second element will be a long string of comma-separated words, in alphabetical
order, that represents a dictionary of some arbitrary length. For example: strArr can be:
["worlcde", "apple,bat,cat,goodbye,hello,yellow,why,world"]. Your goal is to determine the
 minimum number of characters, if any, can be removed from the word so that it matches one of
the words from the dictionary. In this case, your program should return 2 because once you remove
the characters "c" and "e" you are left with "world" and that exists within the dictionary. If
the word cannot be found no matter what characters are removed, return -1.
"""


def CharacterRemoval(strArr):
    chars, rest = strArr
    words = rest.split(",")
    matches = list()
    for word in words:
        if all([word.count(c) == chars.count(c)
                for c in set(word)]):
            matches.append(word)
    curr_min = -1
    for opt in matches:
        diff = len(chars) - len(opt)
        if curr_min == -1:
            curr_min = diff
        if diff < curr_min:
            curr_min = diff
    return curr_min


print(CharacterRemoval(["worlcde", "apple,bat,cat,goodbye,hello,yellow,why,world"]))
print(CharacterRemoval(["qrobzbbankcs", "apple,robbbbbbbanks,cat,robbbanks,hello,robbanks,why,world"]))
print(CharacterRemoval(["worlcde", "apple,bat,cat,goodbye,hello,yellow,why"]))