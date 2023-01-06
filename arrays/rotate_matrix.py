matrix = [  [1,2],
            [3,4]   ]

def rotate(matrix):

    n = len(matrix)

    # reverse a matrix
    # matrix.reverse()
    i = 0
    j = n - 1
    while (i < j):
        matrix[i],matrix[j] = matrix[j], matrix[i]
        i += 1
        j -= 1

    # transpose of a matrix
    for i in range(n):
        for j in range(i+1):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    
    return matrix

print(rotate(matrix))