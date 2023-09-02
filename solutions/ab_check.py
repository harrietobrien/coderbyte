"""
10    For this challenge you will determine if two characters are separated a specific way in the string.

Have the function ABCheck(str) take the str parameter being passed and return the string true if
the characters a and b are separated by exactly 3 places anywhere in the string at least once
(i.e. "lane borrowed" would result in true because there is exactly three characters between a and b).
Otherwise, return the string false.

Sample Test Cases
Input:"after badly"
Output:"false"

Input:"Laura sobs"
Output:"true"
"""


def ABCheck(string: str):
    assert len(string) >= 5
    for i in range((len(string) - 4)):
        if string[i] == "a" and string[i + 4] == "b" or \
                string[i] == "b" and string[i + 4] == "a":
            return True
    return False


tests = ["lane borrowed", "after badly", "Laura sobs", "acccb"]
for test in tests:
    print(len(test))
    print(ABCheck(test))
