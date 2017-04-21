"""
@author: David Lei
@since: 21/04/2017
@modified: 

"""

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)
