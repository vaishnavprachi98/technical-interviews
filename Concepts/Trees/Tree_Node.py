"""
@author: David Lei
@since: 22/08/2016
@modified: 

"""

class Tree_Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.extra_data = None          # can hold any info I forgot to add
        self.left = left
        self.right = right
        self.height = -1                # assume it's a leaf
        self.colour = None              # can use for red/black implementation
        self.balance = 0
