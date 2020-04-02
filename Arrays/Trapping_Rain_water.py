def trapping_rain_water(arr):

    left = 0
    right = len(arr)-1
    max_area = 0

    while True:

        if left == right:
            break

        if arr[left] < arr[right]:

            max_area = max(max_area, arr[left] * (right - left) + 1)
            left += 1

            for i in arr[left:right]:
                max_area -= i

        else:

            max_area = max(max_area, arr[right] * (left - right) + 1)
            right -= 1

            for i in arr[left:right]:
                max_area -= i

    return max_area


arr = [7, 4, 0, 9]
arr2 = [3, 0, 0, 2, 0, 4]
print(trapping_rain_water(arr))
print(trapping_rain_water(arr2))
