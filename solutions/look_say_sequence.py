"""
For this challenge you will determine the next number in a sequence.

Have the function LookSaySequence(num) take the num parameter being passed and return the next
number in the sequence according to the following rule: to generate the next number in a sequence
read off the digits of the given number, counting the number of digits in groups of the same digit.
For example, the sequence beginning with 1 would be: 1, 11, 21, 1211, ... The 11 comes from there
being "one 1" before it and the 21 comes from there being "two 1's" before it. So your program
should return the next number in the sequence given num.
"""


def getDigits(num: int):
    digits = list()
    while num > 0:
        digit = num % 10
        digits.append(digit)
        num //= 10
    return digits


def LookSaySequence(num: int):
    digits = getDigits(num)
    digit_dict = {digit: 0 for digit in digits}
    digit = -1
    count = 1
    for i in range(len(digits)):
        curr = digits[i]
        if digit == digits[i]:
            count += 1
        else:
            count += 1
            digit = curr
            digit_dict[curr] = count




print(LookSaySequence(21))
