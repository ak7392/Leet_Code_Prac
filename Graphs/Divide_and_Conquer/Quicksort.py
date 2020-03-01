def quicksort(arr, lowindex, highindex):
    if lowindex < highindex:
        p = partition(arr, lowindex, highindex)
        quicksort(arr, lowindex, p-1)
        quicksort(arr, p+1, highindex)

    return arr


def partition(arr, lowindex, highindex):
    i = lowindex-1
    pivot = arr[highindex]

    for j in range(lowindex, highindex):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[highindex] = arr[highindex], arr[i+1]
    return i+1


arr = [10, 7, 8, 9, 1, 5]
print(quicksort(arr, 0, len(arr)-1))
