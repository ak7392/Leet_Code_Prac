def rearrange_array(arr):
    result = []
    temp1 = max_elem = max(arr)
    temp2 = min_elem = min(arr)
    temp1 -= 1
    temp2 += 1

    result.append(max_elem)
    result.append(min_elem)
    index1 = arr.index(max_elem)
    index2 = arr.index(min_elem)

    arr.pop(index1)
    arr.pop(index2)

    dic = {}

    for i in arr:
        if i not in dic:
            dic[i] = 1
    print(dic)
    i = 0

    while i < len(arr):
        if temp1 in dic:
            result.append(temp1)
            temp1 -= 1
            i += 1

            if temp2 in dic:
                result.append(temp2)
                temp2 += 1
                i += 1

    return result


arr = [1, 2, 3, 4, 5, 6]
print(rearrange_array(arr))
