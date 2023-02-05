def findPath(self, m, n):
    # code here
    res = []
    vis = [[0]*n for _ in range(n)]
    
    
    def dfs(i, j, move):
        if i == n-1 and j == n-1:
            res.append(move)
            return
        
        if i+1 < n and not vis[i+1][j] and m[i+1][j]:
            vis[i][j] = 1
            dfs(i+1,j,move+"D")
            vis[i][j] = 0
        
        if j-1 >= 0 and not vis[i][j-1] and m[i][j-1]:
            vis[i][j] = 1
            dfs(i,j-1,move+"L")
            vis[i][j] = 0
        
        if j+1 < n and not vis[i][j+1] and m[i][j+1]:
            vis[i][j] = 1
            dfs(i,j+1,move+"R")
            vis[i][j] = 0
        
        if i-1 >= 0 and not vis[i-1][j] and m[i-1][j]:
            vis[i][j] = 1
            dfs(i-1,j,move+"U")
            vis[i][j] = 0
    
    if m[0][0]:
        dfs(0, 0, "")
    return res