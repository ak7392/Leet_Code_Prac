def EAO_2(arr):

    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr[0]
    i = 0
    while i < len(arr)-1:

        if arr[i] == arr[i+1]:
            i = i+2
        else:
            print(arr[i])
        i += 1
