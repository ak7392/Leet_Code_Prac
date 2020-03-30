def Inversion_count(arr):

    Inversion_count = 0

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                Inversion_count += 1
            else:
                continue
    return Inversion_count


arr = [2, 4, 1, 3, 5]
print(Inversion_count(arr))
