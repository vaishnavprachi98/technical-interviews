"""
@author: David Lei
@since: 6/11/2017

https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

Given the head to a doubly linked list reverse it and return the head of the reversed list.

Both pass :)
"""

def ReverseIterative(head):
    if not head:
        return head
    cur = head
    while cur:
        next_node = cur.next
        cur.next = cur.prev
        cur.prev = next_node
        if not next_node: # End of the list.
            return cur
        cur = next_node

def ReverseRecursive(head):
    if not head:
        return head
    if head.next is None:  # Base case, end of the list.
        tmp = head.next
        head.next = head.prev
        head.prev = tmp
        return head
    next_node = head.next
    head.next = head.prev
    head.prev = next_node
    return ReverseRecursive(next_node)
