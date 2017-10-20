# Distjoint Set

a.k.a union-find/merge-find set/structure.

A distjoint set keeps track of elements which are split up distjoint (non overlapping) sets.

Each element stores a
- id
- parent pointer
- rank (used for compression)

Elements can be arranged to be visualized as trees but implementation can be in an array where parents are indicated via index.
- if parent pointer doesn't point to something, it is a root
- else element is part of the set of parent

This takes `O(n)` space as we store n nodes in an array.

| Situation   |   Time Average & Worst |
| ----------- | ---------------------- |
| find()      | O(ia(n))               |
| union()     | O(ia(n))               |

In the best case `find()` will be finding a node who is by it self so it is the root so `O(1)`.
For `union()` in the best case with a large input all nodes are roots, so merging two roots is `O(1)`.

where `ia()` is the inverse ackerman function which grows very very slowly.
`O(ai(n))` is better than the iterated logorithm of n `O(log* (n))`

For `m` operations and `n` elements time complexity is `O(m * ia(n))` there is a proof in CLRS for this time complexity
but for practical cases `O(ia(n)) <= 4` so it is bounded by `O(m)` but when we use path compression `m` tends to be small
as we can find roots faster and thus `union()` and `find()` fast.

TLDR: Upper bounded by `O(ia(n))` which is the inverse ackerman function which for what we care about is small so it is fast :)

Inverse ackerman function sources:
- https://xlinux.nist.gov/dads/HTML/inverseAckermann.html
- https://stackoverflow.com/questions/1424303/uses-of-ackermann-function


## Applications

- connected components in undirected graph
    - check if two nodes belong in same component
    - adding an edge will result in a cycle
- kruskal's minimum spanning tree

[Least/Lowest Common Ancestor](https://www.cs.ox.ac.uk/files/2831/union-find-easy.pdf)
<img src="../images/least_common_ancestor_distjoint_set.png" width="800">
