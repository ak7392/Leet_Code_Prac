def longest_increasing_subsequence(arr):

    n = len(arr)

    # Reference for question:
    # https://www.youtube.com/watch?v=xbJtIC7sNX8

    dp = [arr[i] for i in range(n)]
    # print(dp)

    result = 0

    for i in range(1, n):

        for j in range(0, i):

            if arr[i] > arr[j] and arr[i] + dp[j] > dp[i]:

                dp[i] = arr[i]+dp[j]
    print(dp)

    # for i in range(len(dp)):
    #     result = max(result, dp[i])

    return max(dp)


arr = [5, 8, 3, 7, 9, 1]
# arr2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_increasing_subsequence(arr))
# print(longest_increasing_subsequence(arr2))
