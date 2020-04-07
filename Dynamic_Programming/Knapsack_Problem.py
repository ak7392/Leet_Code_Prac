def knapsack(cost, wts, capacity):

    # Reference - https://www.youtube.com/watch?v=BsD1KGewfBo&t=938s
    result = []

    w, h = capacity+1, len(cost)

    table = [[0 for x in range(w)] for y in range(h)]

    for index in range(len(cost)):
        for weight in range(w):

            if index == 0 or weight == 0:
                table[index][weight] = 0

            elif wts[index] > weight:
                # Just take the value from the column just above the current cost in mentioed column.
                table[index][weight] = table[index-1][weight]
                continue

            else:
                # Taking value of cell just above the current column cost
                prev_cost = table[index-1][weight]

                # Taking value of cell just above the current column cost
                # Subtracting from column weight your row weight
                # now move to column with weight after subtraction
                # pick that cost and add to mentioned cell cost
                new_cost = cost[index] + table[index-1][weight - wts[index]]

                table[index][weight] = max(prev_cost, new_cost)

    return table[-1][-1]


cost = [1, 2, 3]
wts = [4, 5, 1]
capacity = 5
print(knapsack(cost, wts, capacity))
