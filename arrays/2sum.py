class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}

        for i, num in enumerate(nums):
            if target - num in hm:
                return [hm[target - num], i]
            else:
                hm[num] = i
        
        return []
# Two Sum
obj = Solution()
print(f"Two Sum : {obj.twoSum([3,3], 6)})
