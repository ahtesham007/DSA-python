def singleNonDuplicate(nums) -> int:
        l = 0
        hi = len(nums)-2

        while l <= hi:
            mid = l+hi >> 1
            if nums[mid] == nums[mid^1]:
                l = mid + 1
            else:
                hi = mid - 1
        
        return nums[l]

print(singleNonDuplicate([1,1,2,3,3]))