"""
@author: David Lei
@since: 23/08/2016
@modified: 

Based Vertex and Edge clases
- a bit too generic too be honest
- should be speific for use
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

    def to_string(self, ends_vertex_obs = False):
        if ends_vertex_obs:
            return "og: " + str(self.origin.name) + " to: " + str(self.destination.name)
        return "og: " + str(self.origin) + " to: " + str(self.destination)
