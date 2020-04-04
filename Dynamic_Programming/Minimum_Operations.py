def minCost(N, P, Q):
    # Initialize cost to 0
    cost = 0

    # going backwards until we
    # reach initial position
    while (N > 0):
        if (N & 1):
            cost += P
            N -= 1
        else:
            temp = N // 2

            # if 2*X jump is
            # better than X+1
            if (temp * P > Q):
                cost += Q
            # if X+1 jump is better
            else:
                cost += P * temp
            N //= 2
    return cost


# Driver program
N = 8
P = 1
Q = 1
print(minCost(N, P, Q))
