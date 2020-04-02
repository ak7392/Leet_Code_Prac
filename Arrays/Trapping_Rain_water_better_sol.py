def get_rain_water(arr):

    total_water = 0
    Lmax = arr[1]

    for i in range(1, len(arr)-1):

        Lmax = arr[i]
        for j in range(i):
            Lmax = max(Lmax, arr[j])

        Rmax = arr[i]
        for j in range(i, len(arr)):
            Rmax = max(Rmax, arr[j])

        total_water = total_water + (min(Lmax, Rmax) - arr[i])

    return total_water


arr = [7, 4, 0, 9]
print(get_rain_water(arr))
