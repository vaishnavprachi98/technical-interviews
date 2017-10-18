# Basic Graphs

## DFS

Uses a stack, visit the graph nodes by going as deep as possible first.

Time complexity is O(v + e) as we need to visit all nodes and in the worst case iterate through all edges (although might not visit the destination of that edge).

Space complexity is O(v) as we need v extra space for the stack and the output. Dfs will only store as much memory as needed for the longest possible path in the graph, this makes it more memory efficient than bfs.

Worst case space complexity need O(v) nodes on the recursive stack for a linear chain as the graph.

```python
def dfs(graph, node, visited, output):
    visited[node.index] = 1
    output.append(node)
    for edge in graph.get_adjacent_edges(node):  # Visit node depth first (go as far as possible) if not already visited.
        if visited[edge.destination.index] != 1:
            dfs(graph, edge.destination, visited, output)
```

## BFS

Uses a queue, visit the graph nodes by expanding the frontier (reachable nodes) by 1 each time, can use to find shortest path.

Time complexity is O(v + e) as we need to visit all nodes and in the worst case iterate through all edges (although might not visit the destination of that edge).

Space complexity is O(v) as we need v extra space for the queue and the output, it uses more memory as the queue can become very big but dfs uses the recursive stack.

Worst case space complexity need O(v) nodes in the queue for a high branching factor at the root.

```python
def bfs(graph, root):
    q = deque([root])
    visited = [0] * len(graph.get_all_vertices())
    output = []
    while q:
        node = q.popleft()
        if visited[node.index] == 0:
            visited[node.index] = 1
            output.append(node)
        for edge in graph.get_adjacent_edges(node):
            next_node = edge.destination
            if visited[next_node.index] == 0:
                q.append(next_node)
    return output
```

## BFS vs DFS

In both worst case == best case as you need to traverse the entire structure.

Dfs uses the computer recursion stack so is generally faster than in memory of your program.

Bfs will queue every node at a fixed depth. If for example you have 1 root node connected to 1000 nodes bfs will enqueue all them while dfs will just recurse once for each edge meaning it will need memory for 1 next node while bfs stores 1000.

Bfs uses more memory when the branching factor is higher.

<img src="../../images/bfs_vs_dfs.png" width="800">

> Wanna find the (strongly/)connected components of the graph? or solve the maze or sudoku? Use DFS. If you look closely, the Pre-Order, Post-Order and In-Order are all variants of the DFS. So, yes, that's some interesting applications.
> BFS if you want to test if a graph is bipartite, find the shortest path between two nodes or applications that require such tasks.

## Dijkstra

> Dijkstra's original variant found the shortest path between two nodes,[2] but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.

## Bellman-Ford
- `O(V * E)`
- single-source shortest paths
- handles negative weights

Given a graph `G = (V, E)` `bellman-ford()` returns a `False` if there is a negative-weight cycle reachable from the source else `True`.
If there is no such cycle then the algorithm will produce the shortest path.

Progressively decrease estimate distance on the weight of a shortest path until actual weight reached
Relax all edges

This translates to:
```
Do for the number of vertexes:
    relax all edges in any order
```

```python
def relax(edge, parents, distance):
    origin = edge.origin
    destination = edge.destination
    cost = edge.weight

    if distance[origin.index] + cost < distance[destination.index]:
        distance[destination.index] = distance[origin.index] + cost
        parents[destination.index] = origin.index

def bellman_ford(graph, source, parents, distance):  # O(V * E)
    distance[source.index] = 0
    # Does work here.
    for node in graph.get_vertices():  # O(V) Can improve this by stopping if nothing changes.
        for edge in graph.get_all_edges():  # O(E)
            relax(edge, parents, distance)
    # One more check to see if there are negative cycles.
    for edge in graph.get_all_edges():
        if distance[edge.destination.index] > distance[edge.origin.index] + edge.weight:
            return False
    return True
```

Note: This is shortest path from a single source (gets it to every other node). We can run `bellman-ford` `O(V)` times which will be `O(V^2 * E)`, but `E` can go up to `O(V^2)` resulting in `O(V^4)`.
`Floyd-Warshall` can do this in `O(V^3)`

Note: Each iteration of bellman-ford will decrease distance when there is a negative cycle.

## Floyd-Warshall

All pairs shortest paths, gives the shortest path between any two pairs.

O(v^3)

```python
def floyd_warshall(graph):  # O(V^3)
    nodes = graph.get_all_vertices()
    num_nodes = len(nodes)
    # Stores shortest path, distances[i][j] is the shortest path from node i to node j.
    # If no path will be inf.
    distances = [[math.inf for _ in range(num_nodes)] for _ in range(num_nodes) ]
    path = [[-1 for _ in range(num_nodes)] for _ in range(num_nodes) ]

    for node in nodes:
        distances[node.index][node.index] = 0  # A node to itself is 0.

    for edge in graph.get_all_edges():  # graph is directed.
        # You can get from origin to destination of an edge with cost the weight of the edge.
        distances[edge.origin.index][edge.destination.index] = edge.weight
        path[edge.origin.index][edge.destination.index] = edge.origin.index

    for k in range(num_nodes):
        # Is going through node k going to give a shorter distance.
        for i in range(num_nodes):
            # Look at node i.
            for j in range(num_nodes):
                # Try get to node j.
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    # Cost to get to node j from i is greater than the cost to get from i to k and then from k to j.
                    # Meaning we found a shorter path going through node k.
                    distances[i][j] = distances[i][k] + distances[k][j]
                    path[i][j] = path[k][j]  # Update path to show shortest path from i to j goes through k to get to j.

    # Check if there is a negative weight cycle, if a diagonal is negative there is a negative weight cycle.
    for i in range(num_nodes):
        if distances[i][i] < 0:
            print("Has negative weight cycle")
            return False, path

    return distances, path
```

# Comparisons

## Topological Sort

Assumes a dag so the graph can not contain a cycle.

Start from any node, explore it's children, once all children have been added to the set we add it the parent node to the stack.

```python
def topological_sort_rec(dag, node, visited, stack):  # Called O(n) times at max.
    print('called')
    if visited[node.index] != 1:
        visited[node.index] = 1
        for edge in dag.get_adjacent_edges(node):  # Explore all children, O(e).
            if visited[edge.destination.index] == 0:
                topological_sort_rec(dag, edge.destination, visited, stack)
        stack.append(node)  # Add node to the stack only once all children explored.

def topological_sort_aux(dag):
    nodes = dag.get_all_vertices()
    visited = [0] * len(nodes)
    stack = deque()

    for node in nodes: # O(n)
        if visited[node.index] == 0:
            topological_sort_rec(dag, node, visited, stack)
    topological_ordering = []
    while stack: # O(n)
        topological_ordering.append(stack.pop().rep)
    return topological_ordering
```

The upper recursive function is called at max O(n) times where n is the number of nodes as we only want to visit each once.
For each node we visit all it's children (bounded by O(e)) and then once it has no more children we add it to the stack.
It is another O(n) to get the values out of the stack.
As we only explore each child once (go down an edge once) and we explore each node it is O(v + e).

Can be seen as a DFS with an extra stack so O(v + e).