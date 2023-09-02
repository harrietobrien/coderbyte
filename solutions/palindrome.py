"""
14    For this challenge you will determine if a string is written the same way forward and backwards.

Have the function Palindrome(str) take the str parameter being
passed and return the string true if the parameter is a palindrome, (the string is
the same forward as it is backward) otherwise return the string false. For example:
"racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string.

Sample Test Cases
Input:"never odd or even"
Output:"true"

Input:"eye"
Output:"true"
"""


def Palindrome(s: str):
    string = "".join([c for c in s if c.isalpha()])
    return string == string[::-1]


print(Palindrome("never odd or even"))
