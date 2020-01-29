class Solution:
	def four_Sum(self, nums: [int], target: int) -> [[int]]:
		
		nums.sort()
		res = []
		length = len(nums)

		for i in range(length-3):

			if i > 0 and nums[i] == nums[i-1]:
				continue

			for j in range(i+1, length-2):
				if j > i+1 and nums[j] == nums[j-1]:
					continue

				l = j+1
				r = len(nums) - 1

				while(l < r): 
					sum_ = nums[i] + nums[j] + nums[l] + nums[r]

					if sum_ > target:
						r -= 1

					elif sum_ < target:
						l += 1

					else:
						res.append([nums[i], nums[j], nums[l], nums[r]])

						while l < r and nums[l] == nums[l+1]: l += 1
						while l < r and nums[r] == nums[r-1]: r -= 1 

						l += 1
						r -= 1
			return res

nums = [1,2,0,1,4,-5,-9,-4,-5,-9,18]

a = Solution()
print(a.four_Sum(nums, 10))

