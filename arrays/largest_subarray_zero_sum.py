def largest_subarray(nums):
    max_len = sum = 0
    hash_map = {}

    for i in range(len(nums)):
        sum += nums[i]
        if sum == 0:
            max_len = i + 1
        
        if sum in hash_map:
            max_len = max(max_len, i - hash_map[sum])
        else:
            hash_map[sum] = i
        
    return max_len

print(largest_subarray([9, -3, 3, -1, 6, -5]))