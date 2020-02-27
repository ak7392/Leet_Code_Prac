def main(): 

# Adjancency List for edges wherever edges or vertex connected mark 1
# in Ajacency List

	# 0 1 2 3 
#0	  0 1 1 0	
#1    0 0 1 0
#2    1 0 0 1
#3    0 0 0 1
	matrix = [[0,1,1,0],
			  [0,0,1,0],
			  [1,0,0,1],
			  [0,0,0,1],
			  ]	
				
	visited = [0,0,0,0]


	stack = [0]

	visited[0] = 1
	node = stack.pop(len(stack)-1)
	print(node)

	while True: 
		for x in range(0, len(visited)): 

			# Check if the route exists and node is not visited 
			if matrix[node][x] == 1 and visited[x] == 0:

				# Visit the node 
				visited[x] = 1

				# Append the element to stack
				stack.append(x)

		# IF the len of stack becomes zero come out of the loop
		if len(stack) == 0:
			break
		# Otherwise Keep on priting Stack nodes until stack length becomes zero
		node = stack.pop(len(stack)-1)
		print(node)



if __name__ == "__main__":
	main()  
