"""
72    For this challenge you will need to find the smallest repeating substring.

Have the function StringPeriods(str) take the str parameter being passed and determine if there is
some substring K that can be repeated N > 1 times to produce the input string exactly as it appears.
Your program should return the longest substring K, and if there is none it should return the string -1.

For example: if str is "abcababcababcab" then your program should return abcab because that is the longest
substring that is repeated 3 times to create the final string. Another example: if str is "abababababab"
then your program should return ababab because it is the longest substring. If the input string contains
only a single character, your program should return the string -1.
"""


def StringPeriods(s: str):
    all_ss = list()
    n = len(s)
    for i in range(0, n - 1):
        curr_ss = s[:i + 1]
        if n == s.count(curr_ss) * len(curr_ss):
            all_ss.append(curr_ss)
    return max(all_ss, key=len)


print(StringPeriods("abcababcababcab"))
