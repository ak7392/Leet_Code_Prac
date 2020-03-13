

def unique_paths(matrix):
    m = len(matrix)
    n = len(matrix[0])

    numberofpaths = [[0]*m for i in range(n)]
    print(numberofpaths)

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                numberofpaths[i][j] = 1

            else:
                numberofpaths[i][j] = numberofpaths[i-1][j] + \
                    numberofpaths[i][j-1]

    return numberofpaths[-1][-1]


matrix = [['A', 'B', 'C'],
          ['D', 'E', 'F'],
          ['G', 'H', 'I']]

print(unique_paths(matrix))
