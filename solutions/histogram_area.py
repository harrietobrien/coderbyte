"""
For this challenge you will determine the largest area under a histogram.

Have the function HistogramArea(arr) read the array of non-negative integers stored in arr
which will represent the heights of bars on a graph (where each bar width is 1), and determine
the largest area underneath the entire bar graph. For example: if arr is [2, 1, 3, 4, 1]
then this looks like the following bar graph:

You can see in the above bar graph that the largest area underneath the graph is covered
by the x's. The area of that space is equal to 6 because the entire width is 2 and the
maximum height is 3, therefore 2 * 3 = 6. Your program should return 6.
The array will always contain at least 1 element.
"""


def HistogramArea(arr):
    stack, res = [], 0
    arr.append(-1)
    for i in range(len(arr)):
        bar = arr[i]
        step = 0
        while stack and stack[-1][1] >= bar:
            width, height = stack.pop()
            step += width
            res = max(res, step * height)
        stack.append((step + 1, bar))
    return res


print(HistogramArea([2, 1, 3, 4, 1]))
