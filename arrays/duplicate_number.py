def findDuplicate(nums: list[int]) -> int:
    slow = fast = nums[0]
    slow = nums[slow]
    fast = nums[nums[fast]]

    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

def findDuplicateNegative(nums):

    for i in range(len(nums)):
        if nums[abs(nums[i])] > 0:
            nums[abs(nums[i])] = -nums[abs(nums[i])]
        else:
            return abs(nums[i])

print(findDuplicateNegative([1,3,4,2,2]))

