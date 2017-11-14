"""
@author: David Lei
@since: 6/11/2017

https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

Given head pointers to two sorted linked list, merge them and return the head of the merge such
that the resulting linked list is in sorted order.

Passed :)
"""

def MergeLists(headA, headB):
    if headA is None and headB is None:
        return None
    if headA is None and headB is not None:
        return headB
    if headA is not None and headB is None:
        return headB
    # Both heads not none.
    # Use <= to maintain stability.
    if headA.data <= headB.data:
        head = headA
        headA = headA.next
    else:
        head = headB
        headB = headB.next
    current = head
    while headA and headB:
        # Find the smaller element.
        if headA.data <= headB.data:
            current.next = headA
            current = current.next
            headA = headA.next
        else:
            current.next = headB
            current = current.next
            headB = headB.next
    if headA:
        current.next = headA
    elif headB:
        current.next = headB
    return head
