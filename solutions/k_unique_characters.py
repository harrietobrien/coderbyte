"""
For this challenge you will be searching a string for a particular substring.

Have the function KUniqueCharacters(str) take the str parameter being passed and find the
longest substring that contains k unique characters, where k will be the first character from
the string. The substring will start from the second position in the string because the first
character will be the integer k. For example: if str is "2aabbacbaa" there are several substrings
that all contain 2 unique characters, namely: ["aabba", "ac", "cb", "ba"], but your program should
return "aabba" because it is the longest substring. If there are multiple longest substrings,
then return the first substring encountered with the longest length. k will range from 1 to 6.
"""


def KUniqueCharacters(string: str):
    k = int(string[0])
    table = dict()
    start, end = 0, 0
    longest = 0
    start_longest, end_longest = 0, 0
    s = string[1:]
    for end in range(len(s)):
        newCharacter = s[end]
        if newCharacter in table.keys():
            table[newCharacter] += 1
        else:
            table[newCharacter] = 1
        # check if # of distinct chars in window > k
        while len(table) > k:
            startCharacter = s[start]
            start += 1
            table[startCharacter] -= 1
            # if frequency becomes 0 then remove char
            if table[startCharacter] == 0:
                table.pop(startCharacter)
        # check if current window is greatest seen so far
        if end - start + 1 > longest:
            longest = end - start + 1
            start_longest = start
            end_longest = end
    return s[start_longest:end_longest+1]

print(KUniqueCharacters("2aabbacbaa"))
