"""
5    For this challenge you will be capitalizing certain characters in a string.

Have the function LetterCapitalize(str) take the str parameter being passed and
capitalize the first letter of each word. Words will be separated by only one space.

Sample Test Cases
Input:"hello world"
Output:"Hello World"

Input:"i ran there"
Output:"I Ran There"
"""


def LetterCapitalize(s: str):
    words = s.split(" ")
    return " ".join([word.capitalize() for word in words])


print(LetterCapitalize("i ran there"))
