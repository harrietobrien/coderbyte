"""
For this challenge you will determine if the brackets in a string are correctly matched up.

Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the
brackets are correctly matched and each one is accounted for. Otherwise, return 0. For example:
if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" then
the output should be 0 because the brackets do not correctly match up. Only "(" and ")" will
be used as brackets. If str contains no brackets return 1.
"""


def BracketMatcher(s: str):
    matches = {"(": ")", "[": "]", "{": "}"}
    starters = list(matches.keys())
    closers = list(matches.values())
    stack = list()
    for char in s:
        if char not in starters and\
                char not in closers:
            continue
        if char in starters:
            stack.append(char)
        elif not stack or stack[-1] \
                != starters[closers.index(char)]:
            return False
        else:
            stack.pop()
    return not stack


print(BracketMatcher("(hello (world))"))
print(BracketMatcher("((hello (world))"))
