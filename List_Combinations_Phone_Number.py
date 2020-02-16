class Solution: 
	


	def Listpossiblemappings(self, digits: str) -> [str]:

		if len(digits) == 0: 
			return []

		sol = []
		self.dfs(digits, '', sol)

		return sol

	def dfs(self, digits, curr_str, sol):

		if len(digits) == 0: 
			sol.append(curr_str)
			return

		possible_chars = self.number_mapping(digits[0])
		for ch in possible_chars:
			curr_str += ch
			self.dfs(digits[1:], curr_str, sol)
			curr_str = curr_str[:-1]



	def number_mapping(self, digits):

		mapping = {

		'2': 'abc',
		'3': 'def',
		'4': 'ghi',
		'5': 'jkl',
		'6': 'mno',
		'7': 'pqrs',
		'8': 'tuv',
		'9': 'wxyz'
		}

		return mapping[digits]



a = Solution()
print(a.Listpossiblemappings('23'))