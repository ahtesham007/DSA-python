# Recursive solution
def uniquePathsRecursive(m: int, n: int) -> int:
    return countPathRecursive(0, 0, m, n)

def countPathRecursive(i, j, m, n):
    if i == m-1 and j == n-1: return 1
    if i >= m or j >= n:
        return 0
    else:
        return countPathRecursive(i+1, j, m, n) + countPathRecursive(i, j+1, m, n)

# Dynamic Programming
def uniquePaths(m: int, n: int) -> int:
    dp = [[-1]*n for _ in range(m)]
    return countPath(0, 0, m, n, dp)

def countPath(i, j, m, n, dp):
    if i == m-1 and j == n-1: return 1
    if i >= m or j >= n:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        dp[i][j] = countPath(i+1, j, m, n, dp) + countPath(i, j+1, m, n, dp)
        return dp[i][j]

print(uniquePaths(2, 3))