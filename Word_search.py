class Solution:
	def exist(self, board : [[str]], word : str) -> bool:

		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.dfs(board, i, j, word):
					return True
		return False


	def dfs(self, board, row, col, word):

		if len(word) == 0 :
			return True

		if row < 0 or row >= len(board) or col < 0 or col > len(board[0]) or board[row][col] != word[0]:
			return False



		temp = board[row][col] 
		board[row][col] = ''

		result = self.dfs(board, row + 1, col, word[1:]) or self.dfs(board, row - 1, col, word[1:]) or self.dfs(board, row , col + 1, word[1:]) or self.dfs(board, row , col - 1, word[1:])

		board[row][col] = temp

		return result


a = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E']]
c =  "ABCB"

b = Solution()
print(b.exist(a,c))