"""
62    For this challenge you will be converting a string into camel case format.

Have the function CamelCase(str) take the str parameter being passed and return it in proper camel
case format where the first letter of each word is capitalized (excluding the first letter). The string
will only contain letters and some combination of delimiter punctuation characters separating each word.

For example: if str is "BOB loves-coding" then your program should return the string bobLovesCoding.
"""


def CamelCase(string: str):
    import re
    lc_words = list(map(lambda s: s.lower(), re.split("\W+", string)))
    res = list(map(lambda s: s.capitalize(), lc_words[1:]))
    res.insert(0, lc_words[0])
    return "".join(res)


print(CamelCase("BOB loves-coding"))
