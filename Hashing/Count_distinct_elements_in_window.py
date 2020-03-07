def count_window_distinct(win, k):

    dist_count = 0
    for i in range(k):

        j = 0
        while j < i:

            if win[j] == win[i]:
                break
            else:
                j += 1

        if j == i:
            dist_count += 1
    return dist_count


def count_elements_from_array_windows(arr, n, k):

    for i in range(n - k + 1):

        return (count_window_distinct(arr[i:k+i], k))


arr = [1, 2, 1, 3, 4, 2, 3]
n = len(arr)
k = 2
print(count_elements_from_array_windows(arr, n, k))
