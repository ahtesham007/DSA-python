class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}

        for i, num in enumerate(nums):
            if target - num in hm:
                return [hm[target - num], i]
            else:
                hm[num] = i
        
        return []

obj = Solution()
print(obj.twoSum([3,3], 6))