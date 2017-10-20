# Minimum Spanning Tree

Given a graph with weighted edges, find the mininum spanning tree.

> A minimum spanning tree (MST) or minimum weight spanning tree is a subset of the edges of a connected, edge-weighted undirected graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight

A minimum spanning tree connects all the nodes in the least weight/cost as possible.

## Kruskal's Algorithm

Utilizes distjoint sets.

Key idea:
1. sort all edges with smallest weight first
2. for each edge if the source and destination are not in the same distjoint set then we have not seen that vertex yet
3. merge them and add the edge into the mst
4. else we have already see the vertex and got there with a cheaper edge, do nothing
5. return mst

The complexity of Kruskals is `O(E * log E)`.

We iterate through all edges which is `O(E)`.
We need to join `V` nodes so we need to do operations to check if we should join and join at most `2E` times.
For each check we do
1. Do the source and destination have the same disjoint set? This is 2 `.find()` calls
2. `.union()` if needed.

So for each edge we do 3 disjoint set calls which would be `3 * (ia(V))` so in the edge loop we do `O(E * 3 * (ia(V)))` which is bounded by `O(E)`.

However we sort it first which is `O(E log E)` which bounds our complexity.

## Prim's Algorithm

TODO: This.