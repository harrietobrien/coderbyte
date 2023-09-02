"""
12    For this challenge you will be determining how many words a sentence contains.

Have the function WordCount(str) take the str string parameter
being passed and return the number of words the string contains (i.e. "Never eat
shredded wheat" would return 4). Words will be separated by single spaces.

Sample Test Cases
Input:"Hello World"
Output:2

Input:"one 22 three"
Output:3
"""


def WordCount(s: str):
    return len(s.split(" "))


print(WordCount("one 22 three"))
