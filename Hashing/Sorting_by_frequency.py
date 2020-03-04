def sorting_items_freq(arr):
    d = {}
    result = []
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    other_output = []

    for i in sorted(d, key=d.get, reverse=True):
        result += [i] * d[i]

    return result
    #+ sorted(other_output)


arr = [9, 9, 1, 2, 5, 5]
print(sorting_items_freq(arr))
