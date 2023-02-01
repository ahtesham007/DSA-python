def permute(nums):
    res = []

    def dfs(ind, nums):
        if ind == len(nums):
            res.append(nums.copy())
            return
        
        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            dfs(ind + 1, nums)
            nums[ind], nums[i] = nums[i], nums[ind]
    
    dfs(0, nums)
    return res

print(permute([1,2,3]))