def pascal_triangle(num):

    res = [[0 for _ in range(i+1)] for i in range(num)]
    for i in range(num):
        for j in range(i+1):
            if j == 0 or j == i:
                res[i][j] = 1
            else:
                res[i][j] = res[i-1][j-1] + res[i-1][j]
    
    print(res)

     
def pascal_triangle_opt(num):

    res = []
    for i in range(num):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(res[i-1][j-1] + res[i-1][j])
        res.append(row)

    print(res)

pascal_triangle_opt(5)