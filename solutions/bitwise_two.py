"""
44    For this challenge you will perform a bitwise operation on two binary numbers.

Have the function BitwiseTwo(strArr) take the array of strings stored in strArr, which will only
contain two strings of equal length that represent binary numbers, and return a final binary string
that performed the bitwise AND operation on both strings. A bitwise AND operation places a 1 in the
new string where there is a 1 in both locations in the binary strings, otherwise it places a 0 in
that spot. For example: if strArr is ["10111", "01101"] then your program should return the string "00101"
"""


def BitwiseTwo(strArr: list[str]):
    n = int(strArr[0], 2) & int(strArr[1], 2)
    bin_str = ""
    for i in range(len(strArr[0]) - 1, -1, -1):
        k = n >> i
        if k & 1:
            bin_str += "1"
        else:
            bin_str += "0"
    return bin_str


print(BitwiseTwo(["10111", "01101"]))