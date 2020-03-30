def merge_sorted_arrays(arr1, arr2):
    result = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i = i+1
        else:
            result.append(arr2[j])
            j = j+1
    if arr2:
        while j < len(arr2):
            result.append(arr2[j])
            j = j+1
    if arr1:
        while i < len(arr1):
            result.append(arr1[i])
            i = i+1

    print(result)


arr1 = [1, 3, 5, 7, 10, 11, 12]
arr2 = [0, 2, 6, 8, 9]
merge_sorted_arrays(arr1, arr2)
