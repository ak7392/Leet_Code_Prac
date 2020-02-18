class Solution:
    def relativeSortArray(self, arr1: [int], arr2: [int]) -> [int]:
        hsh = {}
        result = []
        count = 0
        for num in arr1: 
            if num in hsh:
                hsh[num] += 1
            else:
                
                hsh[num] = 1
        
        for i in arr1:
            for key, value in hsh.items():
                if key == i:
                    while value <= hsh[key]:
                        result.append(key)
        return result


arr2 = [1,2,3,4,5,6,6,8]
arr1 = [4,5,6,8,3,2,1]

a = Solution()
print(a.relativeSortArray(arr1, arr2))