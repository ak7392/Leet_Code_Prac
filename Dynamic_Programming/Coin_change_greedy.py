# Greedy method


def coin_change(amount):

    coins = [25, 10, 1]
    count = 0

    for coin in coins:
        while amount >= coin:
            amount = amount-coin
            count += 1

    return count


print(coin_change(79))
