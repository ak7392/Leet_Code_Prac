def longest_common_subsequence(arr):
    memo_list = [1 for i in range(len(arr))]
    # print(memo_list)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i] and memo_list[i] + 1 > memo_list[j]:

                memo_list[j] = 1 + memo_list[i]

    return max(memo_list)


arr = [24, 1, 28, 77, 6, 28, 3, 0.40, 5, 35]
print(longest_common_subsequence(arr))
