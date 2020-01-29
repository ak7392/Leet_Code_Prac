class Solution:
	def setZeroes(self, matrix : [[int]]) -> None :

		m = len(matrix)
		n = len(matrix[0])

		row_zero = [for  i in range(m)]
		col_zero = [for j in range(n)]

		bool row_zero 
		bool col_zero 

		for i in range(m): 
			for j in range(n):
				if matrix[i][j] == 0:
					row_zero[i] = 'True'
					col_zero[j] =  'True'


		for  i in range(m):
			for j in rnage(n):
				if row_zero or col_zero:
					matrix[i][j] = 0 



a = [[1,1,1],[1,0,1],[1,1,1]]

b = Solution()
b.setZeroes(a)
 