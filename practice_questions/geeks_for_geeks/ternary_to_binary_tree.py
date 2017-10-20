"""
@author: David Lei
@since: 21/10/2017

http://www.geeksforgeeks.org/convert-ternary-expression-binary-tree/
"""

class Node:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.right = None

# I get the idea but im so tired, redo later.
def ternary_to_binary_tree(string):
    stack = []
    nodes = []
    for char in string:
        if char == "?":
            new_node = Node(char)
            parent = stack.pop()
            parent.left = new_node
            stack.append(parent)
            stack.append(new_node)
        elif char == ":":
            new_node = Node(char)
            stack.pop()
            parent = stack.pop()
            parent.right = new_node
            stack.append(parent)
            stack.append(new_node)
        else:
            new_node = Node(char)
            stack.append(new_node)
            nodes.append(node)