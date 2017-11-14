"""
@author: David Lei
@since: 21/10/2017

-1,2-
-3,5,4,0-
            0    1   2  3  4   5
left   = [4 , -1, 1, -1, 5,  3]
right = [-1, 2, -1, 5,  0,  4]
"""
class Node:
    def __init__(self, id, left, right):
        self.id = id
        self.left = left
        self.right = right

left = [4 , -1, 1, -1, 5,  3]
right = [-1, 2, -1, 5,  0,  4]
node_coords = zip(left, right)

nodes = []
for index, lr in enumerate(node_coords):
    l, r = lr
    node = Node(index, l, r)
    nodes.append(node)

for node in nodes:
    if node.left != -1:
        node.left = nodes[node.left]
    if node.right != -1:
        node.right = nodes[node.right]

potential_heads = [n for n in nodes if n.left == -1]

if len(potential_heads) > 1:
    current = potential_heads[0]
    linked_list_counter = 1
    while True:
        while current.right != -1:  # traverse linked list.
            current = current.right
        # end point of linked list.
        current.right = potential_heads[linked_list_counter]
        potential_heads[linked_list_counter].left = current
        linked_list_counter += 1
        if linked_list_counter >= len(potential_heads):
            break

# Traverse the first node print out values.
current = potential_heads[0]
print("-", end="")
while current != -1:
    print(current.id, end="")
    current = current.right
print("-")
