class Solution: 

	def sub_zero(self, arr: [int]) -> int:

		hash_map = {} 

		curr_sum = 0

		max_len = 0

		for i in range(len(arr)): 

			curr_sum += arr[i]

			if arr[i] == 0 or max_len == 0: 

				max_len = 0

			if curr_sum == 0:

				max_len = i + 1

			if curr_sum in hash_map: 

				max_len = max(max_len, i - hash_map[curr_sum])

			else: 

				hash_map[curr_sum] = i 

		print(max_len)


arr = [10, 5, 20, -20, 15, -15, 30, -25,-4, -1]

a = Solution()

a.sub_zero(arr)


