
class Solution:

from heapq import heappush,heappop

	def __init__(self): 
		self.minheap = []
		self.maxheap = []


	def add_heapdata(self, nums: [int])-> [int]: 
		for i in range(len(nums)):
			if nums[i] % 2 == 1:
				heapq.heappush(self.minheap, nums[i])
				temp = heapq.heappop(self.minheap)
				heapq.heappush(self.minheap, temp)
			else:
				heapq.heappush(self.maxheap, -nums[i])
				temp = heapq.heappop(self.maxheap)
				heapq.heappush(self.maxheap, -temp)

	def MedianFinder(self) -> float:
		if len(self.minheap) == len(self.maxheap):
			return ((self.minheap[0] + self.maxheap[0]) / 2)
		else:
			return (self.maxheap[0])

arr = [12,3,4,5,6,7]

heap = Solution()
heap.add_heapdata(arr)
heap.MedianFinder()

