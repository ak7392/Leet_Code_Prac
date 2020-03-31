class Solution():
    # For more reference refer this video
    # https://www.youtube.com/watch?v=38JLfQGVlkw&t=13s

    def Minimum_Plaforms(self, arr1: int, arr2: int):

        arrival_time = sorted(arr1)
        departure_time = sorted(arr2)
        platforms = 0
        count = 0
        i = 0
        j = 0

        while i < len(arrival_time):

            # Since train is coming and train present at platform is not departed in that case
            # we check till what time arrival array element is less than departure current element and

            if arrival_time[i] < departure_time[j]:

                # we will keep incrementing the pointer of arrival array till that point
                i += 1
                # keep a count of this in another count variable
                count += 1
                # keep a max of available plaforms which increments with every increment in arrival
                # pointer since new train is coming
                platforms = max(platforms, count)

            else:
                # also we will keep decrementing the count with progrssing departure counter since
                # with every departure time  the new platforms will not be required anymore
                # by taking max of both values we get total platforms.
                count -= 1
                j += 1
        return platforms


arr1 = [900, 940, 950, 1100, 1500, 1800]
arr2 = [910, 1200, 1120, 1130, 1900, 2000]
a = Solution()
print(a.Minimum_Plaforms(arr1, arr2))
