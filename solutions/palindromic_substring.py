"""
For this challenge you will be finding the longest palindromic substring.

Have the function PalindromicSubstring(str) take the str parameter being passed and find the
longest palindromic substring, which means the longest substring which is read the same forwards
as it is backwards. For example: if str is "abracecars" then your program should return the
string racecar because it is the longest palindrome within the input string.

The input will only contain lowercase alphabetic characters. The longest palindromic substring
will always be unique, but if there is none that is longer than 2 characters, return the string none.
"""


def PalindromicSubstring(s: str):
    # Palindrome Tree
    class Node:
        def __init__(self, length, suffix=None):
            self.length = length
            self.suffix = suffix
            self.next = dict()

    curr = empty = Node(0, Node(-1))
    final_length = final_index = 0
    for i, c in enumerate(s):
        while i <= curr.length or s[i - 1 - curr.length] != c:
            curr = curr.suffix
        if c in curr.next:
            curr = curr.next[c]
            continue
        node = curr.next[c] = Node(curr.length + 2, empty)
        if node.length > final_length:
            final_length, final_index = node.length, i - node.length + 1
        if node.length > 1:
            curr = curr.suffix
            while i <= curr.length or s[i - 1 - curr.length] != c:
                curr = curr.suffix
            node.suffix = curr.next[c]
        curr = node
    return s[final_index:final_index + final_length]


print(PalindromicSubstring("abracecars"))