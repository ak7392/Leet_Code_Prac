
class Solution:
    def relativeSortArray(self, arr1: [int], arr2: [int]) -> [int]:
        hsh = {}
        result = []
        count = 0
        # this loop populates the dictionary with the number of occurences for each element
        for num in arr1:
            if num in hsh:
                hsh[num] += 1
            else:

                hsh[num] = 1
        # initialise a new list to store the values which exist in both arr2 and arr1
        output = []
        # populate output with the elements multiplied by their occurences (e.g. [1]*2 = [1, 1])
        for elem in arr2:
            output += [elem] * hsh[elem]
        # initialise a new list to store the elements which are in arr1 but not arr2
        extra_output = []
        # populate extra_output with these elements multiplied by their occurences.
        # Note: set(arr1)-set(arr2) provides us with the set of numbers which exist in arr1 but not in arr2
        for elem in set(arr1)-set(arr2):
            extra_output += [elem] * hsh[elem]
        # return the first list and the sorted second list
        return output + sorted(extra_output)


arr1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
arr2 = [2, 1, 8, 3]

a = Solution()
print(a.relativeSortArray(arr1, arr2))
