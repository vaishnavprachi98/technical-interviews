"""
@author: David Lei
@since: 18/10/2017

"""
from collections import deque
from algorithms_datastructures.trees.tree_node import TreeNode
class BinaryTree:

    def __init__(self):
        self.root = None

    def to_singly_linked_list(self, node):
        """Flatten the binary tree into a singly linked list based on in order traversal."""
        if not node.left and not node.right: # At a leaf.
            return node, None

        # Traverse as far as possible down the left chain.
        if node.left:
            start_left_most, end_left_most = self.to_singly_linked_list(node.left)
            # Add in the current node after the node to the left.
            if end_left_most is None:  # Can only add to the start.
                start_left_most.next = node
            else:  # Occurs at the root.
                end_left_most.next = node
        else:
            # No left child.
            start_left_most = node

        # Traverse as far as possible down the right chain.
        if node.right:
            start_right_most, end_right_most = self.to_singly_linked_list(node.right)
            # Add in current not to point to the start of the right component.
            node.next = start_right_most
        else:
            # No right component.
            start_right_most = node

        return start_left_most, start_right_most

    def get_height(self, node):
        if not node:
            return -1
        return max(self.get_height(node.left), self.get_height(node.right) + 1)

    def insert(self, data):
        """Insert data by creating a new node at the next available space, if root is taken finds the first available
        left/right child, binary tree filled out left to right from top to bottom."""
        if self.root is None:
            self.root = TreeNode(data)
            return

        q = deque([self.root])
        while q:
            node = q.popleft()
            if node.left is None:
                node.left = TreeNode(data)
                node.left.parent = node
                break
            q.append(node.left)
            if node.right is None:
                node.right = TreeNode(data)
                node.right.parent = node
                break
            q.append(node.right)

    def remove(self, key):
        """Remove the first node encountered with the same key, finds a leaf to replace that node with."""
        q = deque([self.root])
        leaves = []
        found_leaf = False
        target_node = None
        target_is_leaf = False
        while q:
            if found_leaf and target_node:
                break
            node = q.popleft()

            if node.key == key and target_node is None:  # Want to remove this node.
                target_node = node  # Even if this is a leaf don't swap it with itself.
                if not node.left and not node.right:
                    target_is_leaf = True
                continue
            if node.left is None and node.right is None:
                leaves.append(node)
                found_leaf = True
            else:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        if not target_node:
            raise KeyError("Node with key/data {0} does not exist in tree.".format(key))
        if target_is_leaf:
            if target_node.parent is None:  # Removing the root.
                self.root = None
                return
            # Update parent of leaf.
            if target_node.parent.left == target_node:
                target_node.parent.left = None
            else:
                target_node.parent.right = None
            return
        # Need to replace with a leaf node, the node to remove is an inner node.
        leaf = leaves[0]
        print("Chosen leaf: " + str(leaf.key))
        # Update the parent of the leaf to erase the leaf.
        if leaf == leaf.parent.left:
            leaf.parent.left = None
        else:
            leaf.parent.right = None

        # Update the node replacing the removed node.
        leaf.parent = target_node.parent
        leaf.left = target_node.left
        leaf.right = target_node.right

        return target_node.key

    def in_order(self, node, accumulator: list) -> list:
        """In order traversal is left then root then right."""
        if node.left:
            self.in_order(node.left, accumulator)
        accumulator.append(node.key)
        if node.right:
            self.in_order(node.right, accumulator)

    def post_order(self, node, accumulator: list) -> list:
        """Post order traversal is left then right then root."""
        if node.left:
            self.post_order(node.left, accumulator)
        if node.right:
            self.post_order(node.right, accumulator)
        accumulator.append(node.key)

    def pre_order(self, node, accumulator: list) -> list:
        """Pre order traversal is root then left then right."""
        accumulator.append(node.key)
        if node.left:
            self.pre_order(node.left, accumulator)
        if node.right:
            self.pre_order(node.right, accumulator)

    def print_tuple(self, node):
        """Prints out tuples of (k: key, l: left.key, r: right.key) making it easier to debug the tree."""
        print("(k: {0}, l: {1}, r: {2})".format(node.key,
                                              node.left.key if node.left else '-',
                                              node.right.key if node.right else '-'))
        if node.left:
            self.print_tuple(node.left)
        if node.right:
            self.print_tuple(node.right)

if __name__ == "__main__":
    numbers = [10, 15, 30, 3, 6, -1, 2, 5, -2, -3, -4, -5, -6, 9, 8]
    binary_tree = BinaryTree()
    for number in numbers:
        binary_tree.insert(number)
    print("Tuple representation of tree")
    binary_tree.print_tuple(binary_tree.root)
    print("\n")

    # Truncate tree to make it match https://www.youtube.com/watch?v=ZM-sV9zQPEs&list=PLrmLmBdmIlpv_jNDXtJGYTPNQ2L1gdHxu
    added_in_leaves = [n for n in numbers if n < 0 and n != -1]
    for negative_number in added_in_leaves:
        binary_tree.remove(negative_number)
    binary_tree.remove(-1)

    print("Tuple representation of tree")
    binary_tree.print_tuple(binary_tree.root)
    print("\n")
    # Now binary tree looks the one in the video.

    in_order_traversal = []
    in_order_traversal_expected = [5, 3, 15, 6, 10, 30, 9, 2, 8]

    post_order_traversal = []
    post_order_traversal_expected = [5, 3, 6, 15, 9, 8, 2, 30, 10]

    pre_order_traversal = []
    pre_order_traversal_expected = [10, 15, 3, 5, 6, 30, 2, 9, 8]

    binary_tree.in_order(binary_tree.root, in_order_traversal)
    binary_tree.post_order(binary_tree.root, post_order_traversal)
    binary_tree.pre_order(binary_tree.root, pre_order_traversal)

    print("Preorder traversal {1} is correct: {0}".format(
        pre_order_traversal == pre_order_traversal_expected, pre_order_traversal))
    print("Postorder traversal {1} is correct: {0}".format(
        post_order_traversal == post_order_traversal_expected, post_order_traversal))
    print("Inorder traversal {1} is correct: {0}".format(
        in_order_traversal == in_order_traversal_expected, in_order_traversal))

    print("Height of binary tree: " + str(binary_tree.get_height(binary_tree.root)))

    print("\nTesting binary tree flattening mutations")
    start, start_of_right = binary_tree.to_singly_linked_list(binary_tree.root)
    current = start
    while current.next is not None:
        print("%s -> " % current.key, end="")
        current = current.next
    print(current.key)