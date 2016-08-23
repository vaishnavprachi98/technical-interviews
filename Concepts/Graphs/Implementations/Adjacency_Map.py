"""
@author: David Lei
@since: 21/08/2016
@modified:

An optimal implementation of the Graph data structure supporting
- O(1) find edge
- O(1) remove edge
- O(1) add edge
- O(e/v) enumerate edges for node

with space complexity O(e + v)

Based on: Data Structures and Algorithms in Python
I(v) is the incidence collection of v, or vertices whose edges are
incident (connected) to v
"""

from Structures import Vertex, Edge

class Graph:
    def __init__(self, directed=False):
        """Create empty graph (undirected by default)"""
        self.outgoing = {}
        self.incoming = {} if directed else self.outgoing
        # note above line makes self.incoming point to the same thing as outgoing if not directed
        # if it is directed, there will be another dict for it

    def is_directed(self):
        """Return True of this is a directed graph, else False"""
        return self.incoming is not self.outgoing   # directed maps are distinct

    def vertex_count(self):
        return len(self.outgoing)

    def get_vertices(self):
        """Return an iteration of all vertices of the graph"""
        return self.outgoing.keys()

    def edge_count(self):
        """The total number of edges is the len of self.outgoing[v] or len of dict at the index v
        for each vertex in the graph (self.outgoing)"""
        total = sum(len(self.outgoing[v]) for v in self.outgoing)
        """if directed, then each edge is unique, else we have counted twice the amount of
        edges due to the bi-directional nature of undirected graphs"""
        return total if self.is_directed() else total//2

    def get_edges(self):
        """Return the set of all edges in the graph O(e/v) or average number of edges per vertex"""
        result = set()  # avoid double reporting edges of undirected graph
        """outgoing.values() is the list of the adjacency list, however they point to a
        mapping of edges to allow for the better time complexities"""
        for mapped_edges in self.outgoing.values():
            result.update(mapped_edges.values())    # key is the end vertex, values is the edge
        return result

    def get_edge(self, origin, destination):
        """Return the edge form origin to destination or None if not adjacent
        remember that outgoing[origin] is the hashmap (dictionary) of edges incident (adjacent)
        to the vertex origin, they are stored as destination: edge, so get.(destination) will
        give back an edge (or none)
        """
        return self.outgoing[origin].get(destination)

    def degree(self, v, outgoing_edges=True):
        """Return number of (outgoing) edges adjacent to vertex v
        if the graph is directed, optional parameter used ot count incoming edges"""
        adjacent = self.outgoing if outgoing_edges else self.incoming
        # grab our dictionary of outgoing edges and find those outgoing to vertex v
        return len(adjacent[v])

    def get_adjacent_edges(self, v, outgoing_edges=True):
        """Return all (outgoing) edges adjacent to vertex v
        if graph is directed, optional paramter used to reqest incomign edges"""
        adjacent = self.outgoing if outgoing_edges else self.incoming
        output = []
        for edge in adjacent[v].values():   # can use yield edge instead of appeding to a lsit
            output.append(edge)
        return outgoing_edges

    def insert_vertex(self, x=None):
        v = Vertex(x)
        self.outgoing[v] = {}      # create a new dictionary at that 'index' of outgoing (acts as the array in adj list)
        # note that outgoing[v] creates an input into the dictionary outgoing
        if self.is_directed():
            self.incoming[v] = {}
        return v

    def insert_edge(self, origin, destination, x=None):
        """Insert and return a new Edge from origin to destination"""
        e = Edge(origin, destination, x)
        self.outgoing[origin][destination] = e
        self.incoming[destination][origin] = e
        """It is so easy to add an edge!!!!!
        outcoming[origin] is a dictionary for vertices (and edges) adjacent to the origin vertex
        outcoming[origin][destination] is the key, value mapping form the origin vertex to the destination vertex
        and it sets e to be the value of that entry in the dictionary
        """
        return e

    def print_structure(self):
        print("Printing Structure")
        for vertex in self.outgoing:
            print("\nVertex - ", end="")
            print(vertex, end="")
            print(" - name: " + str(vertex.name) + ", rep: " + str(vertex.rep))
            d = self.outgoing[vertex]
            print("Dictionary at this vertex: " + str(d))
            print("     Keys: " + str(d.keys()))
            print("             ", end="")
            for v in d.keys():
                print(v.name, end=" ")
            print("\n     Values: " + str(d.values()))
            print("             ", end="")
            for e in d.values():
                print(e.name, end=" ")
            print()


    def print_graph(self):
        for thing in self.outgoing:
            print(thing.__class__)
            print(thing)
            print("NODE: name-" + str(thing.name) +", rep-" + str(thing.rep))
            b = self.outgoing[thing]
            print(b)
            print(b.__class__)
            print("things on this noode are: ", end=" -- ")
            print(b.values())
            print("\nNEXT\n")

if __name__ == "__main__":
    G = Graph()
    A = G.insert_vertex('A')
    B = G.insert_vertex('B')
    C= G.insert_vertex('C')
    G.insert_edge(A, B, 'e1')
    G.insert_edge(B, C, 'e2')
    G.insert_edge(A, C, 'c1')

    edges = list(G.get_edges())
    verts = list(G.get_vertices())
    for e in edges:
        print(e.name)
    for v in verts:
        print(v.name)

    print(G.get_edge(C, B).name)    # we inserted an edge from B to C as it is undirected by default, the edge
                                    # C to B exists as well!
    print("Testing a directed graph")

    directedG = Graph(True)
    A = directedG.insert_vertex('A')
    B = directedG.insert_vertex('B')
    C= directedG.insert_vertex('C')
    directedG.insert_edge(A, B, 'e1')
    directedG.insert_edge(B, C, 'e2')
    edges = list(directedG.get_edges())
    verts = list(directedG.get_vertices())
    for e in edges:
        print(e.name)
    for v in verts:
        print(v.name)

    print(directedG.get_edge(C, B)) # directed so the edge is only one way!
    print("\nTest print graph\n")
    G.print_graph()
    G.print_structure()
    #G.get_edge(A, B)
    #print(G.get_vertices())
