matrix = [[0,1,1],[1,1,1],[1,1,0]]

# bruteforce approach
def setZeroesBruteForce(matrix):
    row_len = len(matrix)
    col_len = len(matrix[0])
    for i in range (row_len):
        for j in range(col_len):
            if matrix[i][j] == 0:
                
                ind = i-1
                while ind >= 0:
                    if matrix[ind][j] != 0:
                        matrix[ind][j] = ''
                    ind-=1
                
                ind = i + 1
                while ind < row_len:
                    if matrix[ind][j] != 0:
                        matrix[ind][j] = ''
                    ind+=1
                
                ind = j - 1
                while ind >= 0:
                    if matrix[i][ind] != 0:
                        matrix[i][ind] = ''
                    ind-=1
                
                ind = j + 1
                while ind < col_len:
                    if matrix[i][ind] != 0:
                        matrix[i][ind] = ''
                    ind+=1
    
    for i in range (row_len):
        for j in range(col_len):
            if matrix[i][j] == '':
                matrix[i][j] = 0

    print(matrix)

setZeroesBruteForce(matrix)