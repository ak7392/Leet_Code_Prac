def longest_increasing_subsequence(arr):

    n = len(arr)

    dp = [1 for i in range(n)]

    result = 0

    for i in range(1, n):

        for j in range(0, i):

            # Note this statement below is the crux of the algorithm
            # We check the value of j subsequently in the elements befoer i pointer
            # if j element is greater than i we increase the value of i element in dp list
            # for every increasing subsequnece element found in both locations
            # dp[i] < dp[j] + 1: checks whether value in list dp against value on pointer j in arr
            # is less or equal, if yes we just increment the value
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:

                dp[i] = dp[j] + 1
    # print(dp)

    for i in range(len(dp)):
        result = max(result, dp[i])

    return result


arr = [5, 8, 3, 7, 9, 1]
arr2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(longest_increasing_subsequence(arr))
print(longest_increasing_subsequence(arr2))
