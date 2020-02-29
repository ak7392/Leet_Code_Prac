def Element_appears_Once(arr):

    if len(arr) == 0:
        return []

    if len(arr) == 1:
        return arr[0]

    dict_ = {}
    result = []
    for item in arr:
        if item in dict_:
            dict_[item] += 1
        else:
            dict_[item] = 1

    for key, value in dict_.items():
        if value == 1:
            result.append(key)
    print(result)


arr = [1, 1, 2, 2, 3, 4, 5, 5]
Element_appears_Once(arr)
