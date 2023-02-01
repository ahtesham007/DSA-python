def combSum2(candidates, target):
    ans = []

    def dfs(ind, target, path):
        if target == 0:
            ans.append(path.copy())
            return
        
        for i in range(ind, len(candidates)):
            if i > ind and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target: break

            path.append(candidates[i])
            dfs(i+1, target - candidates[i], path)
            path.pop()
    
    candidates.sort()
    dfs(0, target, [])

    return ans

print(combSum2([1,1,2], 2))