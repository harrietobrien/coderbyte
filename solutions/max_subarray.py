"""
For this challenge you will determine the largest sum subarray.

Have the function MaxSubarray(arr) take the array of numbers stored in arr and determine the
largest sum that can be formed by any contiguous subarray in the array. For example, if arr
is [-2, 5, -1, 7, -3] then your program should return 11 because the sum is formed by the
subarray [5, -1, 7]. Adding any element before or after this subarray would make the sum smaller.
"""

import math


def MaxSubarray(arr: list):
    cur_max, max_till_now = 0, -math.inf
    for c in arr:
        cur_max = max(c, cur_max + c)
        max_till_now = max(max_till_now, cur_max)
    return max_till_now