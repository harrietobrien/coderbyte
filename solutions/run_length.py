"""
For this challenge you will determine the Run Length Encoding of a string.
Have the function RunLength(str) take the str parameter being passed and return a compressed
version of the string using the Run-length encoding algorithm. This algorithm works by taking
the occurrence of each repeating character and outputting that number along with a single
character of the repeating sequence. For example: "wwwggopp" would return 3w2g1o2p. The string
will not contain any numbers, punctuation, or symbols.
"""


def RunLength(string: str):
    res = ""
    for c in string:
        if c in res:
            continue
        count = string.count(c)
        res += f'{count}{c}'
    return res


print(RunLength("wwwggopp"))
