"""
@author: David Lei
@since: 6/11/2017

https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

The height of a single node is 0, the height of a binary tree is the number of edges from the root to it's furthest leaf.

Given the root return the height of the tree.

Passed :)
"""

def height(root):
    if not root:  # At the child of a leaf, will mean leaf returns height of 0.
        return -1
    return max(height(root.left), height(root.right)) + 1