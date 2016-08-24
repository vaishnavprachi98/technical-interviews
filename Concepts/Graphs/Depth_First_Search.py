"""
@author: David Lei
@since: 21/08/2016
@modified: 

How it works
    Depth = go deeper = stack (LIFO)


    ///
        - explore neighbour nodes first
        - then move on to a deeper level

        1. Start with an empty Queue
        2. Initialize each node to have infinity distance
        3. Visit a node, current node = node visited, add it to the output
        4. Loop while not all nodes visited
            5. Visit all nodes you can from current node and Enqueue them and add them to output
            6. When you can't visit anymore, current node = Deque Q
            repeat until finished
        note: if stalemate in picking node pick in alphabetical order

Time complexity: O(v + e)
    - need to look at each node
    - for a given current node, we look at all adjacent edges (eventually look at all edges)
    O(v + e) as we look at all edges and nodes
    O(e) wil at most be O(v^2) and at least O(1)


Space complexity: O(v)
    - output array
    - queue
    both are of the size of the number of nodes = O(2v) = O(v)

Can use to traverse trees or graphs

Note: order you put things in dict isn't always reflected in output, so if i keep running this bfs result on
graph_map might change
http://stackoverflow.com/questions/4458169/in-what-order-does-python-display-dictionary-keys
"The order has to do with how they work internally and what order they end up in the hashtable.
That in turn depends on the keys hash-value, the order they were inserted, and which Python implementation you are using.
The order is arbitrary (but not random) and it will never be useful to know which order it will be."
"""