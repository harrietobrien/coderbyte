"""
39    For this challenge you will be reversing a binary string.

Have the function BinaryReversal(str) take the str parameter being passed, which will be a positive
integer, take its binary representation, reverse that string of bits, and then finally return the
new reversed string in decimal form. For example: if str is "47" then the binary version of this
integer is 00101111. Your program should reverse this binary string which then becomes: 11110100
and then finally return the decimal version of this string, which is 244.
"""


def BinaryReversal(string: str):
    n = int(string)
    bin_str = ""
    for i in range(7, -1, -1):
        k = n >> i
        if k & 1:
            bin_str += "1"
        else:
            bin_str += "0"
    return int(bin_str[::-1], 2)


print(BinaryReversal("47"))
