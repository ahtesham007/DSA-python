def search(nums, target):
    l = 0
    hi = len(nums) - 1

    while l <= hi:
        mid = (l+hi)>>1
        if nums[mid] == target:
            return mid
        
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                hi = mid - 1
            else:
                l = mid + 1
        
        else:
            if nums[mid] < target <= nums[hi]:
                l = mid + 1
            else:
                hi = mid - 1
    
    return -1

print(search([4,5,6,7,0,1,2], 0))