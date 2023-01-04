matrix = [[0, 1, 1], [1, 1, 1], [1, 1, 0]]

# bruteforce approach


def setZeroesBruteForce(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:

                ind = i-1
                while ind >= 0:
                    if matrix[ind][j] != 0:
                        matrix[ind][j] = ''
                    ind -= 1

                ind = i + 1
                while ind < row_len:
                    if matrix[ind][j] != 0:
                        matrix[ind][j] = ''
                    ind += 1

                ind = j - 1
                while ind >= 0:
                    if matrix[i][ind] != 0:
                        matrix[i][ind] = ''
                    ind -= 1

                ind = j + 1
                while ind < col_len:
                    if matrix[i][ind] != 0:
                        matrix[i][ind] = ''
                    ind += 1

    for i in range(row_len):
        for j in range(col_len):
            if matrix[i][j] == '':
                matrix[i][j] = 0

    print(matrix)

# optimized approach


def setZeroesOptimized(matrix) -> None:

    row_len = len(matrix)
    col_len = len(matrix[0])
    rowCol0 = False

    for i in range(row_len):
        if matrix[i][0] == 0:
                rowCol0 = True
        for j in range(1, col_len):
            if matrix[i][j] == 0:
                matrix[0][j] = matrix[i][0] = 0

    for i in range(row_len-1, -1, -1):
        for j in range(col_len-1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if rowCol0:
            matrix[i][0] = 0

    print(matrix)

setZeroesOptimized(matrix)