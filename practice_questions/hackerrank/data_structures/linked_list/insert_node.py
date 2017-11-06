"""
@author: David Lei
@since: 2/11/2017

https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem


 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 return back the head of the linked list in the below method.

"""
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def InsertNth(head, data, position):
    # Assuming position <= len of list.
    if head is None:
        return Node(data, None)

    node = head
    for _ in range(position - 1):
        if not node.next:  # Index > len list.
            break
        node = node.next
    node.next = Node(data, node.next)
    return head


def test():
    head = InsertNth(None, 3, 0)
    head = InsertNth(head, 5, 1)
    head = InsertNth(head, 4, 2)
    head = InsertNth(head, 2, 3)
    head = InsertNth(head, 10, 1)
    while head is not None:
        print(head.data, end=" ")
        head = head.next

if __name__ == "__main__":
    test()