def All_Pair_Sum(arr, target):
    result = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            arr_new = []
            if arr[i]+arr[j] == target:
                arr_new.append(arr[i])
                arr_new.append(arr[j])
                result.append(arr_new)

    return result


arr = [1, 2, 4, 5, 7]
target = 9
print(All_Pair_Sum(arr, target))
