matrix = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1],
          ]


def floodFill(matrix, sr, sc, new_color):
    prev_c = matrix[sr][sc]
    Fill(matrix, sr, sc, prev_c, new_color)
    return matrix


def Fill(matrix, sr, sc, prev_c, new_color):
    if sr < 0 or sc < 0 or sr >= len(matrix) or sc >= len(matrix[0]) or matrix[sr][sc] != prev_c or matrix[sr][sc] == new_color:
        return
    matrix[sr][sc] = new_color
    Fill(matrix, sr-1, sc, prev_c, new_color)
    Fill(matrix, sr+1, sc, prev_c, new_color)
    Fill(matrix, sr, sc-1, prev_c, new_color)
    Fill(matrix, sr, sc+1, prev_c, new_color)


print(floodFill(matrix, 0, 0, 5))

print("Updated screen after call to floodFill:")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=' ')
    print()
