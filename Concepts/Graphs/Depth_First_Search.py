"""
@author: David Lei
@since: 21/08/2016
@modified: 

How it works
    Depth = go deeper = stack (LIFO)

        - explore children as far as possible (keep going until you reach a dead end)
        - update current_node with something that has a path you haven't visited yet and do that

        1. Start with an empty Stack
        2. Initialize each node to have infinity distance
        3. Add root node to the stack
        4. While nodes in stack
            5. current_node = pop stack
                5.a if we haven't seen current_node before (distance="infi")
                    - 'visit' it (distance=0)
                    - add it to output
            6. Loop for each destination node for each incident edge to current_node (for each adjacent node)
                - put the adjacent node on the stack
        repeat process

                  B
                 /
            eg: A
                 \
                  S - C - D
        first push A, in the for each incident edge loop where A is the current node, we will push B and S
        then pop C
        note: if stalemate in picking node pick in alphabetical order

Time complexity: O(v + e)
    - need to look at each node (v)
    - for a given current node, we look at all adjacent edges (eventually look at all edges)
    O(v + e) as we look at all edges and nodes
    O(e) wil at most be O(v^2) and at least O(1)

    note: used aggregate analysis as even though
        loop for all v
            loop for all e to v
        could be assumed to be O(ve), we know that when we execute we will only look at
        all edges in the graph overall and not at each iteration so O(v + e) but e can be at most v^2 leading to O(v^2)



Space complexity: O(v)
    - output array
    - stack
    both are of the size of the number of nodes = O(2v) = O(v) for iterative version

    recursive version can have worst case space O(height)

Can use to traverse trees or graphs
"""
from Linked_Stack import LinkedStack

def depth_first_search_rec_driver(G, root, use_rep=False):
    nodes = G.get_vertices()
    for node in nodes:
        node.distance = "Infinity"
    output = []
    depth_first_search_recursive(G, root, output, use_rep)
    return output

def depth_first_search_recursive(G, node, output, use_rep=False):
    node.distance = 0                               # discovered
    if use_rep:
        output.append(node.rep)
    else:
        output.append(node.name)
    edges_incident = G.get_adjacent_edges(node)
    for edge in edges_incident:
        if edge.destination != node:                # depending on the way we create the edge we need to check for this
            destination_node = edge.destination     # assuming no loops to same node
        else:
            destination_node = edge.origin
        if destination_node.distance == "Infinity":
            depth_first_search_recursive(G, destination_node, output, use_rep)


def depth_first_search_iterative(G, root, use_rep=False):

    nodes = G.get_vertices()
    for node in nodes:
        node.distance = "Infinity"

    S = LinkedStack()
    #root.distance = 0
    S.push(root)
    output = []
    while not S.is_empty():
        current_node = S.pop()                          # update current node

        if current_node.distance != 0:                  # current_node is not discovered
            current_node.distance = 0                   # we have now discovered the current_node
            if use_rep:                                 # add a representation of node to output
                output.append(current_node.rep)
            else:
                output.append(current_node.name)        # add current node to our output

            edges_incident = G.get_adjacent_edges(current_node)
            for edge in edges_incident:
                if edge.destination != current_node:
                    destination_node = edge.destination # get node you can get to from current
                else:
                    destination_node = edge.origin      # depending on how we add edges
                S.push(destination_node)                # push destination on to stack
        # implicit else for a node we have already seen
    #print(output)
    return output

