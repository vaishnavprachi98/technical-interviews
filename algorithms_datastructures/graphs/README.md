# Basic Graphs

## DFS

Uses a stack, visit the graph nodes by going as deep as possible first.

Time complexity is O(v + e) as we need to visit all nodes and in the worst case iterate through all edges (although might not visit the destination of that edge).

Space complexity is O(v) as we need v extra space for the stack and the output. Dfs will only store as much memory as needed for the longest possible path in the graph, this makes it more memory efficient than bfs.

Worst case space complexity need O(v) nodes on the recursive stack for a linear chain as the graph.

## BFS

Uses a queue, visit the graph nodes by expanding the frontier (reachable nodes) by 1 each time, can use to find shortest path.

Time complexity is O(v + e) as we need to visit all nodes and in the worst case iterate through all edges (although might not visit the destination of that edge).

Space complexity is O(v) as we need v extra space for the queue and the output, it uses more memory as the queue can become very big but dfs uses the recursive stack.

Worst case space complexity need O(v) nodes in the queue for a high branching factor at the root.

## BFS vs DFS

In both worst case == best case as you need to traverse the entire structure.

Dfs uses the computer recursion stack so is generally faster than in memory of your program.

Bfs will queue every node at a fixed depth. If for example you have 1 root node connected to 1000 nodes bfs will enqueue all them while dfs will just recurse once for each edge meaning it will need memory for 1 next node while bfs stores 1000.

Bfs uses more memory when the branching factor is higher.

<img src="../../images/bfs_vs_dfs.png" width="300">

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

Note: This is shortest path from a single source (gets it to every other node). We can run `bellman-ford` `O(V)` times which will be `O(V^2 * E)`, but `E` can go up to `O(V^2)` resulting in `O(V^4)`.
`Floyd-Warshall` can do this in `O(V^3)`

Note: Each iteration of bellman-ford will decrease distance when there is a negative cycle.

## Floyd-Warshall




# Comparisons

