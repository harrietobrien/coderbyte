"""
For this challenge you will determine the mode, the number that appears most frequently, in an array.
Have the function SimpleMode(arr) take the array of numbers stored in arr and return the number
that appears most frequently (the mode). For example: if arr contains [10, 4, 5, 2, 4] the output
should be 4. If there is more than one mode return the one that appeared in the array first (ie.
[5, 10, 10, 6, 5] should return 5 because it appeared first). If there is no mode return -1.
The array will not be empty.
"""


def SimpleMode(arr: list):
    count = 1
    mode = -1
    for i in range(len(arr)):
        curr_count = arr.count(arr[i])
        if curr_count > count:
            mode = arr[i]
            count = curr_count
    return mode


print(SimpleMode([10, 4, 5, 2, 4]))
print(SimpleMode([5, 10, 10, 6, 5]))
