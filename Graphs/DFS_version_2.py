

#     4
#    / \ 
#   2   3
#  /\   /\ 
# 5 6  7  8

adj_list = {}
adj_list[4] = [2,3]
adj_list[2] = [5,6]
adj_list[3] = [7,8]
adj_list[5] = []
adj_list[6] = []
adj_list[7] = []
adj_list[8] = []


stack = []
visited = []

def dfs(start):

	stack.append(start)

	while len(stack) > 0: 
		cur = stack.pop()
		for neighbour in adj_list[cur]:
			if not neighbour in visited: 
				stack.append(neighbour)
		print(cur)
		visited.append(cur)


dfs(4)

print(visited)

