# Trees

The focus will be on general trees

## Binary Trees

Binary trees are simply nodes with a left and right pointer (and sometimes parent, it makes things easier).

Common operations on binary trees include:
- traverse()
- insert(key)
- remove(key)
- contains()/has()/search()
- height()/depth()

Extended operations on binary trees include:
- lowest_common_ancestor(key_a, key_b)

### Binary Tree

In binary trees if an operation requires looking at all nodes it is O(n), if you only need to traverse down 1 branch it is O(log n) in the average case where it is balanced but O(n) if it forms a chain.

In a binary tree such as [algorithms_datastructures.trees.binary_tree](./binary_tree.py) the worst case for inserting will require O(n)
as it will try find the node with the first unused leaf which will require you to look at n nodes which are not leaves,
a tighter analysis might suggest it is O(log n) as there will be (n+1)//2 leaves in a complete binary tree so you will find a node to insert
the new node into after n+1 - (n+1)//2 comparisons (the very first leaf not encountered can be used to insert)
and if the tree is not complete it will find the first node with an unused leaf which will occur earlier rather than later but I will treat it as O(n) because I don't want to do the math to figure it out :).

Removing a key just requires you to find the first leaf and to replace it and updating pointers, likewise we can treat it as O(n) in the worst case which requires checking all nodes to see if it matches the key.
Searching is similar to removing.

Best case complexity for inserting and removing will be O(1) if you can insert into a child of the root meaning it formed a chain or if you can remove the root element and there is a leaf on the left of the root
which can be used to replace it. Likewise with search if the root is the key.

Other operations such as height and traversals have worst case == best case as you need to explore all nodes.

Finding the height is O(n) as you need to explore all paths so all nodes which is O(n) nodes.

Tree traversals are `depth first` traversals so O(e + n) applies, since e is just 2 in a binary tree it is O(n). Again this is because you need to explore all nodes.

### Binary Search Tree

## Traversals

### In-Order (l-n-r)

Look at the left side, then the node then the right side.

```python
def in_order(self, node, accumulator: list) -> list:
    """In order traversal is left then root then right."""
    if node.left:
        self.in_order(node.left, accumulator)
    accumulator.append(node.key)
    if node.right:
        self.in_order(node.right, accumulator)
```

### Post-Order (l-r-n)

Look at the left side, then left side then the node.

```python
def post_order(self, node, accumulator: list) -> list:
    """Post order traversal is left then right then root."""
    if node.left:
        self.post_order(node.left, accumulator)
    if node.right:
        self.post_order(node.right, accumulator)
    accumulator.append(node.key)
```

### Pre-Order (n-l-r)

Look at the node first then the left side then the right side.

```python
def pre_order(self, node, accumulator: list) -> list:
    """Pre order traversal is root then left then right."""
    accumulator.append(node.key)
    if node.left:
        self.pre_order(node.left, accumulator)
    if node.right:
        self.pre_order(node.right, accumulator)
```