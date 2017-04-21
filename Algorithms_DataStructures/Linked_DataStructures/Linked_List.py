"""
@author: David Lei
@since: 21/04/2017
@modified: 

"""
from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None  # Start of list.
        self.count = 0  # Number of items in the list.

    def reset(self):
        self.__init__()

    def has_elements(self):
        return self.head is None

    def get_node(self, index):
        # Precondition: Index is properly bounded.
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def insert(self, data, index):
        # Insert into a linked list.

        # Bound indexes, don't allow negative or > self.count.
        if index < 0:
            index = 0
        elif index > self.count:  # Next index in list, assuming 0 indexed.
            index = self.count

        if index == 0:  # Put at start of linkedlist.
            self.head = Node(data, self.head)  # New_node.next points to old head.
        else:
            node_before = self.get_node(index - 1)  # Get node before current node the index.
            # New_node.next points to old node_before.next, update node_before.next to point to new_node.
            node_before.next = Node(data, node_before.next)
            self.count += 1


    def delete(self, index):
        # Bound indexes, don't allow negative or > self.count.
        if index < 0:
            index = 0
        elif index > self.count:  # Next index in list, assuming 0 indexed.
            index = self.count

        if index == 0:
            self.head = self.head.next  # self.head points to node after old self.head (can be none)
        else:
            # Get node 1 before, skip over 1 next.
            node_before = self.get_node(index - 1)
            node_before.next = node_before.next.next  # Skip over index to delete
            self.count -= 1

    def __str__(self):
        stringify = []
        current_node = self.head
        while current_node.next is not None:
            print(current_node)
            stringify.append(current_node.data)
            current_node = current_node.next
        return str(stringify)

if __name__ == "__main__":
    l = LinkedList()
    l.insert("B", 0)
    l.insert("C", 1)
    print(l)
    l.insert("A", 0)
    print(l)
    l.delete(1)
    print(l)