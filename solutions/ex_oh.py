"""
13    For this challenge you will traverse a string and determine if there is an equal amount of certain characters.

Have the function ExOh(str) take the str parameter being passed and return the string true if
there is an equal number of x's and o's, otherwise return the string false. Only these two
letters will be entered in the string, no punctuation or numbers. For example: if str is
"xooxxxxooxo" then the output should return false because there are 6 x's and 5 o's.

Sample Test Cases
Input:"xooxxo"
Output:"true"

Input:"x"
Output:"false"
"""


def ExOh(s: str):
    return "true" if s.count("x") == s.count("o") else "false"


print(ExOh("xooxxo"))
print(ExOh("x"))
