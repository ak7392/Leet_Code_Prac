def Array_sum_div(arr, target):

    found = set()
    output = set()

    for num in arr:
        k = target - num
        if k in found:
            found.add(num)
        else:
            output.add((num, k))

    return output


arr = [4, 1, 2, 5, 3]
target = 6
print(Array_sum_div(arr, target))
