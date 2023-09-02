"""
88    For this challenge you will be determining whether a number is Happy.
"""


def sumSqrDgt(n: int) -> list:
    out = 0
    while n > 0:
        out += math.pow(n % 10, 2)
        n //= 10
    return out


def isHappy(n: int) -> bool:
    prev, next = n, sumSqrDgt(n)
    while prev != next:
        next = sumSqrDgt(sumSqrDgt(next))
        prev = sumSqrDgt(prev)
    return next == 1
