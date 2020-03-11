def Zero_Sum(arr, target):

    result = []
    i = 0
    j = 1

    while j <= len(arr)-2 and i < len(arr)-1:

        if arr[i] + arr[j] < target:
            j += 1

        if arr[i] + arr[j] > target:
            i += 1

        if arr[i] + arr[j] == target:
            new_string = str(arr[i]) + "," + str(arr[j])
            result.append(new_string)
            i += 1
            j += 1

    return result


arr = [6, -1, -3, 4, -2, 2, 4, 6, -12, -7]
target = 0
print(Zero_Sum(arr, target))
