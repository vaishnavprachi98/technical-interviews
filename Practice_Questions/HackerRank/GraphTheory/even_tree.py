"""
a-b-c-d

 	   e1 e2 e3
	e1  
	e2
	e3
"""
class Node:
	def __init__(self, id):
		self.id = id
		self.edges = {}

	def has_edge_to(self, node_id):
		return node_id in self.edges

	def add_edge(self, node_id):
		self.edges[node_id] = node_id
	
	def remove_edge(self, node_id):
		del self.edges [node_id]

no_vert, no_edges = [int(x) for x in input().split()]
verticies = [0] * no_vert
for n in range(no_vert):
	verticies[n] = Node(n + 1)

for e in range(no_edges):
	id_a, id_b = [int(x) for x in input().split()]
	verticies[id_a].add_edge(id_b)
	verticies[id_b].add_edge(id_a)

# Can do in O(n)
# Insight: no edges impacts any other, even before split = even after.

def calculate_tree_vertex_size(current_node, size, nodes, node_dict):
	nodes.append(current_node)
	edge_node_id = current_node.edges
	for node_id in edge_node_id:
		if node_id not in node_dict:
			next_node = verticies[node_id]
			size, nodes = calculate_tree_vertex_size(next_node, nodes)
	return size, nodes
	# find a way to avoid cycles.

def truncate(rest_of_tree, truncate_edge, node_a, node_b):
	# Precondition: Tree has an even number of vertexes.
	size_lhs = calculate_tree_vertex_size()
	size_rhs = calculate_tree_vertex_size()



def explore_path(root_node, connecting_node, tree_verticies_size):
	node_dict = {}
	size = 0
	nodes = []
	edge_nodes = root_node.edges
	for node_id in edge_nodes:
		next_node = verticies[node_id]
		# check cut this
		truncate():


root = verticies[0]

for edge in root.edges:
	# Explore path.


