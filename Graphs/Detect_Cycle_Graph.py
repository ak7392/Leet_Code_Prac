	# _ _ 4
	# \  / \
	#   5   8
	#  /\  / \
	# 7  9 12  15

adj_list = {4: [5,8], 5: [4,7,9], 8: [12,15], 9: [], 7: [], 12: [], 15: []}



stack = []
visited = []

def dfs_detect_cycle(start):

	stack.append(start)

	while len(stack) > 0: 
		cur = stack.pop()
		for neighbour in adj_list[cur]:
			if not neighbour in visited: 
				stack.append(neighbour)
		
		
		visited.append(cur)

	return len(set(visited)) < len(visited)


print(dfs_detect_cycle(4))
print(visited)



