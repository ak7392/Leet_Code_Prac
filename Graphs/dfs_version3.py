


def dfs_stack_recusrion(graph, current_Node=None, explored_nodes={}):
	if graph:
		if not current_Node:
			current_Node = next(iter(graph))

		# print(current_Node)

		explored_nodes[current_Node] = 0
		for next_node in graph[current_Node]:
			if next_node not in explored_nodes: 
				explored_nodes = dfs_stack_recusrion(graph, next_node, explored_nodes)
			elif(explored_nodes[next_node] == 0):
				print("Cycle_detected")

		explored_nodes[current_Node] = 1
		return (explored_nodes)

g  = {
	0: [2,3],
	2: [4,5,6,2],
	3: [],
	4: [],
	5: [],
	6: []
}

print(dfs_stack_recusrion(g))


