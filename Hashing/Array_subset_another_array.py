def Array_Subset_of_another_array(arr1, arr2):

    # max_array = [True] * [max(len(nums1), len(nums2))]
    dic = {}
    for i in arr1:
        if i not in dic:
            dic[i] = 1
        else:
            break

    for i in arr2:
        if i not in dic:
            dic[i] = 1
        else:
            continue

    for key in dic.keys():
        if key in arr1 and arr2:
            arr1.remove(key)
            arr2.remove(key)

    if len(arr1) == 0 or len(arr2) == 0:
        return True
    else:
        return False


arr1 = [1, 2, 8, 6, 9]
arr2 = [1, 2, 3, 7, 8, 10, 12, 6, 4, 9]

print(Array_Subset_of_another_array(arr1, arr2))
