"""
For this challenge you will compute the length of the longest consecutive subsequence.

Have the function LongestConsecutive(arr) take the array of positive integers stored in arr
and return the length of the longest consecutive subsequence (LCS). An LCS is a subset of
the original list where the numbers are in sorted order, from lowest to highest, and are in
a consecutive, increasing order. The sequence does not need to be contiguous and there can
be several different subsequences. For example: if arr is [4, 3, 8, 1, 2, 6, 100, 9] then a
few consecutive sequences are [1, 2, 3, 4], and [8, 9]. For this input, your program should
return 4 because that is the length of the longest consecutive subsequence.
"""


def LongestConsecutive(arr):
    if not arr:
        return 0
    arr = sorted(list(set(arr)))
    counts = list()
    currCount = 1
    prev = arr[0]
    for n in arr[1:]:
        if prev + 1 == n:
            currCount += 1
            prev = n
        else:
            counts.append(currCount)
            currCount = 1
            prev = n
        if n == arr[-1]:
            counts.append(currCount)
    return max(counts) if counts else 1


print(LongestConsecutive([4, 3, 8, 1, 2, 6, 100, 9]))
