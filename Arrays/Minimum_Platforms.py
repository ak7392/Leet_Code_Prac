class Solution():
    def Minimum_Plaforms(self, arr1: int, arr2: int):
        p = 0
        q = 0
        d = {}

        # for i in range(len(arr1)):
        #     arr1[i] = int(arr1[i])

        # for j in range(len(arr2[i])):
        #     arr2[j] = int(arr2[j])

        while p < len(arr1) and q < len(arr2):

            if arr1[p] not in d:
                if arr2[q] not in d:
                    d[arr1[p]] = arr2[q]
                    p += 1
                    q += 1
        for key, value in d.items():
            if key > 1200 or value > 1200:
                d[key] = int(key) - 1200
                # d[value] = int(value) - 1200

                base_arrival = min(d.keys())
                base_departure = min(d.values())

        print(base_arrival)
        print(base_departure)


arr1 = [900, 940, 950, 1100, 1500, 1800]
arr2 = [910, 1200, 1120, 1130, 1900, 2000]
a = Solution()
a.Minimum_Plaforms(arr1, arr2)
