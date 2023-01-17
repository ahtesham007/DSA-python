class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        ans = 1
        prev = nums[0]
        cnt = 1

        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                cnt += 1
            elif nums[i] != prev:
                cnt = 1
            
            prev = nums[i]
            ans = max(cnt, ans)
        
        return ans

obj = Solution()
print(obj.longestConsecutive([1,2,0,1]))