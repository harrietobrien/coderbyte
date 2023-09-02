"""
For this challenge you will determine which word has the greatest number of repeated letters.

Have the function LetterCountI(str) take the str parameter being passed and return the first
word with the greatest number of repeated letters. For example: "Today, is the greatest day ever!"
should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's.
If there are no words with repeating letters return -1. Words will be separated by spaces.
"""


def removePunctuation(s: str):
    import string
    s = s.lower()
    return s.translate(s.maketrans('', '', string.punctuation))


def LetterCount(string: str):
    greatest = ""
    greatest_count = 1
    string = removePunctuation(string)
    for word in string.split():
        counts = [word.count(c) for c in set(word)]
        max_count = max(counts)
        if max_count > greatest_count:
            greatest_count = max_count
            greatest = word
    return -1 if not greatest else greatest


print(LetterCount("Today, is the day!"))
print(LetterCount("Today, is the greatest day ever!"))
