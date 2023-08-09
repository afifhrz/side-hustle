def flippingMatrix(matrix):
    n = len(matrix) // 2
    max_sum = 0

    for i in range(n):
        for j in range(n):
            max_sum += max(
                matrix[i][j],
                matrix[i][2 * n - j - 1],
                matrix[2 * n - i - 1][j],
                matrix[2 * n - i - 1][2 * n - j - 1]
            )
            print(matrix[i][j],
                matrix[i][2 * n - j - 1],
                matrix[2 * n - i - 1][j],
                matrix[2 * n - i - 1][2 * n - j - 1])

    return max_sum

matrix =  [
    [112, 42, 83, 119], 
    [56, 125, 56, 49],
    [15, 78, 101, 43], 
    [62, 98, 114, 108]
    ]

print(flippingMatrix(matrix=matrix))