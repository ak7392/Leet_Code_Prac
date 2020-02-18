class Solution: 
	def Sub_zero(self, arr: [int]) -> [int]: 
		curr_len = 0 
		curr_sum =0
		maxlen = 0
		for i in range(len(arr)):
			curr_sum = 0
			for j in range(i, len(arr)): 

				curr_sum += arr[j]

				if curr_sum == 0: 
					maxlen = max(maxlen, j-i+1)
		print("Max_Length_For_Substring_Assition_to_Zero"+" "+"----->"+" "+str(maxlen))



arr = [1,-2,-4,6,5,11,8]
a = Solution()
a.Sub_zero(arr)