def Find_All_pairs_target_Sum(arr, target):

    arr.sort()
    left = 0
    right = len(arr) - 1
    result = []

    while left <= right:

        if arr[left] + arr[right] > target:
            right -= 1

        elif arr[left] + arr[right] < target:
            left += 1

        elif arr[left] + arr[right] == target:
            result.append(arr[left])
            result.append(arr[right])
            left += 1
            right -= 1
    return result


arr = [1, 2, 4, 5, 7]
target = 9
print(Find_All_pairs_target_Sum(arr, target))
