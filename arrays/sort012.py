def sortColors(nums):
    low = 0
    mid = 0
    size = len(nums)
    high = size - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1
        
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
    
    return nums

print(sortColors([2,0,1]))