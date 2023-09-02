"""
6    For this challenge you will be determining whether or not certain characters are in correct positions.

Have the function SimpleSymbols(str) take the str parameter being passed and determine if it is
an acceptable sequence by either returning the string true or false. The str parameter will be
composed of + and = symbols with several letters between them (ie. ++d+===+c++==a) and for the string
to be true each letter must be surrounded by a + symbol. So the string to the left would be false.
The string will not be empty and will have at least one letter.

Sample Test Cases
Input:"+d+=3=+s+"
Output:"true"

Input:"f++d+"
Output:"false"
"""


def SimpleSymbols(s: str):
    if s[0].isalpha() or s[-1].isalpha():
        return "false"
    for i in range(1, len(s)):
        if s[i].isalpha():
            if not s[i - 1] == s[i + 1] == "+":
                return "false"
    return "true"


print(SimpleSymbols("+d+=3=+s+"))
print(SimpleSymbols("f++d+"))
print(SimpleSymbols("++d+===+c++==a"))
