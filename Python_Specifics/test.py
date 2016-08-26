__author__ = 'David'

'''
AVL tree implementation based on
Algo Data Structures in JAVA text book kinda not really.
'''
# AVL Node ------------------------------------------------------
class AVLNode:
    def __init__(self, data, left, right):
        self.key = data
        self.left = left
        self.right = right
        self.height = 0

    def return_height(self):
        return self.height
# AVL Tree ------------------------------------------------------
class AVLTree:
    def __init__(self):
        self.node = None
        # empty = -1
        # root = 0
        # 1 child = 1
        self.height = -1
        self.balance = 0

    def insert_aux(self,data):
        #node = self.root
        self.insert(data)

    def insert(self, key):

        new_node = AVLNode(key,None,None)

        if self.node:

            # insert left
            if key < self.node.key:
                self.node.left.insert(key)
            # insert right
            elif key > self.node.key:
                self.node.right.insert(key)
        else:
            self.node = new_node
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        self.reBalance()
        # check if we need to change tree after inst to keep AVL property

    def checkHeight(self):
        if self.node:
            if self.node.left:
                self.node.left.checkHeight()
            if self.node.right:
                self.node.right.checkHeight()
            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else:
            self.height = -1

    def reBalance(self):
        # checks bal of tree
        # update first
        self.checkHeight()
        self.checkBalance()
        #print(self.balance)

        while abs(self.balance) >1:
            # left > right
            if self.balance > 1:

                # left - right case --> inside - double r
                if self.node.left.balance < 0:  # right heavy

                    self.node.left.leftRotation()
                    self.checkHeight()
                    self.checkBalance()
                # left - left case --> outside - single r
                self.rightRotation()
                self.checkHeight()
                self.checkBalance()

            # right > left
            if self.balance < -1:
                # right - left case --> inside - double r
                if self.node.right.balance > 0:
                    self.node.right.rightRotation()
                    self.checkHeight()
                    self.checkBalance()
                # right - right case --> outside - single r
                self.leftRotation()
                self.checkHeight()
                self.checkBalance()

    def checkBalance(self):
        if self.node:
            if self.node.left:
                self.node.left.checkBalance()
            if self.node.right:
                self.node.right.checkBalance()
            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def rightRotation(self):
        tmp = self.node.left.node
        nLeft = tmp.right.node
        previous = self.node
        self.node = tmp
        previous.left.node = nLeft
        tmp.right.node = previous

    def leftRotation(self):
        tmp = self.node.right.node
        nLeft = tmp.left.node
        previous = self.node
        self.node = tmp
        previous.right.node = nLeft
        tmp.left.node = previous

    def search_aux(self,key):
        current = self.node
        #self.search(key, current)
        self.search(key)
        #print(self.root.key)

    def search(self, key):

        if self.node is None:
            print("not found")
        elif key < self.node.key:
            print(self.node.key, end=" -> ")
            return self.node.left.search(key)
        elif key > self.node.key:
            print(self.node.key, end=" -> ")
            return self.node.right.search(key)

        elif key == self.node.key:
            print(key, end="!")
# lab functions ------------------------------------------------------
def insert_avl_array(A):
    tree = AVLTree()

    for i in A:
        tree.insert_aux(i)
    search_avl_print(6,tree)

def search_avl_print(k,T):
    T.search_aux(k)

def main(filename='5_numbers'):
    try:
        filename += '.txt'
        file = open(filename, 'r')
        text = file.read()
        inputArray = text.split()
        for i in range(len(inputArray)):
            inputArray[i] = int(inputArray[i])
        insert_avl_array(inputArray)

    except FileExistsError:
        print("File not found")
    except ValueError:
        print("not all items in txt file are numbers")

if __name__ == "__main__":
    main()
