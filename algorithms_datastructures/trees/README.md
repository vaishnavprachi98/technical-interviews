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

### Properties

- **Complete binary tree**: If all levels are filled, with the exception of the last with it being filled left to right.
- **Full/Perfect binary tree**: All levels filled including the last.
- **Depth**: Length of path from the node to the root, it is 0 at the root
- **Height**: Length of path of that node to the lowest leaf, height of the tree is longest path from root to any leaf node.
- **Max number of children at a level**: at level i the max number of children are 2^i as each node can have only 2 children.
- **Nodes in a binary tree**: 2^(h + 1) - 1 where h is the number of levels in the tree, the -1 for level 0 where we just have root.
- **Height of a binary tree given n nodes**: n = 2^(h + 1) - 1 => n + 1 = 2^(h + 1) => log(n + 1) - 1
- **Balanced**: if for each node absolute value of difference between height of left and right subtree <= 1, abs(height_left - height_right) <= 1.
- **Leaves in a complete binary tree**: (n+1)//2 where n is the number of nodes. n is always odd in a complete binary tree. Each level above has 2^i nodes.
    Eg: height = 3m level 0 has 2^0 nodes, level 1 has 2^1 nodes, level 2 has 2^2 nodes, level 3 has 2^3 nodes. The sum of nodes from level 1 to 2 is 7, the nodes on level 3 are 8, (15 + 1 // 2) = 8.

Some [notes on binary trees](https://www.cise.ufl.edu/class/cop3530sp13/lectures/Lecture18.pdf)

Note: For complete binary trees arrays are usually use to implement them.

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

Same as a binary tree but with all nodes to the left of a node <= node and all nodes to the right of it > than node.

Left <= Root < Right

Binary trees are useful because of the L < Root < R property which allows searches, insertions and deletions by the height of the tree.

In the average case the tree is balance and the height is O(log n) and thus searching, deletion and insertion are fast. In the worst case where it forms a linear chain this becomes O(n).

[Balance BST notes](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec06.pdf)

## Traversals

All traversals are O(n) as you need to visit all n nodes.

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