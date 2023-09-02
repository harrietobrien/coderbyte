"""
49    For this challenge you will determine if three elements can sum to some larger number.

Have the function ThreeSum(arr) take the array of integers stored in arr, and determine if any
three distinct numbers (excluding the first element) in the array can sum up to the first element
in the array. For example: if arr is [8, 2, 1, 4, 10, 5, -1, -1] then there are actually three
sets of triplets that sum to the number 8: [2, 1, 5], [4, 5, -1] and [10, -1, -1]. Your program
should return the string true if 3 distinct elements sum to the first element, otherwise your
program should return the string false. The input array will always contain at least 4 elements.
"""


def ThreeSum(arr):
    target = arr[0]
    nums = sorted(arr[1:])
    threeSums = list()
    for i in range(len(nums)):
        if nums[i] != target and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == target:
                threeSums.append([nums[i], nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif nums[i] + nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
    return "true" if threeSums else "false"


print(ThreeSum([8, 2, 1, 4, 10, 5, -1, -1]))
