"""
4    For this challenge you will be adding up all the numbers from 1 to a certain argument.

Have the function SimpleAdding(num) add up all the numbers from 1 to num. For the test cases,
the parameter num will be any number from 1 to 1000.

Sample Test Cases
Input:12
Output:78

Input:140
Output:9870
"""


def SimpleAdding(num: int):
    return int(num * (num + 1) / 2)


print(SimpleAdding(140))
