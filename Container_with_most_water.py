
class Solution :
	def max_area(self, hieght:  [int]) -> int:
		left = 0 
		right = len(hieght) - 1
		area = 0
		while (left < right):
			if hieght[left] < hieght[right]:
				area  = max( hieght[left] * (right-left), area)
				left += 1
			else:
				area = max(hieght[right] * (right-left), area)

		return area


hieght = [1,2,3,4,5,6,7,8,9]

a = Solution()
print(a.max_area(hieght))
