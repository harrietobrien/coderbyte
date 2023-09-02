"""
42    For this challenge you will find the first non-repeating character in a string.

Have the function NonrepeatingCharacter(str) take the str parameter being passed, which
will contain only alphabetic characters and spaces, and return the first non-repeating
character. For example: if str is "agettkgaeee" then your program should return k. The
string will always contain at least one character and there will always be at
least one non-repeating character.
"""


def NonrepeatingCharacter(s: str):
    char_counts = {c: s.count(c) for c in set(s)}
    for char in s:
        if char_counts[char] == 1:
            return char


print(NonrepeatingCharacter("agettkgaeee"))