def test_dictionary_adj_map_output():
    for i in range(5):
        from Concepts.Graphs.Implementations.Adjacency_Map import Graph_Map
        from Concepts.Graphs.Implementations.Adjacency_List import Graph_List

        # example from https://en.wikipedia.org/wiki/Depth-first_search
        # iterative version correct order: A, E, F, B, D, C, G
        # recursive version correct order: A, B, D, F, E, C, G (went to D first instead of F)
        # this is also a correct dfs ordering: A, B, F, E, D, C, G
        # each of them follow what dfs does which is exploring as far as possible along each branch before back tracking

        graph_map = Graph_Map()
        # set up adj map graph
        A = graph_map.add_vertex('A')
        B = graph_map.add_vertex('B')
        C = graph_map.add_vertex('C')
        D = graph_map.add_vertex('D')
        E = graph_map.add_vertex('E')
        F = graph_map.add_vertex('F')
        G = graph_map.add_vertex('G')
        graph_map.add_edge(A, B)
        graph_map.add_edge(A, C)
        graph_map.add_edge(A, E)
        graph_map.add_edge(B, D)
        graph_map.add_edge(B, F)
        graph_map.add_edge(C, G)
        graph_map.add_edge(E, F)
        source = A
        dfs1 = depth_first_search_iterative(graph_map, source)
        print("DFS on adj_map graph (iterative): " + str(dfs1))
        # possible outputs:
        # example graph based on https://en.wikipedia.org/wiki/Depth-first_search
        # DFS on adj_map graph (iterative): ['A', 'B', 'D', 'F', 'E', 'C', 'G'], recursive correct form wiki
        # DFS on adj_map graph (iterative): ['A', 'E', 'F', 'B', 'D', 'C', 'G'], iterative correct fro wiki
        # DFS on adj_map graph (iterative): ['A', 'B', 'F', 'E', 'D', 'C', 'G'], correct
        # DFS on adj_map graph (iterative): ['A', 'C', 'G', 'E', 'F', 'B', 'D'], correct


        # due to randomness with {} sometimes we get a different order using a adj map

if __name__ == "__main__":
    from Concepts.Graphs.Implementations.Adjacency_Map import Graph_Map
    from Concepts.Graphs.Implementations.Adjacency_List import Graph_List

    # recursive version correct order: A, B, D, F, E, C, G (went to D first instead of F)
    # this is also a correct dfs ordering: A, B, F, E, D, C, G
    # each of them follow what dfs does which is exploring as far as possible along each branch before back tracking

    graph_map = Graph_Map()
    # set up adj map graph
    A = graph_map.add_vertex('A')
    B = graph_map.add_vertex('B')
    C = graph_map.add_vertex('C')
    D = graph_map.add_vertex('D')
    E = graph_map.add_vertex('E')
    F = graph_map.add_vertex('F')
    G = graph_map.add_vertex('G')
    graph_map.add_edge(A, B)
    graph_map.add_edge(A, C)
    graph_map.add_edge(A, E)
    graph_map.add_edge(B, D)
    graph_map.add_edge(B, F)
    graph_map.add_edge(C, G)
    graph_map.add_edge(E, F)
    source = A
    dfs1_itr = depth_first_search_iterative(graph_map, source)
    dfs1_rec = depth_first_search_rec_driver(graph_map, source)
    print("DFS on adjacent map, sometimes different order (all correct, check against 4 solns in test()")
    print("DFS on adj_map graph (iterative): " + str(dfs1_itr))
    print("DFS on adj_map graph (recursive): " + str(dfs1_rec))

    """ Note
    due to randomness with {} sometimes we get a different order using a adj map
    however they are all correct orderings by picking arbitrary adjacent nodes
    see the tests below
    """

    print("Test")
    test_dictionary_adj_map_output()

    print("\nDFS on adjacent list")
    graph_list = Graph_List(7)
    # set up adj map graph, slightly different set up due to diff underlying structure
    a = graph_list.add_vertex(0,'A')
    b = graph_list.add_vertex(1,'B')
    c = graph_list.add_vertex(2,'C')
    d = graph_list.add_vertex(3,'D')
    e = graph_list.add_vertex(4,'E')
    f = graph_list.add_vertex(5,'F')
    g = graph_list.add_vertex(6, 'G')
    # this is directed
    graph_list.add_edge(a, b)
    graph_list.add_edge(a, c)
    graph_list.add_edge(a, e)
    graph_list.add_edge(b, f)
    graph_list.add_edge(b, d)
    graph_list.add_edge(c, g)
    graph_list.add_edge(e, f)

    graph_list.add_edge(b, a)
    graph_list.add_edge(c, a)
    graph_list.add_edge(e, a)
    graph_list.add_edge(f, b)
    graph_list.add_edge(d, b)
    graph_list.add_edge(g, c)
    graph_list.add_edge(f, e)
    source2 = a

    dfs2_itr = depth_first_search_iterative(graph_list, source2, use_rep=True)
    print("DFS on adj_list graph (iterative): " + str(dfs2_itr))
    dfs2_rec = depth_first_search_rec_driver(graph_list, source2, use_rep=True)
    print("DFS on adj_list graph (recusrive): " + str(dfs2_rec))

    # all correct