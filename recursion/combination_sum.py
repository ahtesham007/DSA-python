def combinationSum(nums, target):
    res = []

    def dfs(ind, target, path):
        if ind == len(nums):
            if target == 0:
                res.append(path.copy())
            return
        
        if nums[ind] <= target:
            path.append(nums[ind])
            dfs(ind, target - nums[ind], path)
            path.pop()
        dfs(ind + 1, target, path)
    
    nums.sort()
    dfs(0, target, [])
    return res

print(combinationSum([2,3,4], 6))