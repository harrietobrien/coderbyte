"""
3    For this challenge you will be manipulating characters in a string.

Have the function LetterChanges(str) take the str parameter being passed and modify it
using the following algorithm. Replace every letter in the string with the letter
following it in the alphabet (i.e. c becomes d, z becomes a). Then capitalize every
vowel in this new string (a, e, i, o, u) and finally return this modified string.

Sample Test Cases
Input:"hello*3"
Output:"Ifmmp*3"

Input:"fun times!"
Output:"gvO Ujnft!"
"""


def LetterChanges(string: str):
    res = ""
    for c in string:
        if not c.isalpha():
            res += c
        else:
            res += chr(ord(c) + 1)
    return res


print(LetterChanges("hello*3"))
