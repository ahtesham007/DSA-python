class Solution:
    def threeSum(self, nums):
        res = []
        n = len(nums)
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            lo = i + 1
            hi = n - 1
            target = -num

            while lo < hi:
                temp = nums[lo] + nums[hi]
                if temp == target:
                    res.append([num,nums[lo],nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                
                elif temp > target:
                    hi -= 1
                else:
                    lo += 1
        
        return res
                

