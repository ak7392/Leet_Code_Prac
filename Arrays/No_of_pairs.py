def no_of_pairs(arr1, arr2):
    count = 0
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if pow(arr1[i], arr2[j]) > pow(arr2[j], arr1[i]):
                count += 1
    print(count)


arr1 = [2, 1, 6]
arr2 = [1, 5]
no_of_pairs(arr1, arr2)
