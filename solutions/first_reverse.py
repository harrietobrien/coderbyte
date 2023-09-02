"""
2    For this challenge you will be reversing a string.

Have the function FirstReverse(str) take the str parameter
being passed and return the string in reversed order.

Sample Test Cases
Input:"coderbyte"
Output:"etybredoc"

Input:"I Love Code"
Output:"edoC evoL I"
"""


def FirstReverse(string: str):
    return string[::-1]


print(FirstReverse("coderbyte"))
