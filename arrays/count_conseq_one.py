def count(nums):
    ans, cnt = 0, 0

    for num in nums:
        if num:
            cnt += 1
        else:
            cnt = 0
        
        ans = max(ans, cnt)
    
    return ans