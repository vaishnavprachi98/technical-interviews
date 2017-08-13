"""
@author: David Lei
@since: 13/08/2017

Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    seen = {head}
    current = head.next
    while current is not None:
        if current in seen:
            return True
        seen.add(current)
        current = current.next

