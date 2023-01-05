def next_permutation(nums):
    size = len(nums)

    if size == 1:
        return
    
    indx1 = size - 2
    while indx1 >= 0 and nums[indx1] >= nums[indx1 + 1]:
        indx1 -= 1
    
    if indx1 >= 0:
        indx2 = size - 1
        while nums[indx2] <= nums[indx1]:
            indx2 -= 1

        nums[indx1], nums[indx2] = nums[indx2], nums[indx1]
    
    nums[indx1 + 1:] = nums[indx1 + 1:][::-1]

    return nums


print(next_permutation([3,2,1]))