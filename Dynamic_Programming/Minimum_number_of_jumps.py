def longest_increasing_subsequence(arr):

    n = len(arr)

    dp = [n+2 for i in range(n)]

    result = 0

    for i in range(n):

        for j in range(1, arr[i]+1):

            if i+j < n and dp[i+j] > dp[i] + 1:
                dp[i+j] = dp[i] + 1

    if dp[n+2] == n+2:
        return -1

    return dp[-1]


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
# arr2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_increasing_subsequence(arr))
# print(longest_increasing_subsequence(arr2))
