# Reference  - https://www.youtube.com/watch?v=vH3Ly0GMCQo
class Solution():
    def Inversion_count(self, arr):

        if not arr:
            return 0
        return self.merge_and_count(arr, 0, len(arr)-1)

    def merge_and_count(self, arr, start, end):
        if start >= end:
            return 0

        count = 0
        mid = (start + end)//2

        # Basically we have subdivided our problem into two halves which will further break down
        # to eventually add up to a final solution
        count += self.merge_and_count(arr, start, mid)
        count += self.merge_and_count(arr, mid+1, end)

        left = start
        right = mid + 1

        # Crux of the problem lies  in this solution approach where we are trying to iterate and
        # actually work the logic of comparing the aray left and right.
        while left <= mid and right <= end:
            if arr[left] > arr[right]:
                count += mid - left + 1
                right += 1
            else:
                left += 1

        # here end+1 is given just so we want to include the last element of the array
        # This is not a sorting question hence we will just sort using the simple sorting function
        # by sorting in O(N log N) time complexity.
        arr[start:end+1] = sorted(arr[start:end+1])

        return count


a = Solution()

arr = [2, 4, 1, 3, 5]
print(a.Inversion_count(arr))
