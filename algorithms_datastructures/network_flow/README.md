# Network flow
> Content from MIT Introduction to Algorithms CLRS & MPC & http://www.math.caltech.edu/~2014-15/1term/ma006a/class14.pdf
- A DAG with edges having non negative capacity.
- `No Reverse Edge`: If there is an edge from `u` to `v` then there must not be an edge from `v` to `u`
- No self loops
- How much stuff can you push from `s (source)` to `t (target)`.

For convenience can assume the graph is connected and for each node `v` there exists some path from `s -> v -> t` 

Formally Let `G=(V, E)` be a flow network (holds above properties) with capacity function `c()`.
A `flow` in `G` is a function `f()` such that:
1. **Capacity constraint**: For all `v, u` in `V` `0 <= f(u, v) <= c(u, v)`
For all `v`, `u` in `V` the edge between them has the `flow` (given by `f(u, v)`) >= 0 and `capacity` (given by `c(u, v)`) is >= flow.
If the edge doesn't exist from node `v` to `u` then the `flow` and `capacity` is 0.
Pretty much means that `flow` is 0 if edge doesn't exist, `capacity` is >= to `flow`.

**TLDR: Flow from 1 node to another must be non negative and can't exceed capacity**

2. **Flow Conservation**: For all `u` in `V - {s, t}` `sum flow(v, u) == sum(flow(u, v)` for all `v` in `V`. 
Pretty much means for all nodes in V the flow from it to any other must equal the `flow`` from the other node to it.
Or the `flow`` between an edge is the same regardless of direction.

**TLDR: Total flow into a node other than source or sink must equal total flow out of that node, flow in == flow out.**

## Cuts
A `cut` partitions the nodes in a `flow network` into two sets `S` and `T` such that `s (source) ∈ S` and `t (target) ∈ T`.

<img src="../../images/networkflow_cut.png" width="500">

## Max Flow == Min Cut
The size of the `minimum cut` is equal to the size of the `maximum flow`

The `minimum cut` is defined as the cost to remove some edges so that we can't get to S anymore.
Cost is usually the sum of max flow of the removed edges.
`max flow <= min cut`

## Models problems such as
- liquid through pipes 
- sending max packages through routes
- assignment

# Variations to vanilla network flow

## Handling anti parallel edges
If there exists two edges `(v1, v2)` and `(v2, v1)` then assumption `(v1, v2)` is in `E` and `(v2, v1)` is not is violated.
These edges are called `anti-parallel`.

**TLDR: two edges are anti-parallel if they are between the same pair of vertices but in opposite directions i.e. v1 -> v2 and v1 <- v2.**

Remove the `anti-parallel` edges, add a new node `v'` such that the edge `(v1, v2)` is replaced by `(v1, v')` and `(v', v2)`

**Pretty much add an edge node and pipe the old edge through it, now the property `no reverse edge` holds.**

## Several Sources and Targets
Add a `super source S` and `super target T`, add an edge from the `super source/target` to the `sources/targets` with infinite capacity.
Then can just run normal algorithm.

<img src="../../images/networkflow_superST.png" width="500">

## Edge-disjoint paths
Given a network flow graph find the maximum number of edge-disjoint paths from `source` to `target`.

**Two paths are edge-independent (or edge-disjoint) if they do not have any internal edge in common.**

Pretty much two paths are `edge-disjoint` if they don't have any of the same edges.
 
1. Assign 1 capacity to each edge (called a `1-0 network`).
2. Do a `max flow`, the max at the `target` is the number of `disjoint-edge paths`.

To get the path, do a `dfs` from `s`, for each edge encountered make capacity 0.

Do number of `disjoint-edge paths` times to get all paths.

If you want only `n` paths extend `t` with another node `T (super sink)` and give the edge in between a capacity of `n` i.e. for 2 paths make the capacity from `t` to `T` `n` and do a `dfs()` from there.

