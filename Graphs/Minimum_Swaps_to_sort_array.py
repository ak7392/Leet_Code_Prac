def min_swaps(arr):
    counter = 0
    arr_dict = {}
    length = len(arr)

    for i, item in enumerate(arr):
        arr_dict[item] = i

    checked = [False] * length

    for key, value in sorted(arr_dict.items(), key=lambda x: x[0]):

        if checked[key] or key == value:
            continue

        c_count = 0
        value = key

        while not checked[value]:

            checked[value] = True
            value = arr_dict[value]
            c_count += 1

        counter += c_count - 1
    return counter


arr = [0, 2, 3, 4, 1, 6, 5]
print(min_swaps(arr))
