class Solution:
	def minRotated(self, nums: [int]) -> int:
		if len(nums) == 0:
			return 0
		if len(nums) == 1:
			return nums[0]

		i = 0
		j = len(nums)-1			

		while(i<j):

			mid = (i+j) // 2

			if mid > 0 and nums[mid] < nums[mid-1]:
				nums[mid]

			elif (nums[i] <= nums[mid] and nums[mid] > nums[j]):
				i = mid + 1
				print(i)
			else: 
				j = mid - 1 

		return nums[i]

a = [4,5,6,7,0,1,2]
b = Solution()
print(b.minRotated(a)) 


