"""
@author: David Lei
@since: 21/08/2016
@modified: 

A BST implementation supporting
- insert
- remove
- look up
- get min
- get max

assuming left < key =< right
"""

from Tree_Node import Tree_Node

class Binary_Search_Tree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert(self, key):
        """specify the value of the key for the new node
        will create node for you and call auxiliary function to recursively find where the
        new node belongs"""
        new_node = Tree_Node(key)
        if self.is_empty():                                     # make root point to the head of the tree (new node)
            self.root = new_node
        else:
            self._insert_aux(self.root, new_node)
    def _insert_aux(self, current_node, new_node):
        if new_node.key < current_node.key:                      # check if new node lies to the left
            if current_node.left is not None:                    # if None, we found where to put it
                self._insert_aux(current_node.left, new_node)    # else recursively find where to put
            else:
                current_node.left = new_node
        else:                                                    # new node lies to the right
            if current_node.right is not None:
                self._insert_aux(current_node.right, new_node)
            else:
                current_node.right = new_node

    def get_min(self):
        if not self.is_empty():
            current_node = self.root
            while current_node.left is not None:
                current_node = current_node.left
            return current_node.key
        else:
            raise Exception

    def get_max(self):
        if not self.is_empty():
            current_node = self.root
            while current_node.right is not None:
                current_node = current_node.right
            return current_node.key
        else:
            raise Exception

    def look_up(self, key):
        """Recursively searches if key is in the tree, returns False if not"""
        return self._look_up_aux(self.root, key)
    def _look_up_aux(self, current_node, key):
        if key < current_node.key:
            if current_node.left is not None:
                self._look_up_aux(current_node.left, key)
            else:
                return False
        elif key > current_node.key:
            if current_node.right is not None:
                self._look_up_aux(current_node.right, key)
            else:
                return False
        else:                                               # current_node.key = key
            return current_node

    def remove(self, key):
        """Remove a node with value key from the tree
        cases:
            1. node is a leaf, just get rid of it (easy)
            2. node has 1 child, make child go directly to parent of node, will maintain BST ordering (easy)
            3. node has 2 children, harder

        """
        if self._look_up_aux(self.root, key):                # check key in tree
            pass
        else:
            raise Exception

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, current_node):
        if current_node is not None:
            self._in_order(current_node.left)
            print(current_node.key)
            self._in_order(current_node.right)

if __name__ == "__main__":
    BST = Binary_Search_Tree()
    a = [5,10,-5,7,8,1,6,9,10,-6]
    for n in a:
        if n == -6:
            a = 1
        BST.insert(n)

    BST.in_order()