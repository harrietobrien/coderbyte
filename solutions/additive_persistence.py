"""
27    For this challenge you will be determining the additive persistence for a given number.

Have the function AdditivePersistence(num) take the num parameter being passed which will always
be a positive integer and return its additive persistence which is the number of times you must
add the digits in num until you reach a single digit. For example: if num is 2718 then your
program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9, and you stop at 9.
"""


def AdditivePersistence(num):
    assert num > 0
    n = num
    count, digit_sum = 0, 0
    while n > 0:
        digit_sum += n % 10
        count += 1
        if digit_sum >= 9:
            return count
        n /= 10


nums = [2718, 111111111]
for num in nums:
    print(AdditivePersistence(num))
