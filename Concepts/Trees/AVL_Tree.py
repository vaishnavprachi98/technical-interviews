"""
@author: David Lei
@since: 21/08/2016
@modified:

Material from Data Structures & Algorithm analysis in Java (Weiss 3rd ed)

AVL property - Binary Search Tree with a balance property

Idea: keep tree shallow so we don't get the O(n) worst case for search, insert, delete like in a BST

Forces max height of tree to be bounded by log n (AVL tree height is at most roughly 1.44 log(N + 2) − 1.328)

balance <= 1
    where balance is defined as |height_LeftSubtree - height_RightSubtree|
    update heights recursively starting at leaves

need to store:
    - heights
    - balance

To maintain AVL property, after changing tree structure (insert, delete)
    1. update heights
    2. update balances
    3. rebalance (via rotations)
___________
|Rotations|
-----------
    balance is calculated by left_height - right_height
    if the balance is > 1, then the left side is heavier (violates the AVL property)
    if balance < -1, then the right side is heavier (or larger)

    if positive we need to start with a left rotation

    if negative we need to start with a right rotation

    assuming that the node that violates the balance condition is *, thus * needs to be rebalanced
        - a node can only have at most 2 children
        - height imbalance requires *'s subtrees differ by 2
                           *
                        /     \
                  lChild       rChild
                 /    \        /      \
            lSubT    rSubT   lSubT   rSubT
             o         i       i       o

        so violation can occur in 4 places:
            1. insertion into left subtree of left child of *   | insertion occurs 'outside', left left
            2. insertion into right subtree of left child of *  | insertion occurs 'inside', right left
            3. insertion into left subtree of right child of *  | insertion occurs 'inside', left right
            4. insertion into right subtree of right child of * | insertion occurs 'outside', right right
        o = 'outside' can be fixed with a single rotation
        i = 'inside' needs more complex double rotation

        treat caps as twice height of lower case

                    k2                                      k1              drag z down, make k1 new root
                  /   \                                    /  \             attach y to k2
                k1    z     => rotate right =>             X    k2
               /  \                                            / \
              X   y                                           y   z

            h b     k2 violates balance property           h b
        k2|4 2                                          k2|3 0
        k1|3 1                                          k1|2 0
        z |1 0                                          z |1 0
        X |2 0                                          X |2 0
        y |1 0                                          y |1 0


            A                               B
           /                               / \
          B     => right rotation =>       C   A      this keeps BST property and keeps tree shallower allowing O(log n ) operations
         /
        C

- insert is same as BST with updating height after and rebalanced to enforce AVL property
- look up, get min, get max is same as BST
"""
from Tree_Node import Tree_Node

class AVL_Tree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def is_leaf(self, node):
        return node.left is None and node.right is None

    def rebalance(self):
        while abs(self.root.balance) > 1:
            if self.root.balance > 1:

            # rebalance
            pass


    def update_balances(self):
        """Recursively update balances by going to the left most leaf and working it's way up
        works as of 26/8/16 yay :D"""
        start = self.root
        self._update_balances_aux(start)
    def _update_balances_aux(self, current_node):

        if current_node.left is not None:
            l = self._update_balances_aux(current_node.left)
        elif current_node.left is None:
            l = -1
        else:
            l = current_node.height

        if current_node.right is not None:
            r = self._update_balances_aux(current_node.right)
        elif current_node.right is None:
            r = - 1
        else:
            r = current_node.height
        current_node.balance = l - r
        return current_node.height

    def update_heights(self):
        """Recursively update heights by going to leaves and work it's way up
        works as of 26/8/16 yay :D"""
        if self.is_empty():
            raise Exception ('Empty tree')
        else:
            start = self.root
            self._update_heights_aux(start)
    def _update_heights_aux(self, current_node):
        if current_node is None:
            return -1
        else:
            current_node.height = 1 + max(self._update_heights_aux(current_node.left), self._update_heights_aux(current_node.right))
            return current_node.height

    # Borrowed fns from BST

    def insert(self, key):
        # BST insert
        new_node = Tree_Node(key)
        if self.is_empty():                                     # make root point to the head of the tree (new node)
            self.root = new_node
        else:
            self._insert_aux(self.root, new_node)
        # maintain AVL property
        self.update_heights()
        self.update_balances()
       # self.rebalance()

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

    def get_min(self, start_node=None):
        if not self.is_empty():
            if start_node:
                current_node = start_node       # can specify a start node to search on a particular part of the tree
            else:
                current_node = self.root
            while current_node.left is not None:
                current_node = current_node.left
            return current_node
        else:
            raise Exception

    def get_max(self, start_node=None):
        if not self.is_empty():
            if start_node:
                current_node = start_node
            else:
                current_node = self.root
            while current_node.right is not None:
                current_node = current_node.right
            return current_node
        else:
            raise Exception

    def look_up(self, key):
        """Recursively searches if key is in the tree, returns False if not"""
        if self.is_empty():
            raise Exception
        return self._look_up_aux_rec(self.root, key)

    def _look_up_aux_rec(self, current_node, key, parent=None): # returns parent as well now, less initiative as iterative
        if key < current_node.key:
            if current_node.left is not None:
                parent = current_node
                return self._look_up_aux_rec(current_node.left, key, parent)
            else:
                return False, parent
        elif key > current_node.key:
            if current_node.right is not None:
                parent = current_node
                return self._look_up_aux_rec(current_node.right, key, parent)
            else:
                return False, parent
        else:                                               # current_node.key = key
            return current_node, parent

    def _look_up_aux_itr(self, key):
        """Alternative look up that returns the parent of the
        node (if the node is in the tree) as well"""
        if self.is_empty():
            raise Exception
        current_node = self.root                            # start at root with parent = None
        parent = None
        while current_node is not None:
            if key < current_node.key:                      # search left
                if current_node.left is not None:           # iff left is not None
                    parent = current_node                   # update parent node to current node
                    current_node = current_node.left        # update current node to the left link
                else:
                    raise Exception ('Key not in tree, key: ' + str(key))
                    #return False, parent                    # left is None, item not found, return False, parent
            elif key > current_node.key:                    # search right
                if current_node.right is not None:          # iff right is not None
                    parent = current_node                   # update parent to current node
                    current_node = current_node.right       # update current node to right link
                else:
                    raise Exception ('Key not in tree, key: ' + str(key))
                    #return False, parent                    # right is None, item not found, return False, parent
            else:   # current_node.key == key
                return current_node, parent

if __name__ == "__main__":
    AVL_Tree = AVL_Tree()
    #a = [10, 5, 11, 6, 7, 15]
    a = [10, 5, 4, 3, 12, 11]
    for n in a:
        AVL_Tree.insert(n)
    print(AVL_Tree.get_min())

    """Test AVL Tree before any rotations, making sure b, h values are correct

                                             10 (h=3, b=1)
                                             /             \
                                5 (h=2, b=2)                 12 (h=1, b=1)
                                /       \                    /            \
                    4 (h=1, b=1)         x         11 (h=0, b=0)             x
                    /       \                     /           \
        3 (h=0, b=0)         x                   x            x
        /           \
       x             x
    where x is None (height = -1)
    """
