import collections

class Node:
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.data)

f = Node("F", None, None)
e = Node("E", None, None)
d = Node("D", None, None)
c = Node("C", e, f)
b = Node("B", d, None)
a = Node("A", b, c)

q = collections.deque()

def print_by_level_iter(root):
	q.append((root, 0))
	table = []
	while q:
		cur_node, cur_node_level = q.popleft()
		# Table len should only ever be < by 1.
		if len(table) - 1 < cur_node_level:
			table.append([]) 
		table[cur_node_level].append(str(cur_node))

		if cur_node.left:
			q.append((cur_node.left, cur_node_level + 1))
		if cur_node.right:
			q.append((cur_node.right, cur_node_level + 1))

	for row in table:
		print(row)


print_by_level_iter(a)
