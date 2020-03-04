def swapping_elements(arr1, arr2):

    new_sum1 = 0
    new_sum2 = 0
    k = False
    for i in arr1:
        for j in arr2:

            new_sum1 = new_sum1 - i + j
            new_sum2 = new_sum2 - j + i

            if new_sum1 == new_sum2:
                value1 = i
                value2 = j

                k = True

            if k:
                break

    return arr1[value1], arr2[value2]


arr1 = [4, 1, 2, 1, 1, 2]
arr2 = [3, 6, 3, 3]
print(swapping_elements(arr1, arr2))
