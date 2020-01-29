
class Solution:
	def three_sum(self, nums: [int]) -> [[int]] :

		res = []
		nums.sort()
		length = len(nums)

		for i in range(length - 2):

			if i > 0 and nums[i] == nums[i-1]:
				continue

			l = i +1 
			r = len(nums) - 1

			while l < r:
				total = nums[i] + nums[l] + nums[r]

				if total == 0:

					res.append([nums[i], nums[l], nums[r]])
					l += 1
					r -= 1

					while l < r and nums[l] == nums[l+1]:
						l += 1
					while l < r and nums[r] == nums[r-1]:
						r -= 1

				if total < 0:
					l += 1
					while l < r and nums[l] == nums[l+1]:
						l += 1
				else:
					r -= 1
					while l < r and nums[r] == nums[r-1]:
						r -= 1
		return res


nums = [-1, 2, 3,1,-3,-1]

a = Solution()
print(a.three_sum(nums))





