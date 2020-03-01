def mergeSort(arr):

    if len(arr) > 1:
        mid = len(arr)//2
        leftList = arr[:mid]
        rightList = arr[mid:]
        mergeSort(leftList)
        mergeSort(rightList)

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
