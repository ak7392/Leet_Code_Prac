class Solution:

	def numIslands(self, grid):

		count = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == '1': 
					self.dfs_explore(grid, i, j)

					count += 1

		return count


	def dfs_explore(self, grid, i, j):

		if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
			return 
		grid[i][j] = '#'
		self.dfs_explore(grid, i+1, j)
		self.dfs_explore(grid, i-1, j)
		self.dfs_explore(grid, i, j+1)
		self.dfs_explore(grid, i, j-1)


grid = [['1','1','0','1'],
		['0','1','0','0'],
		['0','0','0','0'],
		['1','0','1','1'],
		['1','1','1','1']
		]

a = Solution()

print(a.numIslands(grid))
