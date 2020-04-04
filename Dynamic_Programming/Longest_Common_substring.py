def longest_common_sub(str1, str2):
    # Reference for this vedio -
    # https://www.youtube.com/watch?v=LAKWWDX3sGw
    n1 = len(str1)
    n2 = len(str2)
    result = 0

    dp = [[0]*(n2+1) for j in range(n1+1)]

    for i in range(n1+1):
        for j in range(n2+1):
            # Filling all the rows and column with index 0
            # This prepares our base case
            if i == 0 or j == 0:
                dp[i][j] == 0
            # if the string macthes the digonal element is copied to current element
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                result = max(result, dp[i][j])

            else:
                dp[i][j] = 0

    return result


str1 = "ABCDGH"
str2 = "ACDGHR"
print(longest_common_sub(str1, str2))
