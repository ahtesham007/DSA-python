def findPath(self, m, n):
    # code here
    res = []
    vis = [[0]*n for _ in range(n)]
    
    di = [1, 0, 0, -1]
    dj = [0, -1, 1, 0]
    
    def dfs(i, j, move):
        if i == n-1 and j == n-1:
            res.append(move)
            return
        dire = "DLRU"
        for ind in range(4):
            ni = i + di[ind]
            nj = j + dj[ind]

            if ni >= 0 and nj >= 0 and ni<n and nj<n and not vis[ni][nj] and m[ni][nj]:
                vis[i][j] = 1
                dfs(ni, nj, move+dire[ind])    
                vis[i][j] = 0    
        # if i+1 < n and not vis[i+1][j] and m[i+1][j]:
        #     vis[i][j] = 1
        #     dfs(i+1,j,move+"D")
        #     vis[i][j] = 0
        
        # if j-1 >= 0 and not vis[i][j-1] and m[i][j-1]:
        #     vis[i][j] = 1
        #     dfs(i,j-1,move+"L")
        #     vis[i][j] = 0
        
        # if j+1 < n and not vis[i][j+1] and m[i][j+1]:
        #     vis[i][j] = 1
        #     dfs(i,j+1,move+"R")
        #     vis[i][j] = 0
        
        # if i-1 >= 0 and not vis[i-1][j] and m[i-1][j]:
        #     vis[i][j] = 1
        #     dfs(i-1,j,move+"U")
        #     vis[i][j] = 0
    
    if m[0][0]:
        dfs(0, 0, "")
    return res