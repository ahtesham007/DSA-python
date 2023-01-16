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
def uniquePathsdp(m: int, n: int) -> int:
    dp = [[-1]*n for _ in range(m)]
    return countPathdp(0, 0, m, n, dp)

def countPathdp(i, j, m, n, dp):
    if i == m-1 and j == n-1: return 1
    if i >= m or j >= n:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    else:
        dp[i][j] = countPathdp(i+1, j, m, n, dp) + countPathdp(i, j+1, m, n, dp)
        return dp[i][j]

# Combination Approach
def uniquePaths(m: int, n: int) -> int:
    steps = m + n - 2
    
    denominator = m - 1
    res = 1
    for i in range(1, denominator + 1):
        res = res * (steps - denominator + i) // i
    return res              


print(uniquePaths(3, 7))