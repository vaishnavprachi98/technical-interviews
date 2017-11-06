"""
@author: David Lei
@since: 31/10/2017

https://www.hackerrank.com/challenges/reverse-a-linked-list

 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.


 1 -> 2 -> 3 -> 4 -> Null

 becomes

 4 -> 3 -> 2 -> 1 -> Null
"""

# Iterative version works.
def Reverse(head):
    current = head
    prev = None
    while current.next is not None:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    current.next = prev
    return current

#  Recursive version works.
def Reverse_recursive(head):
    return reverse_recursive(head, None)

def reverse_recursive(node, prev):
    # Want to return the last node as that is the new head.
    next_node = node.next
    node.next = prev  # Reverse direction.
    if not next_node:
        return node # Last node, new head.
    return reverse_recursive(next_node, node) # Do for each element in list.
