def coin_change(coins, amount):

    t = []
    #  since no. of coins to make amount 0 is zero
    t.append(0)

    # we calculate min coins req. for each amount until the amount we want
    for i in range(1, amount+1):

        # we set a large inital value (which if not changed, means the curr. amount impossible to obtain)
        t.append(amount+1)

        # we try to calculate min coins that would be required, progressively introducing each type of coin
        for coin in coins:

            # if coins value is less than amount, and
            # if  the total no. of coins - curr coin (1) and no of coins to make up the balance < known value
            if coin <= i and t[i-coin] + 1 < t[i]:
                t[i] = t[i-coin] + 1

    return t[-1] if t[-1] != amount+1 else -1
    # return -1 if for a amount, no combination is able to change value from the initial value we had set.


coins = [22, 1, 12]
print(coin_change(coins, 15))
