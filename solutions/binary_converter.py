"""
For this challenge you will be converting a number from binary to decimal.

Have the function BinaryConverter(str) return the decimal form of the binary value. For example:
if 101 is passed return 5, or if 1000 is passed return 8.
"""


def BinaryConverterBuiltin(string: str):
    return int(string, 2)


def BinaryConverterNaive(string: str):
    decimal = 0
    n = len(string)
    for i in range(n):
        digit = int(string[i])
        decimal += digit * 2 ** (n - i - 1)
    return decimal


print(BinaryConverterBuiltin("101"))
print(BinaryConverterBuiltin("1000"))

print(BinaryConverterNaive("101"))
print(BinaryConverterNaive("1000"))
