"""
0    For this challenge you will be determining the largest word in a string.

Have the function LongestWord(sen) take the sen parameter being passed and return the largest word
in the string. If there are two or more words that are the same length, return the first word from
the string with that length. Ignore punctuation and assume sen will not be empty.

Sample Test Cases
Input:"fun&!! time"
Output:"time"

Input:"I love dogs"
Output:"love"
"""


def LongestWord(sen: str):
    import string
    rm_punc = sen.translate(sen.maketrans('', '', string.punctuation))
    longest = ""
    for word in rm_punc.split(" "):
        if len(word) > len(longest):
            longest = word
    return longest


print(LongestWord("I love dogs"))
