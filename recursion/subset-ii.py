def subsetsWithDup(nums):
    res = []
    subset = []

    def dfs(ind):
        res.append(subset.copy())

        for i in range(ind, len(nums)):
            if i != ind and nums[i] == nums[i-1]:
                continue
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
    
    nums.sort()

    dfs(0)
    return res

print(subsetsWithDup([1,2,2]))
