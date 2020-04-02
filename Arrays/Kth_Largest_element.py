import heapq


class Solution():

    def Kth_largest_element(self, nums, k):

        heap = []

        for x in nums:
            heapq.heappush(heap, x)

        for _ in range(k):
            res = heapq.heappop(heap)

        return res


a = Solution()
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(a.Kth_largest_element(arr, 4))
