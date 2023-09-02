"""
11    For this challenge you will be counting all the vowels in a string.

Have the function VowelCount(str) take the str string
parameter being passed and return the number of vowels the string contains
(i.e. "All cows eat grass" would return 5). Do not count y as a vowel for this challenge.

Sample Test Cases
Input:"hello"
Output:2

Input:"coderbyte"
Output:3
"""


def VowelCount(s: str):
    vowels = "aeiouAEIOU"
    return len([char for char in s
                if char in vowels])


print(VowelCount("All cows eat grass"))
