"""
For this challenge you will transform a string using the Caesar Cipher.

Have the function CaesarCipher(str,num) take the str parameter and perform a Caesar Cipher shift
on it using the num parameter as the shifting number. A Caesar Cipher works by shifting each letter
in the string N places down in the alphabet (in this case N will be num). Punctuation, spaces, and
capitalization should remain intact. For example if the string is "Caesar Cipher" and num is 2
the output should be "Ecguct Ekrjgt".
"""


def CaesarCipher(string: str, num: int):
    res = ""
    for i in range(len(string)):
        char = string[i]
        if not char.isalpha():
            res += char
        else:
            res += chr(ord(char) + num)
    return res


print(CaesarCipher("Caesar Cipher", 2))
