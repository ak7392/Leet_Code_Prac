adjc_List = {}
adjc_List['a'] = ['d']
adjc_List['b'] = ['d']
adjc_List['c'] = ['e']
adjc_List['d'] = ['e']
adjc_List['f'] = ['b']
adjc_List['g'] = ['b']
adjc_List['e'] = []



visited = {}
visited['a'] = False
visited['b'] = False
visited['c'] = False
visited['d'] = False
visited['e'] = False
visited['f'] = False
visited['g'] = False
output_stack = []

def topological_sort(vertex):
	

	if not visited[vertex]:
		visited[vertex] = True 

		for neighbour in adjc_List[vertex]:
			topological_sort(neighbour)
		
		output_stack.insert(0, vertex)



for vertex in visited:
	(topological_sort(vertex))


print(output_stack)





