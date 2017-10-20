"""
@author: David Lei
@since: 21/10/2017

Woot works!

https://leetcode.com/problems/invert-binary-tree/description/
"""

def invert_tree(node):
    left = None
    right = None

    if node.left:
        left = invert_tree(node.left)

    if node.right:
        right = invert_tree(node.right)

    node.left = right
    node.right = left
    return node