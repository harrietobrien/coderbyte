"""
75    For this challenge you will determine how to create evenly matched brackets.

have the function RemoveBrackets(str) take the str string parameter being passed, which will
contain only the characters "(" and ")", and determine the minimum number of brackets that need
to be removed to create a string of correctly matched brackets. For example: if str is "(()))"
then your program should return the number 1. The answer could potentially be 0, and there will
always be at least one set of matching brackets in the string.

traverse the string
any opening tags get stored in stack
if we have a closing tag compare it to the stack
If they match than pop the top value of our stack
if they do not match we will still add it to the stack
we will traverse the whole string and repeat the above steps
in the end if the stack has any elements in it, this signals the number of brackets we would need to remove
"""


def RemoveBrackets(str):
    stack = list()
    for i in range(len(str)):
        if str[i] == '(':
            stack.append(str[i])
        elif str[i] == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(str[i])
    return len(stack)


print(RemoveBrackets("(()))"))
print(RemoveBrackets("(())()((("))
