"""
For this challenge you will be determining if a string is a valid number.

Have the function FormattedNumber(strArr) take the strArr parameter being passed, which
will only contain a single element, and return the string true if it is a valid number
that contains only digits with properly placed decimals and commas, otherwise return th
string false. For example: if strArr is ["1,093,222.04"] then your program should return
the string true, but if the input were ["1,093,22.04"] then your program should return
the string false. The input may contain characters other than digits.

Examples

Input: ["0.232567"]
Output: true

Input: ["2,567.00.2"]
Output: false
"""


def FormattedNumber(strArr):
    s = strArr[0]
    decimal_count = s.count(".")
    if decimal_count > 1:
        return "false"
    elif decimal_count == 1:
        # _ : mantissa
        int_part, _ = s.split(".")
        int_part = int_part.split(",")
        if any(len(int_part[i]) < 3
               for i in range(len(int_part))
               if i != 0):
            return "false"
        return "true"


print(FormattedNumber(["0.232567"]))
print(FormattedNumber(["2,567.00.2"]))
