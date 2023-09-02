"""
53    For this challenge you will determine if a set of characters exists in a string.

Have the function AlphabetSearching(str) take the str parameter being passed and return
the string true if every single letter of the English alphabet exists in the string;
otherwise, return the string false. For example: if str is "zacxyjbbkfgtbhdaielqrm45pnsowtuv"
then your program should return the string true because every character in the alphabet
exists in this string even though some characters appear more than once.
"""


def AlphabetSearching(string: str):
    alphabet = set(map(lambda n: chr(n), list(range(97, 123))))
    return set(string).issuperset(alphabet)


print(AlphabetSearching("zacxyjbbkfgtbhdaielqrm45pnsowtuv"))
print(AlphabetSearching("zacxyjbbkfgtbhdaielqr45pnsowtuv"))
