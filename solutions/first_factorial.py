"""
1    For this challenge you will be determining the factorial for a given number.

Have the function FirstFactorial(num) take the num parameter being passed and return the factorial
of it (i.e. if num = 4, return (4 * 3 * 2 * 1)). For the test cases, the range will be between 1 and 18.

Sample Test Cases
Input:4
Output:24

Input:8
Output:40320
"""


def FirstFactorial(num: int):
    product = 1
    while num:
        product *= num
        num -= 1
    return product


print(FirstFactorial(8))
