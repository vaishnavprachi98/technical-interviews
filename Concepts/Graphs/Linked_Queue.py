"""
@author: David Lei
@since: 25/08/2016
@modified: 

Supporting data structure for BFS

    [item, next] --> [item, next] --> [item, next]
front (deque from here)           end (enqueue from here)
"""
class LinkedNode:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class LinkedQ:
    def __init__(self):
        self.front = None
        self.end = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, x):
        new_node = LinkedNode(x)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node   # self.rear will point at the last node
        self.rear = new_node            # always points at last item

    def deque(self):
        if not self.is_empty():
            item = self.front.item
            self.front = self.front.next
            if self.is_empty():
                self.rear = None        # just insace this is the last element, rear will still point to it w/o this
            return item
        raise Exception