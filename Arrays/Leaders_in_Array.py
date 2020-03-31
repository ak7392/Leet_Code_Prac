def Leaders_in_Array(arr):

    n = len(arr)
    temp = []
    # For more optimized solution refer below Link
    # https://www.geeksforgeeks.org/leaders-in-an-array/
    for i in range(0, n):

        temp.append(arr[i])
        if arr[i-1] > arr[i]:
            for j in temp:
                if j > arr[i-1]:
                    max_temp = j
                else:
                    continue

    return max_temp


arr = [16, 17, 4, 3, 5, 2]
print(Leaders_in_Array(arr))
