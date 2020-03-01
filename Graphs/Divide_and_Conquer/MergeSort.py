def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        leftList = arr[:mid]
        rightList = arr[mid:]
        mergeSort(leftList)
        mergeSort(rightList)
        i = 0
        j = 0

        k = 0
        # for reference refer https://www.youtube.com/watch?v=_trEkEX_-2Q
        while i < len(leftList) and j < len(rightList):

            if leftList[i] < rightList[j]:
                arr[k] = leftList[i]
                i += 1
                k += 1
            else:
                arr[k] = rightList[j]
                j += 1
                k += 1

        while i < len(leftList):
            arr[k] = leftList[i]
            i += 1
            k += 1
        while j < len(rightList):
            arr[k] = rightList[j]
            j += 1
            k += 1
    return arr


arr = [12, 3, 4, 5, 7, 8]
print(mergeSort(arr))
