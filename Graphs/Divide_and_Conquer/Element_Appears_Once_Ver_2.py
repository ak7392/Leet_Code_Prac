def EAO_2(arr):

    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr[0]
    i = 0
    result = []
    while i < len(arr)-1:

        if arr[i] != arr[i+1]:
            return (arr[i])
        # elif arr[i] == arr[i+1]:
        #     i += 2
        i += 2

    return arr[i]


arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
print(EAO_2(arr))
