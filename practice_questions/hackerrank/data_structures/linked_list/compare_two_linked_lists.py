"""
@author: David Lei
@since: 5/11/2017

https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

2 linked lists are equal if they have the same number of nodes and same data.
Return 1 if equal, otherwise 0.
Either head pointer given may be null.

Passed :)
"""

def CompareLists(headA, headB):
    while True:
        if not headA and headB:
            return 0
        if headA and not headB:
            return 0
        if not headA and not headB: # Only equal if terminate at the same time.
            return 1
        # Both heads have nodes.
        if headA.data != headB.data:
            return 0
        headA = headA.next
        headB = headB.next