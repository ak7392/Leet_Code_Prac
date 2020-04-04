import sys
denominations = [1, 3, 5]
coins_needed = [sys.maxint] * 20
coins_needed[0] = 0

for amt in range(20):
    for coin in denominations:
        if coin <= amt and coins_needed[amt - coin] + 1 < coins_needed[amt]:
            coins_needed[amt] = coins_needed[amt - coin] + 1

print coins_needed
