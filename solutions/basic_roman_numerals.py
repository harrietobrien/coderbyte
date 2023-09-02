"""
48    For this challenge you will be converting a string of Roman numerals.

Have the function BasicRomanNumerals(str) read str which will be a string of Roman numerals.
The numerals being used are: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500 and
M for 1000. In Roman numerals, to create a number like 11 you simply add a 1 after the 10, so
you get XI. But to create a number like 19, you use the subtraction notation which is to add
an I before an X or V (or add an X before an L or C). So 19 in Roman numerals is XIX.  The
goal of your program is to return the decimal equivalent of the Roman numeral given. For
example : if str is "XXIV" your program should return 24.
"""


def BasicRomanNumerals(number: str):
    keys = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    vals = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
    roman_dict = dict(zip(keys, vals))
    roman = 0
    for v in sorted(roman_dict)[::-1]:
        k = roman_dict[v]
        while not number.find(k):
            roman += v
            number = number[len(k):]
    return roman


print(BasicRomanNumerals("XXIV"))
