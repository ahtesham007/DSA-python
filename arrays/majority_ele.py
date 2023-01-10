def majorityElement(nums: list[int]) -> int:
    ans = 0
    count = 0

    for num in nums:
        if count == 0:
            ans = num
        
        if num == ans:
            count += 1
        else:
            count -= 1
    
    return ans

print(majorityElement([2,2,1,1,1,2,2]))