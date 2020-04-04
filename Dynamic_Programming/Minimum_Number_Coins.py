def min_number_coins(coins, amount, n):
    dp = []
    dp.append(0)

    for i in range(1, amount+1):
        dp.append(amount+1)
        for coin in coins:

            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i-coin] + 1

    return dp[-1]


coins = [1, 5, 25, 50]
n = len(coins)
amount = 31
print(min_number_coins(coins, amount, n))
