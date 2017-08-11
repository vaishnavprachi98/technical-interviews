"""
@author: David Lei
@since: 25/08/2016
@modified: 

Supporting data structure for DFS

Note: implementation slightly different to linked queue/list

    [item, next] <-        [item, next] <-       [item, next] <- top points to last node
           ^       |_______________|      |______________|
           |
None ------

we only need to store top, each node's next points to the node before it (allows for easy implementation of pop)
if top is None stack is empty
"""
# supporting structures

class LinkedNode:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class LinkedStack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top == None

    def push(self, x):
        self.count += 1
        current_top_node = self.top
        new_node = LinkedNode(x, current_top_node)  # new node has item x and points to old top (current_top)
        self.top = new_node                         # old top points to new node which is the top of the stack

    def pop(self):
        self.count -= 1
        if not self.is_empty():
            item = self.top.item                    # item to return
            self.top = self.top.next                # points to previous link
            return item
        raise Exception

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

if __name__ == '__main__':
    linkedStack = LinkedStack()

    linkedStack.push(8)
    linkedStack.push(9)
    print(linkedStack.pop())
    print(linkedStack.pop())
    # assertion error
    #print(linkedStack.pop()

    #linkedStack.reset()
    linkedStack.push(11)    # next
    linkedStack.push(12)    # next
    linkedStack.push(13)    # top
    #print(linkedStack.nextDOTnext())
    print(linkedStack.pop())

    def reverse(string):
        stack = LinkedStack()

        for i in string:
            stack.push(i)

        output =""

        while not stack.is_empty():
            output += stack.pop()
        return output
    print(reverse('helloworld'))

