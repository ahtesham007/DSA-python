def searchMatrix(matrix: list[list[int]], target: int):
    lo = 0
    n,m = len(matrix), len(matrix[0])
    high = n*m

    while lo < high:
        mid = (lo + (high-1))//2
        val = matrix[mid//m][mid%m]

        if val == target:
            return True
        elif val < target:
            lo = mid + 1
        else:
            high = mid
    
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))

assert searchMatrix([[1]], 1) == True
assert searchMatrix([[1]], 2) == False
assert searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3) == True
assert searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 15) == False