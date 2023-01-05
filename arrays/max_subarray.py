def maxSubarray(nums):
    curr_sum = 0
    max_sum = nums[0]

    for i in range(len(nums)):
        curr_sum += nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
        
        if curr_sum < 0:
            curr_sum = 0
    
    return max_sum


def printMaxSubarray(nums):
    curr_sum = 0
    max_sum = nums[0]

    s = 0
    e = 0

    for i in range(len(nums)):
        curr_sum += nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            e = i
        
        if curr_sum < 0:
            curr_sum = 0
            s = i + 1
    
    return max_sum,nums[s:e+1]

print(printMaxSubarray([5,4,-1]))