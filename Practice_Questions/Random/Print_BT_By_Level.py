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

# # TODO: this

# def print_by_level_recursive_aux(root):
# 	q = collections.deque()
# 	level = 0
# 	root = root
# 	print_by_level_recursive(q, root, level)

# def print_by_level_recursive(q, root, level):
# 	if not q:
# 		return

# 	cur_node = q.popleft()
# 	if cur_node.left:
# 		q.append(cur_node.left)
# 	if cur_node.right:
# 		q.append(cur_node.right)

# 	print_by_level(q, cur_node, level + 1)




# def recursive_print_bst(root, , currentLevel, level):
# 	if(current_node.left == None and currentLevel = level and current_node.right == None):
# 		print(current_node)
# 		return current_node
# 	else:
# 		nextNodeLeft = current_node.left
# 		nextNodeRight = current_node.right
# 		recursive_print_bst(nextNodeLeft, currentLevel, level+1)
# 		recursive_print_bst(nextNodeRight, currentLevel, level+1)
# 		currentLevel += 1



# def s():
# 	print("a", end="")
# 	print("b", end="")
# 	print(("\n"*1)+"c", end="")
# 	print("z",end="")
# 	print()

