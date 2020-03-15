def Rotated_array_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + (high-low)) // 2

        if low == mid:
            return arr[mid]

        if arr[mid] > arr[high]:
            if target in arr[mid:high]:
                return target

        elif arr[mid] <= arr[high]:
            if target in arr[low:mid]:
                return target

    return False


arr = [4, 5, 6, 7, 1, 3]
print(Rotated_array_search(arr, 2))
