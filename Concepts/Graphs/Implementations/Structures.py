"""
@author: David Lei
@since: 23/08/2016
@modified: 

"""
class Vertex:
    def __init__(self, x=None, point=None, rep=None):
        self.name = x                                   # integer 'name' or index
        self.pointer = point                            # points to a linked list in adjacency list
        self.rep = rep                                  # string representation


class Edge:
    def __init__(self, origin, destination, x=None, weight=None,):
        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.name = x

    def get_endpoints(self):
        return self.origin, self.destination

    def get_opposite(self, vertex):
        """Return the vertex that is opposite v on this edge"""
        return self.destination if vertex is self.origin else self.origin

