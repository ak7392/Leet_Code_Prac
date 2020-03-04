def common_elements(arr1, arr2, arr3):
    # dic = {}
    # result = []
    # for i in arr1:
    #     if i not in dic:
    #         dic[i] = 1

    # for i in arr2:
    #     if i not in dic:
    #         dic[i] = 1

    # for i in arr3:
    #     if i not in dic:
    #         dic[i] = 1

    # for key in dic.keys():
    #     result.append(key)
    # print(result)

    print(list(set(arr1) & set(arr2) & set(arr3)))


arr1 = [1, 2, 2, 3, 4, 8]
arr2 = [2, 3, 4, 6]
arr3 = [4, 9]
common_elements(arr1, arr2, arr3)
