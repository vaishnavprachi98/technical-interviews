"""
@author: David Lei
@since: 28/08/2016
@modified: 

"""

from Concepts.Graphs.Implementations.Adjacency_Matrix import Graph_Matrix

def cycle_in_DAG(graph):
    nodes = graph.get_vertices()
    white = set()
    black = set()
    grey = set()

    for node in nodes:
        white.add(node)

    while len(white) > 0:
        current = white.pop()
        if dfs(current, white, grey, black):
            return True
        return False

    print(nodes)
if __name__ == "__main__":
    my_graph = Graph_Matrix(7)
    # don't need to initialize vertices
    # just edges
    # https://www.youtube.com/watch?v=rKQaZuoUR4M
    my_graph.add_edge(1, 2)
    my_graph.add_edge(2, 3)
    my_graph.add_edge(1, 3)
    my_graph.add_edge(4, 1)
    my_graph.add_edge(4, 5)
    my_graph.add_edge(5, 6)
    my_graph.add_edge(6, 4)

    cycle_in_DAG(my_graph)