A `1-0 network` will enforce that if an edge is chosen then it can't be used in another path form `s` to `t` hence sovling the problem.

## Vertex-disjoint path
Given a network flow graph find the maximum number of `vertex-disjoint` paths from `s` to `t`.

**Two paths are vertex-independent (alternatively, internally vertex-disjoint) if they do not have any internal vertex in common.**

1. Do vertex splitting by adding an edge b/w each vertex and splitting the vertex into two. 
2. Do `edge-disjoint` paths algorithm.

We split a vertex `v` into two `v_in` and `v_out` with an edge with capacity 1 between them.
This will make the `edge-disjoint` algorithm only pick 1 vertex once for each path from `s` to `t`.

## Disconnecting Edges (min number of edges to disconnect source and target)
Given a graph `G` find the minimum number of edges needed to be removed such that there is no path from `s` to `t`.
 
1. Give every edge capacity 1 to form a `1-0 network`
2. Find `max flow` == max number of `edge-disjoint paths`
3. max number of `edge-disjoint paths` == min edges to disconnect `s` and `t`

<img src="../../images/networkflow_min_disconnecting_edges.png" width="500">

## Undirected graph
> 	
There is algorithm called Ford-Fulkerson algorithm which gives the maximum flow of a flow network in polynomial time, you can look it up in the book Algorithm Design by Kleinberg and Tardos, or even in CLRS.

The only thing you need to do to solve your problem is that you should replace every edge in your undirected grah by two edges backwards and forwards with the same capacity and then solve your problem using the Ford-Fulkerson algorithm. It can be easily proven that in such conversion, flow only propagates through one of the two edges and always one of them is not used.

# Ford-Fulkerson
Relies on 
- residual networks
- augmenting paths
- cuts


Iteratively increase the value of flow. Starting with `f(u, v) = 0` at each iteration increase the flow value in G by finding an `augmenting path` in an associated `residual network G'`.
From knowing edges of an `augmenting path` in `G'` you can easily find corresponding edges in `G` to change to increase the flow. Note increasing overall flow might mean you need to decrease flow on some edge.
Repeatedly augment flow until `residual network` has no more `augmenting paths`.

## Residual networks

Given a flow network `G` it's residual network `G'` are it's edges with capacities that represent how we can change the flow.
An edge in `G'` can emit extra flow of the same edge in `G` - `capacity(edge)`, if it is >= then add it from `G` into `G'` so `G'`
will only have edges that can send more flow. We also add `backwards edges` in `G'` so we can see the effect of not sending flow down a path in `G` and instead investing it elsewhere thus cancelling out the flow sent down the path in `G`.
Sending flow back si the same as decreasing flor on the edge.

## Augmenting path

> An augmenting path is a simple path - a path that does not contain cycles - through the graph using only edges with positive capacity from the source to the sink in the residual network.
Pretty much an `augmenting path` is a positive path from `s` to `t` in `G'` which does the extra flow we can push through edges.
> Given a flow network G D .V;E/ and a flow f, an augmenting path p is a simple path from s to t in the residual network Gf . By the definition of the resid- ual network, we may increase the flow on an edge .u; / of an augmenting path by up to cf .u;  / without violating the capacity constraint on whichever of .u;  / and . ; u/ is in the original flow network G.
> Residual capacity of an edge is the difference between the edge's capacity and its flow  = c(e) - f(e). From this we can construct a residual network, denoted G' which models the amount of available capacity on the set of edges

## Cuts
`Ford-Fulkerson` repeatedly augments flow on augmenting paths until max flow is found.
Due to the `max-flow min-cut` theorem, a flow is maximum iff it's residual network contains no augmenting paths.

Intuitively (not sure if this is right but logic seems sound) the max flow means we pushed as much as possible though `G` thus using up as much as of the possible capacity through edges saturating at least 1 edge in the path from `s` to `t` meaning there is no path from `s` to `t` in `G'`

// pg 720