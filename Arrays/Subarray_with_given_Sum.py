
def sub_sum(array, target):
    i = 0
    j = i+1
    length = len(array)
    temp_sum = 0
    temp = []
    result = []

    while i < length-1 and j < length-1:

        temp_sum += array[i] + array[j]

        if temp_sum < target and i > 0 and j > 0:
            j += 1
            temp_sum = 0
            continue

        elif temp_sum == target and i > 0 and j > 0:
            print(i-j)
            for i in array[i:j]:
                temp.append(i)
            result.append(result)
            temp_sum = 0
            i += 1
            j += 1
            continue

        elif temp_sum > target and i > 0 and j > 0:
            temp_sum = 0
            i += 1
            continue
    return result


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sub_sum(array, 7))
