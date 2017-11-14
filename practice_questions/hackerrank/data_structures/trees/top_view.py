"""
@author: David Lei
@since: 6/11/2017

https://www.hackerrank.com/challenges/tree-top-view/problem

Given the root to a binary tree print the top view where the top view is
what is visible from looking at the tree from above.

Passed :)

Note: This 'top view' is different to geeks for geeks definition of top view (that is a lot harder),
    do it if I have time:  http://www.geeksforgeeks.org/print-nodes-top-view-binary-tree/
"""

def collect_left(node, arr):
    if node.left:
        collect_left(node.left, arr)
    arr.append(str(node.data))

# def collect_right(node, arr):
#     if node.right:
#         collect_right(node.right, arr)
#     arr.append(node.data)

def topView(root):
    # Left and right most branches from root are in the top view.
    l = []
    r = []
    # Note: my first approach appended for right and left, it works for right as the traversal order == top order from L->R
    #   but this does not work for left as a <- b is appended as [b, a].
    if root.left:
        collect_left(root.left, l)
    cur = root.right
    while cur:
        r.append(str(cur.data))
        cur = cur.right
    top_view = l + [str(root.data)] + r
    print(" ".join(top_view))  # Can't join ints!