class Solution:
    def maxProduct(self, nums) -> int:
        max_prod = min_prod = res = nums[0]

        for num in nums:
            temp = max(num, max_prod * num, min_prod*num)
            min_prod = min(num, max_prod * num, min_prod*num)
            max_prod = temp

            res = max(res, max_prod)
        
        return res