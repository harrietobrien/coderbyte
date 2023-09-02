"""
For this challenge you will traverse a binary tree and determine if it is symmetric.
Have the function SymmetricTree(strArr) take the array of strings stored in strArr, which will represent
a binary tree, and determine if the tree is symmetric (a mirror image of itself). The array will be
implemented similar to how a binary heap is implemented, except the tree may not be complete and NULL
nodes on any level of the tree will be represented with a #. For example: if strArr is
["1", "2", "2", "3", "#", "#", "3"]
For the input above, your program should return the string true because the binary tree is symmetric.
"""
import math
from dataclasses import dataclass


def SymmetricTree(strArr):
    @dataclass
    class Node:
        value: str
        right: int
        left: int

    # parent (index – 1) // 2
    def buildTree(arrLength, arr, i):
        if i == "#":
            return
        elif i >= 1 + math.floor(math.log2(n)):
            return Node(arr[i], "#", "#")
        else:
            return Node(arr[i],
                        buildTree(arrLength, arr, i * 2 + 1),
                        buildTree(arrLength, arr, i * 2 + 2))
    n = len(strArr)
    root = buildTree(n, strArr, 0)
    if root.left == "#" and root.right == "#":
        return True
    queue = [[root.left, root.right]]
    while queue:
        l, r = queue.pop(0)
        if l != "#" and r != "#":
            print(type(l))
            if l.value != r.value:
                return False
            queue.append([l.left, r.right])
            queue.append([l.right, r.left])
        elif l == "#" and r == "#":
            continue
        else:
            return False
    return True


print(SymmetricTree(["1", "2", "2", "3", "#", "5", "3"]))
