def array_sum_divisibility(arr, target):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] + arr[j]) % target == 0:
                result.append(arr[i])
                result.append(arr[j])
            else:
                continue

    return result


arr = [91, 74, 66, 48]
target = 4
print(array_sum_divisibility(arr, target))
