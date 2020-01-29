import sys

class Solution:
	def three_closest_sum1(self, nums : [int], target: int) -> int:
		
		nums.sort()
		length = len(nums)
		closest_sum = sys.maxsize

		for i in range(length - 2):

			l = i+1
			r = len(nums) - 1

			while(l < r): 

				sum_ = nums[i] + nums[l] + nums[r]

				if abs(target - sum_) < abs(target - closest_sum):
					closest_sum = sum_

				if sum_ > target:
					r -= 1

				else:
					l += 1

		return closest_sum

nums = [1,2,5,3,8,7,9]

a = Solution()
print(a.three_closest_sum1(nums, 4))

