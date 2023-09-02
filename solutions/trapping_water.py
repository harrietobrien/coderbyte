"""
For this challenge you will determine the largest amount of water you can trap within a boundary.

Have the function TrappingWater(arr) take the array of non-negative integers stored in arr, and determine
the largest amount of water that can be trapped. The numbers in the array represent the height of a building
(where the width of each building is 1) and if you imagine it raining, water will be trapped between the two
tallest buildings. For example: if arr is [3, 0, 0, 2, 0, 4] then this array of building heights looks like
the following picture if we draw it out:

Now if you imagine it rains and water gets trapped in this picture, then it'll
look like the following (the x's represent water):

This is the most water that can be trapped in this picture, and
if you calculate the area you get 10, so your program should return 10.
"""


def TrappingWater(arr: list):
    left, right = 0, len(arr) - 1
    left_max, right_max = 0, 0
    area = 0
    while left < right:
        if arr[left] > arr[right]:
            if arr[right] > right_max:
                right_max = arr[right]
            else:
                area += right_max - arr[right]
            right -= 1
        else:
            if arr[left] > left_max:
                left_max = arr[left]
            else:
                area += left_max - arr[left]
            left += 1
    return area


print(TrappingWater([0,1,0,2,1,0,1,3,2,1,2,1]))
