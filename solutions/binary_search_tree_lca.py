"""
For this challenge you will attempt to find the lowest common ancestor of a binary search tree.

have the function BinarySearchTreeLCA(strArr) take the array of strings stored in strArr, which will
contain 3 elements: the first element will be a binary search tree with all unique values in a preorder
traversal array, the second and third elements will be two different values, and your goal is to find
the lowest common ancestor of these two values. For example: if strArr is ["[10,5,1,7,40,50]","1","7"]
then this tree looks like the following:

For the input above, your program should return 5 because that is the value of the node that is
the LCA of the two nodes with values 1 and 7. You can assume the two nodes you are searching for
in the tree will exist somewhere in the tree.
"""
from dataclasses import dataclass

import ast


class BinarySearchTreeLca:
    def __call__(self, str_arr: str) -> str:
        tree_nodes = ast.literal_eval(str_arr[0])
        _left = int(str_arr[1])
        _right = int(str_arr[2])
        _max = max(_left, _right)
        _min = min(_left, _right)
        _low = min(tree_nodes.index(_min), tree_nodes.index(_max))
        xs = []
        for x in tree_nodes[0:_low + 1]:
            if x <= _max:
                xs.append(x)
        return max(xs)


def BinarySearchTreeLCA(strArr):
    bst_str = strArr[0]
    nodes = ast.literal_eval(bst_str)
    print(nodes)
    right, left = int(strArr[1]), int(strArr[2])
    mx, mn = max(left, right), min(left, right)
    mx_index = nodes.index(mx)
    mn_index = nodes.index(mn)
    curr_low = min(mn_index, mx_index)
    lowest = list()
    for node in nodes[:curr_low + 1]:
        if node <= mx:
            lowest.append(node)
    return max(lowest)


print(BinarySearchTreeLCA(["[10,5,1,7,40,50]", "1", "7"]))
