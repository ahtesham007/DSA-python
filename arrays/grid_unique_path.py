def uniquePaths(m: int, n: int) -> int:
    return countPath(0, 0, m, n)

def countPath(i, j, m, n):
    if i == m-1 and j == n-1: return 1
    if i >= m or j >= n:
        return 0
    else:
        return countPath(i+1, j, m, n) + countPath(i, j+1, m, n)

print(uniquePaths(2, 3))