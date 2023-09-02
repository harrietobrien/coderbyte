"""
43    For this challenge you will determine if two elements can sum to some larger number.

Have the function TwoSum(arr) take the array of integers stored in arr, and determine if any two
numbers (excluding the first element) in the array can sum up to the first element in the array.
For example: if arr is [7, 3, 5, 2, -4, 8, 11], then there are actually two pairs that sum to the
number 7: [5, 2] and [-4, 11]. Your program should return all pairs, with the numbers separated
by a comma, in the order the first number appears in the array. Pairs should be separated by a
space. So for the example above, your program would return: 5,2 -4,11
"""


def TwoSum(arr):
    target = arr[0]
    nums = arr[1:]
    twoSums = list()
    diffs = dict()  # count differences
    for i, n in enumerate(nums):
        if n in diffs:
            # indices
            j, k = diffs[n], i
            twoSums.append([nums[j], nums[k]])
        else:
            diffs[target - n] = i
    res = list()
    for pair in twoSums:
        res.append(",".join([str(n) for n in pair]))
    return " ".join(res)


print(TwoSum([7, 3, 5, 2, -4, 8, 11]))
