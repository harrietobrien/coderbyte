"""
26    For this challenge you will be determining whether a number is a power of two.

Have the function PowersofTwo(num) take the num parameter being passed which will be an integer and return
the string true if it's a power of two. If it's not return the string false. For example, if the input is 16
then your program should return the string true but if the input is 22 then the output should be the string false.

Sample Test Cases
Input:4
Output:"true"

Input:124
Output:"false"
"""


def PowersofTwo(num):
    # returns "true" if power of 2 otherwise "false"
    check = num and not (num & num - 1)
    return "true" if check else "false"


def largestPowerOf2LTENaive(n):
    # NAIVE SOLUTION
    # the largest power of 2 that is LTE to n
    power = 0
    while 2 ** power <= n:
        power += 1
    power -= 1
    return power, 2 ** power


def largestPowerOf2LTELog(n):
    import math
    power = int(math.log(n, 2))
    return power, 2 ** power


print(PowersofTwo(4))
print(PowersofTwo(124))

print(largestPowerOf2LTENaive(124))
print(largestPowerOf2LTELog(124))
