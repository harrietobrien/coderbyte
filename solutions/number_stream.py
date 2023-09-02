"""
73    For this challenge you will determine if a stream of digits occurs in a string.

Have the function NumberStream(str) take the str parameter being passed which will contain the
numbers 2 through 9, and determine if there is a consecutive stream of digits of at least N length
where N is the actual digit value. If so, return the string true, otherwise return the string false.
For example: if str is "6539923335" then your program should return the string true because there is
a consecutive stream of 3's of length 3. The input string will always contain at least one digit.
"""


def NumberStream(s: str):
    check = [f'{str(n) * n}' for n in range(2, 10)]
    return "true" if any(opt in s for opt in check) else "false"


print(NumberStream("6539923335"))